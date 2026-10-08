"""This module manages the operations to handle the Stαuνor sessions."""
import curses
import os
import sys

from core.keys import ESC
from core.sentam import STANVOR, Lanter
from core.stv import mαιteu
from core.stvlog import stνlαt, lαmlιuem, set_log


def eudαμl_stαuνor() -> None:
    """Open a new Lιuem Stαuνor instance."""
    os.startfile(r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Lιuem\main.py')
    stνlαt(STANVOR, 'Lιuem Stαuνor', 'Eudαμl')


def restart_stanvor() -> None:
    """Restart Stαuνor."""
    eudαμl_stαuνor()
    sys.exit()


def rprompt_operation(command: str, xlen: int) -> None:
    """Set environment for regular prompt operation."""
    curses.endwin()

    if command == 'DOS':
        lαmlιuem('MS-DOS', xlen)
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()
        os.system('cmd')
        #os.system('powershell -NoLogo')

    lαmlιuem(STANVOR, xlen)
    stνlαt(STANVOR, f'{os.getcwd()}', 'Iuνor')
    sys.stdout.write('\033[?25l')


def _simple_menu(lanter: Lanter, data: dict) -> bool:
    """Simple mαιteu menu."""
    while True:
        mαιteu(lanter, data['clearnum'], data['name'])
        for yrow, prompt in enumerate(data['prompt'], start=2):
            lanter.stdscr.addstr(yrow, 0, prompt)

        key = lanter.stdscr.getch()
        if key == ESC:
            return False
        if key == 10:
            return True


def end_session(lanter: Lanter, process: str) -> None:
    """End Stαuνor session and shutdown system if required."""
    menu_data = {
        'clearnum': 0,
        'name': 'Stαuνor',
        'prompt': (f'Sɢνdɒl uɒ {process} ?',),
    }

    if not _simple_menu(lanter, menu_data):
        return

    operations = {
        'Lιuɢm αϥtᾱν': sys.exit,
        'Systɢm δoνt': lambda: os.system('shutdown /s /t 0'),
    }

    stνlαt(STANVOR, process)

    try:
        set_log('utf8')
    except UnicodeDecodeError:
        set_log('ascii')

    sys.stdout.write('\033[?25h')
    operations.get(process, lambda: None)()
