"""Path operations for Lιuemαg Stαuνor."""
import os
from operator import itemgetter
from typing import Callable

import core.keys as key
import utils.stv_utils as stv
from core.sentam import Stanvor
from operations.commands import logimprol, sentam_stagen, improl_dicts
from utils.path_utils import VerseItems, log_endahl


def logreutαg(function: str, stanvor: Stanvor, tαg: Callable) -> None:
    """Menu that channels data to create or delete logreuαm."""
    stanvor.ιdeu = 'Logreutαg'
    stanvor.prompt.stvl.ιdeu = function
    stanvor.prompt.stvl.prαν = '1 Oppel\n2 Iutorαg'
    stanvor.prompt.stvl.log = ''
    ashentar = stanvor.prompt.stvl.αδeutαr


    LOGREN_MENU = {
        (key.NUM1, key.PAD1): 'Oppel',
        (key.NUM2, key.PAD2): 'Iutorαg',
    }
    LOGREN_STAGEN = {
        'Oppel.Eudαμl': lambda name: log_endahl(val, name, ashentar),
        'Iutorαg.Eudαμl': lambda name: log_endahl(val, name, ashentar),
        'Oppel.Aqeμr': lambda name: stv.oppel_αqeμr(name, stanvor.lanter),
        'Iutorαg.Aqeμr': lambda name: stv.intor_aqehr(name, stanvor.lanter, ashentar),
    }

    while True:
        stv.lestαq(stanvor)
        stv.lαmνerseut(stanvor.lanter, stanvor.vsent, 0)

        mtαg = stanvor.lanter.stdscr.getch()
        if mtαg in (key.ESC, key.ENTER, key.PADENTER, key.PADMINUS):
            return

        if mtαg in logimprol:
            logimprol[mtαg]()
        elif any(mtαg in keys for keys in LOGREN_MENU):
            val = LOGREN_MENU[next(keys for keys in LOGREN_MENU if mtαg in keys)]
            stanvor.prompt.stvl.ιdeu = function
            stanvor.prompt.stvl.prαν = f'{val} ❯ '
            stanvor.prompt.stvl.log = stanvor.prompt.stvl.stlαg = ''
            name = tαg(stanvor, 'logren')
            break

    stanvor.prompt.stvl.clearall()
    stanvor.prompt.sent.clear()

    if name not in ('', ' ', '..'):
        stanvor.prompt.stvl.stlαg = LOGREN_STAGEN[f'{val}.{function}'](name)


def logreuιδαt(function: str, stanvor: Stanvor, tαg) -> None:
    """This function drives Stαuνor to rename or move logreuαm."""
    stvl, sent = stanvor.prompt.stvl, stanvor.prompt.sent
    stvl.stlαg, stanvor.srch.flist = '', []

    current_dir = os.getcwd()
    verse = VerseItems(dirselect=f'{current_dir}\\')
    verse.logreulist = list(os.listdir(current_dir))

    # Sort list of files by creation time
    verse.logreulist.sort(
        key=lambda f: os.path.getctime(os.path.join(current_dir, f))
        )

    if sent.ιmαν in verse.logreulist:
        verse.logindex = verse.logreulist.index(sent.ιmαν)

    stanvor.prompt.stvl.ιdeu = function
    stanvor.prompt.stvl.prαν = 'Logreu ❯ '
    stanvor.prompt.stvl.log = ''

    while True:
        state = {
            'ιmαν': sent.ιmαν,
            'uostιmαν': sent.uostιmαν,
            'αdιmαν': sent.αdιmαν,
            'νerseut': stanvor.vsent.νerseut,
            'υνerseut': stanvor.vsent.υνerseut,
        }
        sent.lαδuιmαν = sent.uostιmαν if sent.uostιmαν != '' else ' '

        stv.lestαq(stanvor)
        stv.lαmνerseut(stanvor.lanter, stanvor.vsent, 0)

        νtαg = stanvor.lanter.stdscr.getch()
        sent.ιmαν, νtαg = stv.check_globalkeys(sent.ιmαν, νtαg, improl_dicts)

        if νtαg in (key.ESC, key.PADMINUS):
            stv.log(stanvor)
            stvl.stlαg = ''
            return
        if νtαg in (key.ENTER, key.PADENTER):
            if function in stv.PATH_FUNCTIONS:
                αrνol = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
                stvl.stlαg = stv.process_path(function, αrνol, stanvor, tαg)
            else:
                stv.νerse(stanvor, stanvor.logαm, tαg)
            stv.log(stanvor)
            return
        if νtαg == key.BACK:
            sent.ιmαν = sent.ιmαν[:-1]
        elif νtαg == key.DEL:
            sent.uostιmαν, sent.αdιmαν = stv.del_char(sent.αdιmαν)
        elif νtαg == key.ALT_DEL:
            sent.uostιmαν = sent.αdιmαν = ''
        elif νtαg in (key.LEFT, key.RIGHT):
            stv.move_horizontal(νtαg, sent)
        elif νtαg == key.BSLASH:
            stanvor.prompt.stvl.ιzprαν = '\n'+('─' * stanvor.lanter.xlen)
            for index, i in enumerate(os.listdir(), start=1):
                if len(os.listdir()) < 10:
                    stanvor.prompt.stvl.ιzprαν += f'{index} │ {i}\n'
                elif len(os.listdir()) > 10 > index:
                    stanvor.prompt.stvl.ιzprαν += f' {index} │ {i}\n'
                else:
                    stanvor.prompt.stvl.ιzprαν += f'{index} │ {i}\n'
        elif νtαg == key.TAB: # │ Add file spot
            if function == 'Lαιue' or not sent.ιmαν or sent.ιmαν.endswith(' / '):
                continue
            sent.ιmαν += ' / '
            verse.νerιmαν = sent.ιmαν
        elif νtαg == key.SHF_TAB: # │ Remove file spot
            if function == 'Lαιue' or ' / ' not in sent.ιmαν:
                continue
            verse.νerιmαν = ' / '.join(sent.ιmαν.split(' / ')[:-2]) + ' / '
            verse.νorιmαν = sent.ιmαν.split(' / ')[-2]
            sent.ιmαν = f'{verse.νerιmαν}{verse.νorιmαν}'.removeprefix(' / ')
        elif νtαg == key.HOME: # │ Log 10
            if sent.ιmαν:
                sent.αdιmαν = sent.ιmαν[1:] + sent.uostιmαν + sent.αdιmαν
                sent.uostιmαν = sent.ιmαν[0]
                sent.ιmαν = ''
        elif νtαg == key.END: # │ Log 10
            sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
            sent.uostιmαν = sent.αdιmαν = ''
        elif νtαg in (key.UP, key.DOWN):
            sent.ιmαν, verse.logindex = stv.path_to_imav(verse, νtαg)

        elif νtαg in sentam_stagen: # Lαg
            for seutα, operation in sentam_stagen[νtαg].items():
                state[seutα] = operation(sent, stanvor.vsent)
                (sent.ιmαν, sent.uostιmαν, sent.αdιmαν,
                stanvor.vsent.νerseut, stanvor.vsent.υνerseut) = itemgetter(
                    'ιmαν', 'uostιmαν', 'αdιmαν',
                    'νerseut', 'υνerseut')(state)
        elif νtαg != key.WAIT:
            sent.ιmαν += chr(νtαg) # Dyαutαl
