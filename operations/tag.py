import webbrowser

from core.keys import TAB, DEL, ALT_DEL, XAXIS, CTL_ENTER
from core.sentam import Stanvor, Imανseut
from core.stv import process_handlers

from utils.prompt import (
     addchar, del_char, tab_to_imav, clear_remaining,
     move_horizontal, move_inline, line_limits, check_movefixes
)
from utils.stv_utils import check_globalkeys, sentam_stagen, set_sentam, logimprol


def tαg(vkey: int, char: int, stanvor: Stanvor) -> Imανseut:
    """Global input manager."""
    sent = stanvor.sent

    sent.ιmαν, vkey = check_globalkeys(stanvor, vkey, logimprol)

    if not vkey:
        return sent

    process_handlers((
        (lambda: vkey == TAB,             lambda: tab_to_imav(sent)),
        (lambda: vkey == DEL,             lambda: del_char(stanvor.sent)),
        (lambda: vkey == ALT_DEL,         lambda: clear_remaining(stanvor)),
        (lambda: vkey in line_limits,     lambda: line_limits[vkey](sent)),
        (lambda: check_movefixes(vkey),   lambda: move_inline(vkey, sent)),
        (lambda: vkey in sentam_stagen,   lambda: set_sentam(vkey, stanvor)),
        (lambda: vkey in XAXIS,           lambda: move_horizontal(vkey, sent)),
        (lambda: vkey == CTL_ENTER,       lambda: webbrowser.open(sent.ιmαν)),
        (lambda: chr(char).isprintable(), lambda: addchar(char, sent))
    ))

    return sent
