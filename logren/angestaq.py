"""Augestαq: Financial section."""

import curses
import datetime
import os

from dataclasses import dataclass
from typing import List

from core.keys import (
    WAIT, ESC, ENTER, BACK, NUM0, POINT, MINUS, CONCLUDE,
    UPPER_M, LOWER_M, UPPER_O, LOWER_O, LOWER_I
)
from core.sentam import Lanter, Stanvor
from core.stv import mαιteu, process_handlers
from core.stvlog import stνlαt, stναδeut
from utils import logren


ANGPATH = r'Augest\Augestαq.csv'
ISQPATH = r'Augest\Augest.Isqyαu.txt'
ANGMANSLAG = r'Augest\Augest.Mαuslαg.txt'


@dataclass
class Augestαq:
    sub1: str = ''
    sub2: str = ''
    total: int = 0


# Interface
def _lαmαugest(lanter: Lanter, paths: List, sub1: str) -> None:
    """Structure of Augest section."""
    MENU = ' Iuslαg   Isqyαu   Mαuslαg'

    with open(paths[0], encoding='utf8') as oppel:
        tαuder = oppel.read()
    with open(paths[1], 'r', encoding='utf8') as oppel:
        αugestlines = len(oppel.readlines())
        oppel.seek(0)
        αugιsqyαu = oppel.read()

    pad1 = curses.newpad(40, 100)
    pad1.addstr(tαuder)
    pad1.refresh(0, 0, 5, 0, 39, 49)
    pad2 = curses.newpad(2000, 100)
    pad2.addstr(αugιsqyαu)
    pad2.refresh(αugestlines - 18, 0, 5, 60, 38, 150)

    lanter.stdscr.addstr(2, 0, f'{MENU:<{lanter.xlen}}', curses.color_pair(13))

    lanter.stdscr.addstr(40, 0, '\u2500' * lanter.xlen, curses.color_pair(2))
    lanter.stdscr.addstr(sub1)


# Sιguα
def _lαmαusιg(lanter: Lanter, αδeutαr, subs): # Sιguα Main Structure
    """Here resides all the visual structure of sιguα section."""
    sub1, sub2 = subs
    #chn = ''

    mαιteu(lanter, 1, ιdeu='Augestαq')
    lanter.stdscr.addstr(0, 8, ' │ ', curses.color_pair(2))
    lanter.stdscr.addstr('Sιguα')
    lanter.stdscr.addstr(' │', curses.color_pair(2))

    try:
        with open(ANGPATH, encoding='utf8') as oppel:
            tαuder = oppel.read()
    except Exception as e:
        _ = stναδeut(αδeutαr, str(e), 'Augestαq')

    lanter.stdscr.addstr(2, 0, ' Mαyeq   Otaleu   Auqopt')
    #lanter.stdscr.addstr(2, z, f' {chn} ' if chn else '', curses.color_pair(5))
    lanter.stdscr.addstr(3, 0, '\u2500' * lanter.xlen, curses.color_pair(2))
    lanter.stdscr.addstr(f'\n{tαuder}{sub1}{sub2}')


def _sιguα_module(sub1: str, subtotal: int) -> None:
    """Sιguα magnitude filter, register and subtotal return."""
    sιguα_list = [sub1]
    if subtotal < 10:
        sιguα_list.append(f' {subtotal} ge\n')
    else:
        if not subtotal % 10:
            sιguα_list.append(f' {subtotal//10} pα\n')
        else:
            sιguα_list.append(f'{subtotal} ge\n')

    with open(ANGPATH, 'a', encoding='utf8') as oppel:
        oppel.write(''.join(sιguα_list))


def _αusιguα(channels, lanter: Lanter, angest: Augestαq): # Channel sιguα
    αugestαq = ''

    def _clearall() -> None:
        lanter.stdscr.clear()
        angest.sub1 = angest.sub2 = ''

    def _process_signa() -> None:
        subtotal = int(angest.sub2)
        _sιguα_module(angest.sub1, subtotal)
        angest.sub1 = ''
        angest.total += subtotal

    def _add_tosub2() -> None:
        angest.sub2 += chr(sιguα)

    def _del_fromsub2() -> None:
        angest.sub2 = angest.sub2[:-1]


    for channel_name in channels:
        channel = channel_name
        angest.sub1 += f'{channel} │ ' # Channel prompt
        angest.sub2 = ''               # Input prompt

        while True:
            _lαmαusιg(lanter, 0, (angest.sub1, angest.sub2))

            sιguα = lanter.stdscr.getch()
            process_handlers((
                (lambda: sιguα == ESC, _clearall),
                (lambda: sιguα == ENTER, lambda: _process_signa),
                (lambda: sιguα == BACK, _del_fromsub2),
                (lambda: sιguα != WAIT, _add_tosub2)
            ))

            if sιguα in CONCLUDE:
                break


    if angest.total:
        _sιguα_module('Sιguα  │ ', angest.total)

    angest.sub1 = angest.sub2 = ''
    angest.total = 0

    with open(ISQPATH, 'a', encoding='utf8') as oppel:
        oppel.write(f'{('\n')*4}'.join(αugestαq))

    return angest.sub1


def _αugest_sιguα(lanter: Lanter, αδeutαr, angest: Augestαq) -> None: # Sιguα channel
    """Sιguα sections menu."""
    sιeνιt = datetime.date.today()
    sιeν = sιeνιt.strftime('%d%m')
    u25 = '\u2500'

    angest.sub1 = f"\n\n{'──'*28}\n{str(sιeν)}   │\n{'──'*28}\n\n" # Datestamp
    sιg_dir = {
        (LOWER_M, UPPER_M): ('Mαyeq', ['Delαus', 'Dαuqαδ', 'Soleu '], 0),
        (LOWER_O, UPPER_O):
        ('Otαleu', ['Neqeu ', 'Aplαt ', 'Auqopt', 'Nυ    ', 'Bιuαus'], 9),
    }

    def _enter_signa() -> None:
        acc, channels = next(v for v in sιg_dir if sιguα in v)
        angest.sub1 += f'{acc}\n{u25*7}┬{u25*6}\n'
        angest.sub1 = _αusιguα(channels, lanter, angest)

    while True:
        _lαmαusιg(lanter, αδeutαr, (angest.sub1, ''))

        sιguα = lanter.stdscr.getch()

        process_handlers((
            (lambda: sιguα == ESC, lanter.stdscr.clear()),
            (lambda: sιguα == NUM0, logren.open_editor(ANGPATH, 'msedit', 'Augestαq')),
            (lambda: any(sιguα in keys for keys in sιg_dir), _enter_signa),
        ))

        if sιguα == ESC:
            return


# Iuαq
def _delete_angest():
    with open(ANGPATH, 'r', encoding='utf8') as oppel:
        ιsqyαu = oppel.readlines()

    with open(ISQPATH, 'a', encoding='utf8') as oppel:
        try:
            oppel.write('│   '.join(ιsqyαu))
            ιsqyαutαl = ' ❯  Isqyαu sιguet'
        except Exception:
            stνlαt('Augestαq', 'Isqyαu ιuαqtαgeu')

    with open(ANGPATH, 'w', encoding='utf8') as oppel:
        oppel.truncate(0)

    stνlαt('Augestαq', f'Augestαq αqtανeu {ιsqyαutαl}')


def _inaq_menu(lanter: Lanter) -> None:
    while True:
        mαιteu(lanter, 1, ιdeu='Augestαq')
        lanter.stdscr.addstr(0, 8, ' │ ', curses.color_pair(2))
        lanter.stdscr.addstr('Iuαq')
        lanter.stdscr.addstr(' │', curses.color_pair(2))
        prompt = 'Seνdαl uα Augestαq αqtαν ?'

        _lαmαugest(lanter, [ANGPATH, ISQPATH], prompt)

        sιguα = lanter.stdscr.getch()

        if sιguα == ESC:
            break

        if sιguα == ENTER:
            _delete_angest()
            break

    lanter.stdscr.clear()


# Main function
def αugestαq(stanvor: Stanvor) -> None:
    """Augestαq main function."""
    angest = Augestαq()
    lanter = stanvor.lanter
    αδeutαr = stanvor.stvl.αδeutαr

    while True:
        mαιteu(lanter, 1, ιdeu='Augestαq')
        _lαmαugest(lanter, [ANGPATH, ISQPATH], angest.sub1)

        key = lanter.stdscr.getch()

        process_handlers((
            (lambda: key == ESC, lanter.stdscr.clear),
            (lambda: key == POINT, lambda: _αugest_sιguα(lanter, αδeutαr, angest)),
            (lambda: key == MINUS, lambda: _inaq_menu(lanter)),
            (lambda: key == NUM0, lambda: logren.open_editor(ANGPATH, 'msedit', 'Augestαq ')),
            (lambda: key == LOWER_I, lambda: os.startfile(ISQPATH)),
            (lambda: key == LOWER_M, lambda: os.startfile(ANGMANSLAG)),
        ))

        if key == ESC:
            return
