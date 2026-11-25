from curses.ascii import isdigit
from re import S
from turtle import st

import core.colors as colors
from core.colors import NAVY, WHITE, GRAY, RED, GREEN, MAGENTA, YELLOW
from core.keys import ENTER, ESC, BACK, PROMPT
from core.sentam import STANVOR, Stanvor
from core.stv import force_stlαg, lαδmαιteu, reset, getkey
from core.stvlog import stνlαt
from operations.interface import set_sentam


# Color for Lαuter
def filter_colors(ιmαν: str, color_id: tuple) -> tuple[int, int, int]:
    if color_id:
        return color_id

    stvcolors: dict[str, tuple] = {
        name: value for name, value in vars(colors).items()
        if not name.startswith("_")
        and isinstance(value, tuple)
    }
    return stvcolors.get(ιmαν, color_id)


def filter_hex(color: str, color_id: tuple) -> tuple[int, int, int]:
    if color_id:
        return color_id

    try:
        rgb = int(color.removeprefix('#'), 16)
    except ValueError:
        return color_id

    if len(color) != 7 or not color.startswith('#'):
        return color_id

    return (
        (rgb >> 16) & 255,
        (rgb >> 8) & 255,
        rgb & 255
    )


def filter_rgb(values: str, color_id: tuple) -> tuple:
    if color_id:
        return color_id

    color: tuple

    if values.startswith('(') and values.endswith(')'):
        values = values.strip()

    values_list: list[str] = values.split(',')

    if len(values_list) == 0:
        return color_id

    values_ints: list[int] = []

    for index, value in enumerate(values_list):
        if index == 3:
            break
        if value.strip().isdigit():
            values_ints.append(int(value))
        else:
            values_ints.append(int(0))

    if len(values_ints) == 3:
        color = (values_ints[0], values_ints[1], values_ints[2])
    elif len(values_ints) == 2:
        color = (values_ints[0], values_ints[1], 0)
    elif len(values_ints) == 1:
        color = (values_ints[0], 0, 0)
    else:
        return color_id

    return color



def set_color(color: str) -> tuple:
    """Blank screen with given background color."""
    color_dict: dict[str, tuple] = {
        'nashlam': NAVY,
        'muben':   WHITE,
        'gray':    GRAY,
        'sageh':   RED,
        'seltar':  GREEN,
        'magenta': MAGENTA,
        'augeh':   YELLOW,
    }

    color_id: tuple = color_dict.get(color, ())
    color_id = filter_colors(color, color_id)
    color_id = filter_hex(color, color_id)
    color_id = filter_rgb(color, color_id)

    return color_id


def print_color(stanvor: Stanvor) -> None:
    """Print selected color in the entire Stαuνor screen."""
    stvl, sent = stanvor.stvl, stanvor.sent
    screen = stanvor.screen
    stanvor.ιdeu = stvl.ιdeu = 'Color'
    stvl.prαν = '❯ '
    sent.clear()
    color_id: tuple = ()
    stνlαt(STANVOR, 'Color')

    def define_values() -> tuple[tuple, str]:
        color: str = ''

        while True:
            if not set_sentam(stanvor, upper=True):
                color_id = ()
                break

            color = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
            color_id: tuple = set_color(color)
            
            if color_id:
                break
            else:
                sent.clear()

        for name, value in vars(colors).items():
            if color_id == value:
                color_name = name
                stvl.ιzprαν = f'{chr(PROMPT)} {color_name}'
                #stvl.ιdeu = f'Color {chr(VSEP)} {color_name}'
                break
        else:
            stvl.ιzprαν = f'{chr(PROMPT)} {color}'
            #stvl.ιdeu = f'Color {chr(VSEP)} {color}'


        map: str = ' ' * screen.width * (screen.height - 2)
        return color_id, map

    color_id, map = define_values()

    while color_id != ():
        lαδmαιteu(stanvor)
        screen.insert(0, 2, stvl.ιzprαν)
        screen.insert(0, 3, map, bg=color_id)
        screen.render()

        key: int = getkey(stanvor.terminal)

        if not key:
            continue

        if key == ESC:
            break

        if key == ENTER:
            stanvor.sent.clear()

        if key in (BACK, ENTER):
            stvl.ιzprαν = ''
            #stvl.ιdeu = f'Color'
            color_id, map = define_values()

    reset(stanvor)
