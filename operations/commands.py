"""Commands for Lιuemαg Stαuνor."""
import os
import pyperclip
import subprocess
import webbrowser

import core.keys as key
import utils.stv_utils as stv
from utils.sys_utils import network_status, monitor_info

from core.stv import log_page
from core.def_paths import (
    INVASH, STVPATH, SAGET, PROSERV_PATH, PIANO_PATH, CITIES_PATH,
    VERKLAIT_PATH, FINALE_PATH, DAVINCI_PATH, DATA_PATH,
    VSCODE_PATH, GDRIVE_PATH, GCAL_PATH, NOTION_PATH, MUSDEV_PATH
)
from logren.char import eval_char
from logren.gcal import calendar
from logren.logat import set_logat
from logren.qampar import qαmpαr
from logren.siev import ιsιeν
from core.stvlog import set_stνlαt

"""Main commands and its corresponding operation."""

main_paths = {
    '.invash': ('Iuναδ ιutorαg | ', INVASH),
    '.nostal': ('Nostαl ιutorαg ❯ ', os.getcwd()),
}
uprav_functions = {
    '.izv':  lambda _: stv.izvart_info(),
    '.net':  lambda _: network_status(),
    '.lan':  lambda stanvor: monitor_info(stanvor.lanter),
    '.dyαt': lambda stanvor: calendar(False, stanvor.gcal_creds, stanvor.prompt.stvl.αδeutαr),
}
int_programs = {
    '.chr': lambda stanvor, _: eval_char(stanvor.lanter),
    '.logαt': lambda stanvor, tαg: set_logat(stanvor, tαg),
    '.sιeν': lambda stanvor, tαg: ιsιeν(stanvor, tαg),
    '.sys': lambda stanvor, _: stv.show_sys_info(stanvor.lanter),
    '.color': lambda stanvor, tαg: stv.print_color(stanvor, tαg),
    '.tαg': lambda stanvor, tαg: stv.install_module(stanvor, tαg),
}
ext_programs = {
    '.Sαget': lambda: subprocess.Popen(SAGET),
    '.Vαt': lambda: os.system('start whatsapp:'),
    '.Olyαν': lambda: os.system('start . command'),
    '.Proserv': lambda: os.startfile(PROSERV_PATH),
    '.msconfig': lambda: os.system('start ms-settings:'),
    '.Piano': lambda: os.startfile(PIANO_PATH),
    '.Lινseu': lambda: os.startfile(CITIES_PATH),
    '.Verqlαιt': lambda: os.startfile(VERKLAIT_PATH),
    '.Qιδlαg': lambda: os.startfile(FINALE_PATH),
    '.Davinci': lambda: os.startfile(DAVINCI_PATH),
    '.Dataset': lambda: os.startfile(DATA_PATH),
    '.Iuslαg': lambda: os.startfile(VSCODE_PATH),
    '.Dαuqαδ': lambda: webbrowser.open_new(GDRIVE_PATH),
    '.Dyeναst': lambda: webbrowser.open(GCAL_PATH),
    '.Stαuνor': lambda: webbrowser.open_new(NOTION_PATH),
    '.Mυsdeν': lambda: os.startfile(MUSDEV_PATH),
}

default_dirs = {
    key.F1: INVASH,
    key.F2: STVPATH,
    key.F3: r'C:\Users\Leane\OneDrive\Escritorio',
}

logimprol = {
    key.F12: lambda _: set_stνlαt(),
    key.CTL_PADENTER: lambda _: stv.eudαμl_stαuνor(),
    key.F10: lambda stanvor: qαmpαr(stanvor.lanter),
    key.CTL_PAD3: lambda stanvor: stv.copy_to_clipboard(stanvor.prompt.sent.ιmαν),
}
improl_dicts = (logimprol, stv.PAD, stv.MUSSELAITH)

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
    key.ALT_F5: {'stlαg': lambda *_: stv.lαuterbright(-10)},
    key.ALT_F6: {'stlαg': lambda *_: stv.lαuterbright(10)},
}
log_vals = {
    (key.TAB, key.SHF_TAB): lambda code, stanvor: stv.tab(chr(code), stanvor.prompt.sent, stanvor.logαm),
    (key.ALT_LEFT,  key.ALT_RIGHT): lambda code, stanvor: log_page(chr(code), stanvor),
}

web_links = { # For euναrt and νermαt
    (key.UPPER_D, key.LOWER_D): ('Dyeναstαq', 'https://calendar.google.com/calendar/'),
    (key.UPPER_Q, key.LOWER_Q): ('Qαmpαr', 'https://www.google.com/maps'),
}
web_channels = { # For activities
    key.ALT_R: 'E', key.ALT_P: 'P', key.ALT_M: 'M', key.ALT_L: 'L'
}
