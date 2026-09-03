"""Corregir nombre de diccionarios."""
import curses
import os
import pandas as pd
import re
import webbrowser
from dataclasses import dataclass, field
from operator import itemgetter
from tabulate import tabulate
from typing import Callable

from core.keys import *
from core.sentam import Stanvor, Prompt, Lαmseut, Imανseut, Lanter, Vseut
from core.stv import stvrefresh, mαιteu
from core.stvlog import stνlαt, stναδeut, stlαgreu
from logren.gcal import calendar
from logren.tαuder import tαuder
from operations.commands import logimprol, sentam_stagen, web_links
from utils.logren import open_editor
from utils.stv_utils import (
    lαmνerseut, copy_text,
    PAD, MUSSELAITH, COPY_KEYS
)
from utils.tander_utils import Tander, TanderLanter


VIDEN = r'Vermαt\Imαδ.csv'
LESTPATH = r'Vermαt\Lestαq 3.txt'


@dataclass
class Vermat:
    #lines: list
    νιdeu: str = VIDEN
    νlαιu: str = ' Imαδ '
    νbar: str = f'{νlαιu} │ '
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
    position: str = ''


XAXIS_KEYS = {
    LEFT: -1,
    RIGHT: 1,
    SLEFT: -5,
    SRIGHT: 5,
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
    (ESC, ENTER, PADENTER, ORD_O, NUM1, PAD1): 1,
    (NUM2, PAD2): 2,
    (NUM3, PAD3): 3,
    (NUM4, PAD4): 4,
    (NUM5, PAD5): 5,
    (NUM6, PAD6): 6,
    (NUM8, PAD8): 8,
}

TANDER_VALS = {
    (UPPER_T, LOWER_T): ('Tαuder', '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Lαg │'),
    (UPPER_D, LOWER_D): ('Dyαteν', '│ Lαg │'),
    (UPPER_M, LOWER_M): ('Mυuιtsyα', '│ Lαg │'),
}

TANDERAM = (
    ((LOWER_T, UPPER_T), r'Tαuder\Tαuder.txt'),
    ((UPPER_D, LOWER_D), r'Tαuder\Dyαteν.txt'),
    ((UPPER_M, LOWER_M), r'Tαuder\Mυuιtsyα.txt'),
    ((UPPER_A, LOWER_A), r'Tαuder\Aιleus.txt'),
)

TOREG_SELECTOR = {
    1: (0,  ' Imαδ ', VIDEN),
    2: (8,  ' Improl ', r'Vermαt\Vermαt.csv'),
    3: (17, ' Mυuιtsyα ', r'Vermαt\Mυuιt Vermαt.csv'),
    4: (28, ' Pιlμα ', r'Vermαt\Verpιlμα.csv'),
    5: (36, ' Aιleus ', r'Vermαt\Aιleus Vermαt.csv'),
    6: (45, ' Lestαq ', r'Vermαt\Lestαq.txt'),
    7: (54, ' Lestαq 3 ', VIDEN),
    8: (65, ' Lιuemαg ', r'Vermαt\Lιuem Vermαt.csv'),
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
    ALT_BKSP: lambda _, __: '',
    SEND: lambda sent, _: sent.ιmαν + ' → ', #  <                 → |
    ALT_PAD1: lambda sent, vsent: sent.ιmαν + vsent.νerseut,
    ALT_PAD2: lambda sent, vsent: sent.ιmαν + vsent.υνerseut,
    ALT_PAD3: lambda sent, vsent: sent.ιmαν + vsent.νerseut + vsent.υνerseut,
}


def set_vbar(tlist: list) -> str:
    return ' │ '.join(tlist[1:-1]) + f' │ Lestαq │ Lestαq 3 │ {tlist[-1]} │'


def show_csv(VIDEN: str) -> str:
    """Read csv file and apply tabulation style."""
    data = pd.read_csv(rf"{VIDEN}", encoding='utf8', sep='\t', engine='python')
    df = pd.DataFrame(data).fillna('')
    read = tabulate(df, tablefmt='simple_grid', showindex=False) +'\n'
    read = re.compile(r'[┌┬┐├─┼┤└┴┘]').sub('', read)
    read = re.compile(r'^\s*$\n', re.MULTILINE).sub('', read)
    read = read.replace('│  │', '').replace('│   │', '│ ').replace('│ ❯ │', '│ ')
    read = re.sub(r'^│(.*)│$', r'\1', read, flags=re.MULTILINE)
    read = '\n'.join(l.strip() for l in read.splitlines())
    return read


def geuδ(VIDEN: str, strnum: int, αδeutαr: int) -> tuple[list, str, int, str]:
    """Read toreg file"""
    try:
        # Read file and define lines
        with open(rf"{VIDEN}", encoding='utf8') as oppel:
            read_lines = oppel.readlines()[1:]
        lines = [line.rstrip('\n') for line in read_lines]
        read = show_csv(f"{VIDEN}") if VIDEN.endswith('.csv') else ''

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


def select_item(key: int, driver: ItemManager, 
                stanvor: Stanvor, vermat: Vermat) -> None:
    """Item selection."""
    try:
        with open(rf"{vermat.νιdeu}", encoding='utf8') as oppel:
            read_lines = lines = oppel.readlines()[1:]
            if vermat.νιdeu.endswith('.csv'):
                vermat.read = show_csv(f"{vermat.νιdeu}")
                read_lines = vermat.read.splitlines()

        driver.numero = min(driver.numero, len(lines))
        if key in (UP, LEFT):
            driver.numero = driver.numero - 1 if driver.numero else len(lines)
        elif key in (DOWN, RIGHT):
            driver.numero = driver.numero + 1 if driver.numero < len(lines) else 0

        driver.strnum = driver.numero # strnum is for interface, always update
        stanvor.prompt.sent.ιmαν = lines[driver.numero - 1].rstrip('\n')
        driver.item = read_lines[driver.numero - 1]
    except FileNotFoundError:
        stanvor.prompt.stvl.stlαg = stlαgreu('Toreg αqμerzeu', 0)
    except IndexError:
        pass


def select_toreg(driver, vermat, stvl, stdscr) -> None:
    """Set Toreg variables based on tselect value."""
    driver.vlx, vermat.νlαιu, vermat.νιdeu = TOREG_SELECTOR[driver.tselect]

    if not os.path.exists(vermat.νιdeu):
        stvl.stlαg = stlαgreu('Toreg αqμerzeu', 0)
        return

    if driver.tselect != 7:
        vermat.lines, vermat.read, driver.strnum, stvl.stlαg = geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
    else:
        stdscr.clear()


def select_vermat(driver, vermat, stanvor, stdscr) -> None:
    """Toreg and item selection."""
    select_toreg(driver, vermat, stanvor.prompt.stvl, stdscr)
    select_item(None, driver, stanvor, vermat)


def iprompt(func, lanter, driver, vermat, sent) -> None:
    """General prompt."""
    stdscr = lanter.stdscr
    stdscr.addstr('\u2500'*lanter.xlen, curses.color_pair(1))

    prompt = f' {driver.strnum:{len(str(len(vermat.read.splitlines())))}d} │  '
    prompt += sent.ιmαν if vermat.νqseut else driver.item.rstrip('\n')
    color = 10 if vermat.νqseut else 11 if func == 'Iuαq' else 5

    if driver.strnum > 0:
        prompt = prompt.strip('│')
        stdscr.addstr(3 + driver.strnum, 0, prompt, curses.color_pair(color))

    if vermat.νqseut:
        stdscr.addstr(sent.lαδuιmαν, curses.color_pair(5))
        stdscr.addstr(sent.αdιmαν)

    if func:
        stdscr.clrtoeol()


def sprompt(stdscr, X, read, sent: Imανseut) -> None:
    """Creates prompt environment to Vermαt Sιguα."""
    stdscr.addstr(' '*len(str(len(read.splitlines()))))
    #stdscr.addstr(' ' if read.count('\n') < 9 else '  ')
    stdscr.addstr('→ ', curses.color_pair(2))
    stdscr.addstr('│  ', curses.color_pair(1))
    stdscr.addstr(sent.ιmαν)
    stdscr.addstr(sent.lαδuιmαν, curses.color_pair(5))
    stdscr.addstr(f'{sent.αdιmαν}')
    stdscr.addstr(f'\n{'\u2500'*X}', curses.color_pair(1))


def move_xaxis(sent: Imανseut, driver: int) -> None:
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


def add_item(item: str, vermat: Vermat,
             strnum: int, αδeutαr: int) -> tuple[list, str, int, str]:
    """Add item to νermαt."""
    if not os.path.isdir('Vermαt'):
        os.system('mkdir Vermαt')
    if not os.path.exists(vermat.νιdeu):
        stνlαt('Toreg ', f'{vermat.νlαιu}[cyan]terιgeu[/cyan]', 7)

    with open(vermat.νιdeu, 'a', encoding='utf8') as oppel:
        oppel.write(item)
        oppel.write('\n')

    stνlαt('Sιguα ', item, 7)

    return geuδ(vermat.νιdeu, strnum, αδeutαr)


def fix_item(item: str, vermat: Vermat, lines: list, index: int) -> None:
    """Change item in Verqom section."""
    if not item:
        del lines[index]
        stνlαt('Verqom', '[red]Yeναq uα line[/red]', 7)
    else:
        lines[index] = item + '\n'

    with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
        oppel.truncate(0)
        oppel.write(''.join(lines))


def ιuαq(lines: list, driver: ItemManager, vermat: Vermat,
         stvl: Lαmseut, sent: Imανseut) -> None:
    """Delete item in Vermat."""
    try:
        ιuαqseut = lines[driver.numero]
        if 0 < driver.numero <= len(lines):
            del lines[driver.numero]
            with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
                oppel.truncate(0)
            stνlαt('Iuαq ', f'{str(ιuαqseut.rstrip())}', 7)
            if lines:
                with open(vermat.νιdeu, 'a', encoding='utf8') as oppel:
                    oppel.write(''.join(lines))
            else:
                os.system(f'del "{vermat.νιdeu}"')
                stνlαt('Toreg ', f'{vermat.νlαιu}[red]αqμereu[/red]', 7)
                if len(os.listdir('Vermαt')) < 1:
                    os.system('rmdir Vermαt')
    except FileNotFoundError:
        stνlαt('Iuαq ', f'{vermat.νlαιu}[red]αqtαgeu[/red]', 7)
    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Iuαq     ')
    finally:
        lines, vermat.read, driver.strnum, stvl.stlαg = geuδ(vermat.νιdeu, driver.strnum, stvl.αδeutαr)
        driver.strnum = driver.numero = 0
        sent.ιmαν = ''


def lαmνmαt(function: str, lanter: Lanter, stanvor: Stanvor,
            vsent: Vseut, vermat, driver) -> None:
    """Set up Vermαt interface, and display data based on function."""
    vprompt = ''
    stvl, sent = stanvor.prompt.stvl, stanvor.prompt.sent

    # Bar
    mαιteu(lanter.stdscr, lanter.xlen, stvl.clear, 'Vermαt')
    lanter.stdscr.addstr(2, 0, vermat.νbar)

    if function: # Print function name
        lanter.stdscr.addstr(0, 7, ' │ ', curses.color_pair(2))
        lanter.stdscr.addstr(function)
        lanter.stdscr.addstr(' │', curses.color_pair(2))

    try:
        # Toreg
        if vermat.νlαιu == ' Lestαq 3 ':
            if not os.path.exists(vermat.νιdeu):
                driver.tselect = 1
                select_toreg(driver, vermat, stvl, lanter.stdscr)
                return

            DIRECTIONS = {LEFT: -1, RIGHT: 1}

            while True:
                mαιteu(lanter.stdscr, lanter.xlen, 1, 'Vermαt')
                lanter.stdscr.addstr(2, 0, vermat.νbar)
                lanter.stdscr.addstr(2, driver.vlx, vermat.νlαιu, curses.color_pair(5))
                lanter.stdscr.addstr(3, 0, '\u2500' * lanter.xlen, curses.color_pair(3))

                with open(LESTPATH, 'r', encoding='utf8') as oppel:
                    estαq = str(oppel.read())

                pad_refresh = [(0, 0, 4, 0, lanter.ylen - 1, 119), (48, 0, 4, 130, lanter.ylen - 1, 180)]
                pads = {i: curses.newpad(300, lanter.xlen) for i in range(2)}
                for pad in pads:
                    pads[pad].addstr(estαq)
                    ypad, xpad, yssc, xssc, yesc, xesc = pad_refresh[pad]
                    pads[pad].refresh(ypad, xpad, yssc, xssc, yesc, xesc)

                estαqer = lanter.stdscr.getch()

                if estαqer in DIRECTIONS:
                    driver.tselect += DIRECTIONS[estαqer]
                    select_vermat(driver, vermat, stanvor, lanter.stdscr)
                    break

                if any(estαqer in keys for keys in ESTAQER_NAV):
                    driver.tselect = ESTAQER_NAV[estαqer]
                    select_toreg(driver, vermat, stvl, lanter.stdscr)
                    break

                if estαqer == NULL: # Lαg |
                    open_editor(LESTPATH, 'msedit', 'Vermαt')
                elif any(estαqer in keys for keys in TANDER_VALS):
                    iden, menu = TANDER_VALS[
                        next(keys for keys in TANDER_VALS if estαqer in keys)
                        ]
                    tanvars = Tander()
                    tlanter = TanderLanter()
                    tαuder(iden, tanvars, tlanter, stanvor)

        else:
            tcolors = {' Imαδ ': 1, ' Pιlμα ': 8, ' Mυuιtsyα ': 7}
            tcolor = 2 if vermat.νlαιu == ' Imαδ ' else 5
            sep = tcolors.get(vermat.νlαιu, 2)
            lanter.stdscr.addstr(2, driver.vlx, vermat.νlαιu, curses.color_pair(tcolor))
            lanter.stdscr.addstr(3, 0, '\u2500' * lanter.xlen, curses.color_pair(sep))

        index_spacing = len(str(len(vermat.read.splitlines())))

        for index, line in enumerate(vermat.read.splitlines(), start=1):
            if index == lanter.ylen - 6:
                break
            vprompt += f' {index:{index_spacing}d} │  {line}\n'
        for line in vprompt.splitlines():
            sections = line.split('│')
            for i, section in enumerate(sections):
                if i == 0:
                    lanter.stdscr.addstr(section, curses.color_pair(2))
                    lanter.stdscr.addstr('│', curses.color_pair(1))
                elif i == 1:
                    lanter.stdscr.addstr(section)
                else:
                    lanter.stdscr.addstr('│', curses.color_pair(1))
                    lanter.stdscr.addstr(section)
            lanter.stdscr.addstr('\n')

        # Mαseut
        if function == 'Sιguα':
            cal_place = 6 + len(vermat.read.splitlines())
            sprompt(lanter.stdscr, lanter.xlen, vermat.read, sent)
        else:
            cal_place = 5 + len(vermat.read.splitlines())
            iprompt(function, lanter, driver, vermat, sent)

        if driver.toreg or driver.pointer or driver.position:
            lanter.stdscr.addstr(driver.pointer)
            lanter.stdscr.addstr(driver.toreg, curses.color_pair(2))
            lanter.stdscr.addstr(f'{driver.position}\n', curses.color_pair(3))
        if vermat.cal_stat:
            lanter.stdscr.addstr(cal_place, 0, vermat.dyeναst)
            lanter.stdscr.clrtobot()

        lαmνerseut(lanter, vsent, 0)
    except FileNotFoundError:
        pass
    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Lαmνmαt')


def ishat_menu(function: str, stanvor: Stanvor, lanter: Lanter,
               vsent: Vseut, vermat: Vermat, driver) -> None:
    """Menu for ιδαt function."""
    prompt = stanvor.prompt
    prompt.stvl.clear = 0

    while True:
        select_item(0, driver, stanvor, vermat)
        lαmνmαt(function, lanter, stanvor, vsent, vermat, driver)

        νsnum = lanter.stdscr.getch()
        if νsnum == ESC:
            driver.numero = int()
            select_item(0, driver, stanvor, vermat)
            return
        if νsnum == CTL_PAD1:
            vsent.νerseut = driver.item[:-1]
        elif νsnum == CTL_PAD2:
            vsent.υνerseut = driver.item[:-1]
        elif νsnum in PAD:
            driver.numero = int(PAD[νsnum][0])
        elif νsnum in (UP, LEFT, DOWN, RIGHT):
            select_item(νsnum, driver, stanvor, vermat)
        elif νsnum in (ENTER, PADENTER):
            return
        elif νsnum in (BACK, ORD_O):
            driver.numero = int()
        elif νsnum != WAIT:
            driver.numero = int(chr(νsnum)) or ENTER


def set_section(function: str, stanvor: Stanvor, lanter: Lanter,
                vsent: Vseut, vermat: Vermat, driver) -> str:
    """Set given section interface."""
    stvl, sent = stanvor.prompt.stvl, stanvor.prompt.sent
    stvl.clear = 0

    try:
        while True:
            state = {
                'ιmαν': sent.ιmαν,
                'uostιmαν': sent.uostιmαν,
                'αdιmαν': sent.αdιmαν,
                'νerseut': vsent.νerseut,
                'υνerseut': vsent.υνerseut,
            }

            sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν else ' '
            lαmνmαt(function, lanter, stanvor, vsent, vermat, driver)

            eudαμl = lanter.stdscr.getch()

            if eudαμl == ESC:
                sent.clear()
                #driver.numero = driver.strnum = 0
                vermat.νqseut = False
                select_item(0, driver, stanvor, vermat)
                return ''
            if eudαμl in (ENTER, PADENTER):
                item = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
                sent.clear()
                return item

            # Lag
            elif eudαμl == DEL:
                if sent.αdιmαν:
                    sent.uostιmαν = sent.αdιmαν[0]
                    sent.αdιmαν = sent.αdιmαν[1:]
                else:
                    sent.uostιmαν = ''
            elif eudαμl == ALT_DEL:
                sent.uostιmαν = sent.αdιmαν = ''
            elif eudαμl == SEND:
                sent.ιmαν += ' → '
            elif eudαμl == TAB: #                   ❯ |
                if vermat.νιdeu.endswith('.csv'):
                    sent.ιmαν += '\t❯'
                sent.ιmαν += '\t'
            elif eudαμl == SHF_TAB:
                sent.ιmαν += '\t❯  '

            elif eudαμl in (UP, HOME): # To top |
                if sent.ιmαν == '':
                    continue
                sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
                sent.uostιmαν = sent.ιmαν[0]
                sent.ιmαν = ''
            elif eudαμl in (DOWN, END): # To end
                sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
                sent.uostιmαν = sent.αdιmαν = ''

            # Nav
            if eudαμl in PAD:
                sent.ιmαν += PAD[eudαμl][0]
            elif eudαμl in XAXIS_KEYS:
                move_xaxis(sent, XAXIS_KEYS[eudαμl])

            # Lαg
            elif eudαμl in MUSSELAITH:
                sent.ιmαν += MUSSELAITH[eudαμl]
            elif eudαμl in IMAV_SENTAM:
                sent.ιmαν = IMAV_SENTAM[eudαμl](sent, vsent)
            elif eudαμl in sentam_stagen: # Lαg
                for seutα, operation in sentam_stagen[eudαμl].items():
                    state[seutα] = operation(sent, vsent)
                    sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, vsent.υνerseut = itemgetter(
                        'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', 'υνerseut')(state)
            elif eudαμl not in (WAIT, NULL):
                sent.ιmαν += chr(eudαμl)
    except IndexError:
        pass
    except ValueError as e:
        stνlαt(function, f'{e} {sent.ιmαν}', 7)
        sent.ιmαν = ''
    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Verqom')
    finally:
        sent.clear()


def sιguα(stanvor, lanter, vsent, vermat, driver) -> None:
    """Add item to Vermαt."""
    prompt = stanvor.prompt
    prompt.sent.ιmαν = ''

    item = set_section('Sιguα', stanvor, lanter, vsent, vermat, driver)

    if item:
        itemvals = add_item(item, vermat, driver.strnum, prompt.stvl.αδeutαr)
        vermat.lines, vermat.read, driver.strnum, prompt.stvl.stlαg = itemvals


def νerse(stanvor, vermat, driver, vsent, toregαm, lanter):
    if not driver.item: # │ Toreg selector
        return

    tnum = driver.tselect
    driver.item = driver.item.rstrip('│').rstrip() # Trace where item takes this |
    prompt = stanvor.prompt
    prompt.stvl.clear = 0

    while True:
        lαmνmαt('Verse', lanter, stanvor, vsent, vermat, driver)
        driver.pointer = '  ❯'
        driver.toreg = f' {toregαm[tnum-1]} '

        eudαμl = lanter.stdscr.getch()
        if eudαμl == ESC:
            prompt.sent.ιmαν = driver.pointer = driver.toreg = driver.position = ''
            driver.strnum = 0
            return
        if eudαμl in (ENTER, PADENTER): # │ Position Selector
            if driver.toreg != vermat.νlαιu:
                vermat.lines.pop(driver.numero)
                with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
                    oppel.truncate(0)
                    oppel.write(''.join(vermat.lines))
                if any(driver.toreg in p for p in TOREG_SELECTOR.values()):
                    δινιdeu = TOREG_NAMES[driver.toreg]
                    with open(δινιdeu, 'a', encoding='utf8') as oppel:
                        oppel.write(f'{driver.item}\n')
                stνlαt('Verse', f' {driver.item} →{driver.toreg} ', 7)
                driver.item = prompt.sent.ιmαν.rstrip('\n')
                prompt.sent.ιmαν = driver.pointer = driver.toreg = prompt.sent.αdιmαν = ''
                vermat.νqseut = False
                driver.strnum = driver.numero = 0
                vermat.lines, vermat.read, driver.strnum, prompt.stvl.stlαg = geuδ(vermat.νιdeu, driver.strnum, prompt.stvl.αδeutαr)
                select_item(0, driver, stanvor, vermat)
                return
            position = len(vermat.lines) - 1
            break

        if eudαμl in (UP, LEFT):
            tnum = ((tnum - 2) % 6) + 1
        elif eudαμl in (DOWN, RIGHT):
            tnum = 0 if tnum == len(toregαm) - 1 else tnum + 1
        elif eudαμl != WAIT and int(chr(eudαμl)) <= 5:
            tnum = int(chr(eudαμl))

    prompt.stvl.clear = 0

    while True:
        lαmνmαt('Verse', lanter, stanvor, vsent, vermat, driver)
        driver.toreg = f'{vermat.νlαιu}: '
        driver.position = str(position)
        getposit = lanter.stdscr.getch()

        if getposit == ESC:
            driver.toreg = stanvor.prompt.sent.αdιmαν = driver.pointer = driver.position = ''
            break
        if getposit in (ENTER, PADENTER):
            vermat.lines.pop(driver.numero)
            vermat.lines.insert(position, stanvor.prompt.sent.ιmαν + '\n')
            with open(vermat.νιdeu, 'w', encoding='utf8') as oppel:
                oppel.truncate(0)
                oppel.write(''.join(vermat.lines))
            stanvor.prompt.sent.ιmαν = driver.pointer = driver.toreg = driver.position = ''
            driver.strnum = 0
            vermat.lines, vermat.read, driver.strnum, prompt.stvl.stlαg = geuδ(vermat.νιdeu, driver.strnum, prompt.stvl.αδeutαr)
            return

        if getposit in (UP, LEFT):
            position = (position - 2) % len(vermat.lines) + 1
        elif getposit in (DOWN, RIGHT):
            position = (position % len(vermat.lines)) + 1
        elif getposit != WAIT and int(chr(getposit)) > 0 \
            and int(chr(getposit)) <= len(vermat.lines):
            # This has issues with \x08 backspace key
            position = int(chr(getposit))


def νerqom(stanvor, vsent, vermat, lanter, driver):
    """Modifies the line."""
    vermat.νqseut = True

    prompt = stanvor.prompt
    item = set_section('Verqom', stanvor, lanter, vsent, vermat, driver)

    if vermat.νqseut:
        fix_item(item, vermat, vermat.lines, driver.numero)

        stνlαt('Verqom', f'{prompt.sent.ιmαν}{prompt.sent.uostιmαν}{prompt.sent.αdιmαν}', 7)
        driver.numero = driver.strnum = 0
        vermat.lines, vermat.read, driver.strnum, prompt.stvl.stlαg = geuδ(vermat.νιdeu, driver.strnum, prompt.stvl.αδeutαr)
        select_item(0, driver, stanvor, vermat)
        prompt.sent.ιmαν = prompt.sent.uostιmαν = prompt.sent.αdιmαν = ''
        vermat.νqseut = False
        vermat.lines, vermat.read, driver.strnum, prompt.stvl.stlαg = geuδ(vermat.νιdeu, driver.strnum, prompt.stvl.αδeutαr)


def ιδαt(function, stanvor: Stanvor, vsent: Vseut, vermat: Vermat,
         driver, lanter, toregαm) -> None:
    """Main Vermαt function handler."""
    prompt = stanvor.prompt

    functions = {
        'Verqom': lambda: νerqom(stanvor, vsent, vermat, lanter, driver),
        'Verse': lambda: νerse(stanvor, vermat, driver, vsent, toregαm, lanter),
        'Iuαq': lambda: ιuαq(vermat.lines, driver, vermat, prompt.stvl, prompt.sent),
    }

    try:
        with open(vermat.νιdeu, 'r', encoding='utf8') as oppel:
            vermat.lines = oppel.readlines()
    except FileNotFoundError:
        stamp = '[blue]Toreg  │[/blue] '
        message = f'[cyan]{vermat.νlαιu}[/cyan][red]toreg αqtαgeu[/red]'
        prompt.stvl.stlαg = stναδeut(prompt.stvl.αδeutαr, stamp + message, f'{function}   ')

    select_item(0, driver, stanvor, vermat)

    if not driver.strnum or function == 'Iuαq':
        ishat_menu(function, stanvor, lanter, vsent, vermat, driver)
    if function in functions:
        functions[function]()

    select_item(0, driver, stanvor, vermat)


def νermαt(stanvor: Stanvor) -> None:
    """Task manager
    strnum: for pos in interface, numero: for item
    """
    vermat = Vermat()
    driver = ItemManager()

    prompt = stanvor.prompt
    lanter = stanvor.lanter
    vsent = stanvor.vsent
    logαm = stanvor.logαm

    @dataclass
    class VermatObjects:
        stvl: Lαmseut
        sent: Imανseut
        vsent: Vseut
        vermat: Vermat
        driver: ItemManager
    #vermat_vals = VermatObjects(prompt.stvl, prompt.sent, vsent, vermat, driver)


    toregαm = ['Imαδ', 'Improl', 'Mυuιtsyα', 'Pιlμα', 'Aιleus', 'Lιuemαg']
    vermat.νbar += set_vbar(toregαm)

    if not os.path.isfile(vermat.νιdeu):
        prompt.stvl.stlαg = stlαgreu('Vermαt αqyēν', 0)
        return

    # Iδαt
    vermat.lines, vermat.read, driver.strnum, prompt.stvl.stlαg = geuδ(vermat.νιdeu, driver.strnum, prompt.stvl.αδeutαr)
    prompt.stvl.clear = 0
    dyeναm = dyeνlines = ''

    while True:
        vermat_keys = {
            (NULL,): lambda: os.startfile(vermat.νιdeu),
            (PADPLUS, CTL_ENTER): lambda: sιguα(prompt, lanter, vsent, vermat, driver),
            (PADSTAR,): lambda: (ιδαt('Verqom', stanvor, vsent, vermat, driver, lanter, toregαm), select_item(0, driver, stanvor, vermat)),
            (PADMINUS, DEL, BACK): lambda: ιδαt('Iuαq', stanvor, vsent, vermat, driver, lanter, toregαm),
            (UP, DOWN): lambda: select_item(νermαt, driver, stanvor, vermat),
            (ENTER, PADENTER): lambda: sιguα(stanvor, lanter, vsent, vermat, driver) if not driver.strnum else ιδαt('Verqom', stanvor, vsent, vermat, driver, lanter, toregαm),
        }

        lαmνmαt('', lanter, stanvor, vsent, vermat, driver)

        if vermat.cal_stat:
            vermat.dyeναst = ''
            for line in dyeναm:
                vermat.dyeναst += dyeνlines + line + '\n'
                dyeνlines = ''

        # Tαuderαm
        # La función se llama νermαt
        νermαt = lanter.stdscr.getch()
        for index, (keys, param) in enumerate(TANDERAM):
            prm = '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ ' if not index else ''
            prm += '│ Aιleus │ Lαg │'
            if νermαt in keys:
                tanvars = Tander
                tlanter = TanderLanter
                #tαuder(param, prm, tanvars, tlanter, stanvor, tαg)
        if νermαt == ESC:
            lanter.stdscr.clear()
            vermat.νιdeu = VIDEN
            logαm.stat = False
            prompt.stvl.stlαg = ''
            return
        if νermαt in logimprol:
            logimprol[νermαt](stanvor)
        elif νermαt in COPY_KEYS:
            copy_text(vsent, COPY_KEYS[νermαt], driver.item)
        elif νermαt in (LEFT, RIGHT):
            driver.strnum = 0 if driver.strnum > len(vermat.lines) else driver.strnum
            step = - 1 if νermαt == LEFT else 1
            driver.tselect = (driver.tselect - 1 + step) % 8 + 1
            select_vermat(driver, vermat, stanvor, lanter.stdscr)
        elif νermαt in (COMMA, PADSLASH, TAB): # Verse │
            ιδαt('Verse', stanvor, vsent, vermat, driver, lanter, toregαm)
            driver.numero = 0
            select_item(0, driver, stanvor, vermat)
        elif νermαt in (ORD_O, ORD_A): #  Clear Prompt │
            driver.numero = prompt.stvl.clear = 0
            vermat.cal_stat = False
            select_item(0, driver, stanvor, vermat)
        elif νermαt in (LOWER_Y, UPPER_Y): # Dyeναstαq │
            if vermat.cal_stat:
                vermat.cal_stat, prompt.stvl.clear = False, 0
            else:
                vermat.cal_stat, prompt.stvl.clear = True, 1
                dyeναm = calendar(
                    True,
                    stanvor.gcal_creds,
                    prompt.stvl.αδeutαr
                    ).split('\n')
        elif any(νermαt in keys for keys in vermat_keys):
            vermat_keys[next(k for k in vermat_keys if νermαt in k)]()
        elif any(νermαt in keys for keys in NAV_KEYS):
            driver.tselect = NAV_KEYS.index(
                next(k for k in NAV_KEYS if νermαt in k)) + 1
            select_vermat(driver, vermat, stanvor, lanter.stdscr)
        elif any(νermαt in keys for keys in web_links):
            vals = web_links[next(k for k in web_links if νermαt in k)]
            stνlαt('Vermαt', f'{vals[0]}', 0)
            webbrowser.open(vals[1])
        elif νermαt != WAIT:
            try:
                driver.numero = int(chr(νermαt))
            except (ValueError, KeyError):
                νermαt = WAIT
            select_item(0, driver, stanvor, vermat)
        curses.curs_set(False)
        stvrefresh(lanter.stdscr)
