"""Activity selection in Stαuνor."""
import curses
import datetime
import os
import os.path

from typing import Callable

import core.def_paths as dfp
import core.keys as key

from core.audio import set_audio, drive_audio
from core.def_paths import LOG_FILE
from core.filesystem import log, logvals
from core.keys import (
    ORD_A, O_ORDS, CTL_ENTER, ALT_F12, ALT_END, SEND, PAD_KEYS
)
from core.search import SEARCH
from core.sentam import STANVOR, Stanvor, Lαmseut, File
from core.stv import (
    stvrefresh, lestαq, set_filedata, reset, set_invash, process_handlers
)
from core.stvlog import (
    ASHENTARS, set_ashentar_mode, stνlαt, stναδeut, clear_log, set_αδeutαr
)
from logren.tαuder import tαuder

from operations.commands import main_paths, uprav_funcs, stv_actions
from operations.logrenam import intlogren, strlogren, ext_progs
from operations.tag import tαg

from utils.info import sys_eudyαt
from utils.logren import open_pyside, open_video
from utils.session_manager import open_cmd
from utils.stv_utils import (
    HNAV, open_point_command, manage_command, set_ilog, play_alarm
)
from utils.sys_utils import wifi_status, show_vars, set_syscursor


web_chnls = {key.ALT_R: 'E', key.ALT_P: 'P', key.ALT_M: 'M', key.ALT_L: 'L'}

media_drivers = {
    dfp.VIDEO_EXT: lambda file, _:        open_video(file),
    dfp.IMG_EXT:   lambda file, _:        open_pyside(file),
    dfp.TEXT_EXT:  lambda file, stanvor: tαuder(stanvor, file),
    dfp.AUDIO_EXT: lambda file, stanvor: drive_audio('play', stanvor, file),
}


class StanvorManager:
    """The object that contains both graphical and input interfaces."""
    def run(self, stanvor: Stanvor) -> None:
        lestαq(stanvor)
        _process_input(stanvor)
        stvrefresh(stanvor.lanter.stdscr)


# This decorator is not in use
def _stamp_stvlat(function: Callable, cmd: str) -> Callable:
    """Decorate the operation with a stamp in stvlαt."""
    def wrapper():
        function(cmd)
        stνlαt(STANVOR, f'❯ {cmd}')
    return wrapper


def _check_dots(cmd: str) -> bool:
    """Check if the commmand is not just points, but ends with one."""
    return cmd not in ('.', '..') and cmd.endswith('.')


def _look_twodots(cmd: str) -> bool:
    """Check if the command ends with two dots."""
    return cmd != '..' and cmd.endswith('..') and os.path.isfile(cmd)


def _go_todir(dir: str, stanvor) -> None:
    """Change the current working directory to the specified path."""
    os.chdir(dir)
    stνlαt(STANVOR, os.getcwd(), 'Iuνor')
    stanvor.lanter.start, stanvor.lanter.end = 0, stanvor.lanter.ylen - 5
    log(stanvor)


#@_stamp_stvlat
def _open_file(file: str) -> None:
    """Open a file using the default application."""
    file = file[:-2]
    os.startfile(f'"{file}"')
    stνlαt(STANVOR, f'{file}')


def _log_stamp(command: Callable) -> None:
    """Make stamp based on command."""
    if command not in intlogren.values():
        return
    
    comname = command.__name__

    if comname in ('ιuνor', '<lambda>'):
        return

    unique_letters = { 'ν': 'v', 'u': 'n', 'υ': 'u', 'δ': 'sh'}
    stamp = comname.translate(str.maketrans(unique_letters))
    stamp = stamp.replace('cn', 'cu').upper()
    stνlαt(STANVOR, f'<{stamp}>')


def _open(command: Callable, stanvor: Stanvor) -> None:
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


def _show_wifi(stanvor) -> None:
    """Show wifi info."""
    stanvor.wifi_on, stanvor.prompt.stvl.υprαν = wifi_status(stanvor.wifi_on)


def _show_log(stanvor: Stanvor) -> None:
    """Show the log."""
    stvl = stanvor.prompt.stvl
    stvl.ιdeu = 'Log'
    stvl.prαν = open_point_command(str(LOG_FILE), stanvor.lanter.ylen)


def _clear_log(stanvor: Stanvor) -> None:
    """Clear the log."""
    stanvor.prompt.stvl.stlαg = clear_log()


def _show_today(stanvor) -> None:
    """Show the current day."""
    date2 = datetime.date.today().strftime('%w.%#e%#m%y | %j')
    stanvor.prompt.stvl.prαν = f'Mαtιν \u276f  {date2}\n'


def _show_vars(command: str, stanvor: Stanvor) -> None:
    """Show variables."""
    stvl = stanvor.prompt.stvl
    all_values = {'.locals': locals(), '.globals': globals()}
    stvl.ιdeu  = f'{command.strip(".").capitalize()} Seutαm'
    stvl.υprαν = show_vars(all_values[command])


def _runext(command: str, stanvor: Stanvor) -> None:
    """Run external programs."""
    ext_progs.get(command, lambda: None)()
    stνlαt(STANVOR, f'❯ {command}')
    stanvor.prompt.stvl.clear()


def _show_file(command, stanvor) -> None:
    """Show file."""
    stvl = stanvor.prompt.stvl
    stvl.prαν = open_point_command(command, stanvor.lanter.ylen)
    stvl.ιdeu, stvl.log = command[:-1], '❯ '


def _set_intor(command: str, stanvor: Stanvor) -> None:
    """Set directory."""
    stvl, sent = stanvor.prompt.stvl, stanvor.prompt.sent
    stvl.log, sent.ιmαν = main_paths[command]


def _set_uprav(command, stanvor) -> None:
    """Set υprαν."""
    stanvor.prompt.stvl.υprαν = uprav_funcs[command](stanvor)


def _set_ashent(command: str, stanvor: Stanvor) -> None:
    """Set αδeutαr."""
    stvl = stanvor.prompt.stvl
    stvl.αδeutαr, stvl.stlαg = set_αδeutαr(command)


def _process_send(stanvor: Stanvor) -> None:
    """Process input when the Enter key is pressed."""
    stvl, sent = stanvor.prompt.stvl, stanvor.prompt.sent
    cmd = sent.ιmαν + sent.uostιmαν + sent.αdιmαν

    sent.clear()
    stanvor.lanter.stdscr.clrtoeol()
    stvl.stlαg = stanvor.srch.path = ''
    rprompts = ('.stlam', 'DOS')
    stvars = ('.locals', '.globals')

    if not process_handlers((
        (lambda: cmd == '.log',      lambda: _show_log(stanvor)), # FIX IT
        (lambda: cmd == '.oldlog',   lambda: _clear_log(stanvor)),
        (lambda: cmd == '.end',      lambda: sys_eudyαt(stanvor)),
        (lambda: cmd == '.wifi',     lambda: _show_wifi(stanvor)),
        (lambda: cmd == '.mat',      lambda: _show_today(stanvor)),
        (lambda: cmd in ext_progs,   lambda: _runext(cmd, stanvor)),
        (lambda: cmd in stvars,      lambda: _show_vars(cmd, stanvor)),
        (lambda: cmd in main_paths,  lambda: _set_intor(cmd, stanvor)),
        (lambda: cmd in uprav_funcs, lambda: _set_uprav(cmd, stanvor)),
        (lambda: cmd in ASHENTARS,   lambda: _set_ashent(cmd, stanvor)),
        (lambda: cmd in rprompts,    lambda: open_cmd(cmd, stanvor.lanter)),
        (lambda: cmd in strlogren,   lambda: _open(strlogren[cmd], stanvor)),
        (lambda: _look_twodots(cmd), lambda: _open_file(cmd)),
        (lambda: _check_dots(cmd),   lambda: _show_file(cmd, stanvor)),
        (lambda: os.path.isdir(cmd), lambda: _go_todir(cmd, stanvor)),
    )):
        msg, _ = manage_command(cmd, media_drivers, stanvor)
        stνlαt(STANVOR, msg)

    stanvor.ιdeu = STANVOR
    stanvor.prompt.stvl.clear()
    stanvor.logαm.nlog = 0
    stvl.log = '❯ ' if stvl.prαν else ''


def _set_ashentar(stvl: Lαmseut) -> None:
    """Set ashentar mode variables."""
    setattr(stvl, 'αδeutαr', set_ashentar_mode(stvl))


def _add_path_marker(sent) -> None:
    """Add a path marker."""
    sent.ιmαν += '>'
    if sent.ιmαν != '>>' and sent.ιmαν.endswith('>>'):
        sent.ιmαν = f'{os.getcwd()}{os.sep}{sent.ιmαν[:-2]}'


def _set_cwdir(sent, stvl) -> None:
    """Set current directory info."""
    stvl.log = 'Nostαl ιutorαg ❯ '
    sent.ιmαν = os.getcwd()


def _show_dirlist(stanvor: Stanvor) -> None:
    """Show dirlist."""
    log(stanvor)
    setattr(stanvor.prompt.stvl, 'stlαg', '')


def _switch_fileon(filedata: File) -> None:
    """
    Switch filedata object state (on/off).
    Regarding to state, its content is shown by stvl.
    """
    setattr(filedata, 'on', not filedata.on)


def _drivestv(cmd: int, stanvor: Stanvor) -> None:
    """Drive stv_operations."""
    stv_actions[cmd](stanvor)


def _nav_xaxis(cmd, sent) -> None:
    """Navigate horizontally in prompt."""
    sent_tuple = HNAV.get(cmd, lambda: None)(sent)
    sent.ιmαν, sent.uostιmαν, sent.αdιmαν = sent_tuple


def _locpad(code: int, stanvor: Stanvor) -> None:
    """Jump to a specific path based on its numkey index."""
    sent, logαm = stanvor.prompt.sent, stanvor.logαm
    if code in key.PAD:
        logαm.nlog = min(len(logαm.ιlog)-1, key.PAD[code][1])
    elif code in key.LOGPAD:
        logαm.nlog = min(len(logαm.ιlog)-1, key.LOGPAD[code])

    sent.ιmαν = logαm.ιlog[logαm.nlog]
    sent.uostιmαν = sent.αdιmαν = ''


def _set_webchns(cmd: int, stvl: Lαmseut) -> None:
    """Set log to web channels."""
    setattr(stvl, 'log', f'{web_chnls[cmd]}❯ ')


def _search(stanvor: Stanvor, cmd: int) -> None:
    """Manage search actions."""
    sent = stanvor.prompt.sent
    setattr(sent, 'ιmαν', SEARCH[cmd](sent, stanvor.srch))


def _look_logvals(cmd: int) -> bool:
    """Check if cmd is in logvals."""
    return any(cmd in k for k in logvals)


def _mnglvs(cmd: int, stanvor: Stanvor) -> None:
    """Go to specified path based on cmd."""
    logvals[next(k for k in logvals if cmd in k)](cmd, stanvor)


def _set_stanvor_handlers(stanvor: Stanvor) -> tuple:
    """Dispatch one key cmd to its corresponding input handler."""
    sent, stvl = stanvor.prompt.sent, stanvor.prompt.stvl
    filedata = stanvor.filedata

    stanvor_handlers = (
        (lambda cmd: cmd == ALT_F12,     lambda _: _set_ashentar(stvl)),
        (lambda cmd: cmd == ALT_END,     lambda _: _add_path_marker(sent)),
        (lambda cmd: cmd == ORD_A,       lambda _: _set_cwdir(sent, stvl)),
        (lambda cmd: cmd == CTL_ENTER,   lambda _: _switch_fileon(filedata)),
        (lambda cmd: cmd in SEND,        lambda _: _process_send(stanvor)),
        (lambda cmd: cmd in O_ORDS,      lambda _: _show_dirlist(stanvor)),
        (lambda cmd: cmd in HNAV,        lambda cmd: _nav_xaxis(cmd, sent)),
        (lambda cmd: cmd in PAD_KEYS,    lambda cmd: _locpad(cmd, stanvor)),
        (lambda cmd: cmd in stv_actions, lambda cmd: _drivestv(cmd, stanvor)),
        (lambda cmd: cmd in intlogren,   lambda cmd: _open(intlogren[cmd], stanvor)),
        (lambda cmd: cmd in web_chnls,   lambda cmd: _set_webchns(cmd, stvl)),
        (lambda cmd: cmd in SEARCH,      lambda cmd: _search(stanvor, cmd)),
        (lambda cmd: _look_logvals(cmd), lambda cmd: _mnglvs(cmd, stanvor)),
    )

    return stanvor_handlers


def _process_stanvor_handlers(cmd: int, stanvor: Stanvor) -> None:
    """
    PERMANENT
    This is the code intented to stay as
    the official process_handlers function.
    Must be recalled so at the end of the refactor.
    """

    for matches, process in stanvor.handlers:
        if matches(cmd):
            process(cmd)
            stanvor.ιdeu = STANVOR
            stanvor.handlers = _set_stanvor_handlers(stanvor)
            break
    else:
        stanvor.prompt.sent = tαg(cmd, stanvor)


def _process_input(stanvor: Stanvor) -> None:
    """Read and process one input event, then refresh the screen."""
    sent, stvl = stanvor.prompt.sent, stanvor.prompt.stvl

    try:
        cmd = stanvor.lanter.stdscr.getch()

        _process_stanvor_handlers(cmd, stanvor)
        # Must be recalled as process_handlers() at the end of the refactor.

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


def _manage_drivers(stanvor: Stanvor) -> None:
    """Manage audio and alarm drivers."""
    set_audio(stanvor.audio)
    stanvor.prompt.stvl.stlαg = play_alarm(stanvor.alarm)


def run_interface(stanvor: Stanvor) -> None:
    """Main loop for the Stαuνor interface."""
    stvmng = StanvorManager()
    stanvor.handlers = _set_stanvor_handlers(stanvor)
    stvl, logαm = stanvor.prompt.stvl, stanvor.logαm

    root = set_invash(stvl)
    logαm.ιlog = set_ilog(root)

    stνlαt(STANVOR, root, 'Iuνor')

    while stanvor.on:
        set_syscursor()   
        set_filedata(stanvor)
        _manage_drivers(stanvor)
        stvmng.run(stanvor)
