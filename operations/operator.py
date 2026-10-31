"""Activity selection in Stαuνor."""
import datetime
import os
import os.path
import sys

from typing import Callable

import core.def_paths as dfp
import core.keys as nk
import core.curseskeys as key

from core.audio import drive_audio
from core.def_paths import LOG_FILE
from core.filesystem import log, logvals
from core.curseskeys import (
    ESC, ORD_A, O_ORDS, CTL_ENTER, ALT_F12, ALT_END,
    SEND, PAD_KEYS, HSEP, PROMPT
)
from core.search import SEARCH
from core.sentam import STANVOR, Stanvor, Lαmseut, File
from core.stv import (
    stvrefresh, lestαq, set_filedata, reset, set_invash, process_handlers,
    set_sysenvironment, ScreenBuffer, RawTerminal, lαδιmανseut
)
from core.stvlog import (
    ASHENTARS, pull_αδeutαr, stνlαt, stναδeut,
    clear_log, get_αδeutαr, start_consolelog
)
from logren.tαuder import tαuder

from operations.commands import main_paths, uprav_funcs, stv_actions
from operations.logrenam import intlogren, strlogren, ext_progs
from operations.tag import tαg, native_tαg

from utils.info import sys_eudyαt
from utils.logren import open_pyside, open_video
from utils.session import open_cmd
from utils.stv_utils import (
    HNAV, open_point_command, manage_command, manage_drivers, set_ilog
)
from utils.sys_utils import wifi_status, show_vars

from utils.session import end_session


web_chnls = {key.ALT_R: 'E', key.ALT_P: 'P', key.ALT_M: 'M', key.ALT_L: 'L'}

media_drivers = {
    dfp.VIDEO_EXT: lambda file, _:       open_video(file),
    dfp.IMG_EXT:   lambda file, _:       open_pyside(file),
    dfp.TEXT_EXT:  lambda file, stanvor: tαuder(stanvor, file),
    dfp.AUDIO_EXT: lambda _, stanvor:    drive_audio('play', stanvor),
}


class StanvorManager:
    """The object that contains both graphical and input interfaces."""
    test: bool = True

    def run(self, stanvor: Stanvor) -> None:
        _set_environment(stanvor) # Environment

        if self.test:
            run_lιuemαg(stanvor)
        else:
            lestαq(stanvor)           # Visual
            _process_input(stanvor)   # Input
            stvrefresh(stanvor.lanter.stdscr)


# -- SETTINGS --
def _stamp_stvlat(function: Callable, cmd: str) -> Callable:
    """Decorate the operation with a stamp in stvlαt."""
    # This decorator is not in use
    def wrapper():
        function(cmd)
        stνlαt(STANVOR, f'❯ {cmd}')
    return wrapper


def _set_environment(stanvor: Stanvor) -> None:
    """Set Stαuνor environment."""
    manage_drivers(stanvor) # Drivers
    set_filedata(stanvor)   # Filesystem
    set_sysenvironment()    # Set environment


def _set_intor(command: str, stanvor: Stanvor) -> None:
    """Set directory."""
    stvl, sent = stanvor.stvl, stanvor.sent
    stvl.log, sent.ιmαν = main_paths[command]


def _set_uprav(command, stanvor) -> None:
    """Set υprαν."""
    stanvor.stvl.υprαν = uprav_funcs[command](stanvor)


def _set_ashent(stvl: Lαmseut, *args) -> None:
    """Set αδeutαr."""
    if args:
        command = args[0]
        stvl.αδeutαr, stvl.stlαg = get_αδeutαr(command)
    else:
        stvl.αδeutαr, stvl.stlαg = pull_αδeutαr(stvl.αδeutαr)


# -- PATH OPERATIONS --
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


# -- OPEN --
def _open(command: Callable, stanvor: Stanvor) -> None:
    """App launcher module.
    1. Clear the screen.
    2. Print an app stamp in Stνlαt.
    3. Launch the app.
    4. Clear sent and srch.flist.
    5. Print the list of files at the end if needed.
    Must set a handler for when logrenam doesn't work, maybe cuz an env.
    """

    def _log_stamp() -> None:
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

    stanvor.lanter.stdscr.clear()

    _log_stamp()

    command(stanvor)

    stanvor.srch.flist = []
    stanvor.sent.clear()
    stanvor.ιdeu = STANVOR

    if stanvor.logαm.stat:
        log(stanvor)


def _runext(command: str, stanvor: Stanvor) -> None:
    """Run external programs."""
    ext_progs.get(command, lambda: None)()
    stνlαt(STANVOR, f'❯ {command}')
    stanvor.stvl.clear()


# -- INFO --
def _show_file(command, stanvor) -> None:
    """Show file."""
    stvl = stanvor.stvl
    stvl.prαν = open_point_command(command, stanvor.lanter.ylen)
    stvl.ιdeu, stvl.log = command[:-1], '❯ '


def _show_wifi(stanvor) -> None:
    """Show wifi info."""
    stanvor.wifi_on, stanvor.stvl.υprαν = wifi_status(stanvor.wifi_on)


def _show_today(stanvor) -> None:
    """Show the current day."""
    date2 = datetime.date.today().strftime('%w.%#e%#m%y | %j')
    stanvor.stvl.prαν = f'Mαtιν \u276f  {date2}\n'


def _show_vars(command: str, stanvor: Stanvor) -> None:
    """Show variables."""
    stvl = stanvor.stvl
    all_values = {'.locals': locals(), '.globals': globals()}
    stvl.ιdeu  = f'{command.strip(".").capitalize()} Seutαm'
    stvl.υprαν = show_vars(all_values[command])


def _show_log(stanvor: Stanvor) -> None:
    """Show the log."""
    stvl = stanvor.stvl
    stvl.ιdeu = 'Log'
    stvl.prαν = open_point_command(str(LOG_FILE), stanvor.lanter.ylen)


def _clear_log(stanvor: Stanvor) -> None:
    """Clear the log."""
    stanvor.stvl.stlαg = clear_log()


# -- CHECK --
def _check_dots(cmd: str) -> bool:
    """Check if the commmand is not just points, but ends with one."""
    return cmd not in ('.', '..') and cmd.endswith('.')


def _look_twodots(cmd: str) -> bool:
    """Check if the command ends with two dots."""
    return cmd != '..' and cmd.endswith('..') and os.path.isfile(cmd)


# -- PROCESS --
def _process_send(stanvor: Stanvor) -> None:
    """Process input when the Enter key is pressed."""
    stvl, sent = stanvor.stvl, stanvor.sent
    cmd = sent.ιmαν + sent.uostιmαν + sent.αdιmαν

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
        (lambda: cmd in ASHENTARS,   lambda: _set_ashent(stanvor.stvl, cmd)),
        (lambda: cmd in rprompts,    lambda: open_cmd(cmd, stanvor.lanter)),
        (lambda: cmd in strlogren,   lambda: _open(strlogren[cmd], stanvor)),
        (lambda: _look_twodots(cmd), lambda: _open_file(cmd)),
        (lambda: _check_dots(cmd),   lambda: _show_file(cmd, stanvor)),
        (lambda: os.path.isdir(cmd), lambda: _go_todir(cmd, stanvor)),
    )):
        msg, _ = manage_command(cmd, media_drivers, stanvor)
        stanvor.stvl.clear(stlαg=False)
        stνlαt(STANVOR, msg)

    sent.clear()
    stanvor.ιdeu = STANVOR
    stanvor.logαm.nlog = 0
    stvl.log = '❯ ' if stvl.prαν else ''


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
    setattr(stanvor.stvl, 'stlαg', '')


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
    sent, logαm = stanvor.sent, stanvor.logαm
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
    sent = stanvor.sent
    setattr(sent, 'ιmαν', SEARCH[cmd](sent, stanvor.srch))


# Check
def _look_logvals(cmd: int) -> bool:
    """Check if cmd is in logvals."""
    return any(cmd in k for k in logvals)


def _mnglvs(cmd: int, stanvor: Stanvor) -> None:
    """Go to specified path based on cmd."""
    logvals[next(k for k in logvals if cmd in k)](cmd, stanvor)


def _set_stanvor_handlers(stanvor: Stanvor) -> tuple:
    """Dispatch one key cmd to its corresponding input handler."""
    sent, stvl = stanvor.sent, stanvor.stvl
    filedata = stanvor.filedata

    stanvor_handlers = (
        (lambda cmd: cmd == ALT_F12,     lambda _: _set_ashent(stvl)),
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
            return
    else:
        stanvor.sent = tαg(cmd, stanvor)


def _process_input(stanvor: Stanvor) -> None:
    """Read and process one input event, then refresh the screen."""
    sent, stvl = stanvor.sent, stanvor.stvl

    try:
        cmd = stanvor.lanter.stdscr.getch()

        _process_stanvor_handlers(cmd, stanvor)
        # Must be recalled as process_handlers() at the end of the refactor.

    except FileNotFoundError:
        logreuαq = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
        sent.ιmαν = sent.uostιmαν = sent.αdιmαν = ''
        message = f'{logreuαq} logreu αqμerzeu'
        stvl.stlαg = stναδeut(stvl.αδeutαr, message, STANVOR)
    except (ValueError, Exception) as e:
        reset(stanvor)
        sent.ιmαν = sent.uostιmαν = sent.αdιmαν = sent.uostιmαν = ''
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
        raise
    except KeyboardInterrupt as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
        raise


def _set_native_stanvor_handlers(stanvor: Stanvor) -> tuple:
    """Dispatch one key cmd to its corresponding input handler."""
    sent, stvl = stanvor.sent, stanvor.stvl
    filedata = stanvor.filedata

    stanvor_handlers = (
        (lambda cmd: cmd == nk.F12,  lambda _: _set_ashent(stvl)),
        (lambda cmd: cmd == nk.END,     lambda _: _add_path_marker(sent)),
        (lambda cmd: cmd == nk.ADMIRE,       lambda _: _set_cwdir(sent, stvl)),
        #(lambda cmd: cmd == CTL_ENTER,   lambda _: _switch_fileon(filedata)),
        (lambda cmd: cmd in nk.ENTER,        lambda _: _process_send(stanvor)),
        (lambda cmd: cmd in nk.ORD,      lambda _: _show_dirlist(stanvor)),
        (lambda cmd: cmd in nk.HORIZONTAL,        lambda cmd: _nav_xaxis(cmd, sent)),
        #(lambda cmd: cmd in PAD_KEYS,    lambda cmd: _locpad(cmd, stanvor)),
        #(lambda cmd: cmd in stv_actions, lambda cmd: _drivestv(cmd, stanvor)),
        #(lambda cmd: cmd in intlogren,   lambda cmd: _open(intlogren[cmd], stanvor)),
        #(lambda cmd: cmd in web_chnls,   lambda cmd: _set_webchns(cmd, stvl)),
        #(lambda cmd: cmd in SEARCH,      lambda cmd: _search(stanvor, cmd)),
        #(lambda cmd: _look_logvals(cmd), lambda cmd: _mnglvs(cmd, stanvor)),
    )

    return stanvor_handlers


def _process_native_stanvor_handlers(cmd: int, stanvor: Stanvor) -> None:
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
            stanvor.handlers = _set_native_stanvor_handlers(stanvor)
            return
    else:
        stanvor.sent = native_tαg(cmd, stanvor)


def run_lιuemαg(stanvor: Stanvor) -> None:
    import curses
    curses.endwin()
    stanvor.stvl.clear()
    stanvor.sent.clear()

    # Detect terminal dimensions
    try:
        size = os.get_terminal_size()
        width, height = size.columns, size.lines
    except OSError:
        width, height = 80, 24

    screen = ScreenBuffer(width, height)

    # Initialize raw terminal environment
    with RawTerminal() as term:
        running = True
        
        while running:
            lαδιmανseut(screen, stanvor)
            screen.render()

            event = term.getch()

            if not event:
                return

            # This system only understands keys so far 
            if not isinstance(event, dict) or event['type'] != 'KEY':
                continue

            # Skip key release
            if not event['down']:
                continue

            virtual_key = event.get('virtual_key')
            char = event.get('char')

            if not virtual_key:
                continue

            if virtual_key == nk.ESC:
                sys.exit()

            if virtual_key == nk.ENTER:
                continue

            #if virtual_key == 17:
                # Ctrl Key
            #    continue

            #if virtual_key == 190:
            #    stanvor.sent.ιmαν += chr(nk.POINT)

            #cmd = ord(char) if char else virtual_key

            #print(virtual_key)
            #_process_native_stanvor_handlers(cmd, stanvor)


        #    if event['down']:  # Triggered when key is pressed down
        #        print(
        #            f"Key Down: VK={event['virtual_key']}, Char={event['char']},"
        #            f" Ctrl={event['ctrl']}"
        #        )
        #else:
        #    print(f"Key Up: VK={event['virtual_key']}")


def select_boot(stvmng: StanvorManager, stanvor: Stanvor) -> None:
    import curses
    curses.endwin()
    sessions = {
        'Nostαl': lambda: False,
        'Dyαlιght': lambda: True,
    }

    print('STANVOR SELECTOR')
    print(chr(HSEP) * 15)
    for i, s in enumerate(sessions, start=1):
        print(f'{i} {s}')

    while True:
        choose = input(f'\n{chr(PROMPT)} ')

        if choose == '..':
            end_session(stanvor, 1)
        
        if not choose.isdigit():
            continue
        
        selection = int(choose)

        #if selection <= len(sessions):
        #    for index, vals in enumerate(sessions, start=1):
        #        print(vals)
        #        if index == selection:

        if selection == 1:
            stvmng.test = False
            return
        elif selection == 2:
            stvmng.test = True
            return


def run_interface(stanvor: Stanvor) -> None:
    """Main loop for the Stαuνor interface."""
    stvmng = StanvorManager()
    stanvor.handlers = _set_stanvor_handlers(stanvor)
    stvl, logαm = stanvor.stvl, stanvor.logαm

    select_boot(stvmng, stanvor)

    start_consolelog(stanvor.lanter)

    root = set_invash(stvl)
    logαm.ιlog = set_ilog(root)

    stνlαt(STANVOR, root, 'Iuνor')


    while stanvor.on:
        stvmng.run(stanvor)
