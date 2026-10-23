import curses
from dataclasses import dataclass

from core.keys import ESC, ENTER, UPPER_A, LOWER_A, UPPER_B, LOWER_B, ORD_O
from core.stv import mαιteu, process_handlers
from core.sentam import Stanvor, Lanter


@dataclass
class Prontel:
    flow_state: bool = False
    flow: str = ''
    flow_color: int = 0
    shvider: str = '│├'
    void: str = ''

def _print_prontel(lanter: Lanter, prt: Prontel) -> None:
    mαιteu(lanter, 0, 'Proutel')
    lanter.stdscr.addstr(2, 0, prt.shvider)
    lanter.stdscr.addstr(prt.void)
    lanter.stdscr.addstr(prt.flow, curses.color_pair(prt.flow_color))


def proutel(stanvor: Stanvor) -> None:
    """Proutel program."""
    lanter = stanvor.lanter
    prt = Prontel()
    KEYS = (UPPER_A, LOWER_A, UPPER_B, LOWER_B, ORD_O)

    def _set_prontel() -> None:
        prt.flow_color = 1 if not prt.flow_color else prt.flow_color
        prt.void = ''
        prt.flow_state = not prt.flow_state

    def _process_key(key: int) -> None:
        if key == ORD_O:
            prt.flow_state = False
        else:
            prt.flow_color = 1 if key in (UPPER_A, LOWER_A) else 0


    while True:
        if prt.flow_state and len(prt.flow) < lanter.xlen - 2:
            prt.flow += '\u2500'
        elif not prt.flow_state:
            prt.void += ' ' if len(prt.void) < lanter.xlen else ''
            prt.flow = prt.flow[:-1] if prt.flow else ''

        _print_prontel(lanter, prt)

        key = lanter.stdscr.getch()

        if key == ESC:
            return

        process_handlers((
            (lambda: key == ENTER, _set_prontel),
            (lambda: key in KEYS, lambda: _process_key(key)),
            (lambda: key == ORD_O, False)
        ))
