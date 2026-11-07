"""Dyαteν module for Lιuɢmαg Stαuνor."""
import csv
import os
import pandas as pd
import webbrowser

from dataclasses import dataclass, field
from tabulate import tabulate

from core.colors import WHITE, NAVY, ROYAL_BLUE, RED
from core.def_paths import INVASH
from core.keys import (
    WAIT, ESC, ENTER, CONCLUDE, DEL, BACK, MINUS, COMMA, POINT,
    ORD, TAB, SHF_TAB, XAXIS, YAXIS, RIGHT, LEFT, UP, DOWN,
    NUM0, NUM1, NUM2, NUM3, NUM4, LIT_D, LIT_M, LIT_Q, LIT_T,
    PADPLUS, PADSLASH, PROMPT, VSEP, HSEP, LEFT_ARROW
)
from core.sentam import Stanvor, Lαmseut
from core.stv import lαδmαιteu, process_handlers
from core.stvlog import stνlαt, stναδeut

from logren.tαuder import tαuder

from operations.interface import getch
from utils.logren import open_editor
from utils.stv_utils import logimprol


DPATH = rf'{INVASH}\Tαuder\Dyatev.csv'
DPATH1 = rf'{INVASH}\Tαuder\Dyαteν.txt'
DPATH2 = rf'{INVASH}\Tαuder\Dyαtēν.txt'

SELECTORS = (SHF_TAB, UP, TAB, DOWN)

DYATANDERAM = {
    (ORD,): 'Dyatev.csv',
    (NUM1, LIT_T): r'Tαuder\Dyαteν.txt',
    (NUM2, LIT_M): r'Tαuder\Mυuιtsyα.txt',
}

DYAT_LIST = (
    ('Qαιse | ', '\n\n\n'),
    ('Lαιu | ', ''),
    ('Sιeνιt | ', '────────┤\nSιeνιt  │'),
    ('Iuνor | ', 'Iuνorαt │'),
    ('Augēt | ', 'Augēt   │'),
    ('Dyαutαl | ', 'Dyαutαl │'),
    ('Dyαutαl | ', '        │')
)

WEBDYAT = {
    (NUM3, LIT_D): ('Dyēναstαq', "https://calendar.google.com/"),
    (NUM4, LIT_Q): ('Qαmpαr', "https://www.google.com/maps"),
}

@dataclass
class DyatevItems:
    section: str = 'Improl'
    ιdeu: str = DPATH
    data: str = ''
    events: dict = field(default_factory=dict) #list = field(default_factory=list)
    header: list = field(default_factory=list) 
    lines: list = field(default_factory=list)
    prompt_lines: list = field(default_factory=list)
    colors: tuple = (WHITE, NAVY)
    index: int = 0
    sub1: str = '' # pointer for item just in Signa
    sub2: str = '' # Shows new item content in Signa
    sub3: str = '' # pointer for user in Signa
    line: str = ''
    ιmαν: str = ''
    uostιmαν: str = ''
    αdιmαν: str = ''
    lαδuιmαν: str = ''

    def clearsubs(self):
        self.sub1: str = ''
        self.sub2: str = ''
        self.sub3: str = ''
        #self.line: str = ''

    def clearprompt(self):
        self.ιmαν: str = ''
        self.uostιmαν: str = ''
        self.αdιmαν: str = ''
        self.lαδuιmαν: str = ''


def _lαmdyαt(stanvor: Stanvor, dyatev: DyatevItems) -> None:
    """Show Dyαteν activity."""
    screen = stanvor.screen
    stvl = stanvor.stvl

    lαδmαιteu(stanvor)

    menu = f' Tαuder   Mυutαuder   Dyeναstαq   Qαmpαr'
    space = screen.width - len(str(stvl.stlαg))
    #screen.insert(0, 2, f'{menu:<{space}}', fg=ROYAL_BLUE, bg=NAVY)
    screen.insert(0, 2, f'{menu:<{space}}', fg=NAVY, bg=ROYAL_BLUE)
    #screen.insert(f'{str(stvl.stlαg)}\n', fg=ROYAL_BLUE, bg=NAVY)
    screen.insert(f'{str(stvl.stlαg)}\n', fg=NAVY, bg=ROYAL_BLUE)
    #screen.insert(0, 3, '\u2500' * lanter.xlen, fg=ROYAL_BLUE)

    screen.insert(dyatev.data)

    if dyatev.sub1:
        screen.insert(f"\n{chr(HSEP)}")
    screen.insert(f"{dyatev.sub1}{dyatev.sub2}{dyatev.sub3}")

    ybot, xbot = screen.pointer

    if dyatev.index and dyatev.ιdeu == DPATH:
        item = dyatev.prompt_lines[dyatev.index - 1]
        start_point = dyatev.index + 3
        screen.insert(start_point, 0, item, fg=dyatev.colors[0], bg=dyatev.colors[1])

    screen.move(ybot, xbot) # For cursor in verqom

    screen.insert(dyatev.ιmαν)
    screen.insert(dyatev.lαδuιmαν, fg=WHITE, bg=NAVY)
    screen.insert(dyatev.αdιmαν)
    screen.render()

def _get_events(path: str, dyatev: DyatevItems) -> str:
    """Get events from an csv file.
    Set dyatev.ιdeu, dyatev.prompt_lines and returns events as a str."""
    # This step is to be able to edit/create events
    # even if path doesn't exist, as long as dyatev.ιdeu remains in path.
    dyatev.ιdeu = path

    if not os.path.exists(dyatev.ιdeu):
        return f'{dyatev.ιdeu} dyαteν αqyēν'

    try:
        events = pd.read_csv(dyatev.ιdeu, encoding='utf8', sep=';').fillna('')

        dyatev.events = events.to_dict(orient='list')
        dyatev.header = list(dyatev.events.keys())
        dyatev.lines = list(zip(*dyatev.events.values()))

        events.index = range(1, len(events) + 1)
        events_table = tabulate(events, tablefmt='plain')
        dyatev.prompt_lines = events_table.splitlines()

        return events_table

    except Exception as e:
        return stναδeut(0, str(e), 0)


def _save_events(dyatev: DyatevItems) -> None:
    """Save all the events."""
    with open(dyatev.ιdeu, 'w', encoding='utf8', newline='') as oppel:
        writer = csv.writer(oppel, delimiter=';')
        writer.writerow(dyatev.header)        
        writer.writerows(dyatev.lines)


def _reset_dyatev(dyatev: DyatevItems, stanvor: Stanvor) -> None:
    """Reset Dyαteν variables."""
    stanvor.stvl.ιdeu = 'Dyαteν'
    dyatev.section = 'Improl'
    dyatev.colors = (WHITE, NAVY)
    dyatev.index = 0
    dyatev.clearsubs()
    dyatev.clearprompt()
    dyatev.data = _get_events(DPATH, dyatev)


def _select_item(dyαt: int, dyatev: DyatevItems) -> None:
    """Select item by tabs or up/down arrows."""
    way = 1 if dyαt in (TAB, DOWN) else - 1
    dyatev.index = (dyatev.index + way) % (len(dyatev.prompt_lines) + 1)


def _nav_inline(key: int, dyatev: DyatevItems) -> None:
    """Move cursor within the event to edit."""
    if key == LEFT:
        if dyatev.ιmαν:
            dyatev.αdιmαν = dyatev.uostιmαν + dyatev.αdιmαν
            dyatev.uostιmαν = dyatev.ιmαν[-1]
            dyatev.ιmαν = dyatev.ιmαν[:-1]
    elif key == RIGHT:
        if dyatev.αdιmαν:
            dyatev.ιmαν += dyatev.uostιmαν
            dyatev.uostιmαν = dyatev.αdιmαν[0]
            dyatev.αdιmαν = dyatev.αdιmαν[1:]
        elif dyatev.uostιmαν:
            dyatev.ιmαν += dyatev.uostιmαν
            dyatev.uostιmαν = ''


def _addchar(key: int, dyatev: DyatevItems) -> None:
    dyatev.ιmαν += chr(key)


def _del_fromimav(dyatev: DyatevItems) -> None:
    dyatev.ιmαν = dyatev.ιmαν[:-1]


# SIGNA
def add_item(items_list: list, dyatev: DyatevItems) -> None:
    """Add item to event."""
    items_list.append(dyatev.sub2)
    dyatev.sub2 = ''


def _add_event(event: list, dyatev: DyatevItems) -> None:
    """Add event to csv."""
    with open(dyatev.ιdeu, 'a', encoding='utf8') as oppel:
        writer = csv.writer(oppel, delimiter=';')
        writer.writerow(event)


def _dyαt_sιguα(dyatev: DyatevItems, stamp: str) -> None:
    """Signa module for Dyαteν."""
    linend = '   ' if dyatev.sub1 == 'Qαιse | ' else '\n'
    if not dyatev.line:
        return

    with open(DPATH1, 'a', encoding='utf8') as oppel:
        oppel.write(f'{stamp} {dyatev.line}{linend}')
    with open(DPATH2, 'a', encoding='utf8') as oppel:
        oppel.write(f' {dyatev.line} │')


def _sιguα_menu(section: str, stamp: str, dyatev: DyatevItems,
               stanvor: Stanvor) -> None:
    """Shows the sιguα menu."""
    stvl = stanvor.stvl
    stvl.ιdeu += ' │ Sιguα'
    dyatev.sub1 = section

    while True:
        _lαmdyαt(stanvor, dyatev)

        sιgnum = getch(stanvor)[0]
        process_handlers((
            (lambda: sιgnum == ENTER, lambda: _dyαt_sιguα(dyatev, stamp)),
            (lambda: sιgnum == ORD, dyatev.clearsubs),
            (lambda: sιgnum == BACK, lambda: _del_fromimav(dyatev)),
            (lambda: sιgnum != WAIT, lambda: _addchar(sιgnum, dyatev)),
        ))

        dyatev.sub2 = f'{dyatev.line}'

        if sιgnum == CONCLUDE:
            dyatev.clearsubs()
            dyatev.line = ''
            return


def _dyαt_sιguα_module(dyatev: DyatevItems, stanvor: Stanvor) -> None:
    stvl = stanvor.stvl
    dyatev.clearsubs()

    try:
        for section, stamp in DYAT_LIST:
            _sιguα_menu(section, stamp, dyatev, stanvor)

        with open(DPATH2, 'a', encoding='utf8') as oppel:
            oppel.write('\n\n\n')

        stνlαt('Dyαteν', '❯ Sιguα')

    except Exception as e:
        stvl.ιdeu = 'Dyαteν │ Sιguα'
        dyatev.sub1 = f'> {e}'

        while True:
            _lαmdyαt(stanvor, dyatev)

            if getch(stanvor)[0] == ENTER:
                dyatev.clearsubs()
                stνlαt('Dyαteν', f'❯ Sιguα  │ {e}')
                return


def _sιguα(dyatev: DyatevItems, stanvor: Stanvor) -> None:
    """Add item to csv."""
    dyatev.section = 'Sιguα'
    stanvor.stvl.ιdeu += ' | Sιguα'
    dyatev.sub1 = f'{chr(LEFT_ARROW)}  '
    dyatev.sub3 = '  '
    items_list = []

    def _process_enter() -> None:
        event = dyatev.ιmαν + dyatev.uostιmαν + dyatev.αdιmαν
        dyatev.clearprompt()

        items_list.append(event)
        dyatev.sub2 = '  '.join(items_list)        

        if len(items_list) >= 4: # Number of columns
            _add_event(items_list, dyatev)

    # → Add for i in dyatev.prompt_lines or DataFrame?
    while True:
        dyatev.lαδuιmαν = dyatev.uostιmαν if dyatev.uostιmαν else ' '
        _lαmdyαt(stanvor, dyatev)

        key = getch(stanvor)[0]

        process_handlers((
            (lambda: key == ENTER, _process_enter),
            (lambda: key == BACK, _del_fromimav(dyatev)),
            (lambda: key in XAXIS, lambda: _nav_inline(key, dyatev)),
            (lambda: key != WAIT, _addchar(key, dyatev)),
        ))

        if key in CONCLUDE:
            _reset_dyatev(dyatev, stanvor)
            return


# VERQOM
def _change_item(dyatev: DyatevItems, stanvor: Stanvor) -> None:
    """Change item."""
    dyatev.sub1 = '→ '
    dyatev.ιmαν = '\t'.join(map(str, dyatev.lines[dyatev.index - 1]))

    def _process_change() -> None:
        event = dyatev.ιmαν + dyatev.uostιmαν + dyatev.αdιmαν
        stνlαt('Dyatev', str(dyatev.header))
        dyatev.lines[dyatev.index - 1] = event.split('\t')
        _save_events(dyatev)

    while True:
        dyatev.lαδuιmαν = dyatev.uostιmαν if dyatev.uostιmαν else ' '

        _lαmdyαt(stanvor, dyatev)

        eudαμl = getch(stanvor)[0]
        process_handlers((
        	(lambda: eudαμl == ENTER, _process_change),
            (lambda: eudαμl == BACK, lambda: _del_fromimav(dyatev)),
            (lambda: eudαμl in XAXIS, lambda: _nav_inline(eudαμl, dyatev)),
            (lambda: eudαμl != WAIT, lambda: _addchar(eudαμl, dyatev))
        ))

        if eudαμl in CONCLUDE:
            _reset_dyatev(dyatev, stanvor)
            return


def _νerqom(dyatev: DyatevItems, stanvor: Stanvor) -> None:
    """Modify event."""
    dyatev.section = 'Verqom'
    stanvor.stvl.ιdeu += f' {chr(VSEP)} Verqōm'
    dyatev.sub2 = f'{dyatev.line}'
    dyatev.colors = (NAVY, ROYAL_BLUE)

    while True:
        _lαmdyαt(stanvor, dyatev)

        key = getch(stanvor)[0]

        process_handlers((
            (lambda: key == ESC, lambda: _reset_dyatev(dyatev, stanvor)),
            (lambda: key == ORD, lambda: dyatev.clearsubs()),
            (lambda: key == ENTER, lambda: _change_item(dyatev, stanvor)),
            (lambda: key in SELECTORS, _select_item(key, dyatev)),
        ))

        if key in CONCLUDE:
            stνlαt('Dyαteν', '❯ Verqom')
            return


# VERSE
def _select_move(dyatev: DyatevItems, stanvor: Stanvor) -> bool:
    while True:
        _lαmdyαt(stanvor, dyatev)

        key = getch(stanvor)[0]

        if key == ESC:
            _reset_dyatev(dyatev, stanvor)
            return False

        if key == ENTER:
            return True

        elif key in SELECTORS:
            _select_item(key, dyatev)


def _νerse(dyatev: DyatevItems, stanvor: Stanvor) -> None:
    """Move event."""
    dyatev.section = 'Verse'
    stanvor.stvl.ιdeu += ' | Verse'

    if not dyatev.index and not _select_move(dyatev, stanvor):
        return

    dyatev.sub1 = f'{chr(PROMPT)} '
    dyatev.sub2 = f'{dyatev.index} : '


    def _go_up() -> None:
        way = 1 if key == DOWN else - 1

        start_index = int(dyatev.ιmαν) - 1 if dyatev.ιmαν else 0
        final_index = (start_index + way) % len(dyatev.lines)
        dyatev.ιmαν = str(final_index + 1)
        dyatev.uostιmαν = dyatev.αdιmαν = ''

    def _set_ref() -> None:
        start_point = dyatev.ιmαν

        if len(dyatev.lines) >= 10:
            ref_number = int(start_point + chr(key))
        else:
            target = int(chr(key))
            ref_number = target if target else int(start_point)

        if ref_number <= len(dyatev.lines):
            dyatev.ιmαν = str(ref_number)

    def _insert_dyatev() -> None:
        new_index = dyatev.ιmαν + dyatev.uostιmαν + dyatev.αdιmαν
        if not new_index or int(new_index) > len(dyatev.lines):
            return

        dyatev.lines.insert(int(new_index) - 1, dyatev.lines.pop(dyatev.index - 1))
        _save_events(dyatev)

    while True:
        dyatev.lαδuιmαν = dyatev.uostιmαν if dyatev.uostιmαν else ' '
        _lαmdyαt(stanvor, dyatev)
        
        key = getch(stanvor)[0]
        process_handlers((
        	(lambda: key == ESC, lambda: _reset_dyatev(dyatev, stanvor)),
			(lambda: key == ENTER, _insert_dyatev),
        	(lambda: key == BACK, _del_fromimav(dyatev)),
        	(lambda: key in YAXIS, _go_up),
	        (lambda: key != WAIT and chr(key).isdigit(), _set_ref),
        ))

        if key in CONCLUDE:
            return


# DELETE
def _delete_event(dyatev: DyatevItems) -> None:
    """Delete event."""
    if not dyatev.index or dyatev.index > len(dyatev.lines):
        return

    stνlαt('Dyαteν', f'❯ Iuαq') #│ {'\t'.join(item_to_delete)}', 0)

    index_to_del = dyatev.index - 1
    dyatev.header = list(dyatev.events.keys())
    dyatev.lines = list(zip(*dyatev.events.values()))
    dyatev.lines = [e for i, e in enumerate(dyatev.lines) if i != index_to_del]

    _save_events(dyatev)


def _ιuαq(dyatev: DyatevItems, stanvor: Stanvor) -> None:
    """Delete event."""
    dyatev.section = 'Iuαq'
    stanvor.stvl.ιdeu += ' │ Iuαq'
    dyatev.colors = (0, RED)

    while True:
        _lαmdyαt(stanvor, dyatev)

        key = getch(stanvor)[0]

        if key == ENTER:
            _delete_event(dyatev)
        elif key == ORD:
            dyatev.index = 0
        elif key in SELECTORS:
            _select_item(key, dyatev)

        if key in CONCLUDE:
            return


def _open_dyatander(key: int, stvl: Lαmseut, dyatev: DyatevItems) -> None:
    path = next(value for keys, value in DYATANDERAM.items() if key in keys)

    if not os.path.exists(path):
        stvl.stlαg = f'{path} αqtαgeu'

    dyatev.ιdeu = path

    with open(dyatev.ιdeu, 'r', encoding='utf8') as oppel:
        dyatev.data = oppel.read()


def _open_webdyat(key: int) -> None:
    webvals = next(value for keys, value in WEBDYAT.items() if key in keys)
    stνlαt('Dyαteν', f'❯ {webvals[0]}')
    webbrowser.open(webvals[1])


# Master
dyαt_operations = {
    DEL: _ιuαq,
    MINUS: _ιuαq,
    BACK: _νerqom,
    COMMA: _νerqom,
    ENTER: _sιguα,
    PADPLUS: _sιguα,
    PADSLASH: _νerse,
    POINT: _dyαt_sιguα_module,
}

def dyαteν(stanvor: Stanvor) -> None:
    """Activities section."""
    dyatev = DyatevItems()

    def _set_default_toreg() -> None:
        dyatev.ιdeu = DPATH
        dyatev.data = _get_events(DPATH, dyatev)

    def _operate_dyat() -> None:
        dyαt_operations[key](dyatev, stanvor)
        _reset_dyatev(dyatev, stanvor)

    def _navigate_items() -> None:
        _select_item(key, dyatev)

    def _edit_file() -> None:
        stνlαt('Dyαteν', f'❯ Lαg {dyatev.ιdeu}')
        open_editor(dyatev.ιdeu, 'msedit', 'Dyαteν')
        key = ORD # Must be fixed to update current dyatev page
        _open_dyatander(key, stanvor.stvl, dyatev)


    _reset_dyatev(dyatev, stanvor)

    while True:
        stanvor.stvl.clean = 1
        _lαmdyαt(stanvor, dyatev)

        key = getch(stanvor)[0]

        if key == ESC:
            stanvor.stvl.clear()
            return

        process_handlers((
            (lambda: key == ORD, _set_default_toreg),
            (lambda: key in dyαt_operations, _operate_dyat),
            (lambda: key in logimprol, lambda: logimprol[key](stanvor)),
            (lambda: key in SELECTORS, lambda: _select_item(key, dyatev)),
            (lambda: key == NUM0 and dyatev.ιdeu != DPATH, _edit_file),
            (lambda: key == ENTER and dyatev.ιdeu != DPATH, lambda: tαuder(stanvor, dyatev.ιdeu)),
            (lambda: any(key in keys for keys in DYATANDERAM.keys()), lambda: _open_dyatander(key, stanvor.stvl, dyatev)),
            (lambda: any(key in keys for keys in WEBDYAT.keys()), lambda: _open_webdyat(key))
        ))
