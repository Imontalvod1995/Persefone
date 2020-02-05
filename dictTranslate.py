#####################################################
#                 dictTranslate.py                  #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# Translation of the classes to the characters.     #
#                                                   #
#####################################################

def numberToLabel(number):
    switcher = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "ae",
        11: "am",
        12: "a",
        13: "b",
        14: "con",
        15: "c",
        16: "d",
        17: "em",
        18: "e",
        19: "et",
        20: "f",
        21: "g",
        22: "h",
        23: "i",
        24: "l",
        25: "m",
        26: "n",
        27: "o",
        28: "prae",
        29: "per",
        30: "pro",
        31: "p",
        32: "q",
        33: "r",
        34: "s",
        35: "t",
        36: "tur",
        37: "um",
        38: "u",
        39: "v",
        40: "x",
        41: "y",
        42: "z",
    }
    return switcher.get(number, "Char not found!")
