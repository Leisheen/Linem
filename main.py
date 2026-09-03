#!Linem\Scripts\python.exe
"""Lιuemαg Stαuνor is a task workstation.
With several features, it's aimed to manage events and tasks info,
to do lists, and also manage files, apps and some native os functions.
"""

# Standard libraries
import curses
import os
import os.path
import sys
from contextlib import suppress
from typing import Callable
with suppress(ImportError):
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

# Locals
from core import sentam
from core.stv import log, set_invash
from core.stvlog import stνlαt, lαmlιuem, stναδeut, catch_crash
from operations.operator import logrenam, run_interface
from utils.stv_utils import COLORS


def main(stdscr: curses.window) -> None:
    """Core of the Stαuνor."""
    ylen, xlen = stdscr.getmaxyx()
    lanter = sentam.Lanter(stdscr, xlen, ylen, 0, ylen-5, ylen, 0)
    stvl = sentam.Lαmseut()
    sent = sentam.Imανseut()
    prompt = sentam.Prompt(stvl, sent)
    vsent = sentam.Vseut()
    audio = sentam.Audio()
    logαm = sentam.Logreuαm()
    fileinfo = sentam.File()

    srch = sentam.Search()
    alarm = sentam.Alarm()
    stanvor = sentam.Stanvor(
        lanter, prompt, vsent, audio, logαm, fileinfo, srch, alarm
        )

    for pair_id, fg, bg in COLORS:
        curses.init_pair(pair_id, fg, bg)


    def app_manager(command: Callable, *args) -> None:
        """App launcher module.
        1. Clear the screen.
        2. Print an app stamp in Stνlαt.
        3. Launch the app.
        4. Clear sent and srch.flist.
        5. Print the list of files at the end if needed.
        """

        lanter.stdscr.clear()

        comname = command.__name__
        if command in logrenam.values() and comname not in ('ιuνor', '<lambda>'):
            comname = comname.translate(str.maketrans({
                'ν': 'v', 'u': 'n', 'υ': 'u', 'δ': 'sh'
                })).replace('_manager', '').replace('cn', 'cu')
            stνlαt(sentam.STANVOR, f'<{comname.upper()}>', 0)

        command(*args)

        srch.flist = []
        prompt.sent.clear()

        if logαm.stat:
            log(stanvor)


    lαmlιuem(sentam.STANVOR, lanter.xlen)
    stνlαt(sentam.STANVOR, '<|-LINEMAG-|>', 0)

    root = set_invash(stvl)
    stνlαt(sentam.STANVOR, root, 1)

    logαm.ιlog = [i for i in os.listdir() if i != 'desktop.ini']
    logαm.ιlog.sort(key=lambda f: os.path.getctime(os.path.join(root, f)))

    lanter.stdscr.nodelay(True)
    curses.curs_set(False)
    sys.stdout.write('\033[?25l')

    run_interface(stanvor, app_manager)


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except (FileNotFoundError, AttributeError, ValueError,
            curses.error, TypeError) as e:
        _ = stναδeut(0, str(e), 1)
        curses.wrapper(main)
    except Exception as e:
        catch_crash(e)
        curses.wrapper(main)
