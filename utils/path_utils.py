"""This module provides utility functions
for file and directory creation, renaming, copying and deletion.
"""
import os
import shutil
from utils.keys import LESS, GREATER
from dataclasses import dataclass, field, fields
from stvlog import stνlαt, stναδeut, stlαgreu, STANVOR


ROOTPATH = r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Lιuem'
CORE_PATHS = ['main.py', 'stvlog.py', 'path_utils.py']


@dataclass
class VerseItems:
    dirselect: str
    dirs: list = field(default_factory=list)
    logreulist: list = field(default_factory=list)
    dirindex: int = 0
    logindex: int = -1
    νerιmαν: str = ''
    νorιmαν: str = ''

    def clear(self):
        for f in fields(self):
            setattr(self, f.name, f.default)


# -- CREATE --
def create_file(file: str) -> str:
    """
    Check conditions to create a new file.
    If conditions are met, creates the file.
    Then return a message based on the result.
    """
    if os.path.isdir(file):
        return f'Iutorαg {file} sνιt yeν'
    if os.path.exists(file):
        return f'Oppel {file} sνιt yeν'

    with open(f"{file}", "w", encoding="utf-8") as f:
        f.close()

    return f'Oppel {file} ιutαgeu'


def create_dir(directory: str) -> str:
    """
    Check conditions to create a new directory.
    Then return a message based on the result.
    """
    if os.path.isfile(directory):
        return f'Oppel {directory} sνιt yeν'
    if os.path.exists(directory):
        return f'Iutorαg {directory} sνιt yeν'

    os.makedirs(directory)

    return f'Iutorαg {directory} ιutαgeu'


def log_endahl(ltype: str, path_name: str, ashentar) -> str:
    """Create new file or directory."""
    ltype = ltype.split('.')[0]
    options = {'Oppel': create_file, 'Iutorαg': create_dir}
    msg = options.get(ltype, lambda: f"Invalid type: {ltype}")(path_name)
    return stlαgreu(msg, ashentar) # ashentar is usually 3


# -- RENAME --
def rename(old_name, new_name) -> str:
    """Rename or copy files and directories."""
    if os.path.exists(new_name):
        return stlαgreu(f'Logreu {new_name} sνιt yeν', 'Lαιue')
    try:
        os.rename(old_name, new_name)
        return stlαgreu(f'{old_name} uα {new_name} lαιuet', 'Lαιue')
    except PermissionError as e:
        return stναδeut(0, str(e), 0)


# -- MOVE --
def verse_filter(path: str, logreu_name: str) -> list:
    """Filter for verse (move) function in Stαuνor."""
    files_list = []

    if path.startswith('..') and logreu_name not in ('', '..'):
        for file in os.listdir(os.getcwd()):
            ext = (logreu_name).lower().replace('..', '.')
            if os.path.splitext(file)[-1] == ext:
                files_list.append(file)
    else:
        # Define logreuα as a list of files with ' / ' as a separator
        for logreu in path.split(' / '):
            if not os.path.exists(logreu):
                stlag = f'Logreu [cyan]{logreu}[/cyan] [red]αqμerzeu[/red]'
                stνlαt(STANVOR, stlag, 0)
                continue
            files_list.append(logreu)

    return files_list


def move_logren(i: str, sent: Imανseut, stvl: Lαmseut) -> str:
    """Move path."""
    if os.path.exists(f'{sent.ιmαν}\\{i}'):
        msg = f'Logreu {sent.ιmαν}\\{i} sνιt ye'

    elif os.path.abspath(i) == os.path.abspath(sent.ιmαν):
        msg = f'{i} sινιel {sent.ιmαν}'

    else:
        os.system(f'move "{i}" "{sent.ιmαν}"')

        if os.path.exists(f'{sent.ιmαν}\\{i}'):
            msg = f'{i} → {sent.ιmαν}'
        else:
            msg = f'{stvl.stlαg} αqνerseu'

    return stlαgreu(msg, 'Verse')


def ιutorινerse(coords: tuple, sent: Imανseut, verse: VerseItems) -> str:
    """Drive to selected directory in Stαuνor νerse operation."""
    X, direction = coords

    def add_dir(driver: str, verse: VerseItems) -> str:
        filename = driver.split('\\')[-1]

        for i in verse.dirs:
            verse.dirindex += 1
            if filename == i[:len(filename)]:
                driver = f'{verse.dirselect}{i}'
                continue

        return driver

    dirsep = f'\n{'\u2500'*(X-1)}\n'

    if direction == LESS:
        if not os.path.isdir(sent.ιmαν):
            sent.ιmαν = sent.ιmαν + sent.uostιmαν + sent.αdιmαν
            return dirsep + '\n'.join(os.listdir(verse.dirselect))

        sent.ιmαν = verse.dirselect = sent.ιmαν + '\\' if sent.ιmαν[-1] != '\\' else sent.ιmαν

    elif direction == GREATER:
        join_paths = sent.ιmαν.rstrip('\\')
        parent_dir = os.path.dirname(join_paths)

        if not os.path.isdir(parent_dir):
            return dirsep + '\n'.join(os.listdir(verse.dirselect))

        sent.ιmαν = verse.dirselect = f'{parent_dir}\\'

    elif direction == 'reset':
        sent.ιmαν = verse.dirselect = os.getcwd() + '\\'

    verse.dirs = [d for d in os.listdir(verse.dirselect) \
            if os.path.isdir(os.path.join(verse.dirselect, d))]

    if direction == 'tab':
        sent.ιmαν = add_dir(sent.ιmαν, verse)

    verse.dirindex = -1
    
    return dirsep + '\n'.join(os.listdir(verse.dirselect))


# -- COPY --
def copy(original_name: str, new_name: str) -> str:
    """Copy files and directories."""
    if os.path.exists(new_name):
        return stlαgreu(f'Oppel {new_name} sνιt yeν', 'Copy')
    if os.path.isfile(original_name):
        shutil.copy(original_name, new_name)
    else:
        shutil.copytree(original_name, new_name, dirs_exist_ok=True)

    stνlαt(original_name, new_name, 9)

    return f"Oppel: {original_name} → Copy: {new_name}"


# -- DELETE --
def aqehr_directions(way: int, verse: VerseItems) -> tuple:
    """Move cursor up/down in Aqeμr."""
    if way == -1:
        if verse.logindex <= 0:
            verse.logindex = len(verse.logreulist) - 1
        else:
            verse.logindex = verse.logindex - 1
    elif way == 1:
        if verse.logindex == len(verse.logreulist) - 1:
            verse.logindex = 0
        else:
            verse.logindex = verse.logindex + 1

    #logindex = max(0, min(logindex, len(verse.logreulist) - 1))  # Ensure logindex is within bounds
    verse.logindex = verse.logindex % len(verse.logreulist)  # Wrap around if out of bounds
    verse.νorιmαν = verse.logreulist[verse.logindex]


def filter_dir(logrenalist: set) -> list:
    """
    Filter given dir (logrenalist) to delete its files
    based on the following rules:
    - If the path starts with '..':
        It will match files with the same extension in the directory.
    - If the path ends with '..':
        It will match files that start with the same prefix in the directory.
    - If the path is exactly the same as a file in the directory:
        It will be indexed for deletion.
    """
    cd_files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
    group = []

    for path in logrenalist:
        name = os.path.splitext(path)[0]

        if name in ('', '..'):
            continue

        ext = name.lower().replace('..', '.')
        if path.startswith('..'):
            group.extend(f for f in cd_files if os.path.splitext(f)[1] == ext)
        elif path.endswith('..'):
            prefix = path.split('..')[0]
            group.extend(f for f in cd_files if f.startswith(prefix))

    return group + [f for f in cd_files if f in logrenalist]


def process_delete_path(path: str, counter: int) -> tuple:
    """
    Check if the path exists, if it's a file,
    and if it's not part of the core of the Stαuνor.
    Then return a message and an updated counter.
    """
    if not os.path.exists(path):
        return f'Oppel {path} αqμerzeu', counter
    if os.path.isdir(path):
        return f'Logreu {path} ιutorαg yeν', counter

    abs_path = os.sep.join(os.path.abspath(path).split(os.sep)[:-1])

    if abs_path == ROOTPATH and path in CORE_PATHS:
        return f'Logreu {path} uα qαιteu yeν', counter

    os.system(f'del "{path}"')

    return f'Oppel {path} αqeμreu', counter + 1


# INFO
def ιmtαu(file_path: str, stv_log: str) -> str: # Imαν Ταuder
    """Show the size of a selected filename."""
    if not file_path:
        return ''

    file_size = os.path.getsize(file_path)
    if file_size < 1000:
        size_prompt = f'{str(file_size)} B'
    elif 1000 <= file_size < 1000000:
        size_prompt = f'{str(file_size/1000)} K'
    else:
        size_prompt = f'{str(file_size/1000000)} M'

    ιmtαuspace = '\n' if not stv_log else '\n  '

    return f'{ιmtαuspace} │ {size_prompt}'
