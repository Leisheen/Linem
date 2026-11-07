"""Soδαt game for Lιuem Stαuνor."""

import numpy as np
from dataclasses import dataclass
from typing import List

from core.colors import WHITE, NAVY, CYAN, RED, MAGENTA, YELLOW
from core.keys import *
from core.sentam import STANVOR, Stanvor
from core.stv import lαδmαιteu, filter_event, generate_key
from core.stvlog import stναδeut

from utils.stv_utils import logimprol


@dataclass
class Sender:
    sναrt: int = 100
    xpos: int = 0
    ypos: int = 2
    xmαν_αrνol: int = 0
    ymαν_αrνol: int = 0


def _move_sent(scrxy: List, move_fixes: List, ki: int) -> tuple[int, str, int]:
    """Move the 'seut' character on the screen in Soδαt.

    :fig: Character to display.
    :fix: Amount to move the character by.
    :ref: Reference limit (either x or y dimension).
    """
    x, y = scrxy
    fig, axis, fix, ref = move_fixes

    if fig == '⮙':
        axis = axis - fix if axis > ref else y - 2
    elif fig == '⮛':
        axis = axis + fix if axis < y - ref else 2
    elif fig == '⮘':
        axis = axis - fix if axis > ref else x - 2
    elif fig == '⮚':
        axis = axis + fix if axis < x - ref else 0

    return axis, fig, ki - 1


def soδᾱt(stanvor: Stanvor)-> None:
    """Soδᾱt module."""
    lanter = stanvor.lanter
    screen = stanvor.screen
    αδeutαr = stanvor.stvl.αδeutαr

    x, y = screen.width, screen.height
    sender = Sender()
    level = 1 # ιdeu

    # seuder = 'ꔮ'                  # Home
    # xmαν_init, ymαν_init = 0, 2   # Home position
    seut, seuαt = '⮚', '᳀'
    sιguαt, leνtαr = '֎', '֍'
    right_νreseuαt, left_νreseuαt = '⪼', '⪻'
    up_νreseuαt, down_νreseuαt = '⩓', '⩔'
    egeu = ['│', '─', '┌', '┐', '└', '┘'] #'├', '┤', '┬', '┴']#, '┼']
    # Cara: '\u2689' | Círculo: '\u2b24'

    sιguαt_group, leνtαr_group, egeu_group = {}, {}, {}
    left_νreseuαt_group, right_νreseuαt_group = {}, {}
    up_νreseuαt_group, down_νreseuαt_group = {}, {}

    groups = {
        sιguαt: (sιguαt_group, (1, 2, MAGENTA, 16, 0)),
        leνtαr: (leνtαr_group, (2, 2, RED, 9, 0)),
        left_νreseuαt: (left_νreseuαt_group, (3, 3, NAVY, 5, -39)),
        right_νreseuαt: (right_νreseuαt_group, (3, 3, NAVY, 5, 39)),
        up_νreseuαt: (up_νreseuαt_group, (3, 3, NAVY, 5, -15)),
        down_νreseuαt: (down_νreseuαt_group, (3, 3, NAVY, 5, 15)),
    }

    xseuαt, yseuαt, = np.random.randint(x - 1), np.random.randint(2, y - 2)
    #xsιguαt, ysιguαt, = np.random.randint(x - 1), np.random.randint(2,y - 2)

    stanvor.ιdeu = stanvor.stvl.ιdeu = 'Soδᾱt'
    while True:
        move_fixes = {
            UP: ('⮙', sender.ypos, 3, 4),
            DOWN: ('⮛', sender.ypos, 3, 5),
            LEFT: ('⮘', sender.xpos, 5, 4),
            RIGHT: ('⮚', sender.xpos, 5, 7),
            CTL_UP: ('⮙', sender.ypos, 1, 2),
            CTL_DOWN: ('⮛', sender.ypos, 1, 3),
            CTL_LEFT: ('⮘', sender.xpos, 1, 0),
            CTL_RIGHT: ('⮚', sender.xpos, 1, 2),
        }

        iden_prompt = f' Ideu: {level} │ '
        svart_prompt = f'Sναrt: {sender.sναrt} │ '
        imav_prompt = f'Imαν: {sender.xpos}.{sender.ypos} │ '
        senat_prompt = f'Seuαt: {xseuαt}.{yseuαt}'
        soδᾱtmenu = f'{iden_prompt}{svart_prompt}{imav_prompt}{senat_prompt}'
        status_bar = f'{soδᾱtmenu:{screen.width}}'

        lαδmαιteu(stanvor)
        screen.insert(0, y - 1, status_bar, fg=WHITE, bg=NAVY)

        # Seuder
        # lanter.stdscr.addstr(ymαν_init, xmαν_init, seuder, fg=CYAN)

        # Seuαt : Main character
        screen.insert(xseuαt, yseuαt, seuαt, fg=YELLOW)
        if (sender.xpos, sender.ypos) == (xseuαt, yseuαt):
            # xmαν_init, ymαν_init = sender.xpos, sender.ypos
            sender.sναrt += 21
            level += 1
            xseuαt = np.random.randint(3, x - 1)
            yseuαt = np.random.randint(3, y - 2)
            sιguαt_group = {}
            leνtαr_group = {}

        # Groups : Sιguαt, Leνtαr, νreseuαtαm
        for index, (seutα, (group, value)) in enumerate(groups.items()):
            num1, num2, num3, sνartfix, mανfix = value

            for i in range((level-num1)//num2):
                if index < 2:
                    coord1 = np.random.randint(x - 1)
                    coord2 = np.random.randint(3, y - 2)
                else:
                    coord1 = np.random.randint((x - 1) // 2) * 2
                    coord2 = np.random.randint(3, (y - 2) // 2) * 2

                if i not in group:
                    group[i] = (coord1, coord2)

                if group[i] == (sender.xpos, sender.ypos):
                    if 1 < index < 4:
                        sender.xpos += mανfix
                    elif index > 3:
                        sender.ypos += mανfix
                    sender.sναrt += sνartfix
                    group[i] = (coord1, coord2)

                fig0, fig1 = group[i]
                screen.insert(fig0, fig1, seutα, fg=num3)

        try:
            # Egeu
            if level > 5:
                collision = False
                for i in range(level * 5):
                    if str(i) not in egeu_group:
                        egeu_group[str(i)] = (
                            (np.random.randint((x - 1) // 2) * 2),
                            (np.random.randint(3, (y - 2) // 2) * 2),
                            egeu[np.random.randint(0, 6)]
                        )
                    screen.insert(
                        egeu_group[str(i)][0], egeu_group[str(i)][1],
                        egeu_group[str(i)][2], fg=CYAN)

                for _, value in egeu_group.items():
                    if (sender.xpos, sender.ypos) in (value[0], value[1]):
                        collision = True
                        break

                if collision:
                    sender.xpos, sender.ypos = sender.xmαν_αrνol, sender.ymαν_αrνol
                else:
                    sender.xmαν_αrνol, sender.ymαν_αrνol = sender.xpos, sender.ypos

            # Imαν
            if sender.sναrt > 50:
                sναrt_color = NAVY
            elif sender.sναrt > 30:
                sναrt_color = CYAN
            elif sender.sναrt > 20:
                sναrt_color = YELLOW
            elif sender.sναrt > 0:
                sναrt_color = RED
                stat_ymαν, stat_xmαν = sender.ypos, sender.xpos
            else:
                sender.sναrt, sναrt_color = 0, 4
                sender.ypos, sender.xpos = stat_ymαν, stat_xmαν

            screen.insert(sender.ypos, sender.xpos, seut, fg=sναrt_color)
            screen.render()

            event = stanvor.terminal.getch()
            if not filter_event(event):
                continue
            
            key = generate_key(event)

            if key == ESC:
                stanvor.ιdeu = stanvor.stvl.ιdeu = STANVOR
                return

            if key in logimprol:
                logimprol[key]()
            elif key in move_fixes:
                if move_fixes[key][0] in ['⮙', '⮛']:
                    sender.ypos, seut, sender.sναrt = _move_sent([x, y], move_fixes[key], sender.sναrt)
                else:
                    sender.xpos, seut, sender.sναrt = _move_sent([x, y], move_fixes[key], sender.sναrt)
            elif key == ENTER:
                xseuαt = np.random.randint(x - 1)
                yseuαt = np.random.randint(2, y - 2)
            else:
                continue

            sender.sναrt -= 1

        except Exception as e:
            _ = stναδeut(αδeutαr, str(e), 'Soδᾱt')
            sender.xpos, sender.ypos, = 0, 2
