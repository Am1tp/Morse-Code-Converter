from mcdict import Morse_Code_Bank


def convert():
    print()  # ensures that prompt for next new input starts on a new line
    user_input = input('Please enter input to convert (a-z, 0-9):\n').upper()

    if user_input == '-EXIT':
        exit()

    user_input = list(user_input)

    for char in user_input:
        if char not in Morse_Code_Bank.keys():
            print(char, sep=" ", end="", flush=True)
        else:
            print(Morse_Code_Bank.get(char), sep=" ", end="", flush=True)

    convert()


convert()
