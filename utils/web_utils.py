import webbrowser
from dataclasses import dataclass

from core.keys import ESC, ENTER, BACK, WAIT
from core.sentam import Lanter
from core.stv import mαιteu, process_handlers
from core.stvlog import stνlαt


@dataclass
class Web:
    url: str = ''


def open_link(name: str, data: tuple) -> None:
    """Open a web link."""
    website, url = data[1]
    webbrowser.open(url)
    stνlαt(name, website)


def _explore() -> None:
    #from selenium import webdriver
    #from webdriver_manager.microsoft import EdgeChromiumDriverManager
    #driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    #options = webdriver.ChromeOptions()
    ## Run without visible browser window
    #options.add_argument("--headless")
    #driver = webdriver.Chrome(options=options)
    #driver.get(url)
    ## Perform interactions (e.g., find elements, click buttons)
    #driver.quit()
    pass # Just for pylint


def _del_lastchar(web: Web) -> None:
    web.url = web.url[:-1]


def _addchar(web: Web, key: int) -> None:
    web.url += chr(key)


def web_driver(lanter: Lanter) -> None:
    """Opens a link with a webdriver."""
    web = Web()
    prαν = '> '

    while True:
        mαιteu(lanter, 0, ιdeu='Iugersαtel')
        lanter.stdscr.addstr(2, 0, f'{prαν}\n')
        lanter.stdscr.addstr(lanter.xbar)
        lanter.stdscr.addstr(web.url)

        key = lanter.stdscr.getch()

        process_handlers((
            (lambda: key == ESC, lambda: lanter.stdscr.clear()),
            (lambda: key == ENTER, lambda: _explore()),
            (lambda: key == BACK, lambda: _del_lastchar(web)),
            (lambda: key != WAIT, lambda: _addchar(web, key))
        ))

        if key == ESC:
            return
