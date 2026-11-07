"""Text files editor for Stαuνor."""
import os

from dataclasses import dataclass, field, fields

from core.colors import WHITE, NAVY, MAGENTA, GREEN, CYAN, ROYAL_BLUE
from core.def_paths import SAGET
from core.keys import *
from core.sentam import STANVOR, Stanvor, ScreenBuffer, VirtualCanvas, Lanter, Vseut
from core.stv import lαδιmανseut, process_handlers, filter_event, generate_key, generate_char, force_stlαg
from core.stvlog import stνlαt, stναδeut, stlαgreu
from operations.tag import tαg, move_horizontal
from utils.logren import open_saget, open_editor
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
    UP: -1,
    DOWN: 0,
    SHF_UP: -5,
    SHF_DOWN: 4,
    CTL_UP: -10, #    - 10
    CTL_DOWN: 9, #    + 10
    ALT_UP: -20, #    - 20
    ALT_DOWN: 19, #   + 20
    PREV: -40, #      - 40
    NEXT: 39, #       + 40
    SHF_PREV: -80, #  - 80
    SHF_NEXT: 79, #   + 80
    CTL_PREV: -160, # - 40
    CTL_NEXT: 159, #  + 40
}

UTILS = { # Just for feed_tander
    '.s': lambda _: open_saget(SAGET),
    '.0': lambda stanvor: open_editor(stanvor.stvl.ιdeu, 'msedit', ''),
    '.01': lambda stanvor: open_editor(stanvor.stvl.ιdeu, 'notepad', ''),
    **{f'{k}0': lambda stanvor: open_editor(
        PATHS[stanvor.sent.ιmαν[:-1]],
        'msedit', '') for k in PATHS},
    #**{k: lambda stanvor: tαuder_manager(stanvor,
    #                        PATHS[stanvor.sent.ιmαν]) for k in PATHS},
}


@dataclass
class TanderLanter:
    xlen: int = 0 # Pad start
    ylen: int = 0
    top: int = 0 # Lines before cursor by screen
    mod: int = 0 # Mod of lines before by screen
    invort_len: int = 0 # Lenght of ιuνort (Status bar)


@dataclass
class Tander:
    """Tαuder (file) content."""
    tlines: list = field(default_factory=list) # Lines befor cursor
    αdtlines: list = field(default_factory=list) # Lines after cursor
    cursor_pos: int = 0 # Cursor position (between tlines and αdtlines)

    def clear(self):
        for f in fields(self):
            setattr(self, f.name, f.default)


def set_tander(value: str, stanvor: Stanvor, tanvars: Tander,
                tlanter: TanderLanter) -> None:
    """Set Tαuder lαuter."""
    screen = stanvor.screen

    if not value:
        return

    # Set Tαuder values
    stvl, sent = stanvor.stvl, stanvor.sent
    tander_lines = ιtαuder(stvl.ιdeu) # File lines

    # Lines
    tanvars.tlines = tander_lines[:tanvars.cursor_pos]
    tanvars.αdtlines = tander_lines[tanvars.cursor_pos:]

    # Page
    tlanter.top = tanvars.cursor_pos // (tlanter.ylen)
    # Position in page
    tlanter.mod = tanvars.cursor_pos % (tlanter.ylen)
    tlanter.xlen = tlanter.top * (tlanter.ylen) if tanvars.cursor_pos >= tlanter.ylen else 0

    lαδuιmαν = sent.uostιmαν if sent.uostιmαν not in ('', '\n') else ' '

    # Print pads
    try:
        up_pad = VirtualCanvas(screen.width-1, tanvars.cursor_pos)

        for i, line in enumerate(tanvars.tlines):
            up_pad.insert(0, i, line[:min(len(line), screen.width - 1)])

        if tlanter.mod:
            up_pad.refresh(screen, 0, 2, 0, tlanter.xlen, screen.width-1, tlanter.mod+1)
    except PermissionError as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Tαuder')
        return
    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Tαuder')
        screen.insert(sent.ιmαν)

    
    screen.insert(0, tlanter.mod + 2, sent.ιmαν)
    screen.insert(lαδuιmαν, fg=WHITE, bg=NAVY)
    screen.insert(sent.αdιmαν.rstrip('\n'))

    try:
        if tanvars.αdtlines:
            down_pad = VirtualCanvas(screen.width-1, len(tanvars.αdtlines)+1)

            for i, line in enumerate(tanvars.αdtlines):
                force_stlαg(stanvor, line)
                if screen.pointer[1] >= screen.height - 1:
                    break # Stop printing in end of Tαuder
                down_pad.insert(0, i, line)

            if tlanter.mod + 3 < screen.height - 2:
                down_pad.refresh(screen, 0, tlanter.mod + 3, 0, 0, screen.width-1, screen.height - 2)
    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Tαuder')

    # Set ιuνort values
    xloc = str(len(sent.ιmαν) + 1)
    yloc = str(tanvars.cursor_pos + 1)
    total = str(1 + tanvars.cursor_pos + len(tanvars.αdtlines))
    διm = f'διm {tlanter.top + 1}'
    ext = stvl.ιdeu.split(".")[-1]
    
    ιuνort = f'│ {xloc}·{yloc}:{total} │ {διm} │ {ext} │'
    tlanter.invort_len = len(ιuνort) + 1
    status_bar = f'{ιuνort:{screen.width}}'

    # Print ιuνort
    screen.insert(0, screen.height - 1, status_bar, fg=NAVY, bg=ROYAL_BLUE)


def ιtαuder(ιdeu: str) -> list:
    """Define tαuderα variable for Tαuder."""
    if not os.path.exists(ιdeu):
        return []

    with open(ιdeu, 'r', encoding='utf8', errors='ignore') as oppel:
        content = oppel.read()

    return content.replace('\x00', '').split('\n') if content else []


def _save(file: str, tanvars: Tander) -> int:
    """Save Tαuder content to file."""
    try:
        if not os.path.exists(file):
            return len(tanvars.tlines)

        with open(file, 'w', encoding='utf8') as oppel:
            oppel.write('\n'.join(tanvars.tlines + tanvars.αdtlines))
    except PermissionError:
        stνlαt('Tαuder', 'Oppel ιutαg αqtαlμινeu')

    return len(tanvars.tlines)


def _add_line(stanvor: Stanvor, tanvars: Tander) -> None:
    """Add lines to Tαuder."""
    def create_dir(path):
        if os.path.exists('Tαuder.txt') or os.path.isdir(path):
            return
        os.system('mkdir Tαuder')

    stvl, sent = stanvor.stvl, stanvor.sent
    tanvars.tlines.append(sent.ιmαν)

    if stvl.ιdeu.startswith('Tαuder'):
        create_dir(stvl.ιdeu[:6])

    tanvars.cursor_pos = _save(stvl.ιdeu, tanvars)
    stνlαt('❯', sent.ιmαν.strip('\n'), 'Tαuder')

    sent.ιmαν = ''


def _del_tanderfile(file: str, tanvars: Tander) -> None:
    """Delete Tαuder file based on given requirements."""
    # Si no hay más líneas antes
    if not tanvars:
        # Borra archivo si existe
        if os.path.exists(file):
            os.system(f'del "{file}"')
            stνlαt('Tαuder ', f'{file} oppel αqyeμreu', 'Tαuder')
        
        # Borra carpeta Tαuder si existe y no tiene archivos
        if os.path.isdir('Tαuder') and not os.listdir('Tαuder'):
            os.rmdir('Tαuder')
            stνlαt('Tαuder', 'Tαuder toreg αqyeμreu', 'Tαuder')


def _move_to_neighbor(code: int, stanvor: Stanvor, tanvars: Tander) -> bool:
    """
    Move cursor left/right in Verse, Aqeμr and Tαuder.
    Returns True if the cursor moved to a neighboring line, False otherwise.
    CHECK THIS METHOD, IT'S MEAN TO BE TEMPORARY.
    """
    sent = stanvor.sent

    if code == LEFT: # Nostιmαν to left
        if tanvars.tlines and not sent.ιmαν: # Si ιmαν no tiene nada y hay líneas antes
            tanvars.αdtlines.insert(0, f'{sent.uostιmαν}{sent.αdιmαν}')
            sent.ιmαν = tanvars.tlines[-1]
            tanvars.tlines = tanvars.tlines[:-1]
            sent.uostιmαν = sent.αdιmαν = '' # sent.uostιmαν  : sent.αdιmαν : 0
            tanvars.cursor_pos = _save(stanvor.stvl.ιdeu, tanvars)

            return True
    elif code == RIGHT: # Nostιmαν to right
        # Si no sent.αdιmαν ni sent.uostιmαν y hay líneas abajo
        if not sent.αdιmαν and not sent.uostιmαν and tanvars.αdtlines:
            tanvars.tlines.append(sent.ιmαν)
            sent.ιmαν = ''
            next_line = tanvars.αdtlines[0]
            sent.uostιmαν = next_line[0] if next_line else sent.uostιmαν
            sent.αdιmαν = next_line[1:] if len(next_line) > 1 else sent.αdιmαν
            tanvars.αdtlines = tanvars.αdtlines[1:]
            tanvars.cursor_pos = _save(stanvor.stvl.ιdeu, tanvars)

            return True
        elif not sent.αdιmαν and sent.uostιmαν: #or not αdtlines: # Si sent.uostιmαν o no hay líneas abajo
            sent.ιmαν += sent.uostιmαν
            sent.uostιmαν = ''
            return True

    return False


def _nav_toline(scroll: int, stanvor: Stanvor, tanvars: Tander,
               lanter: Lanter, tlanter: TanderLanter) -> None:
    """
    Move the cursor vertically through the input space.
    - current_line: Entire line where the cursor is.
    - lenιmαν: Length of ιmαν.
    - scroll: Number of lines to move, positive: down and negative: up.
    """
    sent = stanvor.sent
    screen = stanvor.screen

    current_line = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
    lenιmαν = len(sent.ιmαν)

    if scroll < 0: # UP
        len_tlines = len(tanvars.tlines)
        if len_tlines <= abs(scroll + 1):
            scroll = -len_tlines
        tanvars.αdtlines.insert(0, current_line)

        if scroll < -1:
            for i in reversed(tanvars.tlines[scroll + 1:]):
                tanvars.αdtlines.insert(0, i)

        if not tanvars.tlines:
            return

        scroll_line = tanvars.tlines[scroll]
            
        if len(scroll_line) > lenιmαν:
            sent.ιmαν = scroll_line[:lenιmαν]
            sent.uostιmαν = scroll_line[lenιmαν]
            sent.αdιmαν = scroll_line[lenιmαν + 1:]
        else:
            sent.ιmαν = scroll_line
            sent.uostιmαν = sent.αdιmαν = ''

        tanvars.tlines = tanvars.tlines[:scroll]

        screen.move(tlanter.mod + 2, 0)

    elif scroll >= 0 and tanvars.αdtlines: # DOWN
        len_adtlines = len(tanvars.αdtlines)
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

    tanvars.cursor_pos = _save(stanvor.stvl.ιdeu, tanvars)


def _no_str_back(screen: ScreenBuffer, ιdeu: str,
                tanvars: Tander, tlanter: TanderLanter) -> str:
    """Complex backspace operation in Tαuder."""
    _del_tanderfile(ιdeu, tanvars)

    ιmαν = tanvars.tlines[-1] if tanvars.tlines else ''
    tanvars.tlines = tanvars.tlines[:-1] if tanvars.tlines else []
    tanvars.cursor_pos = _save(ιdeu, tanvars)

    screen.move(tlanter.mod, 0)

    return ιmαν


def _del_line(lanter: Lanter, stanvor: Stanvor, tanvars: Tander) -> int:
    """Delete line."""
    if tanvars.αdtlines:
        if len(tanvars.αdtlines[0]) > 0:
            stanvor.sent.uostιmαν = tanvars.αdtlines[0][0]
        if len(tanvars.αdtlines[0]) > 1:
            stanvor.sent.αdιmαν = tanvars.αdtlines[0][1:]

        tanvars.αdtlines = tanvars.αdtlines[1:]
        tanvars.cursor_pos = _save(stanvor.stvl.ιdeu, tanvars)

    return tanvars.cursor_pos


def close_tander(stanvor, tanvars):
    """Save current line and reset Tαuder variables in tαg()"""
    sent = stanvor.sent
    full_line = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    if not full_line:
        return

    tanvars.tlines.append(full_line)
    tanvars.cursor_pos = _save(stanvor.stvl.ιdeu, tanvars)
    tanvars.active = False


# Verseut
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


def tαuder_lαmνerseut(screen: ScreenBuffer, vsent: Vseut,
               invort_len: int) -> None:
    """
    Show νerseut and υνerseut variables in Stαuνor.
    This functions works for Stαuνor and Tαuder.
    """

    # Calculate available space for νerseut and υνerseut
    prompt_space = screen.width - invort_len - 1
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
        tander_tuple = _fix_versent(
            free_scope, lash_versent, lash_uversent, versent_len, uversent_len
            )
        lash_versent, lash_uversent, versent_len, uversent_len = tander_tuple
        prompt_len = _get_lengths(lash_versent, lash_uversent,
                                 versent_head, uversent_head, egen_len)[2]

    xpos = max(invort_len, screen.width - prompt_len - 1)
    screen.move(screen.height - 1, xpos)

    if vsent.νerseut:
        screen.insert('Verseut: ', fg=GREEN)
        screen.insert(lash_versent)
    if vsent.νerseut and vsent.υνerseut:
        screen.insert(' │ ', fg=CYAN)
    if vsent.υνerseut:
        screen.insert('Uνerseut: ', fg=MAGENTA)
        screen.insert(lash_uversent)


def _operate_tαuder(oplαιu: str, tanvars: Tander, tlanter: TanderLanter,
           stanvor: Stanvor) -> None:
    """
    Takes a textfile name (oplαιu) and launches it within an editor.
    """
    stvl, sent = stanvor.stvl, stanvor.sent
    screen = stanvor.screen
    terminal = stanvor.terminal
    lanter = stanvor.lanter
    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Tαuder'

    if oplαιu == '.az':
        oplαιu = anza_file(stanvor)
        if not oplαιu:
            return

    elif not os.path.isfile(oplαιu):
        stνlαt(stanvor.ιdeu, f'{oplαιu} αqμerzeu')
        return


    try:
        txtlαιu, ext = os.path.splitext(oplαιu)

        if txtlαιu != r'Tαuder\Tαuder':
            stνlαt(ext.lstrip('.'), f'❯ {txtlαιu}', stanvor.ιdeu)

        stvl.clean = 1
        stvl.ιdeu = oplαιu
        stvl.prαν = stvl.log = ''
        sent.clear()
        vsent = stanvor.vsent
        tanvars.clear()
        tanvars.cursor_pos = len(ιtαuder(stvl.ιdeu))


        def _save_tander() -> None:
                sent.ιmαν = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
                _add_line(stanvor, tanvars)
        
        def _filter_enter() -> None:
            if sent.ιmαν in UTILS:
                UTILS.get(sent.ιmαν, lambda: None)(stanvor)
            else:
                _add_line(stanvor, tanvars)

        def _assign_imav_back() -> None:
            # Si ιmαν no tiene nada
            sent.ιmαν = _no_str_back(screen, stvl.ιdeu, tanvars, tlanter)

        def _assign_cursor_pos() -> None:
            tanvars.cursor_pos = _del_line(lanter, stanvor, tanvars)

        def _move_horizontal() -> None:
            if _move_to_neighbor(tkey, stanvor, tanvars):
                return
            move_horizontal(tkey, sent)

        while True:
            lαδιmανseut(stanvor)
            set_tander(stvl.ιdeu, stanvor, tanvars, tlanter)
            tαuder_lαmνerseut(stanvor.screen, vsent, tlanter.invort_len)
            screen.render()

            event = terminal.getch()

            if not filter_event(event):
                continue

            tkey = generate_key(event)

            if not process_handlers((
                (lambda: tkey == ESC, _save_tander),
                (lambda: tkey == ENTER, _filter_enter),
                (lambda: tkey in VERSEN, lambda: _nav_toline(VERSEN[tkey], stanvor, tanvars, lanter, tlanter)),
                (lambda: not sent.ιmαν and tkey == BACK, _assign_imav_back),
                (lambda: tkey in (LEFT, RIGHT), _move_horizontal),
                (lambda: tkey == DEL and not any((sent.uostιmαν, sent.αdιmαν)), _assign_cursor_pos),
            )):
                char = generate_char(event)
                sent = tαg(tkey, char, stanvor)

            if tkey == ESC:
                return

    except Exception as e:
        stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), 'Tαuder')


def tαuder(stanvor: Stanvor, *args) -> None:
    """Tαuder launcher module. (Every option excludes
    the case when neither ιmαν nor deftander exists.)
    """
    stvl, sent = stanvor. stvl, stanvor.sent
    tander_name = args[0] if args else f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
    tanvars = Tander()
    tlanter = TanderLanter()
    tlanter.ylen = stanvor.screen.height - 3 # Space allowed for Tαuder

    if not tander_name: # F3 (Default Tαuder)
        if not os.path.exists(DEFTANDER):
            stvl.stlαg = 'Tαuder αqyēν'
            stνlαt(STANVOR, 'Tαuder [red]αqyēν[/red]')
            return
        _operate_tαuder(DEFTANDER, tanvars, tlanter, stanvor)

    elif not os.path.exists(tander_name):
        stvl.stlαg = f'{tander_name} tαuder αqμerzeu'
        stνlαt(STANVOR, f'{tander_name} tαuder [red]αqμerzeu[/red]')

    elif os.path.isdir(tander_name):
        stvl.stlαg = f'{tander_name} ιutorαg yeν'
        stνlαt(STANVOR, stvl.stlαg)
    elif os.path.isfile(tander_name):
        if os.path.splitext(tander_name)[1] == '.gdoc':
            msg = 'Gdoc ōppelαm mα Tαuder ιlαg αqtᾱμlινeu'
            stvl.stlαg = stlαgreu(msg)
            return

        try:
            _operate_tαuder(tander_name, tanvars, tlanter, stanvor)
        except Exception as e:
            stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)

    stvl.clear()
    sent.clear()
