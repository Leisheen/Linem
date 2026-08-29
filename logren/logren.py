import curses
import keyboard
import os
import subprocess
import time

#import fitz # PyMuPDF
import vlc

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QPixmap, QShortcut
from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from stvlog import stνlαt, STANVOR


# System Text editor
def open_editor(file: str, editor: str, lag: str) -> None:
    """Open file in selected editor."""
    command = f'edit "{file}"' if editor == 'msedit' else file
    os.system(f'"{command}"')
    curses.curs_set(0)

    if lag:
        stνlαt(lag, '❯ Lαg', 0)


# Explorer
def open_saget(SAGET):
    """Open Sαget."""
    if not os.path.exists(SAGET):
        stνlαt(STANVOR, '❯ Sαget αqμerzeu', 0)
 
    subprocess.Popen(SAGET)
    stνlαt(STANVOR, '❯ Sαget', 0)


# Pdf for open_pyside()
def charge_pdf(file_path: str):
    """Charge PDF files and convert first page to image for open_pyside().
    from PIL import Image
    from PIL.ImageQt import ImageQt
    doc = fitz.open(file_path)
    page = doc.load_page(0)  # Load the first page
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    qt_image = QPixmap.fromImage(ImageQt.toqimage(img))
    image = Image.open(qt_image)
    return image"""
    return file_path # just for pylint


# Image for open_pyside()
def charge_image(file_path: str):
    """Charge image files for open_pyside()."""
    # Create graphics view and scene
    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setWindowTitle(os.path.basename(file_path))
    view.setScene(scene)

    # Load and display image
    pixmap = QPixmap(os.path.abspath(file_path))
    resized_pixmap = pixmap.scaled(
        750, 560, Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation)
    image_width = resized_pixmap.width()
    scene.addPixmap(resized_pixmap)

    # Set window position
    view.move(1524-image_width, 40)  # Screen coordinates
    return view


# Image and Pdf motor
def open_pyside(file_path: str) -> None:
    """Open img and pdf files based on file_path."""
    app = QApplication.instance() or QApplication([])

    if os.path.splitext(file_path)[1].lower() in ['.pdf']:
        pdf_file = charge_pdf(file_path)
        file = charge_image(pdf_file)
    else:
        file = charge_image(file_path)

    flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    file.setWindowFlags(flags)

    # Add Escape shortcut
    close_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), file)
    close_shortcut.activated.connect(file.close)

    # Show the window
    file.show()
    app.exec()


# Video
def open_video(file_path: str) -> None:
    """Open video files base on file_path."""
    #player = instance.media_player_new()  # Create a new VLC media player instance
    #media = instance.media_new(os.path.abspath(file_path))  # Load the media file
    player = vlc.MediaPlayer(os.path.abspath(file_path))
    player.set_hwnd(0)
    #player.set_media(media)  # Set the media to the player
    #player.set_fullscreen(True)  # Set fullscreen mode
    player.play()

    while True:
        if keyboard.is_pressed('right'):
            player.set_time(player.get_time() + 5000)
        elif keyboard.is_pressed('left'):
            player.set_time(player.get_time() - 5000)
        elif keyboard.is_pressed('space'):
            if player.is_playing():
                player.pause()
            else:
                player.play() #
        elif keyboard.is_pressed('esc'):
            break

        time.sleep(0.1)  # Sleep to prevent high CPU usage

    player.stop()


# Youtube
def open_youtube(url: str) -> str:
    """yt = YouTube(url)
    video =  yt.streams.filter(only_audio=True).first()
    destino = 'temp_audio'
    out_file = video.download(output_path=destino)
    base, _ = os.path.splitext(out_file)
    new_file = base + '.wav'
    os.rename(out_file, new_file)"""
    return url
