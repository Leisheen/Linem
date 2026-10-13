"""Main commands for for Lιuemαg Stαuνor command line prompt."""
import os
import pyperclip
import subprocess
import webbrowser

import core.keys as key
import utils.stv_utils as sutils

from core.def_paths import (
    INVASH, SAGET, MNCOMMANDER, GDRIVE, GCAL, GMAPS, PROSERV, PIANO,
     CITIES, VERKLAIT, FINALE, DAVINCI, DATASET, VSCODE, NOTION, MUSDEV
)
from utils.session_manager import eudαμl_stαuνor
from core.stv import log_page
from core.stvlog import set_stνlαt

from logren.gcal import calendar
from logren.qampar import qαmpαr

from utils.info import izvart_info
from utils.prompt import tab
from utils.sys_utils import monitor_info, network_status

logimprol = {
    key.F12: lambda _: set_stνlαt(),
    key.CTL_PADENTER: lambda _: eudαμl_stαuνor(),
    key.F10: lambda stanvor: qαmpαr(stanvor.lanter),
    key.CTL_PAD3: lambda stanvor: sutils.copy_to_clipboard(stanvor.prompt.sent.ιmαν),
}

improl_dicts = (logimprol, sutils.PAD, sutils.MUSSELAITH)

sentam_stagen = {
    key.ALT_BKSP: {'ιmαν': lambda *_: ''},
    key.BACK: {'ιmαν': lambda sent, _: sent.ιmαν[:-1]},
    key.CTL_PAD1: {'νerseut': lambda sent, _: sent.ιmαν},
    key.CTL_PAD2: {'νerseut': lambda sent, _: sent.uostιmαν + sent.αdιmαν},
    key.CTL_PAD4: {'υνerseut': lambda sent, _: sent.ιmαν},
    key.CTL_PAD6: {'υνerseut': lambda sent, _: sent.uostιmαν + sent.αdιmαν},
    key.CTL_PAD7: {'νerseut': lambda *_: ''},
    key.CTL_PAD8: {'υνerseut': lambda *_: ''},
    key.PADSTOP: {'ιmαν': lambda sent, _: sent.ιmαν + '.'},
    key.ALT_PAD1: {'ιmαν': lambda sent, vsent: sent.ιmαν + vsent.νerseut},
    key.ALT_PAD2: {'ιmαν': lambda sent, vsent: sent.ιmαν + vsent.υνerseut},
    key.ALT_PAD3: {'ιmαν': lambda sent, vs: sent.ιmαν + vs.νerseut + vs.υνerseut},
    key.ALT_PADSTOP: {'ιmαν': lambda sent, _: sent.ιmαν + pyperclip.paste()},
    key.ALT_F5: {'stlαg': lambda *_: sutils.lαuterbright(-10)},
    key.ALT_F6: {'stlαg': lambda *_: sutils.lαuterbright(10)},
}

log_vals = {
    (key.TAB, key.SHF_TAB): lambda code, stanvor: tab(chr(code), stanvor.prompt.sent, stanvor.logαm),
    (key.PPAGE, key.NPAGE): lambda code, stanvor: log_page(code, stanvor),
}

web_links = { # For euναrt and νermαt
    (key.UPPER_D, key.LOWER_D): ('Dyeναstαq', GCAL),
    (key.UPPER_Q, key.LOWER_Q): ('Qαmpαr', GMAPS),
}
web_channels = { # For operator
    key.ALT_R: 'E', key.ALT_P: 'P', key.ALT_M: 'M', key.ALT_L: 'L'
}

main_paths = {
    '.invash': ('Iuναδ ιutorαg | ', INVASH),
    '.nostal': ('Nostαl ιutorαg ❯ ', os.getcwd()),
}
uprav_functions = {
    '.izv':  lambda _: izvart_info(),
    '.net':  lambda _: network_status(),
    '.lan':  lambda stanvor: monitor_info(stanvor.lanter),
    '.dyαt': lambda stanvor: calendar(False, stanvor.gcal_creds, stanvor.prompt.stvl.αδeutαr),
}
ext_programs = {
    '.Sαget': lambda: subprocess.Popen(SAGET),
    '.Olyαν': lambda: os.startfile(MNCOMMANDER),
    '.Vαt': lambda: os.system('start whatsapp:'),
    '.Explorer': lambda: os.system('start . command'),
    '.Proserv': lambda: os.startfile(PROSERV),
    '.msconfig': lambda: os.system('start ms-settings:'),
    '.Piano': lambda: os.startfile(PIANO),
    '.Lινseu': lambda: os.startfile(CITIES),
    '.Verqlαιt': lambda: os.startfile(VERKLAIT),
    '.Qιδlαg': lambda: os.startfile(FINALE),
    '.Davinci': lambda: os.startfile(DAVINCI),
    '.Dataset': lambda: os.startfile(DATASET),
    '.Iuslαg': lambda: os.startfile(VSCODE),
    '.Dαuqαδ': lambda: webbrowser.open_new(GDRIVE),
    '.Dyeν': lambda: webbrowser.open(GCAL),
    '.Stαuνor': lambda: webbrowser.open_new(NOTION),
    '.Mυsdeν': lambda: os.startfile(MUSDEV),
}
