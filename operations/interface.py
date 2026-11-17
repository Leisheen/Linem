from core.keys import ESC, ENTER
from core.sentam import Stanvor
from core.stv import lαδιmανseut, getin
from operations.tag import tαg


# -- MENU --
def set_sentam(stanvor: Stanvor) -> bool:
    while True:
        lαδιmανseut(stanvor)

        tkey, char = getin(stanvor.terminal)

        if tkey == ESC:
            return False
        if tkey == ENTER:
            return True

        stanvor.sent = tαg(tkey, char, stanvor)
