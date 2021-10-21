import random


num_digits = 3
max_guesses = 10


def main():
    print(f""" 
    Bagels is  a deductive logic game 

    I am thinking of a {num_digits} - digit number with no repeated digits.
    Try to guess what it is .Here are some clues:
    when i say:     Means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position. 
    Bagels          No digit is correct
     eg: if secret number 248 and you guess is 843 the clues would be  Fermi Pico
    """)

    while True:

        # storing the secret number
        secret_number = getSecretNum()
        print("I have a secret number ")
        print(f"you have {max_guesses} guesses to get it")

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess # {numGuesses}')
                guess = input('>')

            clues = getClues(guess, secret_number)
            print(clues)
            numGuesses += 1

            if guess == secret_number:
                break
            if numGuesses > max_guesses:

                print("You ran out of guesses.")
                print(f"The answer was {secret_number}")

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secret_number):

    if guess == secret_number:
        return "You got it !"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
