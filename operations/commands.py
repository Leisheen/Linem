"""Main commands for for Lιuemαg Stαuνor command line prompt."""
import os

import core.keys as nk
from core.def_paths import INVASH, GCAL, GMAPS
from core.filesystem import logreu_select
from core.search import set_search, switch_search
from core.stv import reset

from logren.gcal import calendar

from operations.path_operations import logreutαg, logreuιδαt

from utils.info import izvart_info
from utils.session import restart_stanvor, end_session
from utils.sys_utils import monitor_info, network_status


web_links = { # For euναrt and νermαt
    nk.LIT_D: ('Dyeναstαq', GCAL),
    nk.LIT_Q: ('Qαmpαr', GMAPS),
}

main_paths = {
    '.invash': ('Iuναδ ιutorαg | ', INVASH),
    '.nostal': ('Nostαl ιutorαg ❯ ', os.getcwd()),
}

uprav_funcs = {
    '.izv':  lambda _: izvart_info(),
    '.net':  lambda _: network_status(),
    '.lan':  lambda stanvor: monitor_info(stanvor.lanter),
    '.dyαt': lambda stanvor: calendar(
                                    False,
                                    stanvor.gcal_creds,
                                    stanvor.prompt.stvl.αδeutαr
                                    ),
}

stv_actions = {
    nk.ESC:          lambda stanvor: reset(stanvor),
    nk.SHF_PADMINUS: lambda stanvor: reset(stanvor),
    nk.SHF_ENTER:    lambda stanvor: restart_stanvor(stanvor), # PADENTER..
    nk.CTL_PADSLASH: lambda stanvor: set_search(stanvor),
    nk.ALT_PADSLASH: lambda stanvor: switch_search(stanvor.srch),
    nk.PADPLUS:      lambda stanvor: logreutαg('Eudαμl', stanvor),
    nk.PADMINUS:     lambda stanvor: logreutαg('Aqeμr', stanvor),
    nk.SHF_PADPLUS:  lambda stanvor: logreuιδαt('Copy', stanvor),
    nk.PADSTAR:      lambda stanvor: logreuιδαt('Lαιue', stanvor),
    nk.PADSLASH:     lambda stanvor: logreuιδαt('Verse', stanvor),
    nk.UP:           lambda stanvor: logreu_select('up', stanvor),
    nk.DOWN:         lambda stanvor: logreu_select('down', stanvor),
    nk.SHF_F12:      lambda stanvor: end_session(stanvor, 0),
    nk.CTL_DEL:      lambda stanvor: end_session(stanvor, 1),
}
