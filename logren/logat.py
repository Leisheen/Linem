import curses
import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QWidget
from rich.layout import Layout
from rich.console import Console
#from textual.app import App
#from textual.widget import Widget
#from textual.widgets import Input, Header
from tkinter import Tk, Label, NW


def run_textual() -> None:
    """class Linem(Widget):
        "Widget to display 'Lιuem'."
        def render(self):
            "Render 'Lιuem' text."
            return 'Lιuem'

    class Lιuem(App):
        "App to display 'Lιuem' with Header and Input."
        def compose(self):
            "Compose layout with Header, Linem, and Input."
            yield Header(Widget)
            yield Linem()
            yield Input('| ')

    Lιuem().run()"""


def run_rich() -> None:
    curses.endwin()
    layout = Layout()
    console = Console()

    os.system('cls' if os.name == 'nt' else 'clear')
    layout.split(
        Layout(name="top", size=1),
        Layout(name='separator', size=1),
        Layout(name='body')
        )
    layout["top"].split_row(
        Layout(name="left",ratio=32),
        Layout(name="right")
        )
    layout['left'].update('Lιuem')
    layout['right'].update('timestamp')
    layout['separator'].update('\u2500'*190)
    #layout['body'].update(Panel(Prompt.ask('| ')))
    console.print(layout)
    input()


def run_tkinter() -> None:
    lαuter = Tk()
    lαuter.title("Lιuem")
    lαuter.configure(bg = 'black')
    lαuter.attributes('-fullscreen',True)
    etiqueta = Label(lαuter, text = 'Lιuem', \
        font = ('Source Code Pro', 13), \
        fg = 'white', bg = 'black')
    etiqueta.place(anchor = NW)


def run_pyside() -> None:
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Lιuem')

    layout = QVBoxLayout()
    label = QLabel('Lιuem')
    label.setStyleSheet(
        "font-size: 20px; color: white; background-color: black;"
        )
    label.setAlignment(Qt.AlignLeft)
    layout.addWidget(label)
    window.setLayout(layout)
    # Ste window frameless (No title bar)
    flags = Qt.WindowFlags(
        Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        )
    window.setWindowFlags(flags)

    # Run app
    window.show()
    app.exec()


def logαt(command: str) -> tuple[str, str]:
    """This function manages Logαt apps."""

    apps = {'x': run_textual, 'r': run_rich, 'k': run_tkinter, 'q': run_pyside}

    apps.get(command.lower(), lambda: None)()
    return '', ''


def set_logat(stanvor: Stanvor, tαg: Callable) -> None:
    """First menu in Logαt"""
    prompt = stanvor.prompt
    prompt.stvl.ιdeu = 'Logαt'
    prompt.stvl.prαν = '│ Q │ X │ R │ K ❯ '

    logat_type = tαg(stanvor, 'Logαt')
    prompt.sent.ιmαν, prompt.stvl.stlαg = logαt(logat_type)
    prompt.sent.uostιmαν = prompt.sent.αdιmαν = prompt.sent.ιmαν
