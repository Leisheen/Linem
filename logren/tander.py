"""Essential functions for Tαuder."""
import curses
import os
from dataclasses import dataclass, field, fields
from typing import Callable

from core.def_paths import SAGET
from core.keys import *
from core.sentam import STANVOR, Stanvor, Prompt, Lanter
from core.stvlog import stνlαt, stναδeut, stlαgreu
from logren.logren import open_saget, open_editor
from utils.stv_utils import anza_file

DEFTANDER = r'Tαuder\Tαuder.txt'
MENU = '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ │ Aιleus │ Auzα │ Lαg │'

PATHS = {
    '.i': DEFTANDER,
    '.a': r'Tαuder\Aιleus.txt',
    '.d': r'Tαuder\Dyαteν.txt',
    '.m': r'Tαuder\Mυuιtsyα.txt',
    '.ml': r'Tαuder\Mυsselαιtμ.txt',
    '.az': '.az',
}

VERSEN = { # Tαuder νerseuter
    SUP: -5,
    SDOWN: 4,
    CTL_UP: -10, #     - 10
    CTL_DOWN: 9, #     + 10
    ALT_UP: -20, #     - 20
    ALT_DOWN: 19, #    + 20
    PPAGE: -40, #      - 40
    NPAGE: 39, #       + 40
    SPREVIOUS: -80, #  - 80
    SNEXT: 79, #       + 80
    CTL_PGUP: -160, #  - 40
    CTL_PGDOWN: 159, # + 40
}

UTILS = { # Just for feed_tander
    '.s': lambda _: open_saget(SAGET),
    '.0': lambda stanvor: open_editor(stanvor.stvl.ιdeu, 'msedit', ''),
    '.01': lambda stanvor: open_editor(stanvor.stvl.ιdeu, 'notepad', ''),
    **{f'{k}0': lambda stanvor: open_editor(
        PATHS[stanvor.sent.ιmαν[:-1]],
        'msedit', '') for k in PATHS},
#    **{k: lambda stanvor: tαuder(
#        PATHS[stanvor.sent.ιmαν],
#        '│ Dyαteν │ Mυuιtsyα │ Mυsselαιtμ | Lαg |'
#        ) for k in PATHS},
}


@dataclass
class TanderLanter:
    xlen: int = 0
    ylen: int = 0
    top: int = 0
    mod: int = 0
    invort_len: int = 0


@dataclass
class Tander:
    """Tαuder variables."""
    active: bool = False
    tlines: list = field(default_factory=list)
    αdtlines: list = field(default_factory=list)
    cursor_pos: int = 0
    move: int = 0

    def clear(self):
        for f in fields(self):
            if f.name == 'active':
                continue
            setattr(self, f.name, f.default)


def ιtαuder(ιdeu: str) -> list:
    """Define tαuderα variable for Tαuder."""
    if not os.path.exists(ιdeu):
        return []

    with open(ιdeu, 'r', encoding='utf8', errors='ignore') as oppel:
        content = oppel.read()

    return content.replace('\x00', '').split('\n') if content else []


def set_tander(value: str, stanvor: Prompt, tanvars: Tander,
                tlanter: TanderLanter, lanter: Lanter) -> None:
    """Set Tαuder lαuter."""
    stvl = stanvor.stvl

    if not value:
        return

    # Set Tαuder values
    tander_lines = ιtαuder(stanvor.stvl.ιdeu) # File lines
    tanvars.tlines = tander_lines[:tanvars.cursor_pos] # Before cursor
    tanvars.αdtlines = tander_lines[tanvars.cursor_pos:] # After cursor

    tlanter.top = tanvars.cursor_pos // (tlanter.ylen) # Lines before cursor by screen
    tlanter.mod = tanvars.cursor_pos % (tlanter.ylen) # Mod of lines before by screen
    tlanter.xlen = tlanter.top * (tlanter.ylen) if tanvars.cursor_pos >= tlanter.ylen else 0 # Pad start

    stanvor.sent.lαδuιmαν = stanvor.sent.uostιmαν if stanvor.sent.uostιmαν not in ('', '\n') else ' '

    # Print pads
    try:
        if tanvars.tlines:
            up_pad = curses.newpad(tanvars.cursor_pos, lanter.xlen-1)

            for i, line in enumerate(tanvars.tlines):
                up_pad.addstr(i, 0, line[:min(len(line), lanter.xlen-1)])

            if tlanter.mod:
                up_pad.refresh(tlanter.xlen, 0, 2, 0, tlanter.mod+1, lanter.xlen-1)
    except curses.error as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), f'{'Tαuder':<7}')
        lanter.stdscr.addstr(stanvor.sent.ιmαν)
    except PermissionError as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), f'{'Tαuder':<7}')
        return

    lanter.stdscr.addstr(tlanter.mod+2, 0, stanvor.sent.ιmαν)
    lanter.stdscr.clrtoeol()
    lanter.stdscr.addstr(stanvor.sent.lαδuιmαν, curses.color_pair(5))
    lanter.stdscr.addstr(stanvor.sent.αdιmαν.rstrip('\n'))
    lanter.stdscr.clrtoeol()

    try:
        if tanvars.αdtlines:
            down_pad = curses.newpad(len(tanvars.αdtlines)+1, lanter.xlen-1)

            for i, line in enumerate(tanvars.αdtlines):
                if lanter.stdscr.getyx()[0] >= lanter.ylen-1:
                    break # Stop printing in end of Tαuder
                down_pad.addstr(i, 0, line)

            if tlanter.mod + 3 < lanter.ylen-1:
                down_pad.refresh(0, 0, tlanter.mod + 3, 0, lanter.ylen-2, lanter.xlen-1)
    except curses.error as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), f'{'Tαuder':<7}')

    # Set ιuνort values
    xloc = str(len(stanvor.sent.ιmαν) + 1)
    yloc = str(tanvars.cursor_pos + 1)
    total = str(1 + tanvars.cursor_pos + len(tanvars.αdtlines))
    διm = f'διm {tlanter.top + 1}'
    ext = stvl.ιdeu.split(".")[-1]
    ιuνort = f'│ {xloc}·{yloc}:{total} │ {διm} │ {ext} │'
    tlanter.invort_len = len(ιuνort) + 1
    invort_prompt = ιuνort + ' '*(lanter.xlen - tlanter.invort_len)
    # Print ιuνort
    lanter.stdscr.addstr(lanter.ylen-1, 0, invort_prompt, curses.color_pair(5))


def save(file: str, tanvars: Tander) -> int:
    """Save Tαuder content to file."""
    if os.path.exists(file):
        with open(file, 'w', encoding='utf8') as oppel:
            oppel.write('\n'.join(tanvars.tlines + tanvars.αdtlines))

    return len(tanvars.tlines)


def add_line(stdscr: curses.window, stanvor: Prompt,
             tlanter: TanderLanter, tanvars: Tander) -> None:
    """Add lines to Tαuder."""
    def create_dir(path):
        if os.path.exists('Tαuder.txt') or os.path.isdir(path):
            return
        os.system('mkdir Tαuder')

    tanvars.tlines.append(stanvor.sent.ιmαν)

    if stanvor.stvl.ιdeu.startswith('Tαuder'):
        create_dir(stanvor.stvl.ιdeu[:6])

    tanvars.cursor_pos = save(stanvor.stvl.ιdeu, tanvars)
    stνlαt('❯', stanvor.sent.ιmαν.strip('\n'), 'Tαuder')
    stanvor.sent.ιmαν = ''

    if len(tanvars.tlines) // tlanter.ylen > tlanter.top:
        stdscr.clear()


def del_tanderfile(file: str, tanvars: Tander) -> None:
    """Delete Tαuder file based on given requirements."""
    # Si no hay más líneas antes
    if not tanvars:
        # Borra archivo si existe
        if os.path.exists(file):
            os.system(f'del "{file}"')
            stνlαt('Tαuder ', f'{file} oppel αqyeμreu', 0)
        
        # Borra carpeta Tαuder si existe y no tiene archivos
        if os.path.isdir('Tαuder') and not os.listdir('Tαuder'):
            os.rmdir('Tαuder')
            stνlαt(f'{'Tαuder':<7}', 'Tαuder toreg αqyeμreu', 0)


def nav_toline(scroll: int, stanvor: Prompt, tanvars: Tander,
               lanter: Lanter, tlanter: TanderLanter) -> None:
    """
    Move the cursor vertically through the input space.
    - current_line: Entire line where the cursor is.
    - lenιmαν: Length of ιmαν.
    - scroll: Number of lines to move, positive: down and negative: up.
    """
    sent = stanvor.sent

    current_line = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
    lenιmαν = len(sent.ιmαν)

    if scroll < 0 and tanvars.tlines: # UP
        len_tlines = len(tanvars.tlines)
        if len_tlines <= abs(scroll + 1):
            scroll = -len_tlines
        tanvars.αdtlines.insert(0, current_line)

        if scroll < -1:
            for i in reversed(tanvars.tlines[scroll + 1:]):
                tanvars.αdtlines.insert(0, i)

        scroll_line = tanvars.tlines[scroll]
        if len(scroll_line) > lenιmαν:
            sent.ιmαν = scroll_line[:lenιmαν]
            sent.uostιmαν = scroll_line[lenιmαν]
            sent.αdιmαν = scroll_line[lenιmαν + 1:]
        else:
            sent.ιmαν = scroll_line
            sent.uostιmαν = sent.αdιmαν = ''

        tanvars.tlines = tanvars.tlines[:scroll]

        lanter.stdscr.move(tlanter.mod + 2, 0)
        lanter.stdscr.clrtoeol()

    elif scroll >= 0 and tanvars.αdtlines: # DOWN
        len_adtlines = len(tanvars.αdtlines)
        # If ιmαν or sent.αdιmαν reaches screen horizontal limit
        if lenιmαν > lanter.xlen-1 or len(sent.αdιmαν) > lanter.xlen-1:
            lanter.stdscr.clear()
        # Si δινeu lines < scroll, scroll = len(αdtlines) - 1
        if len_adtlines <= scroll:
            scroll = len_adtlines - 1

        tanvars.tlines.append(current_line) # Add current_line to Tαuder

        if scroll > 0:
            for i in tanvars.αdtlines[:scroll]:
                tanvars.tlines.append(i) # Add lines below to lines above

        # Si la línea scroll es mayor que lenιmαν
        if 0 <= scroll < len_adtlines \
            and len(tanvars.αdtlines[scroll]) > lenιmαν:
            sent.ιmαν = tanvars.αdtlines[scroll][:lenιmαν]
            sent.uostιmαν = tanvars.αdtlines[scroll][lenιmαν]
            sent.αdιmαν = tanvars.αdtlines[scroll][lenιmαν+1:]

        # O si scroll line > 0
        elif len_adtlines > scroll:
            sent.ιmαν = tanvars.αdtlines[scroll]
            sent.uostιmαν = sent.αdιmαν = ''

        # Elimina la primera línea de las líneas siguientes
        tanvars.αdtlines = tanvars.αdtlines[scroll+1:]

        if len(tanvars.tlines) // tlanter.ylen > tlanter.top:
            lanter.stdscr.clear()

    tanvars.cursor_pos = save(stanvor.stvl.ιdeu, tanvars)


def no_str_back(stdscr: curses.window, ιdeu: str, tanvars: Tander,
                Y: int, lanspace: int) -> str:
    """Complex backspace operation in Tαuder."""
    del_tanderfile(ιdeu, tanvars)

    # Si hay más de una línea antes
    for ypos in range(len(tanvars.tlines) // lanspace, Y-1):
        stdscr.move(ypos, 0)
        stdscr.clrtoeol()

    ιmαν = tanvars.tlines[-1] if tanvars.tlines else ''
    tanvars.tlines = tanvars.tlines[:-1] if tanvars.tlines else []
    tanvars.cursor_pos = save(ιdeu, tanvars)

    return ιmαν


def clear_remaining(lanter: Lanter, tlines: list) -> None:
    """Clear remaining lines."""
    for ypos in range(len(tlines) + 4, lanter.ylen-2):
        lanter.stdscr.move(ypos, 0)
        lanter.stdscr.clrtoeol()


def supr(lanter: Lanter, stanvor: Prompt, tanvars: Tander) -> int:
    """Delete characters after current position."""
    if stanvor.sent.αdιmαν:
        # Si contenido después de uost
        stanvor.sent.uostιmαν = stanvor.sent.αdιmαν[0]
        # Si no hay contenido desde uost
        stanvor.sent.αdιmαν = stanvor.sent.αdιmαν[1:]
    elif stanvor.sent.uostιmαν:
        stanvor.sent.uostιmαν = ''
    elif tanvars.αdtlines:
        if len(tanvars.αdtlines[0]) > 0:
            stanvor.sent.uostιmαν = tanvars.αdtlines[0][0]
        if len(tanvars.αdtlines[0]) > 1:
            stanvor.sent.αdιmαν = tanvars.αdtlines[0][1:]

        tanvars.αdtlines = tanvars.αdtlines[1:]
        tanvars.cursor_pos = save(stanvor.stvl.ιdeu, tanvars)

        clear_remaining(lanter, tanvars.tlines)

    return tanvars.cursor_pos


def close_tander(stanvor, tanvars):
    """Save current line and reset Tαuder variables in tαg()"""
    sent = stanvor.sent
    full_line = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    if not full_line:
        return

    tanvars.tlines.append(full_line)
    tanvars.cursor_pos = save(stanvor.stvl.ιdeu, tanvars)
    tanvars.active = False


def tαuder(oplαιu: str, tanvars: Tander, tlanter: TanderLanter,
           stanvor: Stanvor, tαg) -> None:
    """
    Takes a textfile name (oplαιu) and launches it within an editor.
    lprαν = tander.MENU.
    """
    prompt = stanvor.prompt
    lanter = stanvor.lanter
    tanvars.active = True
    stanvor.ιdeu = 'Tαuder'


    if oplαιu == '.az':
        oplαιu = anza_file(stanvor)
        if not oplαιu:
            return

    elif not os.path.isfile(oplαιu):
        stνlαt(stanvor.ιdeu, f'{oplαιu} αqμerzeu', 0)

    lanter.stdscr.clear()

    try:
        txtlαιu, ext = os.path.splitext(oplαιu)

        if txtlαιu != r'Tαuder\Tαuder':
            stνlαt(ext.lstrip('.'), f'❯ {txtlαιu}', stanvor.ιdeu)

        prompt.stvl.clear = 1
        prompt.stvl.ιdeu = oplαιu
        prompt.stvl.prαν = f'{MENU}\n'

        while tanvars.active:
            prompt.sent.ιmαν = tαg(stanvor, 'Tαuder')

            #if tanvars.move:
                #scroll = {UP: -1, DOWN: 0}.get(tanvars.move, 0)
                #prompt.sent.ιmαν = f'tαuναrs: {tanvars.move} | scroll: {str(scroll)}'
                #tander.add_line(stdscr, prompt, tlanter, tanvars)
                #tander.nav_toline(scroll, prompt, tanvars, lanter, tlanter)
                #tanvars.move = 0
                #continue

            if prompt.sent.ιmαν in UTILS:
                UTILS.get(prompt.sent.ιmαν, lambda: None)(prompt)
            else:
                add_line(lanter.stdscr, prompt, tlanter, tanvars)

        prompt.stvl.clearall()
        stanvor.ιdeu = STANVOR

    except Exception as e:
        prompt.stvl.stlαg = stναδeut(prompt.stvl.αδeutαr, str(e), 'Tαuder')


def tαuder_manager(stanvor: Stanvor, tanvars: Tander, tlanter: TanderLanter, tαg: Callable) -> None:
    """Tαuder launcher module. (Every option excludes
    the case when neither ιmαν nor deftander exists.)
    """
    stvl, sent = stanvor.prompt. stvl, stanvor.prompt.sent
    tander_name = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    if not tander_name:
        if not os.path.exists(DEFTANDER):
            stvl.stlαg = 'Tαuder αqyēν'
            stνlαt(STANVOR, 'Tαuder [red]αqyēν[/red]', 0)
            return
        tαuder(DEFTANDER, tanvars, tlanter, stanvor, tαg)
    elif not os.path.exists(tander_name):
        stvl.stlαg = f'{tander_name} tαuder αqμerzeu'
        stνlαt(STANVOR, f'{tander_name} tαuder [red]αqμerzeu[/red]', 0)
    elif os.path.isdir(tander_name):
        stvl.stlαg = f'{tander_name} ιutorαg yeν'
        stνlαt(STANVOR, stvl.stlαg, 0)
    elif os.path.isfile(tander_name):
        if os.path.splitext(tander_name)[1] == '.gdoc':
            msg = 'Gdoc ōppelαm mα Tαuder ιlαg αqtᾱμlινeu'
            stvl.stlαg = stlαgreu(msg, 0)
            return

        try:
            tαuder(tander_name, tanvars, tlanter, stanvor, tαg)
        except Exception as e:
            stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)

    stvl.clearall()
    sent.clear()
