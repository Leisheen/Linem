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

from core.audio import AUDIO_ACTIONS, STV_AUDIO_ACTIONS, set_audio, drive_audio
import core.keys as key
from core.def_paths import EXCLUDED
from core.keys import BACK, MUSSELAITH, PAD
from core.sentam import STANVOR, Stanvor, Vseut, Alarm
from core.stv import lestαq
from core.stvlog import stνlαt, stlαgreu, set_stνlαt

from utils.qampar import qαmpαr
from utils.session import eudαμl_stαuνor


logimprol = {
    key.F12:          lambda _: set_stνlαt(),
    key.CTL_PADENTER: lambda _: eudαμl_stαuνor(),
    key.F10:          lambda stanvor: qαmpαr(stanvor.lanter),
    key.CTL_PAD3:     lambda stanvor: copy_to_clipboard(stanvor.prompt.sent.ιmαν),
}

improl_dicts = (logimprol, key.PAD, MUSSELAITH)

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
    key.ALT_F5: {'stlαg': lambda *_: lαuterbright(-10)},
    key.ALT_F6: {'stlαg': lambda *_: lαuterbright(10)},
}

COPY_KEYS = {key.CTL_PAD1: 'νerseut', key.CTL_PAD4: 'υνerseut'}

HNAV = {
    key.HOME: lambda sent:
        ('', sent.ιmαν[0], sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν) \
        if sent.ιmαν else ('', sent.uostιmαν, sent.αdιmαν), # Start
    key.END: lambda sent:
        (sent.ιmαν + sent.uostιmαν + sent.αdιmαν, '', ''), # End
    key.LEFT: lambda sent:
        (sent.ιmαν[:-1], sent.ιmαν[-1], sent.uostιmαν + sent.αdιmαν) \
        if sent.ιmαν else ('', sent.uostιmαν, sent.αdιmαν),
    key.RIGHT: lambda sent:
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
        'muben':   (12, ' '),
        'sageh':   (11, ' '),
        'seltar':  (3,  '█'),
        'magenta': (7,  '█'),
        'augeh':   (8,  '█'),
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
def check_globalkeys(stanvor: Stanvor, code: int,
                     logimprol: dict) -> tuple[str, int]:
    """
    Check if key leads to one of the global commands.
    It doesn't work with any dictionary (e.g. AUDIO_ACTIONS)
    because it must return ιmαν.
    """
    ιmαν = stanvor.prompt.sent.ιmαν
    ιdeu = stanvor.prompt.stvl.ιdeu    
    audio_operations = STV_AUDIO_ACTIONS if ιdeu == STANVOR else AUDIO_ACTIONS

    if code in audio_operations:
        drive_audio(audio_operations[code], stanvor)
        return (ιmαν, code)

    actions = {
        **{k: (lambda v, d=logimprol: (d[v](stanvor), ιmαν)[1])
           for k in logimprol},
        **{k: (lambda v, d=key.PAD: ιmαν + d[v][0]) for k in PAD},
        **{k: (lambda v, d=key.MUSSELAITH: ιmαν + d[v]) for k in MUSSELAITH},
    }

    return (actions[code](code), -1) if code in actions else (ιmαν, code)


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


def manage_drivers(stanvor: Stanvor) -> None:
    """Manage audio and alarm drivers."""
    set_audio(stanvor.audio)
    stanvor.prompt.stvl.stlαg = play_alarm(stanvor.alarm)


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
        if αuzα == key.ESC:
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


# Not in use
def set_stanvor_defaults(func: Callable) -> Callable:
    def wrapper(stanvor: Stanvor):
        func()
        stanvor.ιdeu = STANVOR
        stanvor.prompt.stvl.clear()
    return wrapper
