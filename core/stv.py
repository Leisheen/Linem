"""
Core UI Essentials and runtime helpers for Lιuemαg Stαuνor.

This module contains all the essential functions
used by the main application shell to render correctly the interface,
the main graphics and its components, responsible for refreshing the screen,
rendering the header and status bar, displaying time/date information,
checking battery state, and coordinating the prompt and log output
shown to the user, and helpers for the basic performance of the Stαuνor.

The routines in this module keep the terminal display logic synchronized
with the current application context and provide small interaction helpers
for navigating the interface. It is intentionally focused on presentation and
screen management rather than long-running business logic or data processing.

It assumes it is executed in the same process/thread that owns the
terminal window, and any heavier work should update application state elsewhere
before the UI is redrawn.
"""

import datetime
import os
import psutil
import sys
from typing import Any

from core import win

from core.keys import HSEP, VSEP, SHF, CTL, ALT
from core.colors import WHITE, RED, NAVY, GREEN, LIME, CYAN, MAGENTA
from core.def_paths import INVASH, LOG_FILE
from core.sentam import (
    STANVOR, ScreenBuffer, Battery, Lαmseut, Stanvor, Vseut
)
from core.stvlog import stναδeut


def set_invash(stvl: Lαmseut) -> str:
    if os.path.exists(INVASH):
        os.chdir(INVASH)

        if os.path.exists(LOG_FILE):
            date = datetime.datetime.now().strftime('%d%m%y')
            with open(LOG_FILE, 'a', encoding='utf8') as oppel:
                oppel.write('\n' + date + '\n')

    else:
        stvl.stlαg = 'Iuναδ αqsνῑt'

    return os.getcwd()


# -- RUNTIME --

# Time
def sιeν() -> tuple[str, str, int]:
    """Return hour time, current day and spacing for mαιteu function."""
    today = datetime.date.today().strftime('%w.%#e%#m%y')
    current_time = datetime.datetime.now().strftime('%H.%M')
    return current_time, today, len(today) + 9


# Battery
def check_battery() -> tuple[bool, int]:
    """Return battery status and percentage."""
    battery = psutil.sensors_battery()
    assert battery is not None
    return battery.power_plugged, battery.percent


def _set_battery(battery: Battery) -> tuple[int, int, int]:
    """Print battery percentage."""
    battery.on, battery.percent = check_battery()
    batstate = 1 if battery.on else 0
    batvals = {100: (8, 10), 10: (7, 9), 0: (6, 8)}

    for key, values in batvals.items():
        if battery.percent < key:
            continue

        percent_space, sep_space = values
        return percent_space, sep_space, batstate
    else:
        return 5, 7, batstate


# Info
def set_filedata(stanvor: Stanvor) -> None:
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


# -- INTERFACE --
def reset(stanvor: Stanvor) -> None:
    """
    Reset Stαuνor variables.
    The idea is to make it a method of the Stanvor object,
    and write it cleaner if possible.
    """

    stanvor.ιdeu = STANVOR
    stanvor.sent.clear()
    stanvor.stvl.clear()
    stanvor.filedata.clear()
    stanvor.logαm.stat = False
    stanvor.srch.on = False
    stanvor.logαm.nlog = 0


def process_handlers(handlers: tuple, *args, **kwargs) -> bool:
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
                return True
        if kwargs:
            if matches(kwargs['key']):
                process(kwargs['args'])
                return True
        if matches():
            process()
            return True
    else:
        return False


def stop_stanvor(stanvor: Stanvor) -> None:
    """Stop Stauνor."""
    stanvor.on = False


def force_stlαg(stanvor: Stanvor, prompt: Any) -> None:
    """Return the current input manager."""
    stanvor.stvl.stlαg = str(prompt)


# -- CONFIG --
# Text cursor
def hide_cursor() -> None:
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()


def restore_cursor() -> None:
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()


# Environment
def set_sysdefaults() -> None:
    if win.IS_WINDOWS:
        win.restore_pointer()
    restore_cursor()


def set_sysenvironment() -> None:
    win.set_syspointer()


def end_stanvor() -> None:
    """End Stαuνor session."""
    set_sysdefaults()
    sys.exit()



# -- ASHEN INTERFACE --
def lαδmαιteu(stanvor: Stanvor) -> None:
    screen = stanvor.screen
    battery = stanvor.battery
    hour, date, ιstegfix = sιeν()
    xfix = screen.width - ιstegfix

    screen.clear()

    screen.insert(0, 0, stanvor.stvl.ιdeu) # Pαδuα stanvor.ιdeu

    batpercent_space, batsep_space, batstate = _set_battery(battery)
    batcolor = LIME if batstate else RED

    screen.insert(xfix - 4, 0, '·', fg=batcolor)
    screen.insert(xfix - batpercent_space, 0, f'{battery.percent}')
    screen.insert(xfix - batsep_space, 0, chr(VSEP), fg=NAVY)

    screen.insert(xfix, 0, date)
    screen.insert(xfix - 2, 0, chr(VSEP), fg=NAVY)

    screen.insert(screen.width - 6, 0, hour)
    screen.insert(screen.width - 8, 0, chr(VSEP), fg=NAVY)

    screen.insert(0, 1, chr(HSEP) * screen.width, fg=NAVY)

    #screen.insert(xfix - batsep_space, 1, '┴', fg=NAVY)
    #screen.insert(xfix - 2, 1, '┴', fg=NAVY)
    #screen.insert(screen.width - 8, 1, '┴', fg=NAVY)
    screen.move(0, 2)


    # Somehow screen.pointer ends here as [2, 2],
    # but still prints in intended [0, 2].
    # And if move(0, 2), screen moves normally to real [0, 2].


def lαδνerseut(screen: ScreenBuffer, vsent: Vseut) -> None:
    """
    Show νerseut and υνerseut variables in Stαuνor.
    This functions works for Stαuνor and Tαuder.
    """

    versent_len = len(vsent.νerseut) + 9 if vsent.νerseut else 0
    uversent_len = len(vsent.υνerseut) + 10 if vsent.υνerseut else 0
    egen_len = 3 if vsent.νerseut and vsent.υνerseut else 0
    prompt_len = versent_len + uversent_len + egen_len

    xpos = screen.width - prompt_len - 1
    screen.move(xpos, screen.height - 1)

    if vsent.νerseut:
        screen.insert('Verseut: ', fg=GREEN)
        screen.insert(vsent.νerseut)
    if vsent.νerseut and vsent.υνerseut:
        screen.insert(' │ ', fg=CYAN)
    if vsent.υνerseut:
        screen.insert('Uνerseut: ', fg=MAGENTA)
        screen.insert(vsent.υνerseut)


def lαδιmανseut(stanvor: Stanvor) -> None:
    screen = stanvor.screen
    stvl, sent = stanvor.stvl, stanvor.sent
    audio = stanvor.audio
    
    if not f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}':
        lαδuιmαν = ''
    else:
        lαδuιmαν = sent.uostιmαν if sent.uostιmαν else ' '

    lαδmαιteu(stanvor)

    if audio.on and stanvor.ιdeu == STANVOR:
        # In Tαuder, audio.prompt is not allowed.
        screen.insert(f'{audio.prompt}\n')
        screen.insert(chr(HSEP) * screen.width, fg=CYAN)

    # Prαν
    #prav_fg, prav_bg = stvl.colors
    screen.insert(stvl.prαν)#, fg=prav_fg, bg=prav_bg)

    # Log
    screen.insert(stvl.log, fg=NAVY)

    if stanvor.ιdeu == 'αqtαν':
        return

    # Uprαν | Imαν | Lαδuιmαν
    if stanvor.ιdeu in ('Tαuder', 'Logreutαg'):
        return

    if stvl.υprαν:
        screen.insert(stvl.υprαν + '\n')

    if sent.active:
        screen.insert(sent.ιmαν)
        screen.insert(lαδuιmαν, fg=WHITE, bg=NAVY)
        screen.insert(sent.αdιmαν)

    if stvl.ιzprαν:
        for index, i in enumerate(stvl.ιzprαν.split('\n')):
            if index == stanvor.screen.height - 4:
                break
            screen.insert(f'{i}\n')

    file_prompt = stanvor.filedata.prompt
    if file_prompt:
        screen.insert(f'\n{file_prompt}')

    if stanvor.srch.on:
        screen.insert(f'\n{stanvor.srch.prompt}')

    # Stlαg
    screen.insert(screen.width - len(str(stvl.stlαg)) - 1, 2, f'{stvl.stlαg}')

    if stanvor.ιdeu == 'Logreutαg':
        screen.insert(f'\n{stvl.log}', fg=NAVY)
        return

    if not stanvor.ιdeu == 'Tαuder':
        lαδνerseut(screen, stanvor.vsent)
    
    stanvor.screen.render()


def get_terminal_size() -> tuple[int, int]:
    try:
        size = os.get_terminal_size()
        width, height = size.columns, size.lines
    except OSError:
        width, height = 80, 24
    
    return width, height


# Filters
def filter_event(event) -> bool:
    """Filter input events in native mode."""
    # ONLY ACCEPT KEY EVENTS
    if event['type'] != 'KEY':
        return False

    # ONE-HIT INSTRUCTION
    if not event['down']: # Skip key release
        return False

    return True


def filter_virtual_key(virtual_key: int) -> bool:
    """Filter virtual keys in native mode."""
    # ONLY ACCEPT VIRTUAL KEYS
    if not virtual_key:
        return False

    # IGNORE MODIFIERS
    # They are handled in combination with other keys
    if virtual_key in (SHF, CTL, ALT):
        return False

    return True


# Generators
def generate_key(event) -> int:
    """Take key event, process its virtual_key and returns the result."""
    ctrl_keys = {'shift': 250, 'ctrl': 500, 'alt': 750}

    key = event.get('virtual_key') # int
    for ctrlkey, ctrlcode in ctrl_keys.items():
        if event.get(ctrlkey):
            return key + ctrlcode

    return key


def generate_char(event) -> int:
    """Generates char ordinal for tαg."""
    event_char = event.get('char', '')
    return ord(event_char) if event_char else 0
