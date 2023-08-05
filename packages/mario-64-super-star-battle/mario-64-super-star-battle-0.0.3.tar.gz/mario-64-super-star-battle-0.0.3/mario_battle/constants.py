"""Contains constants for the program."""

# Technically 16-18 aren't courses proper, but to keep things simple
# we've included them with the other courses
COURSE_DICTIONARY = {
    1: {"name": "Bob-omb Battlefield", "played": False},
    2: {"name": "Whomp's Fortress", "played": False},
    3: {"name": "Jolly Roger Bay", "played": False},
    4: {"name": "Cool, Cool Mountain", "played": False},
    5: {"name": "Big Boo's Haunt", "played": False},
    6: {"name": "Hazy Maze Cave", "played": False},
    7: {"name": "Lethal Lava Land", "played": False},
    8: {"name": "Shifting Sand Land", "played": False},
    9: {"name": "Dire, Dire Docks", "played": False},
    10: {"name": "Snowman's Land", "played": False},
    11: {"name": "Wet-Dry World", "played": False},
    12: {"name": "Tall, Tall Mountain", "played": False},
    13: {"name": "Tiny, Huge Island", "played": False},
    14: {"name": "Tick Tock Clock", "played": False},
    15: {"name": "Rainbow Ride", "played": False},
    16: {"name": "Bowser in the Dark World", "played": False},
    17: {"name": "Bowser in the Fire Sea", "played": False},
    18: {"name": "Bowser in the Sky", "played": False},
}

# Thanks to whoever made this!
MARIO_ASCII_ART = """__▒▒▒▒▒
—-▒▒▒▒▒▒▒▒▒
—–▓▓▓░░▓░
—▓░▓░░░▓░░░
—▓░▓▓░░░▓░░░
—▓▓░░░░▓▓▓▓
——░░░░░░░░
—-▓▓▒▓▓▓▒▓▓
–▓▓▓▒▓▓▓▒▓▓▓
▓▓▓▓▒▒▒▒▒▓▓▓▓
░░▓▒░▒▒▒░▒▓░░
░░░▒▒▒▒▒▒▒░░░
░░▒▒▒▒▒▒▒▒▒░░
—-▒▒▒ ——▒▒▒
–▓▓▓———-▓▓▓
▓▓▓▓———-▓▓▓▓
"""

# A string representing a tie
TIE = "tie"

# How much space (in characters) we should leave for a name. If the name
# is longer then the formatting might not be pretty.
MAX_NAME_LENGTH = 20
