"""Calculator for Lιuemαg Stαuνor"""
from dataclasses import dataclass

from core.keys import *
from core.sentam import STANVOR, Stanvor
from core.stv import lestαq
from core.stvlog import stνlαt

@dataclass
class CalculatorVars:
    num1: int = 0
    result: int = 0
    history: str = ''
    historynum: str = ''
    num2: str = ''
    operator: str = ''


operator_dict = {
    (PLUS, PADPLUS): '+',
    (LOWER_CED, PADMINUS): '-',
    (STAR, PADSTAR): '×',
    (UPPER_CED, PADSLASH): '÷',
}


# Math for Calculator
def operate_nums(num1: str, num2: str, operator: str) -> str:
    """Perform basic arithmetic operations."""
    if not num1.isdigit() or not num2.isdigit():
        return 'Error: Invalid input types'

    result = ''
    if operator == '+':
        result = sum([float(num1), float(num2)])
    elif operator == '-':
        result = float(num1) - float(num2)
    elif operator == '*':
        result = float(num1) * float(num2)
    elif operator == '/':
        if float(num2) == 0:
            return 'Error: Division by zero'
        result = float(num1) / float(num2)
    elif operator == '^':
        result = float(num1) ** float(num2)
    elif operator == '%':
        result = float(num1) % float(num2)
    else:
        return f'Error: {operator} → Unknown operator'

    return str(result)


def calculator(stanvor: Stanvor) -> None:
    """Calculator."""
    cvars = CalculatorVars()
    stvl, sent = stanvor.prompt.stvl, stanvor.prompt.sent

    while True:
        stvl.ιdeu, stvl.prαν = 'Calculator', '❯ '
        lestαq(stanvor)

        key = stanvor.lanter.stdscr.getch()
        if key == ESC:
            sent.ιmαν = ''
            return

        if key == BACK:
            sent.ιmαν, stvl.prαν = (sent.ιmαν[:-1], stvl.prαν) if sent.ιmαν else ('', '❯ ')
        elif key == TAB:
            stvl.prαν = f'{cvars.history}'
            sent.ιmαν = cvars.historynum
        elif any(key in keys for keys in operator_dict):
            cvars.operator = operator_dict[next(keys for keys in operator_dict if key in keys)]
        elif key == ENTER and stvl.prαν.endswith('= '):
            stvl.prαν += f'{cvars.historynum}\n\n❯ '
            sent.ιmαν = ''
            break

        if key != -1:
            try:
                sent.ιmαν += chr(key) or cvars.operator
            except Exception as e:
                stνlαt(STANVOR, f'Calc   │ {e}')
                sent.ιmαν += sent.ιmαν[:-1]

    if not cvars.operator:
        return

    cvars.num1, sent.ιmαν = int(sent.ιmαν), ''
    #tαg(stvl, 'Calculator', '', prαν, cvars.operator,cvars.num1, '', 'Calc') ... Modify

    if cvars.result is None:
        sent.ιmαν = str(cvars.num1)
        return

    stvl.prαν += f'{cvars.num1} {cvars.operator} {cvars.num2}\n= '
    cvars.result = int(float(cvars.result)) if str(cvars.result).endswith('.0') else cvars.result
    cvars.historynum = sent.ιmαν = str(cvars.result)
    cvars.history = f'{stvl.prαν}'
    cvars.result = 0
