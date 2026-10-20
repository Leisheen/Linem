"""Main commands for for Lιuemαg Stαuνor command line prompt."""
import os

from core.def_paths import INVASH, GCAL, GMAPS
from core.filesystem import logreu_select
from core.keys import (
    UP, DOWN, ESC, UPPER_D, LOWER_D, UPPER_Q, LOWER_Q, SHF_F12, CTL_PADSTOP,
    PADPLUS, PADMINUS, PADSTAR, PADSLASH, SHF_PADPLUS, PADMINUS, SHF_PADMINUS,
    SHF_PADENTER, CTL_PADSLASH, ALT_PADSLASH
)
from core.search import set_search, switch_search
from core.stv import reset

from logren.gcal import calendar

from operations.path_operations import logreutαg, logreuιδαt

from utils.info import izvart_info
from utils.session_manager import restart_stanvor, end_session
from utils.sys_utils import monitor_info, network_status


web_links = { # For euναrt and νermαt
    (UPPER_D, LOWER_D): ('Dyeναstαq', GCAL),
    (UPPER_Q, LOWER_Q): ('Qαmpαr', GMAPS),
}
main_paths = {
    '.invash': ('Iuναδ ιutorαg | ', INVASH),
    '.nostal': ('Nostαl ιutorαg ❯ ', os.getcwd()),
}
uprav_funcs = {
    '.izv':  lambda _: izvart_info(),
    '.net':  lambda _: network_status(),
    '.lan':  lambda stanvor: monitor_info(stanvor.lanter),
    '.dyαt': lambda stanvor: calendar(False, stanvor.gcal_creds, stanvor.prompt.stvl.αδeutαr),
}

stv_actions = {
    ESC:          lambda stanvor: reset(stanvor),
    SHF_PADMINUS: lambda stanvor: reset(stanvor),
    SHF_PADENTER: lambda _:       restart_stanvor(),
    CTL_PADSLASH: lambda stanvor: set_search(stanvor),
    ALT_PADSLASH: lambda stanvor: switch_search(stanvor.srch),
    PADPLUS:      lambda stanvor: logreutαg('Eudαμl', stanvor),
    PADMINUS:     lambda stanvor: logreutαg('Aqeμr', stanvor),
    SHF_PADPLUS:  lambda stanvor: logreuιδαt('Copy', stanvor),
    PADSTAR:      lambda stanvor: logreuιδαt('Lαιue', stanvor),
    PADSLASH:     lambda stanvor: logreuιδαt('Verse', stanvor),
    UP:           lambda stanvor: logreu_select('up', stanvor),
    DOWN:         lambda stanvor: logreu_select('down', stanvor),
    SHF_F12:      lambda stanvor: end_session(stanvor.lanter, 0),
    CTL_PADSTOP:  lambda stanvor: end_session(stanvor.lanter, 1),
}
