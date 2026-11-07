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

# Locals
from core import sentam as sn
from core.stv import end_stanvor, get_terminal_size
from core.stvlog import stναδeut, catch_crash
from operations.operator import run_lιuemαg


def _build_stanvor() -> sn.Stanvor:
    """Create the app context and the screen-related components."""
        # Detect terminal dimensions
    screen_width, screen_height = get_terminal_size()
    screen = sn.ScreenBuffer(screen_width, screen_height)
    lanter = sn.Lanter().set_lanter(screen)
    terminal = sn.Terminal()
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
        screen, lanter, terminal, battery,
        stvl, sent, vsent, audio, logαm, filedata, srch, alarm
    )

    return stanvor


def main() -> None:
    """Core of the Stαuνor."""
    stanvor = _build_stanvor()
    run_lιuemαg(stanvor)


if __name__ == '__main__':
    try:
        main()
    except (FileNotFoundError, AttributeError, ValueError,
            TypeError, KeyboardInterrupt) as e:
        _ = stναδeut(0, str(e), 1)
        raise
    except Exception as e: # pylint: disable=broad-exception-caught
        # To handle Stαuνor unknown crashes. The crash is logged anyway.
        catch_crash(e)
        raise
    finally:
        end_stanvor()
