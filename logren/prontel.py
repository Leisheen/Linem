from dataclasses import dataclass

from core.colors import NAVY
from core.keys import ESC, ENTER, LIT_A, LIT_B, ORD
from core.stv import lαδmαιteu, process_handlers
from core.sentam import Stanvor
from operations.interface import getch


@dataclass
class Prontel:
    flow_state: bool = False
    flow: str = ''
    flow_colors: tuple = (0, 0)
    shvider: str = '│├'
    void: str = ''

def _print_prontel(stanvor: Stanvor, prt: Prontel) -> None:
    lαδmαιteu(stanvor)
    screen = stanvor.screen
    screen.insert(0, 2, prt.shvider)
    screen.insert(prt.void)
    fg, bg = prt.flow_colors
    screen.insert(prt.flow, fg=fg, bg=bg)
    screen.render()


def proutel(stanvor: Stanvor) -> None:
    """Proutel program."""
    prt = Prontel()
    KEYS = (LIT_A, LIT_B, ORD)

    def _set_prontel() -> None:
        prt.flow_colors = prt.flow_colors if prt.flow_colors else (NAVY, 0)
        prt.void = ''
        prt.flow_state = not prt.flow_state

    def _process_key(key: int) -> None:
        if key == ORD:
            prt.flow_state = False
        else:
            prt.flow_colors = (NAVY, 0) if key == LIT_A else (0, 0)

    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Proutel'
    xlen = stanvor.screen.width
    while True:
        if prt.flow_state and len(prt.flow) < xlen - 2:
            prt.flow += '\u2500'
        elif not prt.flow_state:
            prt.void += ' ' if len(prt.void) < xlen else ''
            prt.flow = prt.flow[:-1] if prt.flow else ''

        _print_prontel(stanvor, prt)

        key = getch(stanvor)[0]

        if key == ESC:
            stanvor.stvl.clear()
            return

        process_handlers((
            (lambda: key == ENTER, _set_prontel),
            (lambda: key in KEYS, lambda: _process_key(key)),
            (lambda: key == ORD, False)
        ))
