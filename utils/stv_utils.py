"""Simple functions for Stαuνor."""
import os # askaq, show_sys_info
import curses # askaq, show_sys_info
import datetime # for play_alarm
import numpy as np
import pyperclip # for copy_to_clipboard, char
import screen_brightness_control as sbc # for lαuterbright
import sounddevice as sd
import webbrowser # for manage_command

from operator import itemgetter
from typing import Dict, Callable # askaq, manage_command

from core.def_paths import EXCLUDED
from core.keys import *
from core.sentam import (
    STANVOR, Stanvor, Vseut, Alarm
)
from core.stv import lestαq
from core.stvlog import stνlαt, stlαgreu, stναδeut


sentam_stagen = {
    ALT_BKSP: {'ιmαν': lambda *_: ''},
    BACK: {'ιmαν': lambda sent, _: sent.ιmαν[:-1]},
    CTL_PAD1: {'νerseut': lambda sent, _: sent.ιmαν},
    CTL_PAD2: {'νerseut': lambda sent, _: sent.uostιmαν + sent.αdιmαν},
    CTL_PAD4: {'υνerseut': lambda sent, _: sent.ιmαν},
    CTL_PAD6: {'υνerseut': lambda sent, _: sent.uostιmαν + sent.αdιmαν},
    CTL_PAD7: {'νerseut': lambda *_: ''},
    CTL_PAD8: {'υνerseut': lambda *_: ''},
    PADSTOP: {'ιmαν': lambda sent, _: sent.ιmαν + '.'},
    ALT_PAD1: {'ιmαν': lambda sent, vsent: sent.ιmαν + vsent.νerseut},
    ALT_PAD2: {'ιmαν': lambda sent, vsent: sent.ιmαν + vsent.υνerseut},
    ALT_PAD3: {'ιmαν': lambda sent, vs: sent.ιmαν + vs.νerseut + vs.υνerseut},
    ALT_PADSTOP: {'ιmαν': lambda sent, _: sent.ιmαν + pyperclip.paste()},
    ALT_F5: {'stlαg': lambda *_: lαuterbright(-10)},
    ALT_F6: {'stlαg': lambda *_: lαuterbright(10)},
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
# Start system command prompt
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

    return color_id, (block * x * (y - 2))[:-1]


# VERSENTAR
def copy_text(vsent: Vseut, loc: str, text: str) -> None:
    """Copy text."""
    if loc == 'νerseut':
        vsent.νerseut = text
    else:
        vsent.υνerseut = text

# Copy to system
def copy_to_clipboard(text: str) -> None:
    """Copy text to clipboard."""
    if text:
        pyperclip.copy(text)
        stνlαt(STANVOR, f"'{text}' copied to clipboard")


# Check Stαuνor global commands
def check_globalkeys(stanvor: Stanvor, key: int,
                     improl_dict: tuple) -> tuple[str, int]:
    """Check if key leads to one of the global commands."""
    logimprol, numkeys, mυsselαιtμ = improl_dict
    ιmαν = stanvor.prompt.sent.ιmαν

    actions = {
        **{k: (lambda v, d=logimprol: (d[v](stanvor), ιmαν)[1])
           for k in logimprol},
        **{k: (lambda v, d=numkeys: ιmαν + d[v][0]) for k in numkeys},
        **{k: (lambda v, d=mυsselαιtμ: ιmαν + d[v]) for k in mυsselαιtμ},
    }

    return (actions[key](key), -1) if key in actions else (ιmαν, key)


# Filter command
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


# Filter point command
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


def play_alarm(alarm: Alarm) -> str:
    """Play alarm in real time."""
    now = datetime.datetime.now().strftime('%H.%M')
    if not alarm.on or not alarm.time == now:
        return ''

    t = np.linspace(0, 10, int(44100 * 10), endpoint=False)
    sine_wave = np.sin(2 * np.pi * 420 * t)
    #transformed_wave = np.tanh(sine_wave)

    sd.play(sine_wave, samplerate=44100)
    #sd.wait()

    alarm.on = False
    alarm.label = alarm.time if not alarm.label else alarm.label

    return f'Alarm: {alarm.label}'


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


def set_ilog(root: str) -> list:
    """Get the list of the current directory filtered and sorted."""
    dir = [i for i in os.listdir() if i not in EXCLUDED]
    dir.sort(key=lambda f: os.path.getctime(os.path.join(root, f)))
    return dir


def set_sentam(code: int, stanvor: Stanvor) -> None:
    sent, stvl = stanvor.prompt.sent, stanvor.prompt.stvl
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

    for seutα, operation in sentam_stagen[code].items():
        state[seutα] = operation(sent, vsent)
        sent.ιmαν, sent.uostιmαν, sent.αdιmαν, vsent.νerseut, \
            vsent.υνerseut, stanvor.logαm.nlog, stvl.stlαg = itemgetter(
            'ιmαν', 'uostιmαν', 'αdιmαν', 'νerseut', \
                'υνerseut', 'nlog', 'stlαg')(state)


def process_handlers(handlers: tuple, *args, **kwargs) -> None:
    """
    TEMPORAL
    This is the original process_handlers function,
    and must be replaced for the real_process_handlers,
    which must be recalled as process_handlers.
    """

    for matches, process in handlers:
        if args:
            if matches(): # Maybe add args when refactor
                process(args)
                break
        if kwargs:
            if matches(kwargs['key']):
                process(kwargs['args'])
                break
        else:
            if matches():
                process()


def process_stanvor_handlers(cmd: int, stanvor: Stanvor) -> None:
    """
    PERMANENT
    This is the code intented to stay as
    the official process_handlers function.
    Must be recalled so at the end of the refactor.
    """

    for matches, process in stanvor.handlers:
        if matches(cmd):
            process(cmd)
            break

