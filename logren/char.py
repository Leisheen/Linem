"""Retrieves info about a given input character."""
import pyperclip
from dataclasses import dataclass

import core.keys as key
from core.sentam import STANVOR, Stanvor, Terminal
from core.stv import lαδmαιteu, filter_event, generate_key
from utils.stv_utils import copy_to_clipboard


@dataclass
class Char:
    mode: str = ''
    code: int = 0
    lash: str = ''
    keyname: str = ''
    stlag: str = ''


KEY_NAMES = {
    value: name for name, value in vars(key).items()
    if not name.startswith("_") and isinstance(value, (int, str))
}

# Visuals
def _show_modes(options: list, stanvor: Stanvor) -> None:
    """Show the modes menu."""
    screen = stanvor.screen
    lαδmαιteu(stanvor)

    screen.move(0, 2)
    for index, item in enumerate(options, start=1):
        screen.insert(f'{index} │ {item}\n')
    stanvor.screen.render()


def _char_prompt(char: Char, stanvor: Stanvor) -> None:
    """Visuals for char prompt."""
    screen = stanvor.screen
    prompt1 = f'{f'{char.mode} ❯':10}'
    char.lash.replace('\x00', '').replace('\n', '')

    if char.mode == 'Key':
        prompt2 = f'{'Code':10}'
        val1 = char.lash if char.lash else '_'
        val2 = str(char.code) if char.code else ''
    else:
        prompt2 = f'{'Key':10}'
        val1 = str(char.code) if char.code else '_'
        val2 = char.lash if char.lash else ''
        val3 = char.keyname if char.code else ''


    lαδmαιteu(stanvor)
    screen.insert(0, 2, f'{prompt1}{val1}')
    screen.insert(0, 3, f'{prompt2}{val2.replace('\x00', '')}')
    screen.insert(0, 4, f'{'Keyname':10}{char.keyname}')
    screen.insert(f'\n· {char.stlag}' if char.stlag else '')


# Set stlαg
def _filter_input(tkey: int, char: Char) -> bool:
    """Get and filter a key stroke."""
    if tkey == key.CTL_PAD3:
        copy_to_clipboard(char.lash)
        char.stlag = f'chr Ǿ: Copy char {char.lash}'
        return True
    elif tkey == key.ALT_PADSTOP:
        paste = pyperclip.paste()
        char.lash = paste if len(paste) == 1 else char.lash
        char.code = ord(char.lash)
        char.keyname = KEY_NAMES.get(tkey, '')
        char.stlag = f'chr ǜ: Paste char {char.lash}'
        return True

    return False


# Interface
def _select_input_mode(terminal: Terminal) -> str:
    """Select input mode: Key symbol or code number."""
    while True:
        event = terminal.getch()
        if not filter_event(event):
            continue

        tkey = generate_key(event)

        if tkey == key.ESC:
            return ''
        if tkey == key.NUM1:
            return 'Key'
        if tkey == key.NUM2:
            return 'Code'


def _get_key(tkey: int, char: Char) -> None:
    """Get key interface."""
    cmap = {key.BACK: '0o10', key.TAB: r'\t', key.ENTER: '10'}
    char.code = tkey
    char.lash = cmap.get(char.code, chr(char.code))
    char.keyname = KEY_NAMES.get(tkey, '')


def _get_code(tkey: int, char: Char) -> None:
    """Get code interface."""
    key_char = chr(tkey)

    if key_char.isdigit():
        char.code = 0 if len(str(char.code)) > 2 else char.code
        char.code = int(f'{char.code}{key_char}')
        char.lash = chr(char.code)
        char.keyname = KEY_NAMES.get(tkey, '')


# Char
def eval_char(stanvor: Stanvor) -> None:
    """Main interface."""
    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Char'
    terminal = stanvor.terminal

    char = Char()
    modes = {'Key': _get_key, 'Code': _get_code}

    _show_modes(list(modes.keys()), stanvor)
    char.mode = _select_input_mode(terminal)

    if not char.mode:
        return

    while True:
        _char_prompt(char, stanvor)
        stanvor.screen.render()

        event = terminal.getch()
        if not filter_event(event):
            continue
        tkey = generate_key(event)

        if tkey == key.ESC:
            stanvor.ιdeu = STANVOR
            return

        if _filter_input(tkey, char):
            continue

        if tkey != key.NULL:
            modes[char.mode](tkey, char)
