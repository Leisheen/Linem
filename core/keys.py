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

ENTER           = 13

SHF             = 16
CTL             = 17
ALT             = 18
BKM             = 20       # Block Mayus

ESC             = 27

SPACE           = 32

# NAV PAGES
PPAGE           = 33        # PREVIOUS PAGE
NPAGE           = 34        # NEXT PAGE
END             = 35        # KEY_END
HOME            = 36        # KEY_HOME

# ARROWS
LEFT            = 37       # KEY_LEFT
UP              = 38       # KEY_UP
RIGHT           = 39       # KEY_RIGHT
DOWN            = 40       # KEY_DOWN

INS             = 45
DEL             = 46

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
F1              = 112       # KEY_F1
F2              = 113       # KEY_F2
F3              = 114       # KEY_F3
F4              = 115       # KEY_F4
F5              = 116       # KEY_F5
F6              = 117       # KEY_F6
F7              = 118       # KEY_F7
F8              = 119       # KEY_F8
F9              = 120       # KEY_F9
F10             = 121       # KEY_F10
F11             = 122       # KEY_F11
F12             = 123       # KEY_F12

NUMLOCK         = 144

PLUS            = 187       # ord('+')
COMMA           = 188       # ord(',')
MINUS           = 189       # ord('-')
POINT           = 190       # ord('.')
CEDILLA         = 191       # ord('ç')


# SPECIAL CHARACTERS
QUESTION        = 219       # ?/'
ORD             = 220       # º/ª
ADMIRE          = 221       # ¡/¿
COMPARE         = 226       # </>

# SEPARATORS
HSEP            = 9472      # ord('─') / '\u2500' / HORIZONTAL_SEP ?
VSEP            = 9474      # ord('│') / '\u2505' / VERTICAL_SEP ?

PROMPT          = 10095     # ord('❯')


VERTICAL        = (UP, DOWN)
HORIZONTAL      = (LEFT, RIGHT)
ARROWS          = (*VERTICAL, *HORIZONTAL)
CONCLUDE        = (ENTER, ESC)
ESCAPE          = (ESC, PADMINUS)

SPECIALS_REF    = ('ALT', 'CTL', 'SHF', 'F', 'PAD')
special_keys    = [WAIT, NULL, TAB, ENTER, ESC, BACK, DEL,
                    LEFT, RIGHT, UP, DOWN, HOME, END]
special_keys    += [y for x, y in vars().items() if x.startswith(SPECIALS_REF)]
SPECIAL         = special_keys