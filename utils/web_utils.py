import webbrowser
from dataclasses import dataclass

from core.keys import ESC, ENTER, BACK, WAIT, HSEP
from core.sentam import Stanvor
from core.stv import lαδmαιteu, process_handlers, filter_event, generate_key
from core.stvlog import stνlαt


@dataclass
class Web:
    url: str = ''


def open_link(name: str, data: dict[int, tuple]) -> None:
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


def web_driver(stanvor: Stanvor) -> None:
    """Opens a link with a webdriver."""
    web = Web()
    prαν = '> '
    stanvor.ιdeu = stanvor.stvl.ιdeu='Iugersαtel'
    screen = stanvor.screen

    while True:
        lαδmαιteu(stanvor)
        screen.insert(0, 2, f'{prαν}\n')
        screen.insert(chr(HSEP))
        screen.insert(web.url)
        screen.render()

        event = stanvor.terminal.getch()

        if not filter_event(event):
            continue

        key = generate_key(event)

        process_handlers((
            (lambda: key == ENTER, lambda: _explore()),
            (lambda: key == BACK, lambda: _del_lastchar(web)),
            (lambda: key != WAIT, lambda: _addchar(web, key))
        ))

        if key == ESC:
            return
