"""My third COMP 110 program!! Actual Wordle!!"""
__author__ = "730658911"
secret = "python"
secret_length: str = str(len(secret))
guess = input(f"What is your {secret_length}-letter guess? ")
# variable "checking" indicates which index of the input word is being checked
checking: int = 0
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
result = ""
while len(guess) != int(secret_length):
    guess = input(f"That was not {secret_length} letters! Try again: ")
# counter = 0
"""while counter<=5:
    check secret[counter] == guess[counter]
"""
while checking != len(secret):
    j = 0
    if secret[checking] == guess[checking]:
        result = result + green_box
        checking = checking + 1
    else: 
        # j is the variable that represents other indices to check
        q = 0
        while j < len(secret):
            if guess[checking] == secret[j]:
                result = result + yellow_box
                j += 1
                q += 1
            else:
                j = j + 1
        if q == 0:
            result = result + white_box
        checking = checking + 1
print(result)
if guess == secret:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")