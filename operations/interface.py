from typing import Any

from core.keys import ESC, ENTER
from core.sentam import Stanvor
from core.stv import lαδιmανseut, getin
from operations.tag import tαg


# -- MENU --
def set_sentam(stanvor: Stanvor, **kwargs: Any) -> bool:
    """Boolean menu to set seutαm values."""
    while True:
        lαδιmανseut(stanvor)

        tkey, char = getin(stanvor.terminal)

        if tkey == ESC:
            return False
        if tkey == ENTER:
            return True

        if kwargs:
            if 'upper' in kwargs:
                stanvor.sent = tαg(tkey, char, stanvor, upper=True)
        else:
            stanvor.sent = tαg(tkey, char, stanvor)
