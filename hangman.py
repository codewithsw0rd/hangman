# Hangman
import random

words =("apple", "ball", "cat", "dog", "elephant")

# dictionary of key
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O  ",
                   " | ",
                   "   "),
               3: (" O ",
                   "/| ",
                   "   "),
               4: (" O ",
                   "/|\\",
                   "   "),
               5: (" O ",
                   "/|\\",
                   "/  "),
               6: (" O ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_answer):
    pass

def hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    print(hint)

if __name__ == '__main__':
    main()
