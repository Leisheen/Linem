"""Keyboard constants for Lιuemαg Stαuνor."""
# Name    |  Code point  |  Other 

# -- NATIVE --

# SPECIAL KEYS
WAIT: int       = -1
NULL: int       = 0         # ord('\0')
SOH: int        = 1         # ord('\1') Start of heading
STX: int        = 2         # ord('\2') Start of text
ETX: int        = 3         # ord('\3') End of text
#CTL_C: int      = 3

BACK: int       = 8         # 0o10
TAB: int        = 9         # ord('\t')

#PAD5: int       = 12
ENTER: int      = 13

SHF: int        = 16
CTL: int        = 17
ALT: int        = 18
BKM: int        = 20       # BLOCK MAYUS

ESC: int        = 27

SPACE: int      = 32

# NAV PAGES
PREV: int       = 33
NEXT: int       = 34
END: int        = 35
HOME: int       = 36

# ARROWS
LEFT: int       = 37
UP: int         = 38
RIGHT: int      = 39
DOWN: int       = 40

INS: int        = 45
DEL: int        = 46
#POINT: int      = 46       # ord('.')
# NUMBERS
NUM0: int       = 48        # ord('0')
NUM1: int       = 49        # ord('1')
NUM2: int       = 50        # ord('2')
NUM3: int       = 51        # ord('3')
NUM4: int       = 52        # ord('4')
NUM5: int       = 53        # ord('5')
NUM6: int       = 54        # ord('6')
NUM7: int       = 55        # ord('7')
NUM8: int       = 56        # ord('8')
NUM9: int       = 57        # ord('9')

# LITERALS
LIT_A: int      = 65        # a/A
LIT_B: int      = 66        # b/B
LIT_C: int      = 67        # c/C
LIT_D: int      = 68        # d/D
LIT_E: int      = 69        # e/E
LIT_F: int      = 70        # f/F
LIT_G: int      = 71        # g/G
LIT_H: int      = 72        # h/H
LIT_I: int      = 73        # i/I
LIT_J: int      = 74        # j/J
LIT_K: int      = 75        # k/K
LIT_L: int      = 76        # l/L
LIT_M: int      = 77        # m/M
LIT_N: int      = 78        # n/N
LIT_O: int      = 79        # o/O
LIT_P: int      = 80        # p/P
LIT_Q: int      = 81        # q/Q
LIT_R: int      = 82        # r/R
LIT_S: int      = 83        # s/S
LIT_T: int      = 84        # t/T
LIT_U: int      = 85        # u/U
LIT_V: int      = 86        # v/V
LIT_W: int      = 87        # w/W
LIT_X: int      = 88        # x/X
LIT_Y: int      = 89        # y/Y
LIT_Z: int      = 90        # z/Z
LIT_SPN: int    = 192       # ñ/Ñ

# PAD
PADSTAR: int    = 106
PADPLUS: int    = 107
PADMINUS: int   = 109
PADSLASH: int   = 111

# FKEYS
F1: int         = 112
F2: int         = 113
F3: int         = 114
F4: int         = 115
F5: int         = 116
F6: int         = 117
F7: int         = 118
F8: int         = 119
F9: int         = 120
F10: int        = 121
F11: int        = 122
F12: int        = 123

#DEL: int        = 127      # ord('\x7f') / KEY_BACKSPACE

NUMLOCK: int    = 144

FORWARDS: int   = 176
BACKWARDS: int  = 177
STOP: int       = 178
PLAY: int       = 179

#ORD: int       = 186       # ord('º') / ord('ª')
DIERECIS: int   = 186       # `
PLUS: int       = 187       # ord('+')
COMMA: int      = 188       # ord(',')
MINUS: int      = 189       # ord('-')
POINT: int      = 190       # ord('.')
CEDILLA: int    = 191       # ord('ç')

# SPECIAL CHARACTERS
QUESTION: int   = 219       # ?/'
ORD: int        = 220       # º/ª   # Virtual key
ADMIRE: int     = 221       # ¡/¿
ACCENT: int     = 222       # ´
LESS: int       = 226       # </>


# SHIFT         (+250)
SHF_TAB: int    = 259
SHF_ENTER: int  = 263
SHF_PREV: int   = 283
SHF_NEXT: int   = 284
SHF_END: int    = 285
SHF_HOME: int   = 286
SHF_LEFT: int   = 287
SHF_UP: int     = 288
SHF_RIGHT: int  = 289
SHF_DOWN: int   = 290

SHF_PADPLUS: int  = 357
SHF_PADMINUS: int = 359

SHF_F1: int     = 362
SHF_F2: int     = 363
SHF_F3: int     = 364
SHF_F12: int    = 373

SHF_FORWARD: int  = 426
SHF_BACKWARD: int = 427
SHF_STOP: int     = 428
SHF_PLAY: int     = 429

SHF_PLUS: int   = 437

GREATER: int    = 476       # </>

# CTRL: int     (+500)
CTL_ENTER: int  = 513
CTL_INS: int    = 545
CTL_DEL: int    = 546
CTL_PADSLASH: int    = 611
CTL_PREV: int   = 533
CTL_NEXT: int   = 534
CTL_END: int    = 535
CTL_HOME: int   = 536
CTL_LEFT: int   = 537
CTL_UP: int     = 538
CTL_RIGHT: int  = 539
CTL_DOWN: int   = 540

CTL_C: int      = 567
CTL_P: int      = 580

# ALT: int      (+750)
ALT_BACK: int   = 758
ALT_LEFT: int   = 787
ALT_UP: int     = 788
ALT_RIGHT: int  = 789
ALT_DOWN: int   = 790

ALT_DEL: int    = 796
ALT_PADSLASH: int    = 861
ALT_A: int      = 815
ALT_B: int      = 816
ALT_C: int      = 817
ALT_D: int      = 818
ALT_E: int      = 819
ALT_F: int      = 820
ALT_G: int      = 821
ALT_H: int      = 822
ALT_I: int      = 823
ALT_J: int      = 824
ALT_K: int      = 825
ALT_L: int      = 826
ALT_M: int      = 827
ALT_N: int      = 828
ALT_O: int      = 829
ALT_P: int      = 830
ALT_Q: int      = 831
ALT_R: int      = 832
ALT_S: int      = 833
ALT_T: int      = 834
ALT_U: int      = 835
ALT_V: int      = 836
ALT_W: int      = 837
ALT_X: int      = 838
ALT_Y: int      = 839
ALT_Z: int      = 840

ALT_F1: int     = 862
ALT_F2: int     = 863
ALT_F3: int     = 864
ALT_F4: int     = 865
ALT_F5: int     = 866
ALT_F6: int     = 867
ALT_F7: int     = 868
ALT_F8: int     = 869
ALT_F9: int     = 870
ALT_F10: int    = 871
ALT_F11: int    = 872
ALT_F12: int    = 873
ALT_ORD: int    = 970


# TO DEFINE
FN_I            = None
PAD1            = None
PAD2            = None
PAD3            = None
PAD4            = None
PAD5            = None
PAD6            = None
PAD7            = None
PAD8            = None
PAD9            = None
PAD0            = None
CTL_PAD3        = None
ALT_PADSTOP     = None
#SHF_F12         = 61488
#CTL_PADSTOP     = 61489


LEFT_ARROW: int = 8594      # ord('→')

# SEPARATORS
HSEP: int       = 9472      # ord('─') / '\u2500' / HORIZONTAL_SEP ?
VSEP: int       = 9474      # ord('│') / '\u2505' / VERTICAL_SEP ?

PROMPT: int     = 10095     # ord('❯')


YAXIS: tuple[int, int]    = (UP, DOWN)
XAXIS: tuple[int, int]    = (LEFT, RIGHT)
ARROWS: tuple             = (*YAXIS, *XAXIS)
CONCLUDE: tuple[int, int] = (ENTER, ESC)
ESCAPE: tuple[int, int]   = (ESC, PADMINUS)
COMPARE: tuple[int, int]  = (LESS, GREATER)

MSLTH_ORDS: list = [
    ALT_C, ALT_A, ALT_Q, ALT_E, ALT_W, ALT_I, ALT_O,
    ALT_U, ALT_Y, ALT_V, ALT_H, ALT_S, FN_I
    ]
MSLTH_STRS: list = ['ϥ', 'α', 'ᾱ', 'ɢ', 'ē', 'ι', 'ō', 'υ', 'ῡ', 'ν', 'ʯ', 'δ', 'ῑ']
MUSSELAITH: dict = {k: v for k, v in zip(MSLTH_ORDS, MSLTH_STRS)}


SPECIALS_REF: tuple = ('ALT', 'CTL', 'SHF', 'F', 'PAD')
special_keys: list  = [WAIT, NULL, TAB, ENTER, ESC, BACK, DEL,
                    LEFT, RIGHT, UP, DOWN, HOME, END]
special_keys += [y for x, y in vars().items() if x.startswith(SPECIALS_REF)]
SPECIAL: list       = special_keys