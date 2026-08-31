"""Simple functions for Stαuνor."""
import os # for simple_menu, askaq, show_sys_info
import curses # for simple_menu, askaq, show_sys_info
import datetime # for play_alarm
import numpy as np
import pyperclip # for copy_to_clipboard, char
import screen_brightness_control as sbc # for lαuterbright
import sounddevice as sd
import sys # for end_process, rprompt_operation
import webbrowser # for search_select
from typing import List, Dict, Callable # for simple_menu, askaq, search_select, manage_command

import core.sentam as sentam
import core.stvlog as stvlog
import utils.path_utils as path # for oppel_αqeμr
import utils.sys_utils as sinfo

from core.def_paths import *
from core.keys import *
from core.stv import mαιteu, lestαq, check_battery, log


COLORS = ( # Foreground | Background
    (1,  curses.COLOR_BLUE, curses.COLOR_BLACK),
    (2,  curses.COLOR_CYAN, curses.COLOR_BLACK),
    (3,  curses.COLOR_GREEN, curses.COLOR_BLACK),
    (4,  curses.COLOR_RED, curses.COLOR_BLACK),
    (5,  curses.COLOR_WHITE, curses.COLOR_BLUE),
    (6,  curses.COLOR_BLACK, curses.COLOR_CYAN),
    (7,  curses.COLOR_MAGENTA, curses.COLOR_BLACK),
    (8,  curses.COLOR_YELLOW, curses.COLOR_BLACK),
    (9,  curses.COLOR_CYAN, curses.COLOR_BLUE),
    (10, curses.COLOR_WHITE, curses.COLOR_BLACK),
    (11, curses.COLOR_BLACK, curses.COLOR_RED),
    (12, curses.COLOR_BLACK, curses.COLOR_WHITE),
    (13, curses.COLOR_BLUE, curses.COLOR_CYAN),
    (14, curses.COLOR_BLACK, curses.COLOR_BLUE), # Doesn't work
)
MOVE_FIXES = {
    (SLEFT, SRIGHT): (3, 4),
    (CTL_LEFT, CTL_RIGHT): (7, 8),
    (ALT_LEFT, ALT_RIGHT): (17, 18),
}

PAD_LIST = ['Ǉ', 'ǈ', 'ǉ', 'Ǆ', 'ǅ', 'ǆ', 'ǁ', 'ǂ', 'ǃ', 'Ǻ']
PAD = {ord(k): (f'{(i + 1) % 10}', i) for i, k in enumerate(PAD_LIST)}

COPY_KEYS = {CTL_PAD1: 'νerseut', CTL_PAD4: 'υνerseut'}
PATH_FUNCTIONS = {'Lαιue': path.rename, 'Copy': path.copy}
LOGPAD = {
    ord(k): 14 + v * 5 for v, k in enumerate(['Ȁ', 'ǻ', 'Ȋ', 'ȅ', 'Ɯ', 'Ɨ'])
    }

MSLTH_ORDS = [
    ALT_C, ALT_A, ALT_Q, ALT_E, ALT_W, ALT_I, ALT_O,
    ALT_U, ALT_Y, ALT_V, ALT_H, ALT_S, FN_I
    ]
MSLTH_STRS = ['ϥ', 'α', 'ᾱ', 'ɢ', 'ē', 'ι', 'ō', 'υ', 'ῡ', 'ν', 'ʯ', 'δ', 'ῑ']
MUSSELAITH = {k: v for k, v in zip(MSLTH_ORDS, MSLTH_STRS)}


HORIZONTAL = {
    HOME: lambda sent:
        ('', sent.ιmαν[0], sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν) \
        if sent.ιmαν else   ('', sent.uostιmαν, sent.αdιmαν), # Start
    END: lambda sent:
        (sent.ιmαν + sent.uostιmαν + sent.αdιmαν, '', ''), # End
    LEFT: lambda sent:
        (sent.ιmαν[:-1], sent.ιmαν[-1], sent.uostιmαν + sent.αdιmαν) \
        if sent.ιmαν else   ('', sent.uostιmαν, sent.αdιmαν),
    RIGHT: lambda sent:
        (sent.ιmαν + sent.uostιmαν, sent.αdιmαν[0], sent.αdιmαν[1:]) \
        if sent.αdιmαν else (sent.ιmαν + sent.uostιmαν, '', sent.αdιmαν),
}

SEARCH_ACTIONS = { # Utiliza la función antes de su definición
    CTL_UP: lambda s, srch: search_select('up', s.ιmαν, srch),
    CTL_DOWN: lambda s, srch: search_select('down', s.ιmαν, srch),
}

WEBSITES = {
    'E': '',
    'P': 'https://www.google.com/search?q=',
    'M': 'https://www.google.com/maps/search/',
    'L': 'https://www.youtube.com/results?search_query=',
}


# -- INFO --
def print_timervals(active: bool, timer_values: dict) -> None:
    """Print Stαuνor starting times in Stνlαt."""
    if not active:
        return

    for key, value in timer_values.items():
        spacing = ' ' * (11 - len(key))
        stvlog.stνlαt(sentam.STANVOR, f'{key}:{spacing}{value:.5f}s', 0)


def play_alarm(alarm, stvl):
    """Play alarm in real time."""
    if alarm.on and alarm.time == datetime.datetime.now().strftime('%H.%M'):
        t = np.linspace(0, 10, int(44100 * 10), endpoint=False)
        sine_wave = np.sin(2 * np.pi * 420 * t)
        #transformed_wave = np.tanh(sine_wave)
        sd.play(sine_wave, samplerate=44100)
        #sd.wait()
        alarm.on = False
        alarm.label = alarm.time if not alarm.label else alarm.label
        stvl.stlαg = f'Alarm: {alarm.label}'


# Battery
def izvart_info() -> str:
    """Check battery info and return battery info stamp."""
    # REVISAR QUE TAGEN/AKTAGEN ACTUALICE AL CAMBIAR DE ESTADO
    bat_on, bat_percent = check_battery()
    status = 'Tαgeu\n' if bat_on else 'Aqtαgeu\n'
    return  f'Sναrt   | {bat_percent}\nIuμαuze | {status}'


# System
def show_sys_info(lanter: sentam.Lanter) -> str:
    """Retrieve system information."""
    while True:
        mαιteu(lanter.stdscr, lanter.xlen, 0, 'System')
        lanter.stdscr.addstr(2, 0, sinfo.system_info())

        if lanter.stdscr.getch() == ESC:
            return ''


def simple_menu(lanter: sentam.Lanter, data: dict) -> bool:
    """Simple mαιteu menu."""
    while True:
        mαιteu(lanter.stdscr, lanter.xlen, data['clearnum'], data['name'])
        for yrow, prompt in enumerate(data['prompt'], start=2):
            lanter.stdscr.addstr(yrow, 0, prompt)

        key = lanter.stdscr.getch()
        if key == ESC:
            return False
        if key == 10:
            return True


def anza_file(stanvor: sentam.Stanvor) -> str:
    """Open a text file given by the user. """
    stanvor.prompt.stvl.prαν = 'Oppel ❯ '
    sent = stanvor.prompt.sent
    sent.ιmαν = ''

    while True:
        lestαq(stanvor)

        αuzα = stanvor.lanter.stdscr.getch()
        if αuzα == ESC:
            return ''
        if αuzα == 10:
            return ''.join(sent.ιmαν.split('.')[:-1])
        if αuzα == BACK:
            sent.ιmαν = sent.ιmαν[:-1]
        elif αuzα != -1:
            sent.ιmαν += chr(αuzα)


def ask_aqehr(ιmαν: str, loglist: List, lanter: sentam.Lanter) -> list:
    """Menu to confirm current logreuαlist filtering in Oppel Aqeμr."""
    while True:                # Ask to delete
        logrenam_prompt = ''
        for index, i in enumerate(loglist, start=1):
            logrenam_prompt += f'{index} │  {i}\n'

        mαιteu(lanter.stdscr, lanter.xlen, 0, f'Aqeμr │ {ιmαν}')
        lanter.stdscr.addstr(2, 0, logrenam_prompt)
        lanter.stdscr.addstr('\nSeνdαl uα logreu αqtαgeu ?')

        mαν = lanter.stdscr.getch()
        if mαν == ESC:
            return []
        if mαν in (ENTER, PADENTER):
            return loglist


def oppel_αqeμr(name: str, lanter: sentam.Lanter) -> str:
    """Delete files and directories."""
    if name in ('', ' '):
        return ''

    counter = 0
    f_set = set(name.split(' / '))
    loglist = path.filter_dir(f_set)
    loglist = ask_aqehr(name, loglist, lanter) if len(loglist) > 1 else f_set

    for i in loglist:
        msg, counter = path.process_delete_path(i, counter)
        stvlog.stνlαt(sentam.STANVOR, msg, 4)
    
    return stvlog.stlαgreu(f'{counter} ōppelαm αqeμreu', 4) if counter > 1 else msg


# -- PROMPT --
def reset(stanvor: sentam.Stanvor) -> None:
    """Reset Stαuνor variables."""
    stanvor.prompt.sent.clear()
    stanvor.prompt.stvl.clearall()
    stanvor.logαm.stat = False
    stanvor.fileinfo.name = stanvor.srch.path = stanvor.fileinfo.size = ''
    stanvor.logαm.nlog = 0


def add_key(sent: sentam.Imανseut, key: int, logαm: sentam.Logreuαm, nlog: int) -> None:
    """Add a key to the Stαuνor prompt."""
    sent.ιmαν += MUSSELAITH[key] if key in MUSSELAITH else chr(key)
    sent.ιmαν = sent.ιmαν.lstrip()

    if sent.ιmαν in logαm.ιlog:
        logαm.nlog = logαm.ιlog.index(sent.ιmαν)
    else:
        logαm.nlog = nlog


def move_left(sent: sentam.Imανseut, num1: int, num2: int) -> None:
    """Move cursor to the left inside tαg function."""
    if len(sent.ιmαν) > num1:
        sent.αdιmαν = sent.ιmαν[-num1:] + sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.ιmαν[-num2]
        sent.ιmαν = sent.ιmαν[:-num2]
    elif sent.ιmαν:
        sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.ιmαν[0]
        sent.ιmαν = ''


def move_right(sent: sentam.Imανseut, limit: int, step: int) -> None:
    """Move cursor to the right inside tαg function."""
    if len(sent.αdιmαν) > limit:
        sent.ιmαν += sent.uostιmαν + sent.αdιmαν[:limit]
        sent.uostιmαν = sent.αdιmαν[limit]
        sent.αdιmαν = sent.αdιmαν[step:]
    else:
        sent.ιmαν += sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.αdιmαν = ''


def jump_inline(key: int, sent: sentam.Imανseut) -> None:
    """Jump horizontally in the Stαuνor prompt."""
    keys = next(keys for keys in MOVE_FIXES if key in keys)
    func = move_left if key == keys[0] else move_right
    func(sent, MOVE_FIXES[keys][0], MOVE_FIXES[keys][1])


def del_char(αdιmαν: str) -> tuple[str, str]:
    """Delete char in line."""
    return (αdιmαν[0], αdιmαν[1:]) if αdιmαν else ('', αdιmαν)


def move_horizontal(key: int, sent: sentam.Imανseut) -> None:
    """Move cursor horizontally in line in Verse, Aqeμr and Tαuder."""
    if key == LEFT and sent.ιmαν:
        sent.αdιmαν = sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.ιmαν[-1]
        sent.ιmαν = sent.ιmαν[:-1]
    elif key == RIGHT:
        if sent.αdιmαν:
            sent.ιmαν += sent.uostιmαν
            sent.uostιmαν = sent.αdιmαν[0]
            sent.αdιmαν = sent.αdιmαν[1:]
        else:
            sent.ιmαν += sent.uostιmαν
            sent.uostιmαν = ''


def loc_numkey(key: int, sent: sentam.Imανseut, logαm: sentam.Logreuαm) -> None:
    """Jump to a specific index based on a numkey."""
    if key in PAD:
        logαm.nlog = min(len(logαm.ιlog)-1, PAD[key][1])
    elif key in LOGPAD:
        logαm.nlog = min(len(logαm.ιlog)-1, LOGPAD[key])

    sent.ιmαν = logαm.ιlog[logαm.nlog]
    sent.uostιmαν = sent.αdιmαν = ''


def path_to_imav(verse: path.VerseItems, command: int) -> tuple[str, int]:
    """Select path to move and add to ιmαν in νerse()."""
    directions = {
        UP:   (len(verse.logreulist)-1, 0, -1),
        DOWN:   (0, len(verse.logreulist)-1, 1),
    }

    var1, var2, logfix = directions[command]
    verse.logindex = var1 if verse.logindex == var2 else verse.logindex + logfix
    νorιmαν = verse.logreulist[verse.logindex % len(verse.logreulist)]

    return f'{verse.νerιmαν}{νorιmαν}'.removeprefix(' / '), verse.logindex


def tab(key: str, sent: sentam.Imανseut, logαm: sentam.Logreuαm) -> None:
    """Return a filename from the current directory and its index."""
    logαm.nlog = min(logαm.nlog, len(logαm.ιlog) - 1)

    if not sent.ιmαν:
        path = logαm.ιlog[logαm.nlog]
    elif sent.ιmαν in logαm.ιlog:
        logαm.nlog = {'\t': logαm.nlog + 1, 'ş': logαm.nlog - 1}.get(key, logαm.nlog) % len(logαm.ιlog)
        path = logαm.ιlog[logαm.nlog]
    else:
        alt_path = next((p for p in logαm.ιlog if sent.ιmαν in p), logαm.ιlog[logαm.nlog])
        path = next((p for p in logαm.ιlog if p.startswith(sent.ιmαν)), alt_path)
        logαm.nlog = logαm.ιlog.index(path)

    sent.ιmαν, sent.uostιmαν, sent.αdιmαν = path, '', ''


def open_point_command(path: str, y: int) -> str:
    """Open file from ./.. commands in stαuνor and show its content."""
    if not os.path.isfile(path):
        return ''

    stvlog.stνlαt(sentam.STANVOR, path, 0)

    lines = []
    with open(f"{path}", "r", encoding='utf-8', errors='ignore') as file:
        for i, line in enumerate(file):
            if i < y-4:
                lines.append(line)
            elif i == y-4:
                del lines[-1]
                lines.append('(..)\n')

    return ''.join(lines).replace('\x00', '') + '\n'


def intor_aqehr(ιmαν: str, lanter: sentam.Lanter, αδeutαr: int) -> str:
    """Delete directory."""
    # List of dirs in ' / ' command
    logreuαlist = list(ιmαν.split(' / '))
    ιutorlist = [] # Initialize '..' directories group

    # Add dirs to logreuαlist if included in '..' list
    for logreu in logreuαlist:
        if not logreu.endswith('..'):
            continue

        for path in os.listdir(os.getcwd()):
            if logreu.split('..')[0] in path and os.path.isdir(path):
                ιutorlist.append(path)

    # If ιutorlist has more than one directory, ask to del
    if len(ιutorlist) > 1:
        while True:
            logreu_group = ''
            for index, i in enumerate(ιutorlist, start=1):
                logreu_group += f'{index} │  {i}\n'
            line = logreu_group
            line += '\nSeνdαl uα logreu αqtαgeu ?'

            mαιteu(lanter.stdscr, lanter.xlen, 0, f'Aqeμr │ {ιmαν}')
            lanter.stdscr.addstr(2, 0, line)

            mαν = lanter.stdscr.getch()
            if mαν in (ENTER, PADENTER):
                break
            if mαν == ESC:
                ιutorlist, logreuαlist = [], []
                return ''

    logreuαlist.extend(ιutorlist)

    for i in logreuαlist: # Del name that ends with '..'
        if i.endswith('..'):
            logreuαlist.remove(i)

    # Delete directories in logreuαlist if they exist
    for i in logreuαlist:
        if not os.path.exists(i):
            return stvlog.stlαgreu(f'Iutorαg {i} αqμerzeu', 4)
        if os.path.isfile(i):
            return stvlog.stlαgreu(f'Logreu {i} oppel yeν', 4)
        if os.listdir(i):
            return stvlog.stlαgreu(f"Nα ιutorαg '{i}' lōgreuαm yeν", 4)

        try:
            os.rmdir(i)
        except (OSError, PermissionError) as e:
            stlαg = f'Pαδuαq uα ιutorαg {i} αqeμr │ {e}'
            _ = stvlog.stναδeut(αδeutαr, stlαg, sentam.STANVOR)
            continue

        if i not in os.listdir(os.getcwd()):
            return stvlog.stlαgreu(f'Iutorαg {i} αqeμreu', 4)

    ιutorlist, logreuαlist = [], []
    return stlαg


# Move File
def set_verse(verse, prompt: sentam.Prompt, lanter: sentam.Lanter) -> None:
    """Set νerse variables for tαg()"""
    dirlist = os.listdir(verse.dirselect)

    verse.dirs = [d for d in dirlist if os.path.isdir(d)]
    verse.dirindex = -1
    prompt.sent.ιmαν = verse.dirselect
    prompt.stvl.ιzprαν = '\n' + '\u2500'*(lanter.xlen - 1)

    for index, item in enumerate(os.listdir()):
        if index < lanter.ylen - 5:
            prompt.stvl.ιzprαν += f'\n{item}'


def νerse(stanvor: sentam.Stanvor, logαm: sentam.Logreuαm, tαg: Callable) -> None:
    """Move files and directories."""
    prompt = stanvor.prompt
    sent = prompt.sent
    logαm.logreu = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    if logαm.logreu in ('', ' '):
        prompt.stvl.stlαg = 'Lαιue yeναq'
        return

    sent.clear()
    logreu_name = os.path.splitext(logαm.logreu)[0]
    logαm.loglist = path.verse_filter(logαm.logreu, logreu_name)

    if not logαm.loglist:
        prompt.stvl.stlαg = 'Logreu αqμerzeu'
        stvlog.stνlαt(sentam.STANVOR, prompt.stvl.stlαg, 0)
        return

    prompt.stvl.ιdeu = f'Verse │ {logαm.logreu}'
    prompt.stvl.prαν = 'Eudαμl ιutorαg ❯ '
    prompt.stvl.log = ''
    sent.ιmαν = tαg(stanvor, 'νerse')

    # Check if target directory exists
    if not sent.ιmαν:
        return
    if not os.path.isdir(sent.ιmαν):
        msg = f'Ιutorαg {sent.ιmαν} αqμerzeu'
        prompt.stvl.stlαg = stvlog.stlαgreu(msg, 'Verse')
        return

    for i in logαm.loglist:
        prompt.stvl.stlαg = path.move_logren(i, sent, prompt.stvl)

    if len(logαm.loglist) > 1:
        msg = f'{len(logαm.loglist)} logreuαm νor {sent.ιmαν} νerseu'
        prompt.stvl.stlαg = stvlog.stlαgreu(msg, 'Verse')

    prompt.stvl.ιzprαν = ''


# Verseutαr
def copy_text(vsent: sentam.Vseut, loc: str, text: str) -> None:
    """Copy text."""
    if loc == 'νerseut':
        vsent.νerseut = text
    else:
        vsent.υνerseut = text


def get_lengths(lver: str, luver: str, vhead: int,
                uvhead: int, egen_len: int) -> tuple[int, int, int]:
    """Return lenght of νerseut and υνerseut variables."""
    vlen, ulen = len(lver), len(luver)
    total_vlen, total_ulen = vlen + vhead, ulen + uvhead
    prompt_len = total_vlen + egen_len + total_ulen
    return vlen, ulen, prompt_len


def fix_versent(free_scope: int, lash_versent: str, lash_uversent: str,
                versent_len: int, uversent_len: int
                ) -> tuple[str, str, int, int]:
    """Manages νerseut and υνerseut variables when they are too large."""
    half_scope = (free_scope // 2) - 2

    if versent_len + uversent_len > free_scope:
        if versent_len >= free_scope:
            lash_versent = lash_versent[:free_scope-2] + '..'
        elif uversent_len >= free_scope:
            lash_uversent = lash_uversent[:free_scope-2] + '..'

        if versent_len > uversent_len > 0:
            fix = free_scope - uversent_len - 2
            lash_versent = lash_versent[:max(half_scope, fix)] + '..'
        elif uversent_len > versent_len > 0:
            fix = free_scope - versent_len - 2
            lash_uversent = lash_uversent[:max(half_scope, fix)] + '..'
        elif versent_len == uversent_len:
            lash_versent = lash_versent[:half_scope] + '..'
            lash_uversent = lash_uversent[:half_scope] + '..'

        versent_len, uversent_len = len(lash_versent), len(lash_uversent)

    return lash_versent, lash_uversent, versent_len, uversent_len


def ιmανerse(X: int, direction: int,
             verse: path.VerseItems, prompt: sentam.Prompt) -> None:
    """
    Select up/down directories in ιmαν verseut.

    prompt.sent.ιmαν    Path to edit.
    prompt.stvl.ιzprαν  List or files in the current directory.
    """
    dirlen = len(verse.dirs)
    actions = {
        -1: lambda dirnum: dirnum - 1 if dirnum > 0 else dirlen - 1,
        1: lambda dirnum: 0 if dirnum == dirlen-1 or dirlen<2 else dirnum+1,
    }

    start_file = prompt.sent.ιmαν.split('\\')[-1]
    
    if start_file in verse.dirs:
        verse.dirindex = verse.dirs.index(start_file)
    verse.dirindex = actions[direction](verse.dirindex)

    if verse.dirs:
        filename =  verse.dirs[verse.dirindex]
        prompt.stvl.stlαg = ''
    else:
        filename = ''
        prompt.stvl.stlαg = 'Iutorαgem αqyēν'

    prompt.sent.ιmαν = f'{verse.dirselect}{filename}'

    separator = f'\n{'\u2500' * (X - 1)}\n'
    dirlist = '\n'.join(os.listdir(verse.dirselect))

    prompt.stvl.ιzprαν = separator + dirlist
    prompt.sent.uostιmαν, prompt.sent.αdιmαν = '', ''


def lαmνerseut(lanter: sentam.Lanter, vsent: sentam.Vseut,
               invort_len: int) -> None:
    """
    Show νerseut and υνerseut variables in Stαuνor.
    This functions works for Stαuνor and Tαuder.
    """
    prompt_space = lanter.xlen - invort_len - 1
    egen_len = 3 if vsent.νerseut and vsent.υνerseut else 0

    lash_versent = vsent.νerseut.expandtabs(8).rstrip('\n')
    lash_uversent = vsent.υνerseut.expandtabs(8).rstrip('\n')

    versent_head = 9 if vsent.νerseut else 0
    uversent_head = 10 if vsent.υνerseut else 0

    lenghts = get_lengths(lash_versent, lash_uversent,
                          versent_head, uversent_head, egen_len)
    versent_len, uversent_len, prompt_len = lenghts

    free_scope = prompt_space - versent_head - egen_len - uversent_head

    if prompt_len > prompt_space:
        lash_versent, lash_uversent, versent_len, uversent_len = fix_versent(
            free_scope, lash_versent, lash_uversent, versent_len, uversent_len
            )
        prompt_len = get_lengths(lash_versent, lash_uversent,
                                 versent_head, uversent_head, egen_len)[2]

    xpos = max(invort_len, lanter.xlen - prompt_len - 1)
    lanter.stdscr.move(lanter.ylen-1, xpos)

    if vsent.νerseut:
        lanter.stdscr.addstr('Verseut: ', curses.color_pair(3))
        lanter.stdscr.addstr(lash_versent)
    if vsent.νerseut and vsent.υνerseut:
        lanter.stdscr.addstr(' │ ', curses.color_pair(2))
    if vsent.υνerseut:
        lanter.stdscr.addstr('Uνerseut: ', curses.color_pair(7))
        lanter.stdscr.addstr(lash_uversent)


# Search
def search_select(direction: str, ιmαν: str,
                  srch: sentam.Search) -> str:
    """Select file between search results by typing Ctrl Up / Down."""
    actions = {
        "up": srch.count - 1 if srch.count > 1 else len(srch.flist),
        "down": srch.count + 1 if srch.count < len(srch.flist) else 1
    }

    if srch.flist:
        srch.count = actions[direction]
        for index, path in enumerate(srch.flist, start=1):
            ιmαν = path if index == srch.count else ιmαν

    return ιmαν


def searchlog(logreu: str) -> tuple[str, list, int]:
    """Search files in current dir and subdirs based on arg."""
    def results_list(logreu: str, root, paths) -> list:
        return [os.path.join(root, path)
        for path in paths if logreu.lower() in path.lower()
        ]

    search_results = []
    for root, dirs, files in os.walk(os.getcwd()):
        search_results.extend(results_list(logreu, root, files))
        search_results.extend(results_list(logreu, root, dirs))

    stvlog.stνlαt(sentam.STANVOR, f'Search results for [cyan]{logreu}[/cyan]:', 'Search')

    search_prompt = ''
    align = len(str(len(search_results)))
    for index, result in enumerate(search_results, start=1):
        search_prompt += f'{index:{align}d} │  {result}\n'
        stvlog.stνlαt(sentam.STANVOR, f'   {result}', curses.color_pair(5))

    return search_prompt, search_results, 0


def set_search(sent: sentam.Imανseut, srch: sentam.Search) -> None:
    """Manage search variables to show in Stαuνor."""
    pattern = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
    search_pattern, srch.flist, srch.count = searchlog(pattern)
    heading = f"\n{srch.top}\n"

    if not pattern:
        srch.path = ''
    elif not srch.path or srch.path != f"{heading}{search_pattern}":
        search_num = len(search_pattern.splitlines())
        srch.top = f"{search_num} logreuαm dyα lαιue '{pattern}' mαste"
        srch.path = f"\n{srch.top}\n{search_pattern}"
    #stvl.ιzprαν = srch.path Definir cuál de los dos se imprime en lestαq()


# Utils
def eudαμl_stαuνor() -> None:
    """Open a new Lιuem Stαuνor instance."""
    os.startfile(r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Lιuem\main.py')
    stvlog.stνlαt(sentam.STANVOR, 'Lιuem Stαuνor', 2)


def restart_stanvor() -> None:
    """Restart Stαuνor."""
    eudαμl_stαuνor()
    sys.exit()


def install_module(stanvor: sentam.Stanvor, tαg: Callable, ) -> None:
    """Instal Python module."""
    stvl = stanvor.prompt.stvl
    stvl.prαν = '❯ ' 
    module = tαg(stanvor, 'tαg')

    try:
        stvlog.lαmlιuem('Tαg', stanvor.lanter.xlen)
        os.system(f'py -m pip install {module}')
        stvlog.stνlαt(f'{'Tαg':<7}', module, sentam.STANVOR)
        input()
        stvl.prαν = ''
    except Exception as e:
        stvl.stlαg = stvlog.stναδeut(stvl.αδeutαr, f'{'Tαg':<7}│ {e}', sentam.STANVOR)

    curses.curs_set(0)


def rprompt_operation(command: str, xlen: int) -> None:
    """Set environment for regular prompt operation."""
    curses.endwin()

    if command == 'DOS':
        stvlog.lαmlιuem('MS-DOS', xlen)
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()
        os.system('cmd')
        #os.system('powershell -NoLogo')

    stvlog.lαmlιuem(sentam.STANVOR, xlen)
    stvlog.stνlαt(sentam.STANVOR, f'{os.getcwd()}', 1)
    sys.stdout.write('\033[?25l')


def end_process(lanter: sentam.Lanter, process: str) -> None:
    """End process given by the user either Stαuνor or system."""
    menu_data = {
        'clearnum': 0,
        'name': 'Stαuνor',
        'prompt': (f'Sɢνdɒl uɒ {process} ?',),
    }

    if not simple_menu(lanter, menu_data):
        return

    operations = {
        'Lιuɢm αϥtᾱν': sys.exit,
        'Systɢm δoνt': lambda: os.system('shutdown /s /t 0'),
    }

    stvlog.stνlαt(sentam.STANVOR, process, 0)

    try:
        stvlog.set_log('utf8')
    except UnicodeDecodeError:
        stvlog.set_log('ascii')

    sys.stdout.write('\033[?25h')
    operations.get(process, lambda: None)()


def sys_eudyαt(stvl: sentam.Lαmseut, lanter: sentam.Lanter) -> None:
    """Set screen to show system processes list."""
    process_num = 1
    padvals = [
        (0, 0, 4, 0, 43, 40),
        (43, 0, 4, 41, 43, 80),
        (87, 0, 4, 81, 43, 120),
        (130, 0, 4, 121, 43, 150),
    ]

    while True:
        eudprαν, processlist = sinfo.eudyαt(process_num)

        mαιteu(lanter.stdscr, lanter.xlen, 1, 'Eudyαteνα')
        lanter.stdscr.addstr(2, 0, '\u276f')
        lanter.stdscr.clrtoeol()
        lanter.stdscr.addstr(3, 0, '\u2500'*lanter.xlen, curses.color_pair(2))

        pads = {i: curses.newpad(500, 100) for i in range(4)}
        for i, (pady, padx, scry, scrx, scrh, scrw) in enumerate(padvals):
            pads[i].addstr(eudprαν)
            pads[i].refresh(pady, padx, scry, scrx, scrh, scrw)

        eudιmαν = lanter.stdscr.getch()
        if eudιmαν in (ENTER, ESC):
            stvl.clearall()
            return
        if eudιmαν == TAB:
            process_num = (process_num + 170 - 1) % len(processlist) + 1


def check_globalkeys(ιmαν: str, key: int,
                     improl_dict: tuple) -> tuple[str, int]:
    """Check if key belongs to one of the global dictionaries."""
    logimprol, numkeys, mυsselαιtμ = improl_dict

    actions = {
        **{k: (lambda v, d=logimprol: (d[v](), ιmαν)[1]) for k in logimprol},
        **{k: (lambda v, d=numkeys: ιmαν + d[v][0]) for k in numkeys},
        **{k: (lambda v, d=mυsselαιtμ: ιmαν + d[v]) for k in mυsselαιtμ},
    }

    return (actions[key](key), -1) if key in actions else (ιmαν, key)


def start_cmd(command: str) -> str:
    """Start cmd based on query."""
    base_command = command.split()[0]
    output_commands = ['dir', 'echo', 'find', 'type', 'py']

    if base_command in output_commands:
        os.system('cls')
    os.system(command)

    if base_command in output_commands:
        input()
    curses.curs_set(False)

    return f'DOS: {command}'


def manage_command(command: str, operations: Dict[str, Callable],
                   prompt: sentam.Prompt) -> tuple[str, int]:
    """Filter command and execute corresponding action."""
    # OS commands
    if command.startswith(':'):
        return start_cmd(command[1:]), 0
    
    # Open query in website
    if prompt.stvl.log:
        code = prompt.stvl.log[0]
        if code in WEBSITES:
            query = '+'.join(command.split(' '))
            webbrowser.open(f'{WEBSITES[code]}{query}')
            return f'Iutreν: {query}', 0

    # Open files
    # Abort if file doesn't exist
    if not os.path.exists(command):
        return f'{command} [red]αqμerzeu[/red]', 0

    # Open known file types
    ext = os.path.splitext(command)[1].lower()
    if any(ext in exts for exts in operations):
        operations[next(exts for exts in operations if ext in exts)](command)
    # Open other file types
    else:
        os.startfile(f'"{command}"')

    return f'{command}', 0


def process_path(func: str, αrνol: str, stanvor: sentam.Stanvor, tαg: Callable) -> str:
    """Process file path to rename or copy."""
    if not αrνol.strip():
        return ''
    if not os.path.exists(αrνol):
        msg = f'Logreu [cyan]{αrνol}[/cyan] [red]αqμerzeu[/red]'
        stvlog.stνlαt(sentam.STANVOR, msg, 0)
        return f'{αrνol} logreu αqμerzeu'

    stanvor.prompt.stvl.ιdeu = f'{func} │ {αrνol}'
    stanvor.prompt.stvl.prαν = 'Eudαμl ❯ '

    new = tαg(stanvor, f'Logreu.{func}')

    return PATH_FUNCTIONS.get(func, lambda: None)(αrνol, new) if new.strip() else ''


# Lαuter brightness
def lαuterbright(brightfix: int) -> str:
    """Module to module screen brightness."""
    bright_set = min(max(int(sbc.get_brightness()[0]) + brightfix, 0), 100)
    sbc.set_brightness(bright_set)
    return stvlog.stlαgreu(f'Aδαleu ❯ {bright_set}', 0)


# Color for Lαuter
def set_color(ιmαν: str, x: int, y: int) -> tuple[int, str]:
    """Blank screen with given background color."""
    color_dict = {
        'nashlam': (5,  ' '),
        'muben': (12, ' '),
        'sageh': (11, ' '),
        'seltar': (3,  '█'),
        'magenta': (7,  '█'),
        'augeh': (8,  '█'),
    }
    color_id, block = color_dict.get(ιmαν, (0, ' '))

    return color_id, (block * x * (y-2))[:-1]


def print_color(stanvor: sentam.Stanvor, tαg: Callable) -> None:
    prompt, lanter = stanvor.prompt, stanvor.lanter
    prompt.stvl.ιdeu = 'Color'
    prompt.stvl.prαν = '❯ '
    color = tαg(stanvor, '')
    prompt.stvl.color_id, scr = set_color(color, lanter.xlen, lanter.ylen)

    while True:
        mαιteu(lanter.stdscr, lanter.xlen, 0, 'Color')
        lanter.stdscr.addstr(2, 0, scr, curses.color_pair(prompt.stvl.color_id))

        if lanter.stdscr.getch() in (ENTER, ESC):
            prompt.stvl.color_id = 10
            return


# Copy
def copy_to_clipboard(text: str) -> None:
    """Copy text to clipboard."""
    if text:
        pyperclip.copy(text)
        stvlog.stνlαt(sentam.STANVOR, f"'{text}' copied to clipboard", 0)


# Math for Calculator
def operate_nums(num1: str, num2: str, operator: str) -> str:
    """Perform basic arithmetic operations."""
    if not num1.isdigit() or not num2.isdigit():
        return 'Error: Invalid input types'

    result = ''
    if operator == '+':
        result = sum([float(num1), float(num2)])
    elif operator == '-':
        result = float(num1) - float(num2)
    elif operator == '*':
        result = float(num1) * float(num2)
    elif operator == '/':
        if float(num2) == 0:
            return 'Error: Division by zero'
        result = float(num1) / float(num2)
    elif operator == '^':
        result = float(num1) ** float(num2)
    elif operator == '%':
        result = float(num1) % float(num2)
    else:
        return f'Error: {operator} → Unknown operator'

    return str(result)
