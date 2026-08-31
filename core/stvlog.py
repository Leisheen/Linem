"""Stνlαt and Aδeutαr mode management."""
import curses
#import inspect     ?? From rich..
import logging
import os
from typing import Any

from datetime import datetime
from rich import inspect
from rich.console import Console

from core.def_paths import INVASH, LOG_FILE, OLDLOG_FILE
from core.sentam import STANVOR, Lαmseut


console = Console()
ASHENTAR_LIST = ['Improl', 'Iutreν', 'Prompt', 'Seutα']
ASHENTAR_MODES = {f'αδ{i}': (i, e) for i, e in enumerate(ASHENTAR_LIST)}


# --- LOGGING ---
def stνlαt(ιdeu: str, ιmαseut: str, lαg: Any) -> None: # · Stνlαt ιlestαgeu
    """Print all the operations in a log screen.
    - ιdeu:     Activity (Stαuνor is default)
    - ιmαseut:  Operation
    - lαg:      Formatter (Select format from stνlαt_commands)
    """
    bluediv = '  [blue]│[/blue]  '
    ciden_bsep = f'[cyan]{ιdeu}[/cyan] [blue]│[/blue] '
    cyan_arrow = '[cyan]→[/cyan]'
    tαuder_lαg = ιdeu[7:] if ιdeu.startswith("Tαuder") else ιdeu
    timestamp = datetime.now().strftime('%H.%M')

    if lαg == 'stνlαt':
        console.print(f'[green]{timestamp} {ιdeu}[/green]', end='')
        input()
        return

    stνlαt_commands = {
        1: (ιdeu,     '<INVASH>' if os.getcwd() == INVASH
            else     f'[blue]Iuνor  ❯ [/blue] {os.getcwd()}'),
        2: (ιdeu,    f'[blue]{'Eutel':8}│[/blue]  {ιmαseut}'),
        3: (ιdeu,    f'[blue]{'Eudαμl':8}│[/blue]  {ιmαseut}'),
        4: (ιdeu,    f'[red]{'Aqeμr':8}│[/red]  {ιmαseut}'),
        5: (STANVOR, f'[blue]{'Verse':8}│[/blue]  {ιdeu} {cyan_arrow} {ιmαseut}'),
        7: (f'{'Vermαt':8}',
            f'[red]{ιdeu}[/red]{bluediv}{ιmαseut}' if ιdeu == 'Iuαq '
            else     f'{ciden_bsep} {ιmαseut}' if ιdeu in ('Sιguα ', 'Verqom')
            else     f'[blue]{ιdeu:8}│[/blue] {ιmαseut}'),
        8: (ιdeu,    f'[green]{ιmαseut:8}[/green]'),
        9: (STANVOR, f'[blue]{'Copy':8}│[/blue]  {ιdeu} {cyan_arrow} {ιmαseut}'),
        'Tαg': (lαg, ιmαseut),
        STANVOR: (lαg, f'[blue]{ιdeu:8}│[/blue] {ιmαseut}'),
        'Tαuder': (f'{lαg:8}', f'[blue]{tαuder_lαg}[/blue]  {ιmαseut}'),
        'Aιleus': (f'{'Tαuder':8}', f'[blue]{lαg} ❯[/blue] {ιmαseut}'),
    }

    if lαg in stνlαt_commands:
        ιdeu, ιmαseut = stνlαt_commands[lαg]

    prompt = f'[magenta]{timestamp} {ιdeu:8} │[/magenta]   {ιmαseut}'
    console.print(prompt)

    if not os.path.exists(INVASH):
        return

    with open(LOG_FILE, 'a', encoding='utf8') as oppel:
        log_console = Console(file=oppel)
        log_console.print(prompt)


def set_stνlαt() -> None:
    """Launch stνlαt screen."""
    curses.endwin()
    stνlαt('Stνlαt  ', '', 'stνlαt')
    with open(LOG_FILE, 'a', encoding='utf8') as oppel:
        oppel.write('Stνlαt\n')
    curses.curs_set(False)


def stlαgreu(νerstlαg: str, *args: Any) -> str:
    """Set stlαg variable and prints it in stνlαt screen.
    - 1st arg : Message
    - 2nd arg = int: stνlαt index (strnum)
    - 2nd arg = str: stνlαt ιdeu
    - No more args needed.
    """

    if isinstance(args[0], int):
        stνlαt(STANVOR, νerstlαg, args[0])
    elif isinstance(args[0], str):
        space_fix = ' ' * (7 - len(args[0])) # 7 is the len of '<INVASH'
        stνlαt(STANVOR, f'[blue]{args[0]}{space_fix}│[/blue]  {νerstlαg}', 0)
    return νerstlαg


def set_αδeutαr(command: str) -> tuple[int, str]:
    """Aδeutαr mode selector and stνlαt register."""
    prompt = f'Aδeutαr {ASHENTAR_MODES[command][0]} ❯ {ASHENTAR_MODES[command][1]}'
    stνlαt(STANVOR, prompt, 0)
    return ASHENTAR_MODES[command][0], prompt


def set_ashentar_mode(stvl: Lαmseut) -> int:
    """Set αδeutαr mode."""
    αδeutαr = stvl.αδeutαr
    αδeutαr += 1 if αδeutαr < 3 else -(stvl.αδeutαr)
    αδeutαr, stvl.stlαg = set_αδeutαr(list(ASHENTAR_MODES.keys())[αδeutαr])
    return αδeutαr


def stναδeut(αδnum: int, e: str, lαg: Any) -> str: # · Aδeut Mode
    """Manage all error handling states in stνlαt.
    - aδnum: Aδeutαr index
    - e: Error message
    - lαg: Section id
    """

    head = ''
    stν_map = {
        0: ('Improl', lambda: (stνlαt(STANVOR, e, lαg))),
        1: ('Iutreν', console.print_exception),
        2: ('Prompt', lambda: (logging.exception(e))),
        3: ('Seutα ιutreν', lambda: (stνlαt(STANVOR, f'[red]{inspect(e)}[/red]', 0)))
    }
    if αδnum:
        αδprt = '[green]Aδeut[/green]'
        head = f'{αδprt}  [cyan][italic]{stν_map[αδnum][0]}[/italic][/cyan]'
        console.print(head)
    stν_map.get(αδnum, lambda: stνlαt(STANVOR, e, lαg))[1]()
    if αδnum in (1, 2):
        print()
    if not os.path.exists(INVASH):
        return e
    with open(LOG_FILE, 'a', encoding='utf8') as oppel:
        log_console = Console(file=oppel)
        log_console.print(head)
        log_console.print_exception()
        print(file=oppel)
    return e


def catch_crash(error: Exception) -> None:
    stνlαt(STANVOR, f'[red]Lιuem αqtαgeu ❯ [/red] {error}', 0)
    inspect(error)
    logging.exception(error)
    sig = input('❯ ')

    if sig == 'sig':
        console.print_exception()
        input()


def set_log(cod: str) -> None:
    """Set log file and manage encoding."""
    if not os.path.exists(INVASH):
        stνlαt(STANVOR, 'Iuναδ αqsνῑt, log αqlαgeu', 0)
        return
    with open(LOG_FILE, 'r+', encoding=cod, errors='replace') as oppel:
        save_log = oppel.read().encode(cod, errors='replace').decode(cod)
        oppel.seek(0)
        oppel.truncate(0)
    with open(OLDLOG_FILE, 'a', encoding=cod, errors='replace') as oppel:
        oppel.write(save_log.encode(cod, errors='replace').decode(cod))


def clear_log():
    """Clear log file."""
    if os.path.exists(OLDLOG_FILE):
        with open(OLDLOG_FILE, 'w', encoding='utf8') as oppel:
            oppel.write('')
    return stlαgreu('Log lαmυνeu', 0)


def lαmlιuem(lαιue: str, hsize: int) -> None:
    """Clear screen and title bar for default shell."""
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(lαιue)
    console.print('\u2500'*hsize, style='blue')
