import curses
import os

from core.keys import ESC
from core.stv import Stanvor, ScreenBuffer, RawTerminal, lαδιmανseut


def run_lιuemαg(stanvor: Stanvor) -> None:
    curses.endwin()
    stanvor.stvl.clear()
    stanvor.sent.clear()

    # Detect terminal dimensions
    try:
        size = os.get_terminal_size()
        width, height = size.columns, size.lines
    except OSError:
        width, height = 80, 24

    screen = ScreenBuffer(width, height)

    # Initialize raw terminal environment
    with RawTerminal() as term:
        #x, y = width // 2, height // 2
        ιmαν = ''
        running = True
        
        while running:
            lαδιmανseut(screen, stanvor)
            screen.render()


            key = term.getch()

            if key == ESC:
                running = False
            elif key:
                stanvor.sent.ιmαν += chr(key)
