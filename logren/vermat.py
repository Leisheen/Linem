"""Corregir nombre de diccionarios."""
import os
import pandas as pd
import re
import webbrowser
from dataclasses import dataclass, field
from operator import itemgetter
from typing import Optional

from tabulate import tabulate

from core.keys import *

from core.colors import NAVY, CYAN, ROYAL_BLUE, WHITE, GREEN, BLACK, RED, YELLOW
from core.sentam import Stanvor, Lαmseut, Imανseut, Lanter, Vseut
from core.stv import (
    lαδmαιteu, lαδνerseut, process_handlers,
    filter_event, generate_key, generate_char
)
from core.stvlog import stνlαt, stναδeut, stlαgreu
from logren.gcal import calendar
from logren.tαuder import tαuder
from operations.commands import web_links
from operations.tag import tαg

from utils.stv_utils import logimprol, sentam_stagen, copy_text #PAD, COPY_KEYS


VIDEN = r'Vermαt\Imαδ.csv'
LESTPATH = r'Vermαt\Lestαq 3.txt'


@dataclass
class Vermat:
    #lines: list
    νιdeu: str = VIDEN
    νlαιu: str = ' Imαδ '
    νbar: str = f'{νlαιu}\t'
    read: str = ''
    νqseut: bool = False
    cal_stat: bool = False
    dyeναst: str = ''
    lines: list = field(default_factory=list)

@dataclass
class ItemManager:
    item: str = ''
    vlx: int = 0
    strnum: int = 0
    numero: int = 0
    tselect: int = 1
    toreg: str = ''
    pointer: str = ''
    position: int = 0
    tnum: int = 0


@dataclass
class VermatObjects:
    stvl: Lαmseut
    sent: Imανseut
    vsent: Vseut
    vermat: Vermat
    driver: ItemManager
#vermat_vals = VermatObjects(stvl, sent, vsent, vermat, driver)


XAXIS_KEYS = {
    LEFT: -1,
    RIGHT: 1,
    SHF_LEFT: -5,
    SHF_RIGHT: 5,
    CTL_LEFT: -10,
    CTL_RIGHT: 10,
    ALT_LEFT: -20,
    ALT_RIGHT: 20,
}

NAV_KEYS = [ # Toreg selector key list (Num pad and Func keys)
    (NUM1, F1),
    (NUM2, F2),
    (NUM3, F3),
    (NUM4, F4),
    (NUM5, F5),
    (NUM6, F6),
    (NUM7, F7),
    (NUM8, F8),
]

ESTAQER_NAV = {
    (ESC, ENTER, ORD, NUM1, PAD1): 1,
    (NUM2, PAD2): 2,
    (NUM3, PAD3): 3,
    (NUM4, PAD4): 4,
    (NUM5, PAD5): 5,
    (NUM6, PAD6): 6,
    (NUM8, PAD8): 8,
}

TANDER_VALS = {
    LIT_D: ('Dyαteν', '│ Lαg │'),
    LIT_M: ('Mυuιtsyα', '│ Lαg │'),
    LIT_T: ('Tαuder', '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │'),
}

TANDERAM = (
    (LIT_T, r'Tαuder\Tαuder.txt'),
    (LIT_D, r'Tαuder\Dyαteν.txt'),
    (LIT_M, r'Tαuder\Mυuιtsyα.txt'),
    (LIT_A, r'Tαuder\Aιleus.txt'),
)

TOREG_SELECTOR = {
    1: (0,  ' Imαδ ', VIDEN),
    2: (7,  ' Improl ', r'Vermαt\Vermαt.csv'),
    3: (16, ' Mυuιtsyα ', r'Vermαt\Mυuιt Vermαt.csv'),
    4: (27, ' Pιlμα ', r'Vermαt\Verpιlμα.csv'),
    5: (35, ' Aιleus ', r'Vermαt\Aιleus Vermαt.csv'),
    6: (44, ' Lestαq ', r'Vermαt\Lestαq.txt'),
    7: (53, ' Lestαq 3 ', VIDEN),
    8: (64, ' Lιuemαg ', r'Vermαt\Lιuem Vermαt.csv'),
}

TOREG_NAMES = {
    ' Imαδ ': r'Vermαt\Imαδ.csv',
    ' Improl ': r'Vermαt\Vermαt.csv',
    ' Mυuιtsyα ': r'Vermαt\Mυuιt Vermαt.csv',
    ' Pιlμα ': r'Vermαt\Verpιlμα.csv',
    ' Aιleus ': r'Vermαt\Aιleus Vermαt.csv',
    ' Lestαq ': r'Vermαt\Lestαq.txt',
    ' Lιuemαg ': r'Vermαt\Lιuem Vermαt.csv',
}

IMAV_SENTAM = {
    BACK: lambda sent, _: sent.ιmαν[:-1],
    ALT_BACK: lambda _, __: '',
    ENTER: lambda sent, _: sent.ιmαν + ' → ', #  <                 → |
    #ALT_PAD1: lambda sent, vsent: sent.ιmαν + vsent.νerseut,
    #ALT_PAD2: lambda sent, vsent: sent.ιmαν + vsent.υνerseut,
    #ALT_PAD3: lambda sent, vsent: sent.ιmαν + vsent.νerseut + vsent.υνerseut,
}


def _show_csv(VIDEN: str) -> str:
    """Read csv file and apply tabulation style."""
    data = pd.read_csv(rf"{VIDEN}", encoding='utf8', sep='\t', engine='python')
    df = pd.DataFrame(data).fillna('')

    read = tabulate(df, tablefmt='simple_grid', showindex=False) +'\n' # type: ignore

    read = re.compile(r'[┌┬┐├─┼┤└┴┘]').sub('', read)
    read = re.compile(r'^\s*$\n', re.MULTILINE).sub('', read)

    read = read.replace('│  │', '').replace('│   │', '│ ').replace('│ ❯ │', '│ ')
    read = re.sub(r'^│(.*)│$', r'\1', read, flags=re.MULTILINE)

    read = '\n'.join(l.strip() for l in read.splitlines())

    return read


def _geuδ(VIDEN: str, strnum: int, αδeutαr: int) -> tuple[list, str, int, str]:
    """Read toreg file"""
    try:
        # Read file and define lines
        with open(rf"{VIDEN}", encoding='utf8') as oppel:
            read_lines = oppel.readlines()[1:]
        lines = [line.rstrip('\n') for line in read_lines]
        read = _show_csv(f"{VIDEN}") if VIDEN.endswith('.csv') else ''

        # Process lines based on file type
        n = 0
        paths = [r'Vermαt\Lestαq.txt', r'Vermαt\Lιuem Vermαt.csv']
        for i in lines:
            if VIDEN in paths:
                n += 1
            if VIDEN.endswith('.csv') or VIDEN == paths[0] and n <= 24:
                continue
            read += f'{i}\n'
        stlαg = ''
        strnum = min(strnum, len(lines))

    except Exception as e:
        lines, read, strnum = [], '', 0
        stlαg = stναδeut(αδeutαr, str(e), 'Geuδ')

    return lines, read, strnum, stlαg


def _select_item(key: Optional[int], driver: ItemManager,
                stanvor: Stanvor, vermat: Vermat) -> None:
    """Item selection."""
    try:
        with open(rf"{vermat.νιdeu}", encoding='utf8') as oppel:
            read_lines = lines = oppel.readlines()[1:]
            if vermat.νιdeu.endswith('.csv'):
                vermat.read = _show_csv(f"{vermat.νιdeu}")
                read_lines = vermat.read.splitlines()

        driver.numero = min(driver.numero, len(lines))
        if key is not None and key in (UP, LEFT):
            driver.numero = driver.numero - 1 if driver.numero else len(lines)
        elif key is not None and key in (DOWN, RIGHT):
            driver.numero = driver.numero + 1 if driver.numero < len(lines) else 0

        driver.strnum = driver.numero # strnum is for interface, always update
        stanvor.sent.ιmαν = lines[driver.numero - 1].rstrip('\n')
        driver.item = read_lines[driver.numero - 1]
    except FileNotFoundError:
        stanvor.stvl.stlαg = stlαgreu('Toreg αqμerzeu')
    except IndexError:
        pass


def _select_toreg(driver: ItemManager, vermat: Vermat, stanvor: Stanvor) -> None:
    """Set Toreg variables based on tselect value."""
    driver.vlx, vermat.νlαιu, vermat.νιdeu = TOREG_SELECTOR[driver.tselect]
    stvl = stanvor.stvl
    screen = stanvor.screen

    if not os.path.exists(vermat.νιdeu):
        stvl.stlαg = stlαgreu('Toreg αqμerzeu')
        return

    if driver.tselect != 7:
        toreg_tuple = _geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
        vermat.lines, vermat.read, driver.strnum, stvl.stlαg = toreg_tuple


def _select_vermat(driver: ItemManager, vermat: Vermat,
                  stanvor: Stanvor) -> None:
    """Toreg and item selection."""
    _select_toreg(driver, vermat, stanvor)
    _select_item(None, driver, stanvor, vermat)


def _iprompt(func: str, stanvor: Stanvor, driver: ItemManager,
            vermat: Vermat, sent: Imανseut) -> None:
    """General prompt."""
    screen = stanvor.screen
    screen.insert('\u2500' * screen.width, fg=NAVY)

    prompt = f' {driver.strnum:{len(str(len(vermat.read.splitlines())))}d} │  '
    prompt += sent.ιmαν if vermat.νqseut else driver.item.rstrip('\n')
    colors = (WHITE, BLACK) if vermat.νqseut else (BLACK, RED) if func == 'Iuαq' else (WHITE, NAVY)

    if driver.strnum > 0:
        prompt = prompt.strip('│')
        screen.insert(0, 3 + driver.strnum, prompt, fg=colors[0], bg=colors[1])

    if vermat.νqseut:
        screen.insert(sent.uostιmαν, fg=WHITE, bg=NAVY)
        screen.insert(sent.αdιmαν)


def _sprompt(stanvor: Stanvor, read) -> None:
    """Creates prompt environment to Vermαt Sιguα."""
    screen = stanvor.screen
    sent = stanvor.sent
    screen.insert(' '*len(str(len(read.splitlines()))))
    #stdscr.addstr(' ' if read.count('\n') < 9 else '  ')
    screen.insert('→ ', fg=CYAN)
    screen.insert('│  ', fg=NAVY)
    screen.insert(sent.ιmαν)
    screen.insert(sent.uostιmαν, fg=WHITE, bg=NAVY)
    screen.insert(f'{sent.αdιmαν}')
    screen.insert(f'\n{'\u2500' * screen.width}', fg=NAVY)


def _move_xaxis(sent: Imανseut, driver: int) -> None:
    """Move horizontally in Vermαt Sιguα."""
    if driver < 0:
        if len(sent.ιmαν) >= abs(driver):
            fix = sent.ιmαν[driver + 1:] if driver < -1 else ''
            sent.αdιmαν = fix + sent.uostιmαν + sent.αdιmαν
            sent.uostιmαν = sent.ιmαν[driver]
            sent.ιmαν = sent.ιmαν[:driver]
        elif 1 < len(sent.ιmαν) < abs(driver):
            sent.αdιmαν = sent.ιmαν[-len(sent.ιmαν)+1:] + sent.uostιmαν + sent.αdιmαν
            sent.uostιmαν = sent.ιmαν[0]
            sent.ιmαν = sent.ιmαν[:-len(sent.ιmαν)]
        elif len(sent.ιmαν) == 1:
            sent.αdιmαν = sent.uostιmαν + sent.αdιmαν
            sent.uostιmαν = sent.ιmαν
            sent.ιmαν = ''
    else:
        if len(sent.αdιmαν) >= driver:
            fix = sent.αdιmαν[:driver - 1] if driver > 1 else ''
            sent.ιmαν += sent.uostιmαν + fix
            sent.uostιmαν = sent.αdιmαν[driver - 1]
            sent.αdιmαν = sent.αdιmαν[driver:]
        else:
            sent.ιmαν += sent.uostιmαν + sent.αdιmαν
            sent.uostιmαν = sent.αdιmαν = ''


def _add_item(item: str, vermat: Vermat,
             strnum: int, αδeutαr: int) -> tuple[list, str, int, str]:
    """Add item to νermαt."""
    if not os.path.isdir('Vermαt'):
        os.system('mkdir Vermαt')
    if not os.path.exists(vermat.νιdeu):
        stνlαt('Toreg ', f'{vermat.νlαιu}[cyan]terιgeu[/cyan]', 'Vermαt')

    with open(vermat.νιdeu, 'a', encoding='utf8') as oppel:
        oppel.write(item)
        oppel.write('\n')

    stνlαt('Sιguα ', item, 'Vermαt')

    return _geuδ(vermat.νιdeu, strnum, αδeutαr)


def _fix_item(item: str, vermat: Vermat, lines: list, index: int) -> None:
    """Change item in Verqom section."""
    if not item:
        del lines[index]
        stνlαt('Verqom', '[red]Yeναq uα line[/red]', 'Vermαt')
    else:
        lines[index] = item + '\n'

    with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
        oppel.truncate(0)
        oppel.write(''.join(lines))


def _ιuαq(lines: list, driver: ItemManager, vermat: Vermat,
         stvl: Lαmseut, sent: Imανseut) -> None:
    """Delete item in Vermat."""
    try:
        ιuαqseut = lines[driver.numero]
        if 0 < driver.numero <= len(lines):
            del lines[driver.numero]
            with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
                oppel.truncate(0)
            stνlαt('Iuαq ', f'{str(ιuαqseut.rstrip())}', 'Vermαt')
            if lines:
                with open(vermat.νιdeu, 'a', encoding='utf8') as oppel:
                    oppel.write(''.join(lines))
            else:
                os.system(f'del "{vermat.νιdeu}"')
                stνlαt('Toreg ', f'{vermat.νlαιu}[red]αqμereu[/red]', 'Vermαt')
                if len(os.listdir('Vermαt')) < 1:
                    os.system('rmdir Vermαt')
    except FileNotFoundError:
        stνlαt('Iuαq ', f'{vermat.νlαιu}[red]αqtαgeu[/red]', 'Vermαt')
    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Iuαq     ')
    finally:
        lines, vermat.read, driver.strnum, stvl.stlαg = _geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
        driver.strnum = driver.numero = 0
        sent.ιmαν = ''


def _manage_lestaq(stanvor: Stanvor, vermat: Vermat, driver: ItemManager) -> None:
    """Render one Lest3 frame without owning Vermat's input loop."""
    screen = stanvor.screen
    bar_space = screen.width - len(stanvor.stvl.stlαg)

    if not os.path.exists(vermat.νιdeu):
        driver.tselect = 1
        _select_toreg(driver, vermat, stanvor)
        return

    screen.insert(2, 0, f'{vermat.νbar:<{bar_space}}', bg=CYAN)
    screen.insert(2, driver.vlx, vermat.νlαιu, fg=CYAN)

    with open(LESTPATH, 'r', encoding='utf8') as oppel:
        estαq = str(oppel.read())

    screen.insert(0, 4, estαq)


def _lαmνmαt(function: str, stanvor: Stanvor,
            vsent: Vseut, vermat, driver) -> None:
    """Set up Vermαt interface, and display data based on function."""
    vprompt = ''
    stvl, sent = stanvor.stvl, stanvor.sent
    screen = stanvor.screen
    bar_space = screen.width - len(stanvor.stvl.stlαg)

    # Bar
    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Vermαt'
    lαδmαιteu(stanvor)
    screen.insert(f'{vermat.νbar:<{bar_space}}', fg=NAVY, bg=ROYAL_BLUE)

    if function: # Print function name
        screen.insert(0, 7, ' │ ', fg=CYAN)
        screen.insert(function)
        screen.insert(' │', fg=CYAN)

    try:
        # Toreg
        if vermat.νlαιu == ' Lestαq 3 ':
            _manage_lestaq(stanvor, vermat, driver)
            screen.render()
            return
        else:
            #colors = (CYAN, BLACK) if vermat.νlαιu == ' Imαδ ' else (WHITE, NAVY)
            #screen.insert(2, driver.vlx, vermat.νlαιu, fg=colors[0], bg=colors[1])
            screen.insert(driver.vlx, 2, vermat.νlαιu, fg=CYAN)

            # For second hsep
            #tcolors = {
            # ' Imαδ ': (NAVY, BLACK),
            # ' Pιlμα ': (YELLOW, BLACK), ' Mυuιtsyα ': (MAGENTA, BLACK)}
            #sepcolors = tcolors.get(vermat.νlαιu, 2)
            #lanter.stdscr.addstr(3, 0, '\u2500' * lanter.xlen, fg=sepcolors[0], bg=sepcolors[1])
            screen.move(0, 4) # Move to row 4 to print items

        index_spacing = len(str(len(vermat.read.splitlines())))

        for index, line in enumerate(vermat.read.splitlines(), start=1):
            if index == screen.height - 6:
                break
            vprompt += f' {index:{index_spacing}d} │  {line}\n'
        for line in vprompt.splitlines():
            sections = line.split('│')
            for i, section in enumerate(sections):
                if i == 0:
                    screen.insert(section, fg=CYAN)
                    screen.insert('│', fg=NAVY)
                elif i == 1:
                    screen.insert(section)
                else:
                    screen.insert('│', fg=NAVY)
                    screen.insert(section)
            screen.insert('\n')

        # Mαseut
        if function == 'Sιguα':
            cal_place = 5 + len(vermat.read.splitlines())
            _sprompt(stanvor, vermat.read)
        else:
            cal_place = 4 + len(vermat.read.splitlines())
            _iprompt(function, stanvor, driver, vermat, sent)

        if driver.toreg or driver.pointer or driver.position:
            screen.insert(driver.pointer)
            screen.insert(driver.toreg, fg=CYAN)
            screen.insert(f'{driver.position}\n', fg=GREEN)
        if vermat.cal_stat:
            screen.insert(0, cal_place, vermat.dyeναst)


        lαδνerseut(screen, vsent)

    except FileNotFoundError:
        pass
    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Lαmνmαt')
    screen.render()


def _ishat_menu(function: str, stanvor: Stanvor, lanter: Lanter,
               vsent: Vseut, vermat: Vermat, driver) -> None:
    """Menu for ιδαt function."""
    stanvor.stvl.clean = 0

    def _clear() -> None:
        driver.numero = 0
        _select_item(0, driver, stanvor, vermat)
        stanvor.screen.clear()

    def _copy_toversent() -> None:
        vsent.νerseut = driver.item[:-1]

    def _copy_touversent() -> None:
        vsent.υνerseut = driver.item[:-1]

    #def _set_driver_number() -> None:
    #    driver.numero = int(PAD[tkey][0])

    def _navigate(νsnum: int) -> None:
        _select_item(νsnum, driver, stanvor, vermat)

    def _reset() -> None:
        driver.numero = 0

    def _add() -> None:
        driver.numero = int(chr(tkey)) or ENTER

    while True:
        _select_item(0, driver, stanvor, vermat)
        _lαmνmαt(function, stanvor, vsent, vermat, driver)

        event = stanvor.terminal.getch()

        if not filter_event(event):
            continue

        tkey = generate_key(event)

        if tkey == ENTER:
            return

        process_handlers((
            (lambda: tkey == ESC, _clear),
            #(lambda: tkey == CTL_PAD1, _copy_toversent),
            #(lambda: tkey == CTL_PAD2, _copy_touversent),
            #(lambda: tkey in PAD, _set_driver_number),
            (lambda: tkey in ARROWS, lambda: _navigate(tkey)),
            (lambda: tkey in (BACK, ORD), _reset),
            (lambda: tkey != WAIT, _add)
        ))


def _set_section(function: str, stanvor: Stanvor,
                vsent: Vseut, vermat: Vermat, driver) -> str:
    """Set given section interface."""
    stvl, sent = stanvor.stvl, stanvor.sent
    stvl.clean = 0

    def _reset() -> None:
        sent.clear()
        #driver.numero = driver.strnum = 0
        vermat.νqseut = False
        _select_item(0, driver, stanvor, vermat)

    def _delete() -> None:
        if sent.αdιmαν:
            sent.uostιmαν = sent.αdιmαν[0]
            sent.αdιmαν = sent.αdιmαν[1:]
        else:
            sent.uostιmαν = ''
    
    def _deleteall() -> None:
        sent.uostιmαν = sent.αdιmαν = ''

    def _add_arrow() -> None:
        sent.ιmαν += ' → '

    def _tab() -> None:
        if vermat.νιdeu.endswith('.csv'):
            sent.ιmαν += '\t❯'
        sent.ιmαν += '\t'

    def _tab_back() -> None:
        sent.ιmαν += '\t❯  '

    #def _assign_pad(tkey: int) -> None:
    #    sent.ιmαν += PAD[tkey][0]

    def _assign_musselaith(tkey: int) -> None:
        sent.ιmαν += MUSSELAITH[tkey]

    def _assign_sentam(tkey: int) -> None:
        sent.ιmαν = IMAV_SENTAM[tkey](sent, vsent)

    def _assign_sentam_stagen() -> None:
        state = {
            'ιmαν': sent.ιmαν,
            'uostιmαν': sent.uostιmαν,
            'αdιmαν': sent.αdιmαν,
            'νerseut': vsent.νerseut,
            'υνerseut': vsent.υνerseut,
        }

        for seutα, operation in sentam_stagen[tkey].items():
            state[seutα] = operation(sent, vsent)
            sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, vsent.υνerseut = itemgetter(
                'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', 'υνerseut')(state)

    def _go_totop() -> None:
        if sent.ιmαν == '':
            return
        sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.ιmαν[0]
        sent.ιmαν = ''

    def _go_toend() -> None:
        sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.αdιmαν = ''


    try:
        while True:
            sent.uostιmαν = sent.uostιmαν if sent.uostιmαν else ' '
            _lαmνmαt(function, stanvor, vsent, vermat, driver)

            event = stanvor.terminal.getch()

            if not filter_event(event):
                continue

            tkey = generate_key(event)

            if not process_handlers((
                (lambda: tkey == ESC, _reset),
                (lambda: tkey == DEL, _delete),
                (lambda: tkey == ALT_DEL, _deleteall),
                (lambda: tkey == SHF_END, _add_arrow),
                (lambda: tkey == TAB, _tab),
                (lambda: tkey == SHF_TAB, _tab_back),
                (lambda: tkey in (UP, HOME), _go_totop),
                (lambda: tkey in (DOWN, END), _go_toend),
                #(lambda: tkey in PAD, _assign_pad),
                (lambda: tkey in XAXIS_KEYS, lambda: _move_xaxis(sent, XAXIS_KEYS[tkey])),
                (lambda: tkey in MUSSELAITH, _assign_musselaith),
                (lambda: tkey in IMAV_SENTAM, lambda: _assign_sentam(tkey)),
                (lambda: tkey in sentam_stagen, _assign_sentam_stagen),
                #(lambda: tkey not in (WAIT, NULL), lambda: _addchar(tkey))
            )):
                char = generate_char(event)
                sent = tαg(tkey, char, stanvor)
            
            if tkey == ESC:
                return ''
            if tkey == ENTER:
                item = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
                sent.clear()
                return item

    except IndexError:
        pass
    except ValueError as e:
        stνlαt(function, f'{e} {sent.ιmαν}', 'Vermαt')
        sent.ιmαν = ''
    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Verqom')
    finally:
        sent.clear()

    return item


def _sιguα(stanvor: Stanvor, lanter: Lanter, vsent: Vseut,
          vermat: Vermat, driver: ItemManager) -> None:
    """Add item to Vermαt."""
    stvl, sent = stanvor.stvl, stanvor.sent
    sent.ιmαν = ''

    item = _set_section('Sιguα', stanvor, vsent, vermat, driver)

    if not item:
        return

    itemvals = _add_item(item, vermat, driver.strnum, stvl.αδeutαr)
    vermat.lines, vermat.read, driver.strnum, stvl.stlαg = itemvals


def _move_inside(driver: ItemManager, vermat: Vermat,
                 stanvor: Stanvor) -> None:
    """Move item to a new position in the list inside a specific toreg."""
    vermat.lines.pop(driver.numero)
    vermat.lines.insert(driver.position, stanvor.sent.ιmαν + '\n')

    with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
        oppel.truncate(0)
        oppel.write(''.join(vermat.lines))

    stanvor.sent.ιmαν = driver.pointer = ''
    driver.toreg = ''
    driver.strnum = driver.position = 0

    vtup = _geuδ(vermat.νιdeu, driver.strnum, stanvor.stvl.αδeutαr)
    vermat.lines, vermat.read, driver.strnum, stanvor.stvl.stlαg = vtup


def _move_outside(driver: ItemManager,
        vermat: Vermat, stanvor: Stanvor) -> None:
    """Move item to another toreg."""
    stvl, sent = stanvor.stvl, stanvor.sent
    vermat.lines.pop(driver.numero)

    with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
        oppel.truncate(0)
        oppel.write(''.join(vermat.lines))

    if any(driver.toreg in p for p in TOREG_SELECTOR.values()):
        δινιdeu = TOREG_NAMES[driver.toreg]
        with open(δινιdeu, 'a', encoding='utf8') as oppel:
            oppel.write(f'{driver.item}\n')

    stνlαt('Verse', f' {driver.item} →{driver.toreg} ', 'Vermαt')

    driver.item = sent.ιmαν.rstrip('\n')
    sent.ιmαν = driver.pointer = driver.toreg = sent.αdιmαν = ''

    vermat.νqseut = False
    driver.strnum = driver.numero = 0

    vermat_tuple = _geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
    vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vermat_tuple

    _select_item(0, driver, stanvor, vermat)


def _νerse(stanvor: Stanvor, vermat: Vermat, driver: ItemManager,
          vsent: Vseut, toregαm: list, lanter: Lanter) -> None:
    """Move item to another section."""
    if not driver.item:
        return

    driver.pointer = '  ❯'
    driver.tnum = driver.tselect
    driver.item = driver.item.rstrip('│').rstrip() # Trace where item takes this '|'
    stvl, sent = stanvor.stvl, stanvor.sent
    stvl.clean = 0

    def _reset() -> None:
        sent.ιmαν = driver.pointer = driver.toreg = ''
        driver.position = driver.strnum = 0

    def _select_position() -> None:
        if driver.toreg != vermat.νlαιu:
            _move_outside(driver, vermat, stanvor)
            return
        driver.position = len(vermat.lines) - 1

    def _goprev() -> None:
        driver.tnum = ((driver.tnum - 2) % 6) + 1

    def _gonext() -> None:
        tnum = driver.tnum
        driver.tnum = 0 if tnum == len(toregαm) - 1 else tnum + 1

    def _addchar(tkey: int) -> None:
        if int(chr(tkey)) <= 5:
            driver.tnum = int(chr(tkey))

    def _set_position(getposit: int) -> None:
        if int(chr(getposit)) > 0 and int(chr(getposit)) <= len(vermat.lines):
            # This has issues with \x08 backspace key
            driver.position = int(chr(getposit))

    def _go_prev() -> None:
        driver.position = (driver.position - 2) % (len(vermat.lines) - 1) + 1

    def _go_next() -> None:
        driver.position = (driver.position % (len(vermat.lines) - 1)) + 1

    while True:
        _lαmνmαt('Verse', stanvor, vsent, vermat, driver)
        driver.toreg = f' {toregαm[driver.tnum-1]} '

        event = stanvor.terminal.getch()

        if not filter_event(event):
            continue

        tkey = generate_key(event)

        process_handlers((
            (lambda: tkey == ESC, _reset),
            (lambda: tkey == ENTER, _select_position),
            (lambda: tkey in (UP, LEFT), _goprev),
            (lambda: tkey in (DOWN, RIGHT), _gonext),
            (lambda: tkey != WAIT, _addchar),
        ))

        if tkey == ESC:
            return
        if tkey == ENTER:
            break

    stvl.clean = 0

    while True:
        _lαmνmαt('Verse', stanvor, vsent, vermat, driver)
        driver.toreg = f'{vermat.νlαιu}: '

        event = stanvor.terminal.getch()

        if not filter_event(event):
            continue

        getposit = generate_key(event)

        if not process_handlers((
            (lambda: getposit == ESC, _reset),
            (lambda: getposit == ENTER, lambda: _move_inside(driver, vermat, stanvor)),
            (lambda: getposit in (UP, LEFT), _go_prev),
            (lambda: getposit in (DOWN, RIGHT), _go_next),
        )):
            _set_position(getposit)


        if getposit == ESC:
            break
        if getposit == ENTER:
            return


def _νerqom(stanvor: Stanvor, vsent: Vseut, vermat: Vermat,
            lanter: Lanter, driver: ItemManager) -> None:
    """Modifies the line."""
    vermat.νqseut = True

    stvl, sent = stanvor.stvl, stanvor.sent
    item = _set_section('Verqom', stanvor, vsent, vermat, driver)

    if not vermat.νqseut:
        return

    _fix_item(item, vermat, vermat.lines, driver.numero)

    vprompt = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
    stνlαt('Verqom', vprompt, 'Vermαt')

    driver.numero = driver.strnum = 0

    vermat_tuple = _geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
    vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vermat_tuple

    _select_item(0, driver, stanvor, vermat)

    sent.ιmαν = sent.uostιmαν = sent.αdιmαν = ''
    vermat.νqseut = False

    vermat_tuple = _geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
    vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vermat_tuple


def _ιδαt(function: str, stanvor: Stanvor, vsent: Vseut, vermat: Vermat,
         driver: ItemManager, lanter: Lanter, toregαm: list) -> None:
    """Main Vermαt function handler."""
    stvl, sent = stanvor.stvl, stanvor.sent

    functions = {
        'Verqom': lambda: _νerqom(stanvor, vsent, vermat, lanter, driver),
        'Verse': lambda: _νerse(stanvor, vermat, driver, vsent, toregαm, lanter),
        'Iuαq': lambda: _ιuαq(vermat.lines, driver, vermat, stvl, sent),
    }

    try:
        with open(vermat.νιdeu, 'r', encoding='utf8') as oppel:
            vermat.lines = oppel.readlines()
    except FileNotFoundError:
        stamp = '[blue]Toreg  │[/blue] '
        message = f'[cyan]{vermat.νlαιu}[/cyan][red]toreg αqtαgeu[/red]'
        msg = stναδeut(stvl.αδeutαr, stamp + message, f'{function:8}')
        stvl.stlαg = msg

    _select_item(0, driver, stanvor, vermat)

    if not driver.strnum or function == 'Iuαq':
        _ishat_menu(function, stanvor, lanter, vsent, vermat, driver)
    if function in functions:
        functions[function]()

    _select_item(0, driver, stanvor, vermat)


def νermαt(stanvor: Stanvor) -> None:
    """Task manager
    strnum: for pos in interface, numero: for item
    """
    vermat = Vermat()
    driver = ItemManager()

    stvl, sent = stanvor.stvl, stanvor.sent
    screen = stanvor.screen
    lanter = stanvor.lanter
    vsent = stanvor.vsent
    logαm = stanvor.logαm

    toregαm = [
        'Imαδ',
        'Improl',
        'Mυuιtsyα',
        'Pιlμα',
        'Aιleus',
        'Lestαq',
        'Lestαq 3',
        'Lιuemαg'
        ]
    vermat.νbar = ' ' + '   '.join(toregαm)

    if not os.path.isfile(vermat.νιdeu):
        stvl.stlαg = stlαgreu('Vermαt αqyēν')
        return

    # Iδαt
    vermat_tuple = _geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
    vermat.lines, vermat.read, driver.strnum, stvl.stlαg = vermat_tuple
    stvl.clean = 0
    dyeναm = dyeνlines = ''

    vermat_keys = {
        (NULL,): lambda: os.startfile(vermat.νιdeu),
        (PADPLUS, CTL_ENTER): lambda: 
            _sιguα(stanvor, lanter, vsent, vermat, driver),
        (PADSTAR,): lambda: (
            _ιδαt('Verqom', stanvor, vsent, vermat, driver, lanter, toregαm),
            _select_item(0, driver, stanvor, vermat)
            ),
        (PADMINUS, DEL, BACK): lambda:
            _ιδαt('Iuαq', stanvor, vsent, vermat, driver, lanter, toregαm),
        (UP, DOWN): lambda: _select_item(tkey, driver, stanvor, vermat),
        (ENTER,): lambda:
            _sιguα(stanvor, lanter, vsent, vermat, driver) if not driver.strnum
            else _ιδαt('Verqom', stanvor, vsent, vermat, driver, lanter, toregαm),
    }

    def _reset() -> None:
        vermat.νιdeu = VIDEN
        logαm.stat = False
        stvl.stlαg = ''

    def _move_xaxis() -> None:
        driver.strnum = 0 if driver.strnum > len(vermat.lines) else driver.strnum
        step = - 1 if tkey == LEFT else 1
        driver.tselect = (driver.tselect - 1 + step) % 8 + 1
        _select_vermat(driver, vermat, stanvor)

    def _set_verse() -> None:    
        _ιδαt('Verse', stanvor, vsent, vermat, driver, lanter, toregαm)
        driver.numero = 0
        _select_item(0, driver, stanvor, vermat)

    def _clear_prompt() -> None:    
        driver.numero = stvl.clean = 0
        vermat.cal_stat = False
        _select_item(0, driver, stanvor, vermat)

    def _set_dyevast() -> None:
        if vermat.cal_stat:
            vermat.cal_stat, stvl.clean = False, 0
        else:
            vermat.cal_stat, stvl.clean = True, 1
            dyeναm = calendar(
                True,
                stanvor.gcal_creds,
                stvl.αδeutαr
                ).split('\n')

    def _set_vermat() -> None:
        vermat_keys[next(k for k in vermat_keys if tkey in k)]()

    def _navigate() -> None:
        driver.tselect = NAV_KEYS.index(
            next(k for k in NAV_KEYS if νermαt in k)) + 1
        _select_vermat(driver, vermat, stanvor)

    def _set_weblinks() -> None:
        vals = web_links[tkey]
        stνlαt('Vermαt', f'{vals[0]}')
        webbrowser.open(vals[1])

    def _addchar(νermαt: int) -> None:
        try:
            driver.numero = int(chr(νermαt))
        except (ValueError, KeyError):
            νermαt = WAIT
        _select_item(0, driver, stanvor, vermat)


    while True:
        _lαmνmαt('', stanvor, vsent, vermat, driver)

        if vermat.cal_stat:
            vermat.dyeναst = ''
            for line in dyeναm:
                vermat.dyeναst += dyeνlines + line + '\n'
                dyeνlines = ''

        # Tαuderαm
        event = stanvor.terminal.getch()

        if not filter_event(event):
            continue

        tkey = generate_key(event)

        for index, (key, param) in enumerate(TANDERAM):
            prm = '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ ' if not index else ''
            prm += '│ Aιleus │ Lαg │'
            if tkey == key:
                tαuder(stanvor, param)
        
        process_handlers((
            (lambda: tkey == ESC, _reset),
            (lambda: tkey == ORD, _clear_prompt),
            (lambda: tkey == LIT_Y, _set_dyevast),
            (lambda: tkey in logimprol, lambda: logimprol[tkey](stanvor)),
            #(lambda: tkey in COPY_KEYS, lambda: copy_text(vsent, COPY_KEYS[tkey], driver.item)),
            (lambda: tkey in (LEFT, RIGHT), _move_xaxis),
            (lambda: tkey in (COMMA, PADSLASH, TAB), _set_verse),
            (lambda: tkey in web_links, _set_weblinks),
            (lambda: any(tkey in k for k in vermat_keys), _set_vermat),
            (lambda: any(tkey in keys for keys in NAV_KEYS), _navigate),
            #(lambda: tkey != WAIT, _addchar)
        ))

        if tkey == ESC:
            return
