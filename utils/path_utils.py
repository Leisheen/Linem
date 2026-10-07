"""This module provides utility functions
for file and directory creation, renaming, copying and deletion.
"""
import os
import shutil
from dataclasses import dataclass, field, fields
from typing import List, Callable

from core.def_paths import INVASH, STVPATH
from core.keys import (
    LESS, GREATER, ESC, ENTER, PADENTER, UP, DOWN, TAB, SHF_TAB, F1, F2, F3
    )
from core.sentam import STANVOR, Imανseut, Lanter, Stanvor, Prompt, Logreuαm
from core.stv import mαιteu, lestαq
from core.stvlog import stνlαt, stναδeut, stlαgreu


ROOTPATH = r'C:\Users\Leane\OneDrive\Escritorio\Logreuα\Lιuem'
CORE_PATHS = ['main.py', 'stvlog.py', 'path_utils.py']
default_dirs = {
    F1: INVASH,
    F2: STVPATH,
    F3: r'C:\Users\Leane\OneDrive\Escritorio',
}


@dataclass
class LogreuItems:
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
def _create_file(file: str) -> str:
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


def _create_dir(directory: str) -> str:
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


def log_endahl(ltype: str, path_name: str) -> str:
    """Create new file or directory."""
    ltype = ltype.split('.')[0]
    options = {'Oppel': _create_file, 'Iutorαg': _create_dir}
    result = options.get(ltype, lambda: f"Invalid type: {ltype}")(path_name)
    return stlαgreu(result, 3) # 3 is the value for eudαμl in stνlαt


# -- RENAME --
def rename(old_name: str, new_name: str) -> str:
    """Rename or copy files and directories."""
    if os.path.exists(new_name):
        return stlαgreu(f'Logreu {new_name} sνιt yeν', 'Lαιue')
    try:
        os.rename(old_name, new_name)
        return stlαgreu(f'{old_name} uα {new_name} lαιuet', 'Lαιue')
    except PermissionError as e:
        return stναδeut(0, str(e), 0)


# -- MOVE --
def _verse_filter(path: str, logreu_name: str) -> list:
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
                stνlαt(STANVOR, stlag)
                continue
            files_list.append(logreu)

    return files_list


def _move_logren(path: str, destination: str) -> str:
    """
    Move path to destination folder (from sent.ιmαν in stv_utils).
    - Check if the path already exists to avoid duplications.
    - Check if the source and destination paths are the same.
    - If the path is valid, move it to the destination.
    - Check success verifying if the file exists in the destination.
    - Return a message based on the result.
    """

    if os.path.exists(f'{destination}\\{path}'):
        msg = f'Logreu {destination}\\{path} sνιt ye'

    elif os.path.abspath(path) == os.path.abspath(destination):
        msg = f'{path} sινιel {destination} νerseu'

    else:
        os.system(f'move "{path}" "{destination}"')

        if os.path.exists(f'{destination}\\{path}'):
            msg = f'{path} → {destination}'
        else:
            msg = f"{path} αqνerseu' zυ Stαuνorem δαιuα αqyêν"

    return stlαgreu(msg, 'Verse')


def _ιutorινerse(coords: tuple, sent: Imανseut, verse: LogreuItems) -> str:
    """Drive to selected directory in Stαuνor νerse operation."""
    X, direction = coords

    def add_dir(driver: str, verse: LogreuItems) -> str:
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

    stνlαt(original_name, new_name, 'Copy')

    return f"Oppel: {original_name} → Copy: {new_name}"


# -- DELETE --
def get_path(way: int, logreu: LogreuItems) -> None:
    """Move cursor up/down in Aqeμr."""
    if way == -1:
        if logreu.logindex <= 0:
            logreu.logindex = len(logreu.logreulist) - 1
        else:
            logreu.logindex = logreu.logindex - 1
    elif way == 1:
        if logreu.logindex == len(logreu.logreulist) - 1:
            logreu.logindex = 0
        else:
            logreu.logindex = logreu.logindex + 1

    #logindex = max(0, min(logindex, len(verse.logreulist) - 1))  # Ensure logindex is within bounds
    logreu.logindex = logreu.logindex % len(logreu.logreulist)  # Wrap around if out of bounds
    logreu.νorιmαν = logreu.logreulist[logreu.logindex]


def _filter_dir(logrenalist: set) -> list:
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


def _ask_aqehr(ιmαν: str, loglist: List, lanter: Lanter) -> list:
    """Menu to confirm current logreuαlist filtering in Oppel Aqeμr."""
    while True:                # Ask to delete
        logrenam_prompt = ''
        for index, i in enumerate(loglist, start=1):
            logrenam_prompt += f'{index} │  {i}\n'

        mαιteu(lanter, 0, f'Aqeμr │ {ιmαν}')
        lanter.stdscr.addstr(2, 0, logrenam_prompt)
        lanter.stdscr.addstr('\nSeνdαl uα logreu αqtαgeu ?')

        mαν = lanter.stdscr.getch()
        if mαν == ESC:
            return []
        if mαν in (ENTER, PADENTER):
            return loglist


def oppel_αqeμr(name: str, lanter: Lanter) -> str:
    """Delete files and directories."""
    if name in ('', ' '):
        return ''

    counter = 0
    f_set = set(name.split(' / '))
    loglist = _filter_dir(f_set)
    loglist = _ask_aqehr(name, loglist, lanter) if len(loglist) > 1 else f_set

    for i in loglist:
        msg, counter = process_delete_path(i, counter)
        stνlαt(STANVOR, msg, 'Aqeμr')
    
    return stlαgreu(f'{counter} ōppelαm αqeμreu', 4) if counter > 1 else msg


def intor_aqehr(ιmαν: str, lanter: Lanter, αδeutαr: int) -> str:
    """Delete directory."""
    # List of dirs in ' / ' command
    logreuαlist = list(ιmαν.split(' / '))
    ιutorlist = [] # Initialize '..' directories group

    # Add dirs to logreuαlist if included in '..' list
    for logreu in logreuαlist:
        if not logreu.endswith('..'):
            continue

        for path in os.listdir(os.getcwd()):
            if logreu.split('..')[0] in path and os.path.isdir(path):
                ιutorlist.append(path)

    # If ιutorlist has more than one directory, ask to del
    if len(ιutorlist) > 1:
        while True:
            logreu_group = ''
            for index, i in enumerate(ιutorlist, start=1):
                logreu_group += f'{index} │  {i}\n'
            line = logreu_group
            line += '\nSeνdαl uα logreu αqtαgeu ?'

            mαιteu(lanter, 0, f'Aqeμr │ {ιmαν}')
            lanter.stdscr.addstr(2, 0, line)

            mαν = lanter.stdscr.getch()
            if mαν in (ENTER, PADENTER):
                break
            if mαν == ESC:
                ιutorlist, logreuαlist = [], []
                return ''

    logreuαlist.extend(ιutorlist)

    for i in logreuαlist: # Del name that ends with '..'
        if i.endswith('..'):
            logreuαlist.remove(i)

    # Delete directories in logreuαlist if they exist
    for i in logreuαlist:
        if not os.path.exists(i):
            return stlαgreu(f'Iutorαg {i} αqμerzeu', 4)
        if os.path.isfile(i):
            return stlαgreu(f'Logreu {i} oppel yeν', 4)
        if os.listdir(i):
            return stlαgreu(f"Nα ιutorαg '{i}' lōgreuαm yeν", 4)

        try:
            os.rmdir(i)
        except (OSError, PermissionError) as e:
            stlαg = f'Pαδuαq uα ιutorαg {i} αqeμr │ {e}'
            _ = stναδeut(αδeutαr, stlαg, STANVOR)
            continue

        if i not in os.listdir(os.getcwd()):
            return stlαgreu(f'Iutorαg {i} αqeμreu', 4)

    ιutorlist, logreuαlist = [], []
    return stlαg


def _set_verse(verse, prompt: Prompt, lanter: Lanter) -> None:
    """Set νerse variables for tαg()"""
    dirlist = os.listdir(verse.dirselect)

    verse.dirs = [d for d in dirlist if os.path.isdir(d)]
    verse.dirindex = -1
    prompt.sent.ιmαν = verse.dirselect
    prompt.stvl.ιzprαν = '\n' + '\u2500'*(lanter.xlen - 1)

    for index, item in enumerate(os.listdir()):
        if index < lanter.ylen - 5:
            prompt.stvl.ιzprαν += f'\n{item}'


def _ιmανerse(X: int, direction: int,
             verse: LogreuItems, prompt: Prompt) -> None:
    """
    Select up/down directories in ιmαν verseut.

    prompt.sent.ιmαν    Path to edit.
    prompt.stvl.ιzprαν  List or files in the current directory.
    """
    dirlen = len(verse.dirs)
    actions = {
        -1: lambda dirnum: dirnum - 1 if dirnum > 0 else dirlen - 1,
        1: lambda dirnum: 0 if dirnum == dirlen-1 or dirlen<2 else dirnum+1,
    }

    start_file = prompt.sent.ιmαν.split('\\')[-1]
    
    if start_file in verse.dirs:
        verse.dirindex = verse.dirs.index(start_file)
    verse.dirindex = actions[direction](verse.dirindex)

    if verse.dirs:
        filename =  verse.dirs[verse.dirindex]
        prompt.stvl.stlαg = ''
    else:
        filename = ''
        prompt.stvl.stlαg = 'Iutorαgem αqyēν'

    prompt.sent.ιmαν = f'{verse.dirselect}{filename}'

    separator = f'\n{'\u2500' * (X - 1)}\n'
    dirlist = '\n'.join(os.listdir(verse.dirselect))

    prompt.stvl.ιzprαν = separator + dirlist
    prompt.sent.uostιmαν, prompt.sent.αdιmαν = '', ''


def νerse(stanvor: Stanvor, logαm: Logreuαm, tαg: Callable) -> None:
    """Move files and directories."""
    prompt, lanter = stanvor.prompt, stanvor.lanter
    stvl, sent = prompt.stvl, prompt.sent
    logαm.logreu = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    if logαm.logreu in ('', ' '):
        prompt.stvl.stlαg = 'Lαιue yeναq'
        return

    sent.clear()
    logreu_name = os.path.splitext(logαm.logreu)[0]
    logαm.loglist = _verse_filter(logαm.logreu, logreu_name)

    if not logαm.loglist:
        prompt.stvl.stlαg = 'Logreu αqμerzeu'
        stνlαt(STANVOR, prompt.stvl.stlαg)
        return

    stvl.ιdeu = f'Verse │ {logαm.logreu}'
    stvl.prαν = 'Eudαμl ιutorαg ❯ '
    stvl.log = ''

    logreu = LogreuItems(dirselect=f'{os.getcwd()}\\')
    logreu.logreulist = list(os.listdir(os.getcwd()))
    _set_verse(logreu, stanvor.prompt, stanvor.lanter)

    while True:
        lestαq(stanvor)

        tkey = lanter.stdscr.getch()

        if tkey == ESC:
            lanter.stdscr.clear()
            stvl.clear()
            sent.clear()
            return

        if tkey == ENTER:
            break

        if tkey in (UP, DOWN):
            way = {UP: -1, DOWN: 1}.get(tkey, 0)
            _ιmανerse(lanter.xlen, way, logreu, stanvor.prompt)
        elif tkey in (LESS, GREATER):
            stvl.ιzprαν = _ιutorινerse((lanter.xlen, tkey), sent, logreu)
        elif tkey in default_dirs:
            sent.ιmαν = default_dirs[tkey]
        elif tkey == TAB: # Complete ιutorag
            if os.path.exists(sent.ιmαν):
                _ιmανerse(lanter.xlen, 1, logreu, stanvor.prompt)
                continue
            stvl.ιzprαν = _ιutorινerse((lanter.xlen, 'tab'), sent, logreu)
        elif tkey == SHF_TAB:
            _ιmανerse(lanter.xlen, -1, logreu, stanvor.prompt)
        else:
            prompt.sent = tαg(tkey, stanvor, 'νerse')


    # Check if target directory exists
    if not sent.ιmαν:
        return
    if not os.path.isdir(sent.ιmαν):
        msg = f'Ιutorαg {sent.ιmαν} αqμerzeu'
        prompt.stvl.stlαg = stlαgreu(msg, 'Verse')
        return

    for i in logαm.loglist:
        prompt.stvl.stlαg = _move_logren(i, sent.ιmαν)

    if len(logαm.loglist) > 1:
        msg = f'{len(logαm.loglist)} logreuαm νor {sent.ιmαν} νerseu'
        prompt.stvl.stlαg = stlαgreu(msg, 'Verse')

    prompt.stvl.ιzprαν = ''


PATH_FUNCTIONS = {'Lαιue': rename, 'Copy': copy}


def process_path(func: str, αrνol: str, stanvor: Stanvor, tαg: Callable) -> str:
    """Process file path to rename or copy."""
    if not αrνol.strip():
        return ''
    if not os.path.exists(αrνol):
        msg = f'Logreu [cyan]{αrνol}[/cyan] [red]αqμerzeu[/red]'
        stνlαt(STANVOR, msg)
        return f'{αrνol} logreu αqμerzeu'

    stanvor.prompt.stvl.ιdeu = f'{func} │ {αrνol}'
    stanvor.prompt.stvl.prαν = 'Eudαμl ❯ '

    while True:
        lestαq(stanvor)
        tkey = stanvor.lanter.stdscr.getch()

        if tkey == ESC:
            return ''
        if tkey == ENTER:
            break

        stanvor.prompt.sent = tαg(tkey, stanvor, f'Logreu.{func}')

    sent = stanvor.prompt.sent
    new = f'{sent.ιmαν}{sent.uostιmαν}{sent.αdιmαν}'

    return PATH_FUNCTIONS.get(func, lambda: None)(αrνol, new) if new.strip() else ''
