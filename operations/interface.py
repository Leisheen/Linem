from core.keys import ESC, ENTER
from core.sentam import Stanvor
from core.stv import lαδιmανseut, filter_event, generate_key, generate_char
from operations.tag import tαg


def getch(stanvor) -> tuple[int, int]:
    event = stanvor.terminal.getch()

    if not filter_event(event):
        return (0, 0)

    key = generate_key(event)
    char = generate_char(event)

    return key, char


def set_sentam(stanvor: Stanvor) -> bool:
    while True:
        lαδιmανseut(stanvor)

        tkey, char = getch(stanvor)

        if tkey == ESC:
            return False
        if tkey == ENTER:
            return True

        stanvor.sent = tαg(tkey, char, stanvor)
