"""Keyboard constants for Lιuemαg Stαuνor."""
# Name    |  Code point  |  Other 
WAIT            = -1
NULL            = 0         # ord('\0')
SOH             = 1         # ord('\1') Start of heading
STX             = 2         # ord('\2') Start of text
ETX             = 3         # ord('\3') End of text
CTL_C           = 3

# SPECIAL KEYS
BACK            = 8         # 0o10
TAB             = 9         # ord('\t')
ENTER           = 10
ESC             = 27

STAR            = 42        # ord('*')
PLUS            = 43        # ord('+')
COMMA           = 44        # ord(',')
MINUS           = 45        # ord('-')
POINT           = 46        # ord('.')

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

# SPECIAL CHARACTERS
LESS            = 60        # <
GREATER         = 62        # >
QUESTION        = 63        # ?

# UPPER ALPHA
UPPER_A         = 65        # ord('A')
UPPER_B         = 66        # ord('B')
UPPER_D         = 68        # ord('D')
UPPER_I         = 73        # ord('I')
UPPER_M         = 77        # ord('M')
UPPER_O         = 79        # ord('M')
UPPER_Q         = 81        # ord('Q')
UPPER_T         = 84        # ord('T')
UPPER_V         = 86        # ord('V')
UPPER_Y         = 89        # ord('Y')

BSLASH          = 92        # ord('\\')
UNDERSCORE      = 95        # ord('_')

# LOWER ALPHA
LOWER_A         = 97        # ord('a')
LOWER_B         = 98        # ord('b')
LOWER_D         = 100       # ord('d')
LOWER_I         = 105       # ord('i')
LOWER_M         = 109       # ord('m')
LOWER_O         = 111       # ord('q')
LOWER_Q         = 113       # ord('q')
LOWER_T         = 116       # ord('t')
LOWER_V         = 118       # ord('v')
LOWER_Y         = 121       # ord('y')

# ORDINALS
ORD_A           = 170       # ord('ª')
ORD_O           = 186       # ord('º')
UPPER_CED       = 199       # ord('Ç')

LOWER_CED       = 231       # ord('ç')

# ARROWS
DOWN            = 258       # KEY_DOWN
UP              = 259       # KEY_UP
LEFT            = 260       # KEY_LEFT
RIGHT           = 261       # KEY_RIGHT

HOME            = 262       # ord('Ć') / KEY_HOME
END             = 358       # ord('Ŧ') / KEY_END
# ↳ NO IDEA WHAT KEY IS THIS BUT RETURNS ' → ' IN VERMAT

# FUNCTION
F1              = 265       # KEY_F1
F2              = 266       # ..
F3              = 267
F4              = 268
F5              = 269
F6              = 270
F7              = 271
F8              = 272
F9              = 273
F10             = 274
F11             = 275
F12             = 276
SHF_F1          = 277       # ord('ĕ') / KEY_F13
SHF_F2          = 278       # ord('Ė')
SHF_F3          = 279       # ord('ė')
SHF_F4          = 280       # ord('Ę')
SHF_F12         = 288

# ALT FUNCTION
ALT_F1          = 301       # ord('ĭ') / KEY_F37
ALT_F2          = 302       # ord('Į')
ALT_F3          = 303       # ord('į')
ALT_F5          = 305       # ord('ı')
ALT_F6          = 306       # ord('Ĳ')
ALT_F12         = 312

DEL             = 330       # KEY_DC

# NAV PAGES
NPAGE           = 338       # ord('Œ')
PPAGE           = 339       # ord('œ')

SHF_TAB         = 351       # ord('ş')
SLEFT           = 391       # ord('Ƈ') / KEY_SLEFT
SRIGHT          = 400       # ord('Ɛ') / KEY_SRIGHT
FN_I            = 331       # ord('ŋ') / KEY_IC
SHF_END         = 384       # ord('ƀ') / KEY_SEND
SHF_NEXT        = 394       # ord('Ɗ')
SHF_PREVIOUS    = 396       # ord('ƌ')

# ALT ALPHA
ALT_0           = 407       # ord('Ɨ')
ALT_5           = 412       # ord('Ɯ')
ALT_A           = 417       # ord('ơ')
ALT_C           = 419       # ord('ƣ')
ALT_E           = 421       # ord('ƥ')
ALT_H           = 424       # ord('ƨ')
ALT_I           = 425       # ord('Ʃ')
ALT_L           = 428       # ord('Ƭ')
ALT_M           = 429       # ord('ƭ')
ALT_O           = 431       # ord('Ư')
ALT_P           = 432       # ord('ư')
ALT_Q           = 433       # ord('Ʊ')
ALT_R           = 434       # ord('Ʋ')
ALT_S           = 435       # ord('Ƴ')
ALT_U           = 437       # ord('Ƶ')
ALT_V           = 438       # ord('ƶ')
ALT_W           = 439       # ord('Ʒ')
ALT_Y           = 441       # ord('ƹ')

# CLT HORIZONTAL
CTL_LEFT        = 443       # ord('ƻ')
CTL_RIGHT       = 444       # ord('Ƽ')
CTL_PGUP        = 445       # ord('ƽ')
CTL_PGDOWN      = 446       # ord('ƾ')

# PAD
PAD7            = 449       # ord('ǁ') / KEY_A1
PAD8            = 450       # ord('ǂ') / KEY_A2
PAD9            = 451       # ord('ǃ') / KEY_A3
PAD4            = 452       # ord('Ǆ') / KEY_B1
PAD5            = 453       # ord('ǅ') / KEY_B2
PAD6            = 454       # ord('ǆ') / KEY_B3
PAD1            = 455       # ord('Ǉ') / KEY_C1
PAD2            = 456       # ord('ǈ') / KEY_C2
PAD3            = 457       # ord('ǉ') / KEY_C3
PADSLASH        = 458       # ord('Ǌ')
PADENTER        = 459       # ord('ǋ')
CTL_PADENTER    = 460
PADSTOP         = 462       # ord('ǎ')
PADSTAR         = 463       # ord('Ǐ')
PADMINUS        = 464       # ord('ǐ')
PADPLUS         = 465       # ord('Ǒ')
CTL_PADSTOP     = 466
CTL_PADSLASH    = 470
ALT_PADSLASH    = 474       # ord('ǔ')
ALT_PADSTOP     = 476       # ord('ǜ')
ALT_DEL         = 478

# CTL VERTICAL
CTL_UP          = 480       # ord('Ǡ')
CTL_DOWN        = 481       # ord('ǡ')

# ALT NAV
ALT_PGUP        = 487       # ord('ǧ')
ALT_PGDN        = 488       # ord('Ǩ')
ALT_END         = 489

# ALT ARROWS
ALT_UP          = 490       # ord('Ǫ')
ALT_DOWN        = 491       # ord('ǫ')
ALT_RIGHT       = 492       # ord('Ǭ')
ALT_LEFT        = 493       # ord('ǭ')

ALT_BKSP        = 504       # ord('Ǹ')

# CTRL PAD
PAD0            = 506       # ord('Ǻ')
CTL_PAD0        = 507       # ord('ǻ')
CTL_PAD1        = 508       # ord('Ǽ')
CTL_PAD2        = 509       # ord('ǽ')
CTL_PAD3        = 510       # ord('Ǿ')
CTL_PAD4        = 511       # ord('ǿ')
CTL_PAD5        = 512       # ord('Ȁ')
CTL_PAD6        = 513       # ord('ȁ')
CTL_PAD7        = 514       # ord('Ȃ')
CTL_PAD8        = 515       # ord('ȃ')
CTL_PAD9        = 516       # ord('Ȅ')

# ALT PAD
ALT_PAD0        = 517       # ord('ȅ')
ALT_PAD1        = 518       # ord('Ȇ')
ALT_PAD2        = 519       # ord('ȇ')
ALT_PAD3        = 520       # ord('Ȉ')
ALT_PAD4        = 521       # ord('ȉ')
ALT_PAD5        = 522       # ord('Ȋ')
ALT_PAD6        = 523       # ord('ȋ')
ALT_PAD7        = 524       # ord('Ȍ')
ALT_PAD8        = 525       # ord('ȍ')
ALT_PAD9        = 526       # ord('Ȏ')

ALT_BSLASH      = 528
CTL_ENTER       = 529       # ord('ȑ')
SHF_ENTER       = 530       # ord('Ȓ')

# SHIFT PAD
SHF_PADENTER    = 530
SHF_PADSLASH    = 531
SHF_PADSTAR     = 532
SHF_PADPLUS     = 533
SHF_PADMINUS    = 534

SUP             = 547       # ord('ȣ') / KEY_SUP
SDOWN           = 547       # ord('Ȥ') / KEY_SDOWN

MAC_GREEKU      = 8191      # ord('ῡ')

LEFT_ARROW      = 8594      # ord('→')

# SEPARATORS
HSEP            = 9472      # ord('─') / '\u2500' / HORIZONTAL_SEP ?
VSEP            = 9474      # ord('│') / '\u2505' / VERTICAL_SEP ?

PROMPT          = 10095     # ord('❯')


VERTICAL        = (UP, DOWN)
HORIZONTAL      = (LEFT, RIGHT)
ARROWS          = (*VERTICAL, *HORIZONTAL)
SEND            = (ENTER, PADENTER)
CONCLUDE        = (ENTER, ESC)
ESCAPE          = (ESC, PADMINUS)
COMPARE         = (LESS, GREATER)

PAD_VALS = [PAD1, PAD2, PAD3, PAD4, PAD5, PAD6, PAD7, PAD8, PAD9, PAD0]
PAD = {k: (f'{(i + 1) % 10}', i) for i, k in enumerate(PAD_VALS)}

LOGPAD_VALS = [CTL_PAD5, CTL_PAD0, ALT_PAD5, ALT_PAD0, ALT_5, ALT_0]
LOGPAD = {k: 14 + v * 5 for v, k in enumerate(LOGPAD_VALS)}

MSLTH_ORDS = [
    ALT_C, ALT_A, ALT_Q, ALT_E, ALT_W, ALT_I, ALT_O,
    ALT_U, ALT_Y, ALT_V, ALT_H, ALT_S, FN_I
    ]
MSLTH_STRS = ['ϥ', 'α', 'ᾱ', 'ɢ', 'ē', 'ι', 'ō', 'υ', 'ῡ', 'ν', 'ʯ', 'δ', 'ῑ']
MUSSELAITH = {k: v for k, v in zip(MSLTH_ORDS, MSLTH_STRS)}

O_ORDS = (ORD_O, SHF_PADSTAR)

PAD_KEYS = (*PAD, *LOGPAD)

SPECIALS_REF    = ('ALT', 'CTL', 'SHF', 'F', 'PAD')
special_keys    = [WAIT, NULL, TAB, ENTER, ESC, BACK, DEL,
                    ALT_DEL, LEFT, RIGHT, UP, DOWN, HOME, END]
special_keys    += [y for x, y in vars().items() if x.startswith(SPECIALS_REF)]
SPECIAL         = special_keys