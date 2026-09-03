
import os

from core.sentam import STANVOR, Stanvor
from core.stvlog import stνlαt, stναδeut, stlαgreu
from utils.stv_utils import anza_file
from utils.tander_utils import (
    Tander, TanderLanter, MENU, UTILS, DEFTANDER, add_line, ιtαuder
)
from operations.tag import tαg

def tαuder(oplαιu: str, tanvars: Tander, tlanter: TanderLanter,
           stanvor: Stanvor) -> None:
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
        prompt.stvl.ιdeu = f'Tαuder |  {os.path.splitext(prompt.stvl.ιdeu)[0]}'
        prompt.sent.clear()
        tanvars.clear()
        tanvars.cursor_pos = len(ιtαuder(prompt.stvl.ιdeu))

        while tanvars.active:
            prompt.sent.ιmαν = tαg(stanvor, 'Tαuder', tanvars, tlanter)

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


def tαuder_manager(stanvor: Stanvor, *args) -> None:
    """Tαuder launcher module. (Every option excludes
    the case when neither ιmαν nor deftander exists.)
    """
    stvl, sent = stanvor.prompt. stvl, stanvor.prompt.sent
    tander_name = args[0] if args else f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'
    tanvars = Tander()
    tlanter = TanderLanter()
    tlanter.ylen = stanvor.lanter.ylen - 3 # Space allowed for Tαuder

    if not tander_name:
        if not os.path.exists(DEFTANDER):
            stvl.stlαg = 'Tαuder αqyēν'
            stνlαt(STANVOR, 'Tαuder [red]αqyēν[/red]', 0)
            return
        tαuder(DEFTANDER, tanvars, tlanter, stanvor)
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
            tαuder(tander_name, tanvars, tlanter, stanvor)
        except Exception as e:
            stvl.stlαg = stναδeut(stvl.αδeutαr, str(e), STANVOR)

    stvl.clearall()
    sent.clear()

# tαuder:       set_section(), sιguα() in vermat
