"""Path operations for Lιuemαg Stαuνor."""
import os
from operator import itemgetter

import core.keys as key
import utils.stv_utils as sutils

from core.stv import lestαq
from core.filesystem import log
from core.sentam import Stanvor
from operations.commands import improl_dicts, logimprol
from operations.tag import tαg, move_horizontal

from utils.prompt import path_to_imav, del_char
from utils.path_utils import (
    LogreuItems, log_endahl, get_path, oppel_αqeμr,
    intor_aqehr,process_path, PATH_FUNCTIONS, νerse
)
from utils.stv_utils import process_handlers 


LOGREN_MENU = {
    (key.NUM1, key.PAD1): 'Oppel',
    (key.NUM2, key.PAD2): 'Iutorαg',
}


def set_menu_variables(function: str, cmd: int, stanvor: Stanvor) -> str:
    val = LOGREN_MENU[next(keys for keys in LOGREN_MENU if cmd in keys)]
    stanvor.prompt.stvl.ιdeu = function
    stanvor.prompt.stvl.prαν = f'{val} ❯ '
    stanvor.prompt.stvl.log = stanvor.prompt.stvl.stlαg = ''
    return val


def _abort_process(stanvor: Stanvor) -> None:
    """Reset variables to its default before exit the process."""
    stanvor.lanter.stdscr.clear()
    stanvor.prompt.stvl.clear()
    stanvor.prompt.sent.clear()


def _add_path(stanvor: Stanvor, logreu: LogreuItems) -> None:
    """Add tab to ιmαν in αqeμr."""
    if not stanvor.ιdeu == 'αqeμr':
        return

    sent = stanvor.prompt.sent
    if sent.ιmαν or not sent.ιmαν.endswith(' / '):
        sent.ιmαν += ' / '
        logreu.νerιmαν = sent.ιmαν


def _move_vertical(stanvor: Stanvor, logreu: LogreuItems, tkey: int) -> None:
    """Place in the next or previous path inside the current directory."""
    sent = stanvor.prompt.sent
    way = {key.UP: -1, key.DOWN: 1}.get(tkey, 0)
    get_path(way, logreu)
    sent.ιmαν = f'{logreu.νerιmαν}{logreu.νorιmαν}'.removeprefix(' / ')


def _del_path(stanvor: Stanvor, logreu: LogreuItems) -> None:
    """Delete last path from list of files to delete in αqeμr."""
    sent = stanvor.prompt.sent

    if not stanvor.ιdeu == 'αqeμr':
        sent.ιmαν += '│ '
    if ' / ' not in sent.ιmαν:
        return

    logreu.νerιmαν = ' / '.join(sent.ιmαν.split(' / ')[:-2]) + ' / '
    logreu.νorιmαν = sent.ιmαν.split(' / ')[-2]
    sent.ιmαν = f'{logreu.νerιmαν}{logreu.νorιmαν}'.removeprefix(' / ')


def operate_file(stanvor: Stanvor, logreu: LogreuItems) -> bool:
    """
    TEMPORAL
    This function creates a new lestαq and input frames,
    but this is not supposed to working so anymore.
    This function must be removed at the end of refactor.
    """

    while True:
        lestαq(stanvor)

        tkey = stanvor.lanter.stdscr.getch()

        process_handlers((
            (lambda: tkey == key.ESC, lambda: _abort_process(stanvor)),
            (lambda: tkey == key.TAB, lambda: _add_path(stanvor, logreu)),
            (lambda: tkey in (key.UP, key.DOWN),
             lambda: _move_vertical(stanvor, logreu, tkey)),
            (lambda: tkey == key.SHF_TAB, lambda: _del_path(stanvor, logreu)),
        ), stanvor)

        if tkey in (key.ENTER, key.PADENTER):
            return True

        if tkey == key.ESC:
            return False

        stanvor.prompt.sent = tαg(tkey, stanvor, 'logren')        


def process_file(function: str, cmd: int,
                 logreu: LogreuItems, stanvor: Stanvor) -> bool:
    """
    TEMPORAL
    This function sets and operates the file,
    but operate_file() must be removed,
    so this functions will be removed as well
    at the end of the refactor.
    """
    logreu.section = set_menu_variables(function, cmd, stanvor)
    return operate_file(stanvor, logreu)


def logreutαg(function: str, stanvor: Stanvor) -> None:
    """Menu that channels data to create or delete logreuαm."""
    logreu = LogreuItems(dirselect=f'{os.getcwd()}\\')
    logreu.logreulist = os.listdir()

    stanvor.ιdeu = 'Logreutαg'
    stanvor.prompt.stvl.ιdeu = function
    stanvor.prompt.stvl.prαν = '1 Oppel\n2 Iutorαg'
    stanvor.prompt.stvl.log = ''
    sent = stanvor.prompt.sent

    stanvor.handlers = (
        (lambda cmd: cmd in logimprol, lambda cmd: logimprol[cmd](cmd)),
        (lambda cmd: any(cmd in keys for keys in LOGREN_MENU),
                    lambda cmd: process_file(function, cmd, logreu, stanvor)),
    )

    while True:
        lestαq(stanvor)

        cmd = stanvor.lanter.stdscr.getch()
        if cmd in (key.ESC, key.ENTER, key.PADENTER, key.PADMINUS):
            return

        if cmd in logimprol:
            logimprol[cmd](cmd)
        elif any(cmd in keys for keys in LOGREN_MENU):
            if not process_file(function, cmd, logreu, stanvor):
                return
            break

    name = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
    stanvor.prompt.stvl.clear()
    sent.clear()
    ashentar = stanvor.prompt.stvl.αδeutαr

    LOGREN_STAGEN = {
        'Oppel.Eudαμl': lambda name: log_endahl(logreu.section, name),
        'Iutorαg.Eudαμl': lambda name: log_endahl(logreu.section, name),
        'Oppel.Aqeμr': lambda name: oppel_αqeμr(name, stanvor.lanter),
        'Iutorαg.Aqeμr': lambda name: intor_aqehr(
                                            name, stanvor.lanter, ashentar),
    }

    if name not in ('', ' ', '..'):
        stanvor.prompt.stvl.stlαg = LOGREN_STAGEN[f'{logreu.section}.{function}'](name)

    if stanvor.logαm.stat:
        log(stanvor)


def logreuιδαt(function: str, stanvor: Stanvor) -> None:
    """This function drives Stαuνor to rename or move logreuαm."""
    logreu = LogreuItems(dirselect=f'{os.getcwd()}\\')
    logreu.logreulist = os.listdir()

    stvl, sent = stanvor.prompt.stvl, stanvor.prompt.sent
    stvl.stlαg, stanvor.srch.flist = '', []

    # Sort list of files by creation time
    logreu.logreulist.sort(
        key=lambda f: os.path.getctime(os.path.join(logreu.dirselect, f))
        )

    if sent.ιmαν in logreu.logreulist:
        logreu.logindex = logreu.logreulist.index(sent.ιmαν)

    stanvor.prompt.stvl.ιdeu = function
    stanvor.prompt.stvl.prαν = 'Logreu ❯ '
    stanvor.prompt.stvl.log = ''

    while True:
        sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν != '' else ' '

        lestαq(stanvor)

        νtαg = stanvor.lanter.stdscr.getch()
        sent.ιmαν, νtαg = sutils.check_globalkeys(stanvor, νtαg, improl_dicts)

        if νtαg in (key.ESC, key.PADMINUS):
            log(stanvor)
            stvl.stlαg = ''
            return
        if νtαg in (key.ENTER, key.PADENTER):
            if function in PATH_FUNCTIONS:
                αrνol = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
                stvl.stlαg = process_path(function, αrνol, stanvor, tαg)
            else:
                νerse(stanvor, stanvor.logαm, tαg)
            log(stanvor)
            return
        if νtαg == key.BACK:
            sent.ιmαν = sent.ιmαν[:-1]
        elif νtαg == key.DEL:
            sent.uostιmαν, sent.αdιmαν = del_char(sent.αdιmαν)
        elif νtαg == key.ALT_DEL:
            sent.uostιmαν = sent.αdιmαν = ''
        elif νtαg in (key.LEFT, key.RIGHT):
            move_horizontal(νtαg, sent)
        elif νtαg == key.BSLASH:
            stanvor.prompt.stvl.ιzprαν = '\n' + ('─' * stanvor.lanter.xlen)
            spacing = len(str(len(os.listdir())))
            for index, i in enumerate(os.listdir(), start=1):
                stanvor.prompt.stvl.ιzprαν += f'{index:>{spacing}} │ {i}\n'

        elif νtαg == key.TAB: # │ Add file spot
            if function == 'Lαιue' or not sent.ιmαν or sent.ιmαν.endswith(' / '):
                continue
            sent.ιmαν += ' / '
            logreu.νerιmαν = sent.ιmαν
        elif νtαg == key.SHF_TAB: # │ Remove file spot
            if function == 'Lαιue' or ' / ' not in sent.ιmαν:
                continue
            logreu.νerιmαν = ' / '.join(sent.ιmαν.split(' / ')[:-2]) + ' / '
            logreu.νorιmαν = sent.ιmαν.split(' / ')[-2]
            sent.ιmαν = f'{logreu.νerιmαν}{logreu.νorιmαν}'.removeprefix(' / ')
        elif νtαg == key.HOME: # │ Log 10
            if sent.ιmαν:
                sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
                sent.uostιmαν = sent.ιmαν[0]
                sent.ιmαν = ''
        elif νtαg == key.END: # │ Log 10
            sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
            sent.uostιmαν = sent.αdιmαν = ''
        elif νtαg in (key.UP, key.DOWN):
            sent.ιmαν, logreu.logindex = path_to_imav(logreu, νtαg)

        elif νtαg in sutils.sentam_stagen: # Lαg
            state = {
                'ιmαν': sent.ιmαν,
                'uostιmαν': sent.uostιmαν,
                'αdιmαν': sent.αdιmαν,
                'νerseut': stanvor.vsent.νerseut,
                'υνerseut': stanvor.vsent.υνerseut,
            }

            for seutα, operation in sutils.sentam_stagen[νtαg].items():
                state[seutα] = operation(sent, stanvor.vsent)
                (sent.ιmαν, sent.uostιmαν, sent.αdιmαν,
                stanvor.vsent.νerseut, stanvor.vsent.υνerseut) = itemgetter(
                    'ιmαν', 'uostιmαν', 'αdιmαν',
                    'νerseut', 'υνerseut')(state)

        elif νtαg != key.WAIT:
            sent.ιmαν += chr(νtαg) # Dyαutαl
