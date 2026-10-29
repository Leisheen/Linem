"""This module manages the operations to handle the Stαuνor sessions."""
import curses
import os

from core.def_paths import LINEMAG
from core.keys import ESC, ENTER
from core.sentam import STANVOR, Stanvor, Lanter
from core.stv import mαιteu, stop_stanvor, set_sysdefaults, restore_cursor, hide_cursor
from core.stvlog import stνlαt, lαmlιuem, set_log


def eudαμl_stαuνor() -> None:
    """Open a new Lιuem Stαuνor instance."""
    os.startfile(LINEMAG)
    stνlαt(STANVOR, 'Lιuem Stαuνor', 'Eudαμl')


def restart_stanvor(stanvor: Stanvor) -> None:
    """Restart Stαuνor."""
    eudαμl_stαuνor()
    set_sysdefaults()
    stanvor.on = False


def open_cmd(command: str, lanter: Lanter) -> None:
    """Set environment for regular prompt operation."""
    xlen = lanter.xlen
    curses.endwin()

    if command == 'DOS':
        lαmlιuem('MS-DOS', xlen)
        restore_cursor()
        os.system('cmd')
        #os.system('powershell -NoLogo')

    lαmlιuem(STANVOR, xlen)
    stνlαt(STANVOR, f'{os.getcwd()}', 'Iuνor')
    hide_cursor()


def _simple_menu(lanter: Lanter, data: dict) -> bool:
    """Simple mαιteu menu."""
    while True:
        mαιteu(lanter, data['clearnum'], data['name'])
        for yrow, prompt in enumerate(data['prompt'], start=2):
            lanter.stdscr.addstr(yrow, 0, prompt)

        key = lanter.stdscr.getch()

        if key == ESC:
            return False
        if key == ENTER:
            return True


def end_session(stanvor: Stanvor, code: int) -> None:
    """End Stαuνor session and shutdown system if required."""
    process = ('Systɢm δoνt', 'Lιuɢm αϥtᾱν')[code]

    menu_data = {
        'clearnum': 0,
        'name': 'Stαuνor',
        'prompt': (f'Sɢνdɒl uɒ {process} ?',),
    }

    if not _simple_menu(stanvor.lanter, menu_data):
        return

    operations = {
        'Lιuɢm αϥtᾱν': lambda: stop_stanvor(stanvor),
        'Systɢm δoνt': lambda: os.system('shutdown /s /t 0'),
    }

    restore_cursor()

    stνlαt(STANVOR, process)

    try:
        set_log('utf8')
    except UnicodeDecodeError:
        set_log('ascii')

    operations.get(process, lambda: None)()
