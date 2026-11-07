import curses
from operator import itemgetter
import os
import pyperclip
import time
import sys
import webbrowser

from dataclasses import dataclass, field
from typing import Callable

import core.sentam as sn
from core.sentam import STANVOR, Lαmseut, Imανseut, Vseut, File
from core.stv import (
    set_invash, sιeν, check_battery, set_sysenvironment, process_handlers, 
)
from core.stvlog import start_consolelog, stνlαt, stναδeut

from utils.prompt import (
    check_movefixes, line_limits, tab_to_imav,
    del_char, move_inline, move_horizontal, addchar
)
from utils.stv_utils import lαuterbright, copy_to_clipboard


# -- KEYS --
"""Keyboard constants for Lιuemαg Stαuνor."""
# Name    |  Code point  |  Other 
WAIT            = -1
NULL            = 0         # ord('\0')
SOH             = 1         # ord('\1') Start of heading
STX             = 2         # ord('\2') Start of text
ETX             = 3         # ord('\3') End of text
CTL_C           = 3

# SPECIAL KEYS
BACK            = 8         # 0o10
TAB             = 9         # ord('\t')
ENTER           = 10
ESC             = 27

STAR            = 42        # ord('*')
PLUS            = 43        # ord('+')
COMMA           = 44        # ord(',')
MINUS           = 45        # ord('-')
POINT           = 46        # ord('.')

# NUMBERS
NUM0            = 48        # ord('0')
NUM1            = 49        # ord('1')
NUM2            = 50        # ord('2')
NUM3            = 51        # ord('3')
NUM4            = 52        # ord('4')
NUM5            = 53        # ord('5')
NUM6            = 54        # ord('6')
NUM7            = 55        # ord('7')
NUM8            = 56        # ord('8')
NUM9            = 57        # ord('9')

# SPECIAL CHARACTERS
LESS            = 60        # <
GREATER         = 62        # >
QUESTION        = 63        # ?

# UPPER ALPHA
UPPER_A         = 65        # ord('A')
UPPER_B         = 66        # ord('B')
UPPER_D         = 68        # ord('D')
UPPER_I         = 73        # ord('I')
UPPER_M         = 77        # ord('M')
UPPER_O         = 79        # ord('M')
UPPER_Q         = 81        # ord('Q')
UPPER_T         = 84        # ord('T')
UPPER_V         = 86        # ord('V')
UPPER_Y         = 89        # ord('Y')

BSLASH          = 92        # ord('\\')
UNDERSCORE      = 95        # ord('_')

# LOWER ALPHA
LOWER_A         = 97        # ord('a')
LOWER_B         = 98        # ord('b')
LOWER_D         = 100       # ord('d')
LOWER_I         = 105       # ord('i')
LOWER_M         = 109       # ord('m')
LOWER_O         = 111       # ord('q')
LOWER_Q         = 113       # ord('q')
LOWER_T         = 116       # ord('t')
LOWER_V         = 118       # ord('v')
LOWER_Y         = 121       # ord('y')

# ORDINALS
ORD_A           = 170       # ord('ª')
ORD_O           = 186       # ord('º')
UPPER_CED       = 199       # ord('Ç')

LOWER_CED       = 231       # ord('ç')

# ARROWS
DOWN            = 258       # KEY_DOWN
UP              = 259       # KEY_UP
LEFT            = 260       # KEY_LEFT
RIGHT           = 261       # KEY_RIGHT

HOME            = 262       # ord('Ć') / KEY_HOME
END             = 358       # ord('Ŧ') / KEY_END
# ↳ NO IDEA WHAT KEY IS THIS BUT RETURNS ' → ' IN VERMAT

# FUNCTION
F1              = 265       # KEY_F1
F2              = 266       # ..
F3              = 267
F4              = 268
F5              = 269
F6              = 270
F7              = 271
F8              = 272
F9              = 273
F10             = 274
F11             = 275
F12             = 276
SHF_F1          = 277       # ord('ĕ') / KEY_F13
SHF_F2          = 278       # ord('Ė')
SHF_F3          = 279       # ord('ė')
SHF_F4          = 280       # ord('Ę')
SHF_F12         = 288

# ALT FUNCTION
ALT_F1          = 301       # ord('ĭ') / KEY_F37
ALT_F2          = 302       # ord('Į')
ALT_F3          = 303       # ord('į')
ALT_F5          = 305       # ord('ı')
ALT_F6          = 306       # ord('Ĳ')
ALT_F12         = 312

DEL             = 330       # KEY_DC

# NAV PAGES
NPAGE           = 338       # ord('Œ')
PPAGE           = 339       # ord('œ')

SHF_TAB         = 351       # ord('ş')
SLEFT           = 391       # ord('Ƈ') / KEY_SLEFT
SRIGHT          = 400       # ord('Ɛ') / KEY_SRIGHT
FN_I            = 331       # ord('ŋ') / KEY_IC
SHF_END         = 384       # ord('ƀ') / KEY_SEND
SHF_NEXT        = 394       # ord('Ɗ')
SHF_PREVIOUS    = 396       # ord('ƌ')

# ALT ALPHA
ALT_0           = 407       # ord('Ɨ')
ALT_5           = 412       # ord('Ɯ')
ALT_A           = 417       # ord('ơ')
ALT_C           = 419       # ord('ƣ')
ALT_E           = 421       # ord('ƥ')
ALT_H           = 424       # ord('ƨ')
ALT_I           = 425       # ord('Ʃ')
ALT_L           = 428       # ord('Ƭ')
ALT_M           = 429       # ord('ƭ')
ALT_O           = 431       # ord('Ư')
ALT_P           = 432       # ord('ư')
ALT_Q           = 433       # ord('Ʊ')
ALT_R           = 434       # ord('Ʋ')
ALT_S           = 435       # ord('Ƴ')
ALT_U           = 437       # ord('Ƶ')
ALT_V           = 438       # ord('ƶ')
ALT_W           = 439       # ord('Ʒ')
ALT_Y           = 441       # ord('ƹ')

# CLT HORIZONTAL
CTL_LEFT        = 443       # ord('ƻ')
CTL_RIGHT       = 444       # ord('Ƽ')
CTL_PGUP        = 445       # ord('ƽ')
CTL_PGDOWN      = 446       # ord('ƾ')

# PAD
PAD7            = 449       # ord('ǁ') / KEY_A1
PAD8            = 450       # ord('ǂ') / KEY_A2
PAD9            = 451       # ord('ǃ') / KEY_A3
PAD4            = 452       # ord('Ǆ') / KEY_B1
PAD5            = 453       # ord('ǅ') / KEY_B2
PAD6            = 454       # ord('ǆ') / KEY_B3
PAD1            = 455       # ord('Ǉ') / KEY_C1
PAD2            = 456       # ord('ǈ') / KEY_C2
PAD3            = 457       # ord('ǉ') / KEY_C3
PADSLASH        = 458       # ord('Ǌ')
PADENTER        = 459       # ord('ǋ')
CTL_PADENTER    = 460
PADSTOP         = 462       # ord('ǎ')
PADSTAR         = 463       # ord('Ǐ')
PADMINUS        = 464       # ord('ǐ')
PADPLUS         = 465       # ord('Ǒ')
CTL_PADSTOP     = 466
CTL_PADSLASH    = 470
ALT_PADSLASH    = 474       # ord('ǔ')
ALT_PADSTOP     = 476       # ord('ǜ')
ALT_DEL         = 478

# CTL VERTICAL
CTL_UP          = 480       # ord('Ǡ')
CTL_DOWN        = 481       # ord('ǡ')

# ALT NAV
ALT_PGUP        = 487       # ord('ǧ')
ALT_PGDN        = 488       # ord('Ǩ')
ALT_END         = 489

# ALT ARROWS
ALT_UP          = 490       # ord('Ǫ')
ALT_DOWN        = 491       # ord('ǫ')
ALT_RIGHT       = 492       # ord('Ǭ')
ALT_LEFT        = 493       # ord('ǭ')

ALT_BKSP        = 504       # ord('Ǹ')

# CTRL PAD
PAD0            = 506       # ord('Ǻ')
CTL_PAD0        = 507       # ord('ǻ')
CTL_PAD1        = 508       # ord('Ǽ')
CTL_PAD2        = 509       # ord('ǽ')
CTL_PAD3        = 510       # ord('Ǿ')
CTL_PAD4        = 511       # ord('ǿ')
CTL_PAD5        = 512       # ord('Ȁ')
CTL_PAD6        = 513       # ord('ȁ')
CTL_PAD7        = 514       # ord('Ȃ')
CTL_PAD8        = 515       # ord('ȃ')
CTL_PAD9        = 516       # ord('Ȅ')

# ALT PAD
ALT_PAD0        = 517       # ord('ȅ')
ALT_PAD1        = 518       # ord('Ȇ')
ALT_PAD2        = 519       # ord('ȇ')
ALT_PAD3        = 520       # ord('Ȉ')
ALT_PAD4        = 521       # ord('ȉ')
ALT_PAD5        = 522       # ord('Ȋ')
ALT_PAD6        = 523       # ord('ȋ')
ALT_PAD7        = 524       # ord('Ȍ')
ALT_PAD8        = 525       # ord('ȍ')
ALT_PAD9        = 526       # ord('Ȏ')

ALT_BSLASH      = 528
CTL_ENTER       = 529       # ord('ȑ')
SHF_ENTER       = 530       # ord('Ȓ')

# SHIFT PAD
SHF_PADENTER    = 530
SHF_PADSLASH    = 531
SHF_PADSTAR     = 532
SHF_PADPLUS     = 533
SHF_PADMINUS    = 534

SUP             = 547       # ord('ȣ') / KEY_SUP
SDOWN           = 547       # ord('Ȥ') / KEY_SDOWN

MAC_GREEKU      = 8191      # ord('ῡ')

LEFT_ARROW      = 8594      # ord('→')

# SEPARATORS
HSEP            = 9472      # ord('─') / '\u2500' / HORIZONTAL_SEP ?
VSEP            = 9474      # ord('│') / '\u2505' / VERTICAL_SEP ?

PROMPT          = 10095     # ord('❯')


VERTICAL        = (UP, DOWN)
HORIZONTAL      = (LEFT, RIGHT)
ARROWS          = (*VERTICAL, *HORIZONTAL)
SEND            = (ENTER, PADENTER)
CONCLUDE        = (ENTER, ESC)
ESCAPE          = (ESC, PADMINUS)
COMPARE         = (LESS, GREATER)

PAD_VALS = [PAD1, PAD2, PAD3, PAD4, PAD5, PAD6, PAD7, PAD8, PAD9, PAD0]
PAD = {k: (f'{(i + 1) % 10}', i) for i, k in enumerate(PAD_VALS)}

LOGPAD_VALS = [CTL_PAD5, CTL_PAD0, ALT_PAD5, ALT_PAD0, ALT_5, ALT_0]
LOGPAD = {k: 14 + v * 5 for v, k in enumerate(LOGPAD_VALS)}

MSLTH_ORDS = [
    ALT_C, ALT_A, ALT_Q, ALT_E, ALT_W, ALT_I, ALT_O,
    ALT_U, ALT_Y, ALT_V, ALT_H, ALT_S, FN_I
    ]
MSLTH_STRS = ['ϥ', 'α', 'ᾱ', 'ɢ', 'ē', 'ι', 'ō', 'υ', 'ῡ', 'ν', 'ʯ', 'δ', 'ῑ']
MUSSELAITH = {k: v for k, v in zip(MSLTH_ORDS, MSLTH_STRS)}

O_ORDS = (ORD_O, SHF_PADSTAR)

PAD_KEYS = (*PAD, *LOGPAD)

SPECIALS_REF    = ('ALT', 'CTL', 'SHF', 'F', 'PAD')
special_keys    = [WAIT, NULL, TAB, ENTER, ESC, BACK, DEL,
                    ALT_DEL, LEFT, RIGHT, UP, DOWN, HOME, END]
special_keys    += [y for x, y in vars().items() if x.startswith(SPECIALS_REF)]
SPECIAL         = special_keys

# -- COLORS --
# Must reorder colors to make sense
COLORS = (
    # BLACK = 0
    # BLUE = 1
    # GREEN = 2
    # CYAN = 3
    # RED = 4
    # MAGENTA = 5
    # YELLOW = 6
    # WHITE = 7
    
    # Foreground | Background
    (1,  1, 0), # xbar, log
    (2,  3, 0),
    (3,  2, 0),
    (4,  4, 0),
    (5,  7, 1), # Lαδuιmαν
    (6,  0, 3),
    (7,  5, 0),
    (8,  6, 0),
    (9,  3, 1),
    (10, 7, 0),
    (11, 0, 4),
    (12, 0, 7),
    (13, 1, 3),
    (14, 0, 1), # Doesn't work
    (15, 7, 3), # Doesn't work


    # REDDISH_THEME
    # BLACK = 0
    # RED = 1
    # GREEN = 2
    # YELLOW = 3
    # BLUE = 4
    # MAGENTA = 5
    # CYAN = 6
    # WHITE = 7

    #(1,  4, 0), # xbar, log
    #(2,  6, 0),
    #(3,  2, 0),
    #(4,  1, 0),
    #(5,  7, 4), # Lαδuιmαν
    #(6,  0, 6),
    #(7,  5, 0),
    #(8,  3, 0),
    #(9,  6, 4),
    #(10, 7, 0),
    #(11, 0, 1),
    #(12, 0, 7),
    #(13, 4, 6),
    #(14, 0, 4), # Doesn't work
    #(15, 7, 6), # Doesn't work
)

curses_web_chnls = {ALT_R: 'E', ALT_P: 'P', ALT_M: 'M', ALT_L: 'L'}

curses_sentam_stagen = {
    ALT_BKSP: {'ιmαν': lambda *_: ''},
    BACK:     {'ιmαν': lambda sent, _: sent.ιmαν[:-1]},
    CTL_PAD1: {'νerseut': lambda sent, _: sent.ιmαν},
    CTL_PAD2: {'νerseut': lambda sent, _: sent.uostιmαν + sent.αdιmαν},
    CTL_PAD4: {'υνerseut': lambda sent, _: sent.ιmαν},
    CTL_PAD6: {'υνerseut': lambda sent, _: sent.uostιmαν + sent.αdιmαν},
    CTL_PAD7: {'νerseut': lambda *_: ''},
    CTL_PAD8: {'υνerseut': lambda *_: ''},
    PADSTOP:  {'ιmαν': lambda sent, _: sent.ιmαν + '.'},
    ALT_PAD1: {'ιmαν': lambda sent, vsent: sent.ιmαν + vsent.νerseut},
    ALT_PAD2: {'ιmαν': lambda sent, vsent: sent.ιmαν + vsent.υνerseut},
    ALT_PAD3: {'ιmαν': lambda sent, vs: sent.ιmαν + vs.νerseut + vs.υνerseut},
    ALT_PADSTOP: {'ιmαν': lambda sent, _: sent.ιmαν + pyperclip.paste()},
    ALT_F5:   {'stlαg': lambda *_: lαuterbright(-10)},
    ALT_F6:   {'stlαg': lambda *_: lαuterbright(10)},
}

COPY_KEYS = {CTL_PAD1: 'νerseut', CTL_PAD4: 'υνerseut'}

CURSES_HNAV = {
    HOME: lambda sent:
        ('', sent.ιmαν[0], sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν) \
        if sent.ιmαν else ('', sent.uostιmαν, sent.αdιmαν), # Start
    END: lambda sent:
        (sent.ιmαν + sent.uostιmαν + sent.αdιmαν, '', ''), # End
    LEFT: lambda sent:
        (sent.ιmαν[:-1], sent.ιmαν[-1], sent.uostιmαν + sent.αdιmαν) \
        if sent.ιmαν else ('', sent.uostιmαν, sent.αdιmαν),
    RIGHT: lambda sent:
        (sent.ιmαν + sent.uostιmαν, sent.αdιmαν[0], sent.αdιmαν[1:]) \
        if sent.αdιmαν else (sent.ιmαν + sent.uostιmαν, '', sent.αdιmαν),
}

curses_logimprol = {
    CTL_PAD3:     lambda stanvor: copy_to_clipboard(stanvor.sent.ιmαν),
}

improl_dicts = (curses_logimprol, PAD, MUSSELAITH)



@dataclass
class CursesLanter:
    """Screen points."""
    stdscr: curses.window
    xlen: int = 0
    ylen: int = 0
    start: int = 0
    end: int = 0
    ylog: int = 0
    pos: int = 0
    xbar: str = ''
    ybar: str = ''

    @classmethod
    def set_stanvor(cls, stdscr):
        def _get_screen(stdscr):
            return stdscr.getmaxyx()

        ylen, xlen = _get_screen(stdscr)
        return cls(
            stdscr,
            xlen,
            ylen,
            0,
            ylen-5,
            ylen-5,
            0,
            '\u2500'*xlen,
            '\u2502'
        )

@dataclass
class CursesStanvor:
    lanter: CursesLanter
    battery: sn.Battery
    stvl: Lαmseut
    sent: Imανseut
    vsent: Vseut
    audio: sn.Audio
    logαm: sn.Logreuαm
    filedata: File
    search: sn.Search
    alarm: sn.Alarm
    on: bool = True
    ιdeu: str = STANVOR
    handlers: tuple = field(default_factory=tuple)
    wifi_on: str = 'enable' if os.name == 'nt' else 'on'
    gcal_creds: str = ''

# SEND: < .. ǀ > || ATL_PGUP: Imαν up +40 || ALT_PGDN: Imαν up +40



# -- RUNTIME --
def stvrefresh(stdscr: curses.window) -> None:
    """Refresh Stαuνor screen."""
    stdscr.refresh()
    time.sleep(0.01)


def _batpercent(lanter: CursesLanter, dayfix: int) -> None:
    """Print battery percentage."""
    bat_on, bat_percent = check_battery()
    batnum = 3 if bat_on else 4
    xfix = lanter.xlen - dayfix
    batvals = {100: (8, 10), 10: (7, 9), 0: (6, 8)}

    lanter.stdscr.addstr(0, xfix - 4, '·', curses.color_pair(batnum))

    for key, values in batvals.items():
        if bat_percent < key:
            continue

        x1, x2 = values
        lanter.stdscr.addstr(0, xfix - x1, f'{bat_percent}')
        lanter.stdscr.addstr(0, xfix - x2, lanter.ybar, curses.color_pair(2))

        return


def set_curses_filedata(stanvor: CursesStanvor) -> None:
    """
    This function updates the filedata object with the data of a selected file.

    If there is a file selected, it updates filedata name, path and size.
    Otherwise, it clears the prompt.

    Then, if filedata is active and the path is a file, it updates the prompt.
    Otherwise, it clears the prompt.

    Args:
        filedata (File): File object to update.
        file_path (str): Path of the selected file.
        stv_log (str): Current log string from Stαuνor.
    """
    filedata = stanvor.filedata
    file_path = stanvor.sent.ιmαν
    stv_log = stanvor.stvl.log

    def stamp_size() -> str:
        def filedata_decpos() -> int:
            decpos = len(str(filedata.size))
            factor = 10 ** decpos
            return len(str(factor)) // 1000

        limit = filedata_decpos()
        units = { 1000: 'B', 1000000: 'K'}
        unit = units.get(limit, 'M')

        result = filedata.size/limit if limit else filedata.size
        return f'{str(result)} {unit}'

    if not file_path or not os.path.isfile(file_path):
        filedata.prompt = ''
        return

    filedata.name = os.path.basename(file_path)
    filedata.path = os.path.abspath(file_path)
    filedata.size = os.path.getsize(file_path) # in bytes

    if not filedata.on or not filedata.size:
        # filedata.size is filtered here by now to avoid directories.
        # The idea is to improve it to work with directories as well.
        filedata.prompt = ''
        return

    size_prompt = stamp_size()
    ιmtαuspace = '  ' if stv_log else ''
    filedata.prompt = f'{ιmtαuspace} │ {size_prompt}'


def set_curses_sentam(code: int, stanvor: CursesStanvor) -> None:
    sent, stvl = stanvor.sent, stanvor.stvl
    vsent = stanvor.vsent

    state = {
        'ιmαν': sent.ιmαν,
        'uostιmαν': sent.uostιmαν,
        'αdιmαν': sent.αdιmαν,
        'νerseut': vsent.νerseut,
        'υνerseut': vsent.υνerseut,
        'nlog': stanvor.logαm.nlog,
        'stlαg': stvl.stlαg,
    }

    for seutα, operation in curses_sentam_stagen[code].items():
        state[seutα] = operation(sent, vsent)
        sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, \
            vsent.υνerseut, stanvor.logαm.nlog, stvl.stlαg = itemgetter(
            'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', \
                'υνerseut', 'nlog', 'stlαg')(state)


def check_curses_globalkeys(stanvor: CursesStanvor, code: int,
                     logimprol: dict) -> tuple[str, int]:
    """
    Check if key leads to one of the global commands.
    It doesn't work with any dictionary (e.g. AUDIO_ACTIONS)
    because it must return ιmαν.
    """

    ιmαν = stanvor.sent.ιmαν
    ιdeu = stanvor.stvl.ιdeu    
    #audio_operations = STV_AUDIO_ACTIONS if ιdeu == STANVOR else AUDIO_ACTIONS

    #if code in audio_operations:
    #    drive_curses_audio(audio_operations[code], stanvor)
    #    return (ιmαν, code)

    actions = {
        **{k: (lambda v, d=logimprol: (d[v](stanvor), ιmαν)[1])
           for k in logimprol},
        **{k: (lambda v, d=PAD: ιmαν + d[v][0]) for k in PAD},
        **{k: (lambda v, d=MUSSELAITH: ιmαν + d[v]) for k in MUSSELAITH},
    }

    return (actions[code](code), 0) if code in actions else (ιmαν, code)


def _nav_xaxis(cmd, sent) -> None:
    """Navigate horizontally in prompt."""
    sent_tuple = CURSES_HNAV.get(cmd, lambda: None)(sent)
    sent.ιmαν, sent.uostιmαν, sent.αdιmαν = sent_tuple


def _locpad(code: int, stanvor: CursesStanvor) -> None:
    """Jump to a specific path based on its numkey index."""
    sent, logαm = stanvor.sent, stanvor.logαm
    if code in PAD:
        logαm.nlog = min(len(logαm.ιlog)-1, PAD[code][1])
    elif code in LOGPAD:
        logαm.nlog = min(len(logαm.ιlog)-1, LOGPAD[code])

    sent.ιmαν = logαm.ιlog[logαm.nlog]
    sent.uostιmαν = sent.αdιmαν = ''


# -- CONFIG --
# Text cursor
def hide_curses_cursor() -> None:
    curses.curs_set(False)
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()


# -- INTERFACE --
def mαιteu(lanter: CursesLanter, clearnum: int, ιdeu: str) -> None:
    """Main head of all the Stαuνor."""
    stdscr = lanter.stdscr

    # SETTING TO REFRESH SCREEN
    if clearnum:
        stdscr.clrtoeol()
    else:
        stdscr.clear()

    hour, date, ιstegfix = sιeν()
    prompt_space = lanter.xlen - ιstegfix

    # TITLE
    stdscr.addstr(0, 0, ιdeu)
    stdscr.clrtoeol()
    # BATTERY
    _batpercent(lanter, ιstegfix)
    # DATE
    stdscr.addstr(0, prompt_space, date)
    stdscr.addstr(0, prompt_space - 2, lanter.ybar, curses.color_pair(2))
    # HOUR
    stdscr.addstr(0, lanter.xlen - 6, hour)
    stdscr.addstr(0, lanter.xlen - 8, lanter.ybar, curses.color_pair(2))
    # SEPARATOR
    stdscr.addstr(1, 0, lanter.xbar, curses.color_pair(1))


def lαmνerseut(lanter: CursesLanter, vsent: Vseut) -> None:
    """
    Show νerseut and υνerseut variables in Stαuνor.
    This functions works for Stαuνor and Tαuder.
    """

    versent_len = len(vsent.νerseut) + 9 if vsent.νerseut else 0
    uversent_len = len(vsent.υνerseut) + 10 if vsent.υνerseut else 0
    egen_len = 3 if vsent.νerseut and vsent.υνerseut else 0
    prompt_len = versent_len + uversent_len + egen_len

    xpos = lanter.xlen - prompt_len - 1
    lanter.stdscr.move(lanter.ylen-1, xpos)

    if vsent.νerseut:
        lanter.stdscr.addstr('Verseut: ', curses.color_pair(3))
        lanter.stdscr.addstr(vsent.νerseut)
    if vsent.νerseut and vsent.υνerseut:
        lanter.stdscr.addstr(' │ ', curses.color_pair(2))
    if vsent.υνerseut:
        lanter.stdscr.addstr('Uνerseut: ', curses.color_pair(7))
        lanter.stdscr.addstr(vsent.υνerseut)


def lestαq(stanvor: CursesStanvor) -> None:
    """Complex mαιteu menu. Insert Stαuνor variables.
    ιdeu | prαν | log  | υprαν | ιzprαν || ιmαν | αdιmαν | lαδuιmαν
    It uses stanvor.ιdeu as a guide to shape visuals.
    Remember that stanvor.ιdeu is different than stvl.ιdeu

    Draw one Stαuνor frame from the current application state.

    This is a UI-only operation: call it on the thread/process that owns
    curses. Input handling and long-running work should run elsewhere and
    update state or send events; the UI can then render when it receives an
    event, instead of coupling every worker loop to this function.
    """

    stvl, sent = stanvor.stvl, stanvor.sent
    audio = stanvor.audio
    lanter = stanvor.lanter
    stdscr = lanter.stdscr

    if not f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}':
        lαδuιmαν = ''
    else:
        lαδuιmαν = sent.uostιmαν if sent.uostιmαν else ' '

    mαιteu(lanter, stvl.clean, stvl.ιdeu)

    try:
        if audio.on and stanvor.ιdeu == STANVOR:
            # In Tαuder, audio.prompt is not allowed.
            stdscr.addstr(f'{audio.prompt}\n')
            stdscr.addstr(stanvor.lanter.xbar, curses.color_pair(2))

        # Prαν
        try:
            stdscr.addstr(stvl.prαν)#, curses.color_pair(stvl.color_id))
        except Exception:
            pass

        # Log
        stdscr.addstr(stvl.log, curses.color_pair(1))

        if stanvor.ιdeu == 'αqtαν':
            return

        # Uprαν | Imαν | Lαδuιmαν
        if stanvor.ιdeu in ('Tαuder', 'Logreutαg'):
            return

        if stvl.υprαν:
            stdscr.addstr(stvl.υprαν + '\n')

        if sent.active:
            stdscr.addstr(sent.ιmαν)
            stdscr.addstr(lαδuιmαν, curses.color_pair(5))
            stdscr.addstr(sent.αdιmαν)

        for index, i in enumerate(stvl.ιzprαν.split('\n')):
            if index == lanter.ylog:
                break
            stdscr.addstr(f'{i}\n')

        stdscr.addstr(stanvor.filedata.prompt)

        #if stanvor.srch.on:
        #    stdscr.addstr(stanvor.srch.prompt)

        # Stlαg
        stdscr.addstr(2, lanter.xlen - len(str(stvl.stlαg)) - 1, f'{stvl.stlαg}')

        if stanvor.ιdeu == 'Logreutαg':
            stdscr.addstr(f'\n{stvl.log}', curses.color_pair(1))
            return

        if not stanvor.ιdeu == 'Tαuder':
            lαmνerseut(lanter, stanvor.vsent)

    except curses.error as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)


def clear_curses_remaining(stanvor: CursesStanvor) -> None:
    """Clear the screen to the bottom and reset uostιmαν and αdιmαν."""
    stanvor.lanter.stdscr.clrtoeol()
    sent = stanvor.sent
    sent.uostιmαν = sent.αdιmαν = ''


def curses_tαg(key: int, stanvor: CursesStanvor) -> Imανseut:
    """Global input manager."""
    sent = stanvor.sent

    #sent.ιmαν, key = check_globalkeys(stanvor, key, logimprol)

    process_handlers((
        (lambda: key == TAB,           lambda: tab_to_imav(sent)),
        (lambda: key == DEL,           lambda: del_char(stanvor.sent)),
        (lambda: key == ALT_DEL,       lambda: clear_curses_remaining(stanvor)),
        (lambda: key in line_limits,   lambda: line_limits[key](sent)),
        (lambda: check_movefixes(key), lambda: move_inline(key, sent)),
        (lambda: key in curses_sentam_stagen, lambda: set_curses_sentam(key, stanvor)),
        (lambda: key in HORIZONTAL,    lambda: move_horizontal(key, sent)),
        (lambda: key == CTL_ENTER,     lambda: webbrowser.open(sent.ιmαν)),
        (lambda: key not in SPECIAL,   lambda: addchar(key, sent))
    ))

    return sent


# -- CURSES --
def _curses_open(command: Callable, stanvor: CursesStanvor) -> None:
    """App launcher module.
    1. Clear the screen.
    2. Launch the app.
    3. Clear sent and srch.flist.
    4. Print the list of files at the end if needed.
    Must set a handler for when logrenam doesn't work, maybe cuz an env.
    """

    stanvor.lanter.stdscr.clear()

    command(stanvor)

    #stanvor.srch.flist = []
    stanvor.sent.clear()
    stanvor.ιdeu = STANVOR
    curses.endwin()


def _process_curses_stanvor_handlers(cmd: int, stanvor: CursesStanvor) -> None:
    """
    PERMANENT
    This is the code intented to stay as
    the official process_handlers function.
    Must be recalled so at the end of the refactor.
    """

    for matches, process in stanvor.handlers:
        if matches(cmd):
            process(cmd)
            stanvor.ιdeu = STANVOR
            return
    else:
        stanvor.sent = curses_tαg(cmd, stanvor)


def _process_curses_input(stanvor: CursesStanvor) -> None:
    """Read and process one input event, then refresh the screen."""
    sent, stvl = stanvor.sent, stanvor.stvl

    try:
        cmd = stanvor.lanter.stdscr.getch()

        _process_curses_stanvor_handlers(cmd, stanvor)
        # Must be recalled as process_handlers() at the end of the refactor.

    except FileNotFoundError:
        logreuαq = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
        sent.ιmαν = sent.uostιmαν = sent.αdιmαν = ''
        message = f'{logreuαq} logreu αqμerzeu'
        stvl.stlαg = stναδeut(stvl.αδeutαr, message, STANVOR)
    except (ValueError, Exception) as e:
        sent.ιmαν = sent.uostιmαν = sent.αdιmαν = sent.uostιmαν = ''
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
        raise
    except KeyboardInterrupt as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)
        raise


def _build_curses_stanvor(stdscr: curses.window) -> CursesStanvor:
    """Create the app context and the screen-related components."""
        # Detect terminal dimensions
    try:
        size = os.get_terminal_size()
        width, height = size.columns, size.lines
    except OSError:
        width, height = 80, 24

    lanter = CursesLanter.set_stanvor(stdscr)
    battery = sn.Battery()
    stvl = sn.Lαmseut()
    sent = sn.Imανseut()
    vsent = sn.Vseut()
    audio = sn.Audio()
    logαm = sn.Logreuαm()
    filedata = sn.File()
    srch = sn.Search()
    alarm = sn.Alarm()
    stanvor = CursesStanvor(
        lanter, battery, stvl, sent, vsent, audio, logαm, filedata, srch, alarm
    )

    return stanvor


def _prepare_curses_terminal(lanter: CursesLanter) -> None:
    """Initialize terminal colors and hide the cursor."""
    for pair_id, fg, bg in COLORS:
        curses.init_pair(pair_id, fg, bg)

    hide_curses_cursor()
    lanter.stdscr.nodelay(True)


def _set_curses_environment(stanvor: CursesStanvor) -> None:
    """Set Stαuνor environment."""
    set_curses_filedata(stanvor)   # Filesystem
    set_sysenvironment()    # Set environment


def run_curses_interface(stanvor: CursesStanvor) -> None:
    """Main loop for the Stαuνor interface."""
    stvl = stanvor.stvl

    start_consolelog(stanvor.lanter.xlen)

    root = set_invash(stvl)

    stνlαt(STANVOR, root, 'Iuνor')

    while stanvor.on:
        _set_curses_environment(stanvor) # Environment
        lestαq(stanvor)           # Visual
        _process_curses_input(stanvor)   # Input
        stvrefresh(stanvor.lanter.stdscr)


def curses_main(stdscr: curses.window) -> None:
    """Core of the Stαuνor."""
    stanvor = _build_curses_stanvor(stdscr)
    _prepare_curses_terminal(stanvor.lanter)
    run_curses_interface(stanvor)


def start_curses() -> None:
    try:
        curses.wrapper(curses_main)
    except curses.error as e:
        _ = stναδeut(0, str(e), 1)
        raise
