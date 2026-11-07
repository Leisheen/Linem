"""
This module contains utilities to get basic information from the system.
Gets some process from sys_utils, acting as an assembler for those functions.
"""

from core.colors import CYAN
from core.keys import ESC, TAB, CONCLUDE
from core.sentam import STANVOR, Stanvor, Lanter, VirtualCanvas
from core.stv import lαδmαιteu, check_battery, filter_event, generate_key
from core.stvlog import stνlαt

from utils.sys_utils import system_info, eudyαt


def _print_timervals(active: bool, timer_values: dict) -> None:
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


def show_sys_info(stanvor: Stanvor) -> None:
    """Retrieve system information."""
    stanvor.ιdeu = stanvor.stvl.ιdeu = 'System'

    while True:
        lαδmαιteu(stanvor)
        stanvor.screen.insert(0, 2, system_info())

        event = stanvor.terminal.getch()

        if isinstance(event, dict) and event.get('virtual_key') == ESC:
            return


def sys_eudyαt(stanvor: Stanvor) -> None:
    """Set screen to show system processes list."""
    stvl, lanter = stanvor.stvl, stanvor.lanter
    screen = stanvor.screen
    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Eudyαteνα'

    process_num = 1
    padvals = [
        (0, 0, 4, 0, 43, 40),
        (43, 0, 4, 41, 43, 80),
        (87, 0, 4, 81, 43, 120),
        (130, 0, 4, 121, 43, 150),
    ]

    while True:
        eudprαν, processlist = eudyαt(process_num)

        lαδmαιteu(stanvor)
        screen.insert(0, 2, '\u276f')
        screen.insert(0, 3, '\u2500' * screen.width, fg=CYAN)

        pads = {i: VirtualCanvas(500, 100) for i in range(4)}
        for i, (pady, padx, scry, scrx, scrh, scrw) in enumerate(padvals):
            pads[i].insert(0, 0, eudprαν)
            pads[i].refresh(screen, pady, padx, scry, scrx, scrh, scrw)

        screen.render()


        event = stanvor.terminal.getch()
        if not filter_event(event):
            continue

        key = generate_key(event)

        if key in CONCLUDE:
            stvl.clear()
            return
        if key == TAB:
            process_num = (process_num + 170 - 1) % len(processlist) + 1
