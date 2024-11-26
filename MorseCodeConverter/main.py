Morse_Code_Bank = {
    'A': 'O -',
    'B': '- O O O',
    'C': '- O - O',
    'D': '- O O',
    'E': 'O',
    'F': 'O O - O',
    'G': '- - O',
    'H': 'O O O O',
    'I': 'O O ',
    'J': 'O - - -',
    'K': '- O -',
    'L': 'O - O O',
    'M': '- -',
    'N': '- O',
    'O': '- - -',
    'P': 'O - - O',
    'Q': '- - O -',
    'R': 'O - O',
    'S': 'O O O',
    'T': '-',
    'U': 'O O -',
    'V': 'O O O -',
    'W': 'O - -',
    'X': '- O O -',
    'Y': '- O - -',
    'Z': '- - O O',
    '1': 'O - - - -',
    '2': 'O O - - -',
    '3': 'O O O - -',
    '4': 'O O O O -',
    '5': 'O O O O O',
    '6': '- O O O O',
    '7': '- - O O O',
    '8': '- - - O O',
    '9': '- - - - O',
    '0': '- - - - -',
    " ": '       '
}


def convert():
    user_input = list(input('Please enter input to convert (a-z, 0-9): \n').upper())
    for char in user_input:
        if char in Morse_Code_Bank.keys():
            print(Morse_Code_Bank.get(char), sep=" ", end="", flush=True)


convert()
