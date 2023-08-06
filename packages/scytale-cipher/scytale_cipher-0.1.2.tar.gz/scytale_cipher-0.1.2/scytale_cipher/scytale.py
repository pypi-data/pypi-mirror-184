#! /usr/bin/env python

from math import ceil


def scytale_process(input: str, diameter: int) -> str:
    """
    process encoding or decoding of a string.

    :input: user input string
    :diameter: user diameter or default

    :returns: with scytale encoded string

    """
    out = str()

    for y in range(0, diameter):
        out += input[y::diameter]
    return out


def scytale_init(input: str, diameter: int, mode: int) -> str:
    """
    prepare process of scytale mode

    :input: user input string
    :diameter: user diameter or default
    :mode: bool to predict if input has to be encoded or decoded

    :returns: encoded or decoded string

    """
    input = str(input)
    if mode == 1:
        diameter = ceil(len(input) / diameter)
    return scytale_process(input, diameter)


def main_menu(menu: str) -> None:
    """
    enters the cli-wizard menu loop

    :menu: menu prompt string

    """
    mode = ["encoded", "decoded"]

    while True:
        print(menu)
        user_input = input("Enter your selection:[0] \n")
        try:
            user_input = int(user_input)
        except ValueError:
            if user_input not in ["", "0"]:
                print(
                    f"\n'{user_input}' is not a number. Continuing with 0.\n")
            user_input = 0

        if user_input == 2:
            break
        elif user_input not in [0, 1]:
            print(f"\n'{user_input}' is not a valid entry. Try again!\n")
        else:
            user_string = str(
                input(f"\nPlease enter a string to be {mode[user_input]}: \n"))
            user_diameter = input("\nPlease enter a diameter:[2] \n")
            try:
                user_diameter = int(user_diameter)
            except ValueError:
                if user_input not in ["", "2"]:
                    print(
                        f"\n'{user_diameter}' is not a number. Continuing with 2.\n"
                    )
                user_diameter = 2
            print(f"\nYour {mode[user_input]} string:\n '" +
                  scytale_init(user_string, user_diameter, user_input) + "'\n")


def menu_entries() -> str:
    menu = """What do you wanna do?\n
    [0] Encode a given string (default)\n
    [1] Decode a given string\n
    [2] I wanna go to Rio (exit)\n"""

    return menu


def main() -> None:
    menu = menu_entries()
    main_menu(menu)
    print("\nCya next time! Bye!")


if __name__ == '__main__':
    main()
