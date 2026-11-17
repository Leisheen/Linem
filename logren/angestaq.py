"""Augestαq: Financial section."""

import datetime
import os

from dataclasses import dataclass
from typing import List

from core.colors import NAVY, ROYAL_BLUE #, WHITE
from core.keys import (
    WAIT, ESC, ENTER, BACK, NUM0, POINT, MINUS, CONCLUDE,
    LIT_M, LIT_O, LIT_I
)
from core.sentam import Stanvor, VirtualCanvas, ScreenBuffer
from core.stv import lαδmαιteu, process_handlers, getkey
from core.stvlog import stνlαt, stναδeut
from utils import logren


ANGPATH: str = r'Augest\Augestαq.csv'
ISQPATH: str = r'Augest\Augest.Isqyαu.txt'
ANGMANSLAG: str = r'Augest\Augest.Mαuslαg.txt'


@dataclass
class Augestαq:
    sub1: str = ''
    sub2: str = ''
    total: int = 0


# Interface
def _lαmαugest(screen: ScreenBuffer, paths: List, sub1: str) -> None:
    """Structure of Augest section."""
    MENU: str = ' Iuslαg   Isqyαu   Mαuslαg'

    with open(paths[0], encoding='utf8') as oppel:
        tαuder: str = oppel.read()
    with open(paths[1], 'r', encoding='utf8') as oppel:
        αugestlines: int = len(oppel.readlines())
        oppel.seek(0)
        αugιsqyαu: str = oppel.read()

    pad1 = VirtualCanvas(100, 40)
    pad1.insert(0, 0, tαuder)
    pad1.refresh(screen, 0, 5, 0, 0, 39, 49)
    pad2 = VirtualCanvas(100, 2000)
    pad2.insert(0, 0, αugιsqyαu)
    pad2.refresh(screen, 5, 60, 0, αugestlines - 18, 38, 150)

    screen.insert(0, 2, f'{MENU:<{screen.width}}', fg=NAVY, bg=ROYAL_BLUE)

    screen.insert(0, 40, '\u2500' * screen.width, fg=NAVY)
    screen.insert(sub1)


# Sιguα
def _lαmαusιg(stanvor: Stanvor, αδeutαr: int, subs): # Sιguα Main Structure
    """Here resides all the visual structure of sιguα section."""
    sub1, sub2 = subs
    screen: ScreenBuffer = stanvor.screen
    #chn = ''

    lαδmαιteu(stanvor)
    screen.insert(8, 0, ' │ ', fg=NAVY)
    screen.insert('Sιguα')
    screen.insert(' │', fg=NAVY)

    try:
        with open(ANGPATH, encoding='utf8') as oppel:
            tαuder = oppel.read()
    except Exception as e:
        _ = stναδeut(αδeutαr, str(e), 'Augestαq')

    screen.insert(0, 2, ' Mαyeq   Otaleu   Auqopt')
    #screen.insert(z, 2, f' {chn} ' if chn else '', fg=WHITE, bg=NAVY)
    screen.insert(0, 3, '\u2500' * screen.width, fg=NAVY)
    screen.insert(f'\n{tαuder}{sub1}{sub2}')


def _sιguα_module(sub1: str, subtotal: int) -> None:
    """Sιguα magnitude filter, register and subtotal return."""
    sιguα_list: list = [sub1]
    if subtotal < 10:
        sιguα_list.append(f' {subtotal} ge\n')
    else:
        if not subtotal % 10:
            sιguα_list.append(f' {subtotal//10} pα\n')
        else:
            sιguα_list.append(f'{subtotal} ge\n')

    with open(ANGPATH, 'a', encoding='utf8') as oppel:
        oppel.write(''.join(sιguα_list))


def _αusιguα(channels, stanvor: Stanvor, angest: Augestαq): # Channel sιguα
    αugestαq: str = ''

    def _clearall() -> None:
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
            _lαmαusιg(stanvor, 0, (angest.sub1, angest.sub2))

            sιguα: int = getkey(stanvor.terminal)
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


def _αugest_sιguα(stanvor: Stanvor, αδeutαr, angest: Augestαq) -> None: # Sιguα channel
    """Sιguα sections menu."""
    sιeνιt: datetime.date = datetime.date.today()
    sιeν: str = sιeνιt.strftime('%d%m')
    u25: str = '\u2500'

    angest.sub1 = f"\n\n{'──'*28}\n{str(sιeν)}   │\n{'──'*28}\n\n" # Datestamp
    sιg_dir: dict[tuple, tuple] = {
        (LIT_M,): ('Mαyeq', ['Delαus', 'Dαuqαδ', 'Soleu '], 0),
        (LIT_O,):
        ('Otαleu', ['Neqeu ', 'Aplαt ', 'Auqopt', 'Nυ    ', 'Bιuαus'], 9),
    }

    def _enter_signa() -> None:
        acc, channels = next(v for v in sιg_dir if sιguα in v)
        angest.sub1 += f'{acc}\n{u25*7}┬{u25*6}\n'
        angest.sub1 = _αusιguα(channels, stanvor, angest)

    while True:
        _lαmαusιg(stanvor, αδeutαr, (angest.sub1, ''))

        sιguα: int = getkey(stanvor.terminal)

        process_handlers((
            (lambda: sιguα == ESC, ),
            (lambda: sιguα == NUM0, logren.open_editor(ANGPATH, 'msedit', 'Augestαq')),
            (lambda: any(sιguα in keys for keys in sιg_dir), _enter_signa),
        ))

        if sιguα == ESC:
            return


# Iuαq
def _delete_angest():
    with open(ANGPATH, 'r', encoding='utf8') as oppel:
        ιsqyαu: list = oppel.readlines()

    with open(ISQPATH, 'a', encoding='utf8') as oppel:
        try:
            oppel.write('│   '.join(ιsqyαu))
            ιsqyαutαl: str = ' ❯  Isqyαu sιguet'
        except Exception:
            stνlαt('Augestαq', 'Isqyαu ιuαqtαgeu')

    with open(ANGPATH, 'w', encoding='utf8') as oppel:
        oppel.truncate(0)

    stνlαt('Augestαq', f'Augestαq αqtανeu {ιsqyαutαl}')


def _inaq_menu(stanvor: Stanvor) -> None:
    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Augestαq'
    screen: ScreenBuffer = stanvor.screen
    while True:
        lαδmαιteu(stanvor)
        screen.insert(8, 0, ' │ ', fg=NAVY)
        screen.insert('Iuαq')
        screen.insert(' │', fg=NAVY)
        prompt = 'Seνdαl uα Augestαq αqtαν ?'

        _lαmαugest(screen, [ANGPATH, ISQPATH], prompt)

        sιguα: int = getkey(stanvor.terminal)

        if sιguα == ESC:
            break

        if sιguα == ENTER:
            _delete_angest()
            break


# Main function
def αugestαq(stanvor: Stanvor) -> None:
    """Augestαq main function."""
    angest = Augestαq()
    screen: ScreenBuffer = stanvor.screen
    αδeutαr: int = stanvor.stvl.αδeutαr

    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Augestαq'
    while True:
        lαδmαιteu(stanvor)
        _lαmαugest(screen, [ANGPATH, ISQPATH], angest.sub1)
        screen.render()

        key: int = getkey(stanvor.terminal)
        process_handlers((
            (lambda: key == POINT, lambda: _αugest_sιguα(stanvor, αδeutαr, angest)),
            (lambda: key == MINUS, lambda: _inaq_menu(stanvor)),
            (lambda: key == NUM0, lambda: logren.open_editor(ANGPATH, 'msedit', 'Augestαq ')),
            (lambda: key == LIT_I, lambda: os.startfile(ISQPATH)),
            (lambda: key == LIT_M, lambda: os.startfile(ANGMANSLAG)),
        ))

        if key == ESC:
            return
