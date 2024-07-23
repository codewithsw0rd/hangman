# Hangman
import random

words =("apple", "ball", "cat", "dog", "elephant")

# dictionary of key
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O  ",
                   "   ",
                   "   "),
               2: (" O  ",
                   " |  ",
                   "   "),
               3: ("   ",
                   "   ",
                   "   "),
               4: ("   ",
                   "   ",
                   "   "),
               5: ("   ",
                   "   ",
                   "   "),
               6: ()}