"""This module drives Stαuνor to another directory."""

import curses
import os

import utils.stv_utils as stv
from stvlog import stνlαt, STANVOR, STVPATH, INVASH, INVROOT
from utils.keys import *


def display_invor(lanter: Lanter) -> None:
    """Display the INVOR menu."""
    stv.mαιteu(lanter.stdscr, lanter.xlen, 0, 'Iuνor')
    lanter.stdscr.addstr(1, 0, '\u2500'*lanter.xlen, curses.color_pair(1))

    INVOR_MENU = {
        '·1': 'Iuναδ',
        '·2': 'Olyαν',
        '·3': 'Desktop',
        '·4': 'Root',
        ' 1': 'Tᾱuderα',
        ' 2': 'Nιseu Mυuιt',
        ' 3': 'Mυuιt',
        ' 4': 'Ilαδ',
    }

    for index, key in enumerate(INVOR_MENU.keys()):
        if index == 4:
            lanter.stdscr.addstr('\u2500'*15, curses.color_pair(1))
            lanter.stdscr.addstr('\n')
        lanter.stdscr.addstr(f'{key} │ ', curses.color_pair(3))
        lanter.stdscr.addstr(f'{INVOR_MENU[key]}\n')


def get_intorag(lanter: Lanter) -> str:
    INVOR_MAP = {
        NUM0: INVASH,
        F1: INVASH,
        F2: STVPATH,
        F3: r'C:\Users\Leane\OneDrive\Escritorio',
        F4: INVROOT,
        NUM1: rf'{STVPATH}\Tᾱuderα',
        NUM2: rf'{STVPATH}\Mῡuιtsyα\Nιtsem\Imαδ',
        NUM3: r'C:\Users\Leane\OneDrive\Escritorio\Mυuιt',
        NUM4: r'C:\Users\Leane\OneDrive\Escritorio\Ilαδ',
    }

    while True:
        display_invor(lanter)

        getιuνor = lanter.stdscr.getch()
        if getιuνor in (27, ord('ǐ')):
            return os.getcwd()

        ιutorαg = INVOR_MAP.get(getιuνor, '')
        if ιutorαg:
            return ιutorαg


def ιuνor(stanvor: Stanvor) -> None:
    """This function drives Stαuνor to a selected directory."""
    os.chdir(f'{get_intorag(stanvor.lanter)}')

    stanvor.lanter.start, stanvor.lanter.end = 0, stanvor.lanter.ylen - 5
    stv.log(stanvor)
    stνlαt(STANVOR, os.getcwd(), 1)
    stanvor.lanter.stdscr.nodelay(True)
