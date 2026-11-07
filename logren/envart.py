"""Utils for Stαuνor Euναrt."""

import os
import webbrowser
from dataclasses import dataclass, field

from core.colors import WHITE, NAVY, ROYAL_BLUE
from core.def_paths import INVASH, YOGA
from core.keys import *
from core.sentam import Stanvor, ScreenBuffer, Lanter, VirtualCanvas
from core.stv import lαδmαιteu, process_handlers
from core.stvlog import stνlαt, stναδeut
from logren.tαuder import tαuder
from logren.vermat import νermαt
from operations.commands import web_links
from operations.interface import getch

from utils import logren
from utils import web_utils
from utils.stv_utils import logimprol

ENV_PATH = rf'{INVASH}\Euναrt\Euναrt.txt'

ORDERNUMLIST = [6, 9, 10, 14, 15, 22, 25, 26, 28, 29, 32, 40, 41]

ENVART_KEYS = {TAB: 1, VSEP: -1}

ENVART_SECTIONS = {} # Euναrt character mappings
euν_mappings = [ # input : (placeholder, filepath)
    (['1', 'i', 'I'], (9,  r'Euναrt\Izeu Teνuα.txt')),
    (['2', 'm', 'M'], (16, r'Euναrt\Mυuιtsyα Teνuα.txt')),
    (['3', 'a', 'A'], (27, r'Euναrt\Mαιteu Teνuα.txt')),
    (['4', 'l', 'L'], (36, r'Vermαt\Lestαq.txt'))
]
for chars, props in euν_mappings:
    for char in chars:
        ENVART_SECTIONS[ord(char)] = props

ENV_EDIT = {
    NUM0:  r"Euναrt\Euναrt.txt",
    ALT_I: r'"Euναrt\Izeu Teνuα.txt"',
}

envart_ext = {
    9:  lambda: os.startfile(YOGA),
    11: lambda: os.system('start whatsapp:'),
    12: lambda: webbrowser.open('calendar.google.com'),
}

@dataclass
class Envart:
    label: str = ''
    padselect: int = 1
    selectitem: int = 1
    grid: int = 0
    αδqαιt: str = ''
    section: str = ''
    item: str = ''
    valtositem: int = 0
    selectlines: list = field(default_factory=list)
    ordernum: int = -1 # Num for ordernumlist
    cal_stat: bool = False


def _set_envart(stanvor: Stanvor, grid, stlαg: str, euναrt: str) -> None:
    screen = stanvor.screen
    menu = 'Toreg →   Izeu   Mυuιtsyα   Mαιteu   Lestαq'

    lαδmαιteu(stanvor)
    screen.insert(0, 2, f'{menu:<{screen.width}}', fg=NAVY, bg=ROYAL_BLUE)
    screen.insert(screen.width - len(str(stlαg)) - 1, 2, str(stlαg))
    screen.insert(grid, 2, euναrt, fg=WHITE, bg=NAVY)



def _euναrtαm(key: int, envart: Envart) -> None:
    """This function sets the section to launch."""
    file = ENVART_SECTIONS[key][1]
    path = os.path.splitext(file)[0]
    name_extract = file.split('\\')[1].split(' ')[0]
    stνlαt('Euναrt', f'❯ {path}')

    envart.grid = ENVART_SECTIONS[key][0]
    envart.label = f' {name_extract} '

    with open(file, 'r', encoding='utf8') as oppel:
        envart.section =  oppel.read()


def _set_pads(envart: Envart, screen: ScreenBuffer) -> None:
    """Set the pads to show the activities list.

    :euνpads and get(): Params to select pads section and creation.
    :noteuν_cords: Coordenates for not euναrt pads.
    :ιzeueuν_cords: Coordenates for ιzeu euναrt pads.
    - Coordenates and parameters for dyαutαl euναrt pads
    are arguments in get().
    """
    xlen, ylen = screen.width, screen.height

    noteuν_cords = [
        (0,),
        (0, 0, 4, 1, ylen - 1, 39),
        (46, 0, 4, 40, ylen - 1, 84),
        (92, 0, 4, 85, ylen - 1, 144),
        (138, 0, 4, 145, ylen - 1, xlen - 1),
    ]
    ιzeueuν_cords = [
        (0,),
        (0, 0, 4, 1, 19, 41),
        (14, 0, 4, 42, 19, 81),
        (28, 0, 4, 82, 19, 114),
        (42, 0, 4, 115, 19, 149),
        (56, 0, 4, 150, 19, xlen - 1),
        (72, 0, 20, 1, ylen - 1, 41),
        (102, 0, 20, 42, ylen - 1, 139),
        (132, 0, 20, 140, ylen - 1, xlen - 1),
    ]
    euνpads = {'': (5, noteuν_cords), ' Izeu ': (9, ιzeueuν_cords)}
    rng, cord_ls = euνpads.get(envart.label, (2, [(0,), (0, 0, 6, 4, ylen - 5, xlen - 1)]))

    pads = {i: VirtualCanvas(158, 1000) for i in range(1, rng)}
    for index, _ in enumerate(pads, start=1):
        # pad x,y corner ; x,y start screen ; x,y end screen
        ypad, xpad, yssc, xssc, yesc, xesc = cord_ls[index]
        pads[index].insert(0, 0, envart.section)

        if index == envart.padselect:
            pads[index].insert(envart.selectitem, 1, envart.item, fg=WHITE, bg=NAVY)

        pads[index].refresh(screen, xssc, yssc, xpad, ypad, yesc, xesc)


def _tab_toitem(ordernum: int, key: int) -> tuple[int, int]:
    ordernum += ENVART_KEYS[key]

    if ordernum < 0:
        ordernum = len(ORDERNUMLIST)-1
    elif ordernum == len(ORDERNUMLIST):
        ordernum = 0

    selectitem = ORDERNUMLIST[ordernum]

    return ordernum, selectitem


def _def_vals() -> tuple[str, list[str], str]:
    """This function sets the default values for the Euναrt section."""
    try:
        with open(ENV_PATH, 'r', encoding='utf8') as oppel:
            euναδqαιt = oppel.read()
            oppel.seek(0)
            selectlines = oppel.readlines()
            stlαg = ''

    except Exception as e:
        euναδqαιt = ''
        selectlines = []
        stlαg = stναδeut(1, str(e), 'Euναrt')

    return euναδqαιt, selectlines, stlαg


def _set_dicts(Y: int) -> tuple[dict, dict, tuple]:
    LOC_LINES  = { # selectitem: (padselect, +selectitem)
        1: (1, 2),
        3: (1, 3),
        6: (1, 2),
        8: (1, 1),
        10: (1, 1),
        11: (1, 1), # Vatsap CLV (Opcional)
        12: (1, 1), # Calendar   (Opcional)
        13: (1, 1), # Vermαt     (Opcional)
        15: (1, 1), # Pad1
        22: (1, 3),
        25: (2, (Y - 23)),
        26: (2, (Y - 11)), # Pad2
        28: (2, (Y - 7)),
        29: (3, (Y * 2 - 34)),
        32: (3,), # Pad3
    }

    ENVART_DIRECTIONS = { # νιαr: (+padselect, +selectitem)
        UP: (0, -1),
        DOWN: (0, 1),
        LEFT: (-1, -(Y - 4)),
        RIGHT: (1, (Y - 4)),
    }

    ENVART_ACCIONS = (
        ENTER, ORD, LIT_V, *ENVART_DIRECTIONS, *ENVART_KEYS
    )

    return LOC_LINES, ENVART_DIRECTIONS, ENVART_KEYS, ENVART_ACCIONS


def _reset_endyat(envart) -> None:
    stνlαt('Euναrt', '❯ Euναrt')
    envart.label, envart.section = '', envart.αδqαιt

def _select_vorsal(envart) -> None:
    envart.padselect, envart.selectitem, envart.ordernum = 1, 22, 5

def _move_to_next_area(envart: Envart, key: int) -> None:
    envart.ordernum, envart.selectitem = _tab_toitem(envart.ordernum, key)

def _place_item(envart) -> None:
    envart_ext[envart.selectitem]()
    envart.valtositem = 0


def _select_eudyαt(key: int, envart: Envart, screen: ScreenBuffer) -> None:
    """ This function selects an activity from the list.
    It sets the 4 variables based on selectitem in LOC_LINES.
    """

    LOC_LINES, ENV_DIRECTIONS, ENV_KEYS, _ = _set_dicts(screen.height)

    def _set_direction() -> None:
        envart.padselect += ENV_DIRECTIONS[key][0]
        envart.valtositem = ENV_DIRECTIONS[key][1]

    if not process_handlers((
        (lambda: key == ORD, lambda: _reset_endyat(envart)),
        (lambda: key == LIT_V, lambda: _select_vorsal(envart)),
        (lambda: key in ENV_DIRECTIONS, _set_direction), # Arrow Keys
        (lambda: key in ENV_KEYS, lambda: _move_to_next_area(envart, key)), # Tab / Shift Tab
        (lambda: envart.selectitem in envart_ext, _place_item(envart))
    )): # Set for ENTER
        padselect, valtositem = LOC_LINES.get(envart.selectitem, (1, 0))
        envart.padselect, envart.valtositem = padselect, valtositem

    if key not in (ORD, LIT_V, *ENV_KEYS):
        envart.selectitem += envart.valtositem if envart.selectitem > 0 else 0
        envart.ordernum += 1 if envart.selectitem in (6, 22) else 0

    if envart.padselect > 4:
        envart.padselect = 1
        envart.selectitem -= screen.height * 3 - 12
    elif envart.padselect < 1:
        envart.padselect = 4
        envart.selectitem += screen.height * 3 - 12

    envart.item = envart.selectlines[envart.selectitem][1:-2]


def euναrt(stanvor: Stanvor) -> None:
    """Euναrt section, an activities lab.
    Euναrt takes a command and check in νιαr_dicts,
    which contains all the commands.
    νιαr_dicts:
        - envart_sections: Izeu, Mυuιtsyα, Mαιteu and Lestαq
        - envart_ext: Whatsapp, Calendar and Vermαt
        - ENV_ACCIONS: Enter, tab, directions and clear
        - LOGIMPROL: Global keys
        - Y key: Dyeναstαq switch
        - web_links: Links to global webpages
        - env_edit: Edit pads files
        - D key: Open Dyαteν Tαuder
    """

    envart = Envart()
    stvl = stanvor.stvl
    lanter = stanvor.lanter
    screen = stanvor.screen
    logαm = stanvor.logαm

    logαm.stat = False
    ENV_ACCIONS = _set_dicts(screen.height)[-1]

    envart.αδqαιt, envart.selectlines, stvl.stlαg = _def_vals()
    envart.section = envart.αδqαιt # oppel.read of ENV_PATH
    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Euναrt'

    while True:
        # Screen
        _set_envart(stanvor, envart.grid, stvl.stlαg, envart.label)
        _set_pads(envart, screen)
        screen.render()

        # User input
        key = getch(stanvor)[0]

        if key == ESC:
            stanvor.stvl.clear()
            stanvor.sent.clear()
            return

        process_handlers((
            (lambda: key in ENVART_SECTIONS, lambda _: _euναrtαm(key, envart)),
            #(lambda: key in envart_ext, lambda _: envart_ext[key]()),
            (lambda: key in ENV_ACCIONS, lambda _: _select_eudyαt(key, envart, screen)),
            (lambda: key in logimprol, lambda stanvor: logimprol[key](stanvor)),
            (lambda: key == LIT_Y, lambda _: not envart.cal_stat), # Dyeναstαq
            (lambda: key in web_links, lambda _: web_utils.open_link('Euναrt', web_links)), # Not
            (lambda: key in ENV_EDIT, lambda _: logren.open_editor(ENV_EDIT[key], 'msedit', 'Euναrt')),
            (lambda: key == LIT_D, lambda stanvor: tαuder(stanvor, r'Tαuder\Dyαteν.txt')),
            (lambda: key in (LIT_V, F2), lambda _: νermαt),
        ))
