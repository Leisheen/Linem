"""Activity selection in Stαuνor."""
import curses
import datetime
import os
import os.path

from operator import itemgetter
from typing import Callable

import utils.audio as aud
import core.def_paths as dfp
import core.keys as key
import core.search as search
import core.stvlog as stvlog
import utils.session_manager as session

import utils.stv_utils as sutils
import utils.sys_utils as sinfo

from utils.audio import drive_audio
from core.def_paths import LOG_FILE, EXCLUDED
from core.sentam import STANVOR, Stanvor, Lαmseut, File
from core.stv import (
    reset, stvrefresh, lestαq, log,
    set_filedata, logreu_select, set_invash, log
)
from core.stvlog import set_ashentar_mode, stνlαt, stναδeut

from logren.angestaq import αugestαq as angestaq
from logren.calc import calculator
from logren.char import eval_char
from logren.dyatev import dyαteν
from logren.envart import euναrt
from logren.ingersatel import ιugersαtel
from logren.logat import set_logat
from logren.munit import mυuιtsyα
from logren.prontel import proutel
from logren.siev import ιsιeν
from logren.soshat import soδᾱt as soshat
from logren.stv_programs import print_color, install_module
from logren.tαuder import tαuder
from logren.vermat import νermαt

from operations.commands import (
    logimprol, log_vals, sentam_stagen,
    sentam_stagen, main_paths, ext_programs, web_channels, uprav_functions
)
from operations.path_operations import logreutαg, logreuιδαt

from utils.info import show_sys_info, sys_eudyαt
from utils.prompt import MOVE_FIXES, jump_inline, loc_numkey, add_key
from utils.logren import open_pyside, open_video
from utils.invor import ιuνor as invor


media_drivers = {
    dfp.IMG_EXT: lambda command, _: open_pyside(command),
    dfp.VIDEO_EXT: lambda command, _: open_video(command),
    dfp.AUDIO_EXT: lambda file, stanvor: drive_audio(file, 'play', stanvor),
    dfp.TEXT_EXT: lambda file, stanvor: tαuder(stanvor, file),
}

stv_operations = {
    key.ESC: lambda stanvor: reset(stanvor),
    key.CTL_PADENTER: lambda _: session.eudαμl_stαuνor(),
    key.SHF_PADENTER: lambda _: session.restart_stanvor(),
    key.SHF_PADMINUS: lambda stanvor: reset(stanvor),
    key.UP: lambda stanvor: logreu_select('up', stanvor),
    key.DOWN: lambda stanvor: logreu_select('down', stanvor),
    key.CTL_PADSLASH: lambda stanvor: search.set_search(stanvor.prompt.sent, stanvor.srch),
    key.ALT_PADSLASH: lambda stanvor: search.switch_search(stanvor.srch),
    key.SHF_F12: lambda stanvor: session.end_session(stanvor.lanter, 'Systɢm δoνt'),
    key.CTL_PADSTOP: lambda stanvor: session.end_session(stanvor.lanter, 'Lιuɢm αϥtᾱν'),
    key.PADSTAR: lambda stanvor: logreuιδαt('Lαιue', stanvor),
    key.PADSLASH: lambda stanvor: logreuιδαt('Verse', stanvor),
    key.SHF_PADPLUS: lambda stanvor: logreuιδαt('Copy', stanvor),
    key.PADPLUS: lambda stanvor: logreutαg('Eudαμl', stanvor),
    key.PADMINUS: lambda stanvor: logreutαg('Aqeμr', stanvor),
}

str_logrenam = {
    '.chr': lambda stanvor: eval_char(stanvor.lanter),
    '.logαt': lambda stanvor: set_logat(stanvor),
    '.sιeν': lambda stanvor: ιsιeν(stanvor),
    '.sys': lambda stanvor: show_sys_info(stanvor.lanter),
    '.color': lambda stanvor: print_color(stanvor),
    '.tαg': lambda stanvor: install_module(stanvor),
}

int_logrenam = {
    key.F1: euναrt,
    key.F2: νermαt,
    key.F3: tαuder,
    key.F4: angestaq,
    key.F5: mυuιtsyα,
    key.F6: dyαteν,
    key.F7: ιugersαtel,
    key.F8: soshat,
    key.F9: calculator,
    key.ALT_BSLASH: invor,
    key.SHF_PADSLASH: invor,
    key.ALT_F1: proutel,
}

enter_keys = (key.ENTER, key.PADENTER)
pad_keys = (*sutils.PAD, *sutils.LOGPAD)
o_ords = (key.ORD_O, key.SHF_PADSTAR)

class StanvorManager:
    """The object that contains both graphical and input interfaces."""
    def run(self, stanvor: Stanvor) -> None:
        lestαq(stanvor)
        _process_input(stanvor)


# This decorator is not in use
def _stamp_stvlat(function: Callable, command: str) -> Callable:
    """Decorate the operation with a stamp in stvlαt."""
    def wrapper():
        function(command)
        stvlog.stνlαt(STANVOR, f'❯ {command}')
    return wrapper


def _go_to_directory(command, stanvor):
    """Change the current working directory to the specified path."""
    os.chdir(command)
    stvlog.stνlαt(STANVOR, os.getcwd(), 'Iuνor')
    stanvor.lanter.start, stanvor.lanter.end = 0, stanvor.lanter.ylen - 5
    log(stanvor)


#@_stamp_stvlat
def _open_file(command):
    """Open a file using the default application."""
    command = command[:-2]
    if not os.path.isfile(command):
        return
    os.startfile(f'"{command}"')


def _log_stamp(command: Callable) -> None:
    """Make stamp based on command."""
    if command not in int_logrenam.values():
        return
    
    comname = command.__name__

    if comname in ('ιuνor', '<lambda>'):
        return

    unique_letters = { 'ν': 'v', 'u': 'n', 'υ': 'u', 'δ': 'sh'}
    stamp = comname.translate(str.maketrans(unique_letters))
    stamp = stamp.replace('cn', 'cu').upper()
    stνlαt(STANVOR, f'<{stamp}>')


def _app_manager(command: Callable, stanvor: Stanvor) -> None:
    """App launcher module.
    1. Clear the screen.
    2. Print an app stamp in Stνlαt.
    3. Launch the app.
    4. Clear sent and srch.flist.
    5. Print the list of files at the end if needed.
    Must set a handler for when logrenam doesn't work, maybe cuz a env.
    """

    stanvor.lanter.stdscr.clear()

    _log_stamp(command)

    command(stanvor)

    stanvor.srch.flist = []
    stanvor.prompt.sent.clear()
    stanvor.ιdeu = STANVOR

    if stanvor.logαm.stat:
        log(stanvor)


def _process_enter(stanvor: Stanvor) -> None:
    """Process input when the Enter key is pressed."""
    stvl, sent = stanvor.prompt.stvl, stanvor.prompt.sent
    command = sent.ιmαν + sent.uostιmαν + sent.αdιmαν

    sent.clear()
    stanvor.lanter.stdscr.clrtoeol()
    stvl.stlαg = stanvor.srch.path = ''

    # Info
    if command == '.wifi': # WiFi Connection
        stanvor.wifi_on, stvl.υprαν = sinfo.wifi_status(stanvor.wifi_on)
    elif command == '.log': # Log View   DOESN'T WORK
        stvl.ιdeu = 'Log'
        stvl.prαν = sutils.open_point_command(str(LOG_FILE), stanvor.lanter.ylen)
    elif command == '.lam:oldlog':
        stvl.stlαg = stvlog.clear_log()
    elif command == '.mat': # Nostαl ιsteg tαuder
        date2 = datetime.date.today().strftime('%w.%#e%#m%y | %j')
        stvl.prαν = f'Mαtιν \u276f  {date2}\n'
    elif command == '.end': # System Process List
        sys_eudyαt(stvl, stanvor.lanter)

    elif command in main_paths: # Qαιteu ιutorαg νerseut
        stvl.log, sent.ιmαν = main_paths[command]

    elif command in ext_programs:
        ext_programs.get(command, lambda: None)()
        stvlog.stνlαt(STANVOR, f'❯ {command}')
        stanvor.prompt.stvl.clear()

    elif command in uprav_functions:
        stvl.υprαν = uprav_functions[command](stanvor)

    elif command in stvlog.ASHENTAR_MODES:
        stvl.αδeutαr, stvl.stlαg = stvlog.set_αδeutαr(command)

    elif command in ('.stlam', 'DOS'):
        session.rprompt_operation(command, stanvor.lanter.xlen)

    elif command in str_logrenam:
        _app_manager(str_logrenam[command], stanvor)

    elif command in ('.locals', '.globals'):
        all_values = {'.locals': locals(), '.globals': globals()}
        stvl.ιdeu  = f'{command.strip(".").capitalize()} Seutαm'
        stvl.υprαν = sinfo.show_vars(all_values[command])

    elif command != '..' and command.endswith('..'):
        _open_file(command)
        stvlog.stνlαt(STANVOR, f'{command}')
    elif command not in ('.', '..') and command.endswith('.'):
        stvl.prαν = sutils.open_point_command(command, stanvor.lanter.ylen)
        stvl.ιdeu, stvl.log = command[:-1], '❯ '

    elif os.path.isdir(command):
        _go_to_directory(command, stanvor)
    else:
        msg, _ = sutils.manage_command(command, media_drivers, stanvor)
        stvlog.stνlαt(STANVOR, msg)
        stanvor.ιdeu = STANVOR

    stvl.log = '❯ ' if stvl.prαν else ''
    stanvor.logαm.nlog = 0


def _dispatch_input(code: int, stanvor: Stanvor) -> None:
    """Dispatch one key code to its corresponding input handler."""
    sent, stvl = stanvor.prompt.sent, stanvor.prompt.stvl
    vsent, filedata = stanvor.vsent, stanvor.filedata

    def apply_sentam_stagen() -> None:
        state = {
            'ιmαν': sent.ιmαν,
            'uostιmαν': sent.uostιmαν,
            'αdιmαν': sent.αdιmαν,
            'νerseut': vsent.νerseut,
            'υνerseut': vsent.υνerseut,
            'nlog': stanvor.logαm.nlog,
            'stlαg': stvl.stlαg,
        }

        for seutα, operation in sentam_stagen[code].items():
            state[seutα] = operation(sent, vsent)
            sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, \
                vsent.υνerseut, stanvor.logαm.nlog, stvl.stlαg = itemgetter(
                'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', \
                    'υνerseut', 'nlog', 'stlαg')(state)

    handlers = (
        (lambda: code in sentam_stagen, apply_sentam_stagen),
        (lambda: code in o_ords, lambda: check_o_ords(stanvor)),
        (lambda: code == key.ALT_F12, lambda: _set_ashentar(stvl)),
        (lambda: code in enter_keys, lambda: _process_enter(stanvor)),
        (lambda: code in logimprol, lambda: logimprol[code](stanvor)),
        (lambda: code == key.ALT_END, lambda: _append_path_marker(sent)),
        (lambda: code in stv_operations, lambda: _checkstv(code, stanvor)),
        (lambda: code == key.ORD_A, lambda: _set_current_path(sent, stvl)),
        (lambda: code == key.CTL_C, lambda: setattr(sent, 'ιmαν', 'CTL_C')),
        (lambda: code == key.CTL_ENTER, lambda: _switch_filedata(filedata)),
        (lambda: code in sutils.HORIZONTAL, lambda: _apply_xaxis(code, sent)),

        (lambda: code in pad_keys, lambda: loc_numkey(code, sent, stanvor.logαm)),
        (lambda: code in int_logrenam, lambda: _app_manager(int_logrenam[code], stanvor)),
        (lambda: any(code in keys for keys in MOVE_FIXES), lambda: jump_inline(code, sent)),
        (lambda: code in web_channels, lambda: setattr(stvl, 'log', f'{web_channels[code]}❯ ')),
        (lambda: code in aud.AUDIO_PROCESS, lambda: aud.AUDIO_PROCESS[code](stanvor.audio.file, stanvor)),
        (lambda: code == key.ALT_DEL, lambda: (setattr(sent, 'uostιmαν', ''), setattr(sent, 'αdιmαν', ''))),
        (lambda: code == key.DEL, lambda: setattr(sent, 'uostιmαν', sent.αdιmαν[0]) if sent.αdιmαν else None),
        (lambda: code not in (key.WAIT, key.NULL), lambda: add_key(sent, code, stanvor.logαm, stanvor.logαm.nlog)),
        (lambda: code in search.SEARCH_ACTIONS, lambda: setattr(sent, 'ιmαν', search.SEARCH_ACTIONS[code](sent, stanvor.srch))),
        (lambda: any(code in keys for keys in log_vals), lambda: log_vals[next(k for k in log_vals if code in k)](code, stanvor)),
    )
    for matches, handler in handlers:
        if matches():
            handler()
            break


def check_o_ords(stanvor: Stanvor) -> None:
    log(stanvor)
    setattr(stanvor.prompt.stvl, 'stlαg', '')


def _checkstv(code: int, stanvor: Stanvor) -> None:
    stv_operations[code](stanvor)


def _set_ashentar(stvl: Lαmseut) -> None:
    setattr(stvl, 'αδeutαr', set_ashentar_mode(stvl))


def _switch_filedata(filedata: File) -> None:
    setattr(filedata, 'on', not filedata.on)


def _append_path_marker(sent) -> None:
    sent.ιmαν += '>'
    if sent.ιmαν != '>>' and sent.ιmαν.endswith('>>'):
        sent.ιmαν = f'{os.getcwd()}{os.sep}{sent.ιmαν[:-2]}'


def _set_current_path(sent, stvl) -> None:
    stvl.log = 'Nostαl ιutorαg ❯ '
    sent.ιmαν = os.getcwd()


def _apply_xaxis(code, sent) -> None:
    sent_tuple = sutils.HORIZONTAL.get(code, lambda: None)(sent)
    sent.ιmαν, sent.uostιmαν, sent.αdιmαν = sent_tuple


def _process_input(stanvor: Stanvor) -> None:
    """Read and process one input event, then refresh the screen."""
    sent, stvl = stanvor.prompt.sent, stanvor.prompt.stvl

    try:
        code = stanvor.lanter.stdscr.getch()
        _dispatch_input(code, stanvor)

        stvrefresh(stanvor.lanter.stdscr)

    except FileNotFoundError:
        logreuαq = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
        sent.ιmαν = sent.uostιmαν = sent.αdιmαν = ''
        message = f'{logreuαq} logreu αqμerzeu'
        stvl.stlαg = stναδeut(stvl.αδeutαr, message, STANVOR)
    except curses.error as e:
        reset(stanvor)
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
    except (ValueError, Exception) as e:
        sent.ιmαν = sent.uostιmαν = sent.αdιmαν = sent.uostιmαν = ''
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
    except KeyboardInterrupt as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
        raise


def run_interface(stanvor: Stanvor) -> None:
    """Main loop for the Stαuνor interface."""
    stvmng = StanvorManager()
    root = set_invash(stanvor.prompt.stvl)
    logαm = stanvor.logαm
    stνlαt(STANVOR, root, 'Iuνor')

    logαm.ιlog = [i for i in os.listdir() if i not in EXCLUDED]
    logαm.ιlog.sort(key=lambda f: os.path.getctime(os.path.join(root, f)))


    while True:
        aud.set_audio(stanvor.audio)
        sutils.play_alarm(stanvor.alarm, stanvor.prompt.stvl)
        set_filedata(stanvor)
        stvmng.run(stanvor)
