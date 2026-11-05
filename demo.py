# Escape Characters
print("Dear class, \nThis is unfortunately our last day of python.")

# Absolute v Relative paths.
# data/data.txt relative to where your current working directory
# Absolute paths start from "Home" /users/JackP

# Modules and Libraries
import random 

random_int = random.randint(1,10)
print(random_int)

deck_of_cards = ["King of Spades", "8 of Hearts", "2 of Diamonds"]
random_card = random.choice(deck_of_cards)
print(random_card)

import math

answer = math.sqrt(64)
print(answer)

# File I/O
# Reading, Writing, Append
with open("demo.txt", "a") as file:
    file.write("File I/O is soooo fun!\n ")

# To add to the file, "w" must be changed to "a"