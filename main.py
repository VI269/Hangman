import random
import time
import os
from colorama import Fore
import colorama

colorama.init()

def clearConsole():
    os.system('clear')

def prompt(pr):
    return input(pr)

def display(text):
    print(text)

def wait():
    time.sleep(1)

def choose_the_word():
    with open('words.txt') as f:
        lst = f.read().split(',')
    return random.choice(lst).lower()

def get_guess(let):
    return prompt(f"{Fore.BLUE}Guess a Word({let} Letters) > ").lower()

def main():
    while True:
        clearConsole()
        word = choose_the_word()
        while True:
            guess = get_guess(len(word))
            clearConsole()
            correct = 0
            if len(word) == len(guess):
                for glet in guess:
                    if glet in word:
                        if word.index(glet) == guess.index(glet):
                            correct += 1
                            display(f"{Fore.GREEN}{glet.upper()}")
                        else:
                            display(f"{Fore.YELLOW}{glet.upper()}")
                    else:
                        display(f"{Fore.RED}{glet.upper()}")
                wait()
                clearConsole()
                if correct == len(word):
                    display(f"{Fore.GREEN}All Correct.")
                    wait()
                    clearConsole()
                    break
                elif correct == 0:
                    display(f"{Fore.RED}All Wrong.")
                    wait()
                    clearConsole()
                    continue
                else:
                    display(f"{Fore.YELLOW}Some Correct.")
                    wait()
                    clearConsole()
                    continue
            else:
                display("Wrong # of letters.")
                wait()
                clearConsole()
                break

if __name__ == '__main__':
    main()
