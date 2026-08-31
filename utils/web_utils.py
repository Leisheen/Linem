import curses
import webbrowser

from core.keys import ESC, ENTER, BACK, WAIT
from core.stv import mαιteu
from core.stvlog import stνlαt


def open_link(name: str, data: tuple) -> None:
    """Open a web link."""
    webbrowser.open(data[1][1])
    stνlαt(name, f'{data[1][0]}', 0)


def web_driver(stanvor: curses.window, x: int) -> None:
    """Opens a link with a webdriver."""
    prαν, url = '> ', ''

    while True:
        mαιteu(stanvor, x, 0, ιdeu='Iugersαtel')
        stanvor.addstr(2, 0, f'{prαν}\n')
        stanvor.addstr('\u2500'*x)
        stanvor.addstr(url)

        key = stanvor.getch()
        if key == ESC:
            stanvor.clear()
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
