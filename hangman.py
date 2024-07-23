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

def display_man(wrong_ans):
    pass

def hint(hint):
    pass

def display_ans(ans):
    pass

def main():
    ans = random.choice(words)
    print(ans)

if __name__ == "__name__":
    main()
