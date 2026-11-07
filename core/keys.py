"""Keyboard constants for Lιuemαg Stαuνor."""
# Name    |  Code point  |  Other 

# -- NATIVE --

# SPECIAL KEYS
WAIT            = -1
NULL            = 0         # ord('\0')
SOH             = 1         # ord('\1') Start of heading
STX             = 2         # ord('\2') Start of text
ETX             = 3         # ord('\3') End of text
CTL_C           = 3

BACK            = 8         # 0o10
TAB             = 9         # ord('\t')

PAD5            = 12
ENTER           = 13

SHF             = 16
CTL             = 17
ALT             = 18
BKM             = 20       # BLOCK MAYUS

ESC             = 27

SPACE           = 32

# NAV PAGES
PREV            = 33
NEXT            = 34
END             = 35
HOME            = 36

# ARROWS
LEFT            = 37
UP              = 38
RIGHT           = 39
DOWN            = 40

INS             = 45
DEL             = 46
#POINT           = 46       # ord('.')
# NUMBERS
NUM0            = 48        # ord('0')
NUM1            = 49        # ord('1')
NUM2            = 50        # ord('2')
NUM3            = 51        # ord('3')
NUM4            = 52        # ord('4')
NUM5            = 53        # ord('5')
NUM6            = 54        # ord('6')
NUM7            = 55        # ord('7')
NUM8            = 56        # ord('8')
NUM9            = 57        # ord('9')

# LITERALS
LIT_A           = 65        # a/A
LIT_B           = 66        # b/B
LIT_C           = 67        # c/C
LIT_D           = 68        # d/D
LIT_E           = 69        # e/E
LIT_F           = 70        # f/F
LIT_G           = 71        # g/G
LIT_H           = 72        # h/H
LIT_I           = 73        # i/I
LIT_J           = 74        # j/J
LIT_K           = 75        # k/K
LIT_L           = 76        # l/L
LIT_M           = 77        # m/M
LIT_N           = 78        # n/N
LIT_O           = 79        # o/O
LIT_P           = 80        # p/P
LIT_Q           = 81        # q/Q
LIT_R           = 82        # r/R
LIT_S           = 83        # s/S
LIT_T           = 84        # t/T
LIT_U           = 85        # u/U
LIT_V           = 86        # v/V
LIT_W           = 87        # w/W
LIT_X           = 88        # x/X
LIT_Y           = 89        # y/Y
LIT_Z           = 90        # z/Z
LIT_SPN         = 192       # ñ/Ñ

# PAD
PADSTAR         = 106
PADPLUS         = 107
PADMINUS        = 109
PADSLASH        = 111

# FKEYS
F1              = 112
F2              = 113
F3              = 114
F4              = 115
F5              = 116
F6              = 117
F7              = 118
F8              = 119
F9              = 120
F10             = 121
F11             = 122
F12             = 123

#DEL             = 127      # ord('\x7f') / KEY_BACKSPACE

NUMLOCK         = 144

FORWARDS        = 176
BACKWARDS       = 177
STOP            = 178
PLAY            = 179

#ORD             = 186       # ord('º') / ord('ª')
DIERECIS        = 186       # `
PLUS            = 187       # ord('+')
COMMA           = 188       # ord(',')
MINUS           = 189       # ord('-')
POINT           = 190       # ord('.')
CEDILLA         = 191       # ord('ç')

# SPECIAL CHARACTERS
QUESTION        = 219       # ?/'
ORD             = 220       # º/ª   # Virtual key
ADMIRE          = 221       # ¡/¿
ACCENT          = 222       # ´
LESS            = 226       # </>


# SHIFT         (+250)
SHF_TAB         = 259
SHF_ENTER       = 263
SHF_PREV        = 283
SHF_NEXT        = 284
SHF_END         = 285
SHF_HOME        = 286
SHF_LEFT        = 287
SHF_UP          = 288
SHF_RIGHT       = 289
SHF_DOWN        = 290

SHF_F1          = 362
SHF_F2          = 363
SHF_F3          = 364
SHF_F12         = 373
SHF_PADPLUS     = 357
SHF_PADMINUS    = 359
SHF_PLUS        = 437

GREATER         = 476       # </>

# CTRL          (+500)
CTL_ENTER       = 513
CTL_INS         = 545
CTL_DEL         = 546
CTL_PADSLASH    = 611
CTL_PREV        = 533
CTL_NEXT        = 534
CTL_END         = 535
CTL_HOME        = 536
CTL_LEFT        = 537
CTL_UP          = 538
CTL_RIGHT       = 539
CTL_DOWN        = 540

# ALT           (+750)
ALT_BACK        = 758
ALT_LEFT        = 787
ALT_UP          = 788
ALT_RIGHT       = 789
ALT_DOWN        = 790

ALT_DEL         = 796
ALT_PADSLASH    = 861
ALT_A           = 815
ALT_B           = 816
ALT_C           = 817
ALT_D           = 818
ALT_E           = 819
ALT_F           = 820
ALT_G           = 821
ALT_H           = 822
ALT_I           = 823
ALT_J           = 824
ALT_K           = 825
ALT_L           = 826
ALT_M           = 827
ALT_N           = 828
ALT_O           = 829
ALT_P           = 830
ALT_Q           = 831
ALT_R           = 832
ALT_S           = 833
ALT_T           = 834
ALT_U           = 835
ALT_V           = 836
ALT_W           = 837
ALT_X           = 838
ALT_Y           = 839
ALT_Z           = 840

ALT_F1          = 862
ALT_F2          = 863
ALT_F12         = 873
ALT_ORD         = 970


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


LEFT_ARROW      = 8594      # ord('→')

# SEPARATORS
HSEP            = 9472      # ord('─') / '\u2500' / HORIZONTAL_SEP ?
VSEP            = 9474      # ord('│') / '\u2505' / VERTICAL_SEP ?

PROMPT          = 10095     # ord('❯')


YAXIS           = (UP, DOWN)
XAXIS           = (LEFT, RIGHT)
ARROWS          = (*YAXIS, *XAXIS)
CONCLUDE        = (ENTER, ESC)
ESCAPE          = (ESC, PADMINUS)
COMPARE         = (LESS, GREATER)

MSLTH_ORDS = [
    ALT_C, ALT_A, ALT_Q, ALT_E, ALT_W, ALT_I, ALT_O,
    ALT_U, ALT_Y, ALT_V, ALT_H, ALT_S, FN_I
    ]
MSLTH_STRS = ['ϥ', 'α', 'ᾱ', 'ɢ', 'ē', 'ι', 'ō', 'υ', 'ῡ', 'ν', 'ʯ', 'δ', 'ῑ']
MUSSELAITH = {k: v for k, v in zip(MSLTH_ORDS, MSLTH_STRS)}


SPECIALS_REF    = ('ALT', 'CTL', 'SHF', 'F', 'PAD')
special_keys    = [WAIT, NULL, TAB, ENTER, ESC, BACK, DEL,
                    LEFT, RIGHT, UP, DOWN, HOME, END]
special_keys    += [y for x, y in vars().items() if x.startswith(SPECIALS_REF)]
SPECIAL         = special_keys