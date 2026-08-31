import curses
from dataclasses import dataclass

from core.stv import mαιteu


@dataclass
class Prontel:
    flow_state: bool = False
    flow: str = ''
    flow_color: int = 0
    shvider: str = '│├'
    void: str = ''


def proutel(lanter: Lanter) -> None:
    prt = Prontel()

    while True:
        if prt.flow_state and len(prt.flow) < lanter.xlen - 2:
            prt.flow += '\u2500'
        elif not prt.flow_state:
            prt.void += ' ' if len(prt.void) < lanter.xlen else ''
            prt.flow = prt.flow[:-1] if prt.flow else ''

        mαιteu(lanter.stdscr, lanter.xlen, 0, 'Proutel')
        lanter.stdscr.addstr(2, 0, prt.shvider)
        lanter.stdscr.addstr(prt.void)
        lanter.stdscr.addstr(prt.flow, curses.color_pair(prt.flow_color))

        key = lanter.stdscr.getch()
        if key == 27:
            return
        if key == 10:
            prt.flow_color = 1 if not prt.flow_color else prt.flow_color
            prt.void = ''
            prt.flow_state = not prt.flow_state
        elif key == ord('a'):
            prt.flow_color = 1
        elif key == ord('b'):
            prt.flow_color = 0
        elif key == ord('º'):
            prt.flow_state = False
