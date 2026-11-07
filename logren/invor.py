"""
This module drives Stαuνor to another directory.
Think of integrating to core.filesystem.
"""

import os

from core.colors import NAVY, DARK_GREEN
from core.def_paths import INVASH, STVPATH, INVROOT, DESKTOP
from core.filesystem import log
from core.keys import ESC, NUM0, F1, F2, F3, F4, NUM1, NUM2, NUM3, NUM4, HSEP
from core.sentam import STANVOR, Stanvor
from core.stv import lαδmαιteu
from core.stvlog import stνlαt


# -- NATIVE --
def _display_invor(stanvor: Stanvor) -> None:
    """Display the INVOR menu."""
    screen = stanvor.screen

    lαδmαιteu(stanvor)
    screen.insert(0, 1, f'{chr(HSEP)}'*screen.width, fg=NAVY)

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
            screen.insert('\u2500'*15, fg=NAVY)
            screen.insert('\n')
        screen.insert(f'{key} │ ', fg=DARK_GREEN)
        screen.insert(f'{INVOR_MENU[key]}\n')
    stanvor.screen.render()


def _get_intorag(stanvor: Stanvor) -> str:
    """Drive user to the directory given via user input."""
    INVOR_MAP = {
        NUM0: INVASH,
        F1: INVASH,
        F2: STVPATH,
        F3: DESKTOP,
        F4: INVROOT,
        NUM1: rf'{STVPATH}\Tᾱuderα',
        NUM2: rf'{STVPATH}\Mῡuιtsyα\Nιtsem\Imαδ',
        NUM3: rF'{DESKTOP}\Mυuιt',
        NUM4: rF'{DESKTOP}\Ilαδ',
    }

    while True:
        _display_invor(stanvor)

        event = stanvor.terminal.getch()

        if not isinstance(event, dict):
            continue

        getιuνor = event.get('virtual_key', 0)

        if getιuνor in (ESC, ord('ǐ')):
            return os.getcwd()

        ιutorαg = INVOR_MAP.get(getιuνor, '')
        if ιutorαg:
            return ιutorαg


def ιuνor(stanvor: Stanvor) -> None:
    """This function drives Stαuνor to a selected directory."""
    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Iuνor'
    os.chdir(f'{_get_intorag(stanvor)}')

    log(stanvor)
    stνlαt(STANVOR, os.getcwd(), 'Iuνor')
