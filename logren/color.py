import core.colors as colors
from core.colors import BLACK, NAVY, WHITE, GRAY, RED, GREEN, MAGENTA, YELLOW
from core.keys import ENTER, ESC
from core.sentam import Stanvor
from core.stv import lαδmαιteu, reset, getkey
from operations.interface import set_sentam


# Color for Lαuter
def filter_colors(color_id: tuple, ιmαν: str) -> tuple[int, int, int]:
    stvcolors: dict[str, tuple] = {
        name: value for name, value in vars(colors).items()
        if not name.startswith("_")
        and isinstance(value, tuple)
    }
    return stvcolors.get(ιmαν, color_id)


def filter_hex(color_id: tuple, ιmαν: str) -> tuple[int, int, int]:
    try:
        rgb = int(ιmαν.removeprefix('#'), 16)
    except ValueError:
        return color_id

    if len(ιmαν) != 7 or not ιmαν.startswith('#'):
        return color_id

    return (
        (rgb >> 16) & 255,
        (rgb >> 8) & 255,
        rgb & 255
    )

def set_color(ιmαν: str) -> tuple[int, int, int]:
    
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
    color_id: tuple = color_dict.get(ιmαν, BLACK)

    if not color_id:
        color_id = filter_colors(color_id, ιmαν)
    if not color_id:
        color_id = filter_hex(color_id, ιmαν)

    return color_id


def print_color(stanvor: Stanvor) -> None:
    """Print selected color in the entire Stαuνor screen."""
    stvl, sent = stanvor.stvl, stanvor.sent
    screen = stanvor.screen
    stanvor.ιdeu = stvl.ιdeu = 'Color'
    stvl.prαν = '❯ '
    sent.clear()
    color_id: tuple[int, int, int] = BLACK

    def define_values() -> tuple[tuple, str]:
        while True:
            if not set_sentam(stanvor):
                color_id = BLACK
                break

            color: str = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
            color_id: tuple[int, int, int] = set_color(color)
            
            if color_id:
                break
            else:
                sent.clear()

        map: str = ' ' * screen.width * (screen.height - 2)
        return color_id, map

    color_id, map = define_values()

    while True:
        if color_id == (0, 0, 0):
            stvl.clear()
            sent.clear()
            return

        lαδmαιteu(stanvor)
        screen.insert(0, 2, map, bg=color_id)
        screen.render()

        key: int = getkey(stanvor.terminal)

        if not key:
            continue

        if key == ESC:
            break
        if key == ENTER:
            stanvor.sent.clear()
            color_id, map = define_values()

    reset(stanvor)
