#!Linem\Scripts\python.exe
"""Lιuemαg Stαuνor is a task workstation.
With several features, it's aimed to manage events and tasks info,
to do lists, and also manage files, apps and some native os functions.

Roadmap:
- Professionalize this as an application first: separate UI, domain logic,
    and OS-specific services; add automated tests, type checking, linting, CI,
    user-facing documentation, and reproducible packaging.
- Centralize configuration and logging, validate persisted data, and handle
    unsupported OS features explicitly. Keep the curses interface replaceable.
- Treat a native OS as a separate, long-term project: define its scope and
    architecture, then build and test a bootable prototype in an emulator before
    tackling drivers, memory/process management, storage, and security. Reuse
    this project as an application only after defining a stable OS interface.
"""

import curses
import sys

# Locals
from core import sentam as sn
from core.stv import hide_cursor, end_stanvor
from core.stvlog import stναδeut, catch_crash
from operations.operator import run_interface



def _build_stanvor(stdscr: curses.window) -> sn.Stanvor:
    """Create the app context and the screen-related components."""
    lanter = sn.Lanter.set_stanvor(stdscr)
    battery = sn.Battery()
    stvl = sn.Lαmseut()
    sent = sn.Imανseut()
    vsent = sn.Vseut()
    audio = sn.Audio()
    logαm = sn.Logreuαm()
    filedata = sn.File()
    srch = sn.Search()
    alarm = sn.Alarm()
    stanvor = sn.Stanvor(
        lanter, battery, stvl, sent, vsent, audio, logαm, filedata, srch, alarm
    )

    return stanvor


def _prepare_terminal(lanter: sn.Lanter) -> None:
    """Initialize terminal colors and hide the cursor."""
    for pair_id, fg, bg in sn.COLORS:
        curses.init_pair(pair_id, fg, bg)

    hide_cursor()
    lanter.stdscr.nodelay(True)


def main(stdscr: curses.window) -> None:
    """Core of the Stαuνor."""
    stanvor = _build_stanvor(stdscr)
    _prepare_terminal(stanvor.lanter)
    run_interface(stanvor)


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except (FileNotFoundError, AttributeError, ValueError,
            curses.error, TypeError, KeyboardInterrupt) as e:
        _ = stναδeut(0, str(e), 1)
        raise
    except Exception as e: # pylint: disable=broad-exception-caught
        # To handle Stαuνor unknown crashes. The crash is logged anyway.
        catch_crash(e)
        raise
    finally:
        end_stanvor()
