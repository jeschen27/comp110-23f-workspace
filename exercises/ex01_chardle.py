"""My second program for COMP 110! Wordle!"""
__author__ = "730658911"
word = str(input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5 characters ")
    exit()
letter = str(input("Enter a single character: "))
if len(letter) != 1:
    print("Error: enter only one character ")
    exit()
print("Searching for " + letter + " in " + word)
number_of_instances = 0
if letter == word[0]:
    print(letter + " found at index 0")
    number_of_instances = number_of_instances + 1

if letter == word[1]:
    print(letter + " found at index 1")
    number_of_instances = number_of_instances + 1

if letter == word[2]:
    print(letter + " found at index 2")
    number_of_instances = number_of_instances + 1

if letter == word[3]:
    print(letter + " found at index 3")
    number_of_instances = number_of_instances + 1

if letter == word[4]:
    print(letter + " found at index 4")
    number_of_instances = number_of_instances + 1

if number_of_instances == 0:
    print("No instances of " + letter + " found in " + word)
if number_of_instances == 1:
    print(str(number_of_instances) + " instance of " + letter + " found in " + word)
if number_of_instances > 1:
    print(str(number_of_instances) + " instances of " + letter + " found in " + word)