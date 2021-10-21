#!/usr/bin/env python3


def correct(secret_number, user_input):
    secret_number = [int(x) for x in str(secret_number)]
    user_input = [int(y) for y in str(user_input)]
    if user_input == secret_number:
        return secret_number


def pico(secret_number, user_input):
    secret_number = [int(x) for x in str(secret_number)]
    user_input = [int(y) for y in str(user_input)]
    for i in user_input:
        if i in secret_number:
            return 'pico'


def fermi(secret_number, user_input):
    secret_number = [int(x) for x in str(secret_number)]
    user_input = [int(y) for y in str(user_input)]
    for i in range(len(secret_number)):
        for j in range(len(user_input)):
            if secret_number[i] == user_input[j] and i == j:
                return "fermi"


def bagels(secret_number, user_input):
    secret_number = [int(x) for x in str(secret_number)]
    user_input = [int(y) for y in str(user_input)]
    for i in user_input:
        if i not in secret_number:
            return 'bagels'


def main():
    secret_number = 345
    count = 0
    max_guess = 10
    print("Welcome to the guessing game")
    print("*"*50)
    print("There is a secret three digit number  you have 10 tries to guess it")
    print("*"*50)
    print("With every guess the output will guide you to the correct number  ")
    print("*"*50)
    print(f"This are the responses you get \n  \n PICO - when your guess has a correct digit in it \n \n FERMI - a correct digit in the correct place \n \n BAGELS - has no correct digits \n \n ex  exit the game")
    print("*"*50)
    print("Your input should be numbers  except for exit ")
    print("*"*50)

    while True:
        if count != max_guess:
            print("Enter your  Guess")
            user_input = input()
            if user_input.isdigit():
                    if correct(secret_number, user_input):
                        print(
                            f"Yes you got it {correct(secret_number,user_input)}")
                        break

                    elif fermi(secret_number, user_input):
                        count += 1
                        print(fermi(secret_number, user_input))

                    elif pico(secret_number, user_input):
                        count += 1
                        print(pico(secret_number, user_input))

                    elif bagels(secret_number, user_input):
                        count += 1
                        print(bagels(secret_number, user_input))

                    else:
                        break
            elif user_input =='ex':
                break       
            else:
                print("Not a valid input Read the instructions at the top")
        else:
            break


if __name__ == '__main__':
    main()
