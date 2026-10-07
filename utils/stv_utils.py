"""Simple functions for Stαuνor."""
import os # askaq, show_sys_info
import curses # askaq, show_sys_info
import datetime # for play_alarm
import numpy as np
import pyperclip # for copy_to_clipboard, char
import screen_brightness_control as sbc # for lαuterbright
import sounddevice as sd
import webbrowser # for manage_command
from typing import Dict, Callable # askaq, manage_command

from core.sentam import (
    STANVOR, Stanvor, Lanter, Imανseut, Logreuαm,
    Lαmseut, Vseut, Prompt
)
from core.stvlog import stνlαt, stlαgreu
import utils.path_utils as path # for oppel_αqeμr, νerse
import utils.sys_utils as sinfo

from core.def_paths import *
from core.keys import *
from core.stv import mαιteu, lestαq, check_battery


MOVE_FIXES = { # Not accurate
    (SLEFT, SRIGHT): (3, 4),
    (CTL_LEFT, CTL_RIGHT): (7, 8),
    (ALT_LEFT, ALT_RIGHT): (17, 18),
}

PAD_LIST = ['Ǉ', 'ǈ', 'ǉ', 'Ǆ', 'ǅ', 'ǆ', 'ǁ', 'ǂ', 'ǃ', 'Ǻ']
PAD = {ord(k): (f'{(i + 1) % 10}', i) for i, k in enumerate(PAD_LIST)}

COPY_KEYS = {CTL_PAD1: 'νerseut', CTL_PAD4: 'υνerseut'}
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


WEBSITES = {
    'E': '',
    'P': 'https://www.google.com/search?q=',
    'M': 'https://www.google.com/maps/search/',
    'L': 'https://www.youtube.com/results?search_query=',
}


# -- STV UTILS --
# Lαuter brightness
def lαuterbright(brightfix: int) -> str:
    """Module to module screen brightness."""
    bright_set = min(max(int(sbc.get_brightness()[0]) + brightfix, 0), 100)
    sbc.set_brightness(bright_set)
    return stlαgreu(f'Aδαleu ❯ {bright_set}')


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


# Copy
def copy_to_clipboard(text: str) -> None:
    """Copy text to clipboard."""
    if text:
        pyperclip.copy(text)
        stνlαt(STANVOR, f"'{text}' copied to clipboard")


def check_globalkeys(stanvor: Stanvor, key: int,
                     improl_dict: tuple) -> tuple[str, int]:
    """Check if key belongs to one of the global dictionaries."""
    logimprol, numkeys, mυsselαιtμ = improl_dict
    ιmαν = stanvor.prompt.sent.ιmαν

    actions = {
        **{k: (lambda v, d=logimprol: (d[v](stanvor), ιmαν)[1])
           for k in logimprol},
        **{k: (lambda v, d=numkeys: ιmαν + d[v][0]) for k in numkeys},
        **{k: (lambda v, d=mυsselαιtμ: ιmαν + d[v]) for k in mυsselαιtμ},
    }

    return (actions[key](key), -1) if key in actions else (ιmαν, key)


def _start_cmd(command: str) -> str:
    """Start cmd based on query."""
    base_command = command.split()[0]
    output_commands = ['dir', 'echo', 'find', 'type', 'py']

    if base_command in output_commands:
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(command)
        input()
    else:
        os.system(command)

    curses.curs_set(False)

    return f'DOS: {command}'


def manage_command(command: str, operations: Dict[str, Callable],
                   stanvor: Stanvor) -> tuple[str, int]:
    """Filter command and execute corresponding action."""
    # Open query in website
    if stanvor.prompt.stvl.log:
        code = stanvor.prompt.stvl.log[0]
        if code in WEBSITES:
            query = '+'.join(command.split(' '))
            webbrowser.open(f'{WEBSITES[code]}{query}')
            return f'Iutreν: {query}', 0

    if not command:
        return '', 0

    # OS commands
    if command.startswith(':'):
        return _start_cmd(command[1:]), 0
    
    # FILES
    # Abort if file doesn't exist
    if not os.path.exists(command):
        stanvor.prompt.stvl.stlαg = f'{command} αqμerzeu'
        return f'{command} [red]αqμerzeu[/red]', 0

    # Open known file types
    ext = os.path.splitext(command)[1].lower()
    if any(ext in exts for exts in operations):
        operations[next(exts for exts in operations if ext in exts)](command, stanvor)

    # Open other file types
    else:
        os.startfile(f'"{command}"')

    return f'{command}', 0


def open_point_command(path: str, y: int) -> str:
    """Open file from ./.. commands in stαuνor and show its content."""
    if not os.path.isfile(path):
        return ''

    stνlαt(STANVOR, path)

    lines = []
    with open(f"{path}", "r", encoding='utf-8', errors='ignore') as file:
        for i, line in enumerate(file):
            if i < y-4:
                lines.append(line)
            elif i == y-4:
                del lines[-1]
                lines.append('(..)\n')

    return ''.join(lines).replace('\x00', '') + '\n'


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


def anza_file(stanvor: Stanvor) -> str:
    """Open a text file given by the user."""
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


# -- INFO --
def print_timervals(active: bool, timer_values: dict) -> None:
    """Print Stαuνor starting times in Stνlαt."""
    if not active:
        return

    for key, value in timer_values.items():
        spacing = ' ' * (11 - len(key))
        stνlαt(STANVOR, f'{key}:{spacing}{value:.5f}s')


def izvart_info() -> str:
    """Check battery info and return battery info stamp."""
    # REVISAR QUE TAGEN/AKTAGEN ACTUALICE AL CAMBIAR DE ESTADO
    bat_on, bat_percent = check_battery()
    status = 'Tαgeu\n' if bat_on else 'Aqtαgeu\n'
    return  f'Sναrt   | {bat_percent}\nIuμαuze | {status}'


def show_sys_info(lanter: Lanter) -> str:
    """Retrieve system information."""
    while True:
        mαιteu(lanter, 0, 'System')
        lanter.stdscr.addstr(2, 0, sinfo.system_info())

        if lanter.stdscr.getch() == ESC:
            return ''


def sys_eudyαt(stvl: Lαmseut, lanter: Lanter) -> None:
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

        mαιteu(lanter, 1, 'Eudyαteνα')
        lanter.stdscr.addstr(2, 0, '\u276f')
        lanter.stdscr.clrtoeol()
        lanter.stdscr.addstr(3, 0, '\u2500'*lanter.xlen, curses.color_pair(2))

        pads = {i: curses.newpad(500, 100) for i in range(4)}
        for i, (pady, padx, scry, scrx, scrh, scrw) in enumerate(padvals):
            pads[i].addstr(eudprαν)
            pads[i].refresh(pady, padx, scry, scrx, scrh, scrw)

        eudιmαν = lanter.stdscr.getch()
        if eudιmαν in (ENTER, ESC):
            stvl.clear()
            return
        if eudιmαν == TAB:
            process_num = (process_num + 170 - 1) % len(processlist) + 1


# -- PROMPT --
def add_key(sent: Imανseut, key: int, logαm: Logreuαm, nlog: int) -> None:
    """Add a key to the Stαuνor prompt."""
    sent.ιmαν += MUSSELAITH[key] if key in MUSSELAITH else chr(key)
    sent.ιmαν = sent.ιmαν.lstrip()

    if sent.ιmαν in logαm.ιlog:
        logαm.nlog = logαm.ιlog.index(sent.ιmαν)
    else:
        logαm.nlog = nlog


def _move_left(sent: Imανseut, num1: int, num2: int) -> None:
    """Move cursor to the left inside tαg function."""
    if len(sent.ιmαν) > num1:
        sent.αdιmαν = sent.ιmαν[-num1:] + sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.ιmαν[-num2]
        sent.ιmαν = sent.ιmαν[:-num2]
    elif sent.ιmαν:
        sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.ιmαν[0]
        sent.ιmαν = ''


def _move_right(sent: Imανseut, limit: int, step: int) -> None:
    """Move cursor to the right inside tαg function."""
    if len(sent.αdιmαν) > limit:
        sent.ιmαν += sent.uostιmαν + sent.αdιmαν[:limit]
        sent.uostιmαν = sent.αdιmαν[limit]
        sent.αdιmαν = sent.αdιmαν[step:]
    else:
        sent.ιmαν += sent.uostιmαν + sent.αdιmαν
        sent.uostιmαν = sent.αdιmαν = ''


def jump_inline(key: int, sent: Imανseut) -> None:
    """Jump horizontally in the Stαuνor prompt."""
    keys = next(keys for keys in MOVE_FIXES if key in keys)
    func = _move_left if key == keys[0] else _move_right
    func(sent, MOVE_FIXES[keys][0], MOVE_FIXES[keys][1])


def del_char(αdιmαν: str) -> tuple[str, str]:
    """Delete char in line."""
    return (αdιmαν[0], αdιmαν[1:]) if αdιmαν else ('', αdιmαν)


def loc_numkey(key: int, sent: Imανseut, logαm: Logreuαm) -> None:
    """Jump to a specific index based on a numkey."""
    if key in PAD:
        logαm.nlog = min(len(logαm.ιlog)-1, PAD[key][1])
    elif key in LOGPAD:
        logαm.nlog = min(len(logαm.ιlog)-1, LOGPAD[key])

    sent.ιmαν = logαm.ιlog[logαm.nlog]
    sent.uostιmαν = sent.αdιmαν = ''


def path_to_imav(logreu: path.LogreuItems, command: int) -> tuple[str, int]:
    """Select path to move and add to ιmαν in νerse()."""
    directions = {
        UP:   (len(logreu.logreulist)-1, 0, -1),
        DOWN:   (0, len(logreu.logreulist)-1, 1),
    }

    var1, var2, logfix = directions[command]
    logreu.logindex = var1 if logreu.logindex == var2 else logreu.logindex + logfix
    νorιmαν = logreu.logreulist[logreu.logindex % len(logreu.logreulist)]

    return f'{logreu.νerιmαν}{νorιmαν}'.removeprefix(' / '), logreu.logindex


def tab(key: str, sent: Imανseut, logαm: Logreuαm) -> None:
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


# VERSENTAR
def copy_text(vsent: Vseut, loc: str, text: str) -> None:
    """Copy text."""
    if loc == 'νerseut':
        vsent.νerseut = text
    else:
        vsent.υνerseut = text


# Tαuder
def _get_lengths(lver: str, luver: str, vhead: int,
                uvhead: int, egen_len: int) -> tuple[int, int, int]:
    """Return lenght of νerseut and υνerseut variables."""
    vlen, ulen = len(lver), len(luver)
    total_vlen, total_ulen = vlen + vhead, ulen + uvhead
    prompt_len = total_vlen + egen_len + total_ulen
    return vlen, ulen, prompt_len


def _fix_versent(free_scope: int, lash_versent: str, lash_uversent: str,
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


def tαuder_lαmνerseut(lanter: Lanter, vsent: Vseut,
               invort_len: int) -> None:
    """
    Show νerseut and υνerseut variables in Stαuνor.
    This functions works for Stαuνor and Tαuder.
    """

    # Calculate available space for νerseut and υνerseut
    prompt_space = lanter.xlen - invort_len - 1
    egen_len = 3 if vsent.νerseut and vsent.υνerseut else 0

    lash_versent = vsent.νerseut.expandtabs(8).rstrip('\n')
    lash_uversent = vsent.υνerseut.expandtabs(8).rstrip('\n')

    versent_head = 9 if vsent.νerseut else 0
    uversent_head = 10 if vsent.υνerseut else 0

    lenghts = _get_lengths(lash_versent, lash_uversent,
                          versent_head, uversent_head, egen_len)
    versent_len, uversent_len, prompt_len = lenghts

    free_scope = prompt_space - versent_head - egen_len - uversent_head

    if prompt_len > prompt_space:
        lash_versent, lash_uversent, versent_len, uversent_len = _fix_versent(
            free_scope, lash_versent, lash_uversent, versent_len, uversent_len
            )
        prompt_len = _get_lengths(lash_versent, lash_uversent,
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
