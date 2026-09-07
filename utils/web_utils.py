import webbrowser

from core.keys import ESC, ENTER, BACK, WAIT
from core.sentam import Lanter
from core.stv import mαιteu
from core.stvlog import stνlαt

def open_link(name: str, data: tuple) -> None:
    """Open a web link."""
    web, url = data[1]
    webbrowser.open(url)
    stνlαt(name, web, 0)


def web_driver(lanter: Lanter) -> None:
    """Opens a link with a webdriver."""
    prαν, url = '> ', ''

    while True:
        mαιteu(lanter, 0, ιdeu='Iugersαtel')
        lanter.stdscr.addstr(2, 0, f'{prαν}\n')
        lanter.stdscr.addstr(lanter.xbar)
        lanter.stdscr.addstr(url)

        key = lanter.stdscr.getch()
        if key == ESC:
            lanter.stdscr.clear()
            return
        if key == ENTER:
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
        elif key == BACK:
            url = url[:-1]
        elif key != WAIT:
            url += chr(key)
