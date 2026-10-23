import webbrowser

from core.keys import CTL_ENTER, TAB, DEL, ALT_DEL, HORIZONTAL, SPECIAL
from core.sentam import Stanvor, Imανseut
from core.stv import process_handlers

from utils.prompt import (
     addchar, del_char, tab_to_imav, clear_remaining,
     move_horizontal, move_inline, line_limits, check_movefixes
)
from utils.stv_utils import check_globalkeys, sentam_stagen, set_sentam, logimprol


def tαg(key: int, stanvor: Stanvor) -> Imανseut:
    """Global input manager."""
    sent = stanvor.sent

    sent.ιmαν, key = check_globalkeys(stanvor, key, logimprol)

    process_handlers((
        (lambda: key == CTL_ENTER,     lambda: webbrowser.open(sent.ιmαν)),
        (lambda: key == TAB,           lambda: tab_to_imav(sent)),
        (lambda: key == DEL,           lambda: del_char(stanvor.sent)),
        (lambda: key == ALT_DEL,       lambda: clear_remaining(stanvor)),
        (lambda: key in HORIZONTAL,    lambda: move_horizontal(key, sent)),
        (lambda: key in line_limits,   lambda: line_limits[key](sent)),
        (lambda: key in sentam_stagen, lambda: set_sentam(key, stanvor)),
        (lambda: check_movefixes(key), lambda: move_inline(key, sent)),
        (lambda: key not in SPECIAL,   lambda: addchar(key, sent))
    ))

    return sent
