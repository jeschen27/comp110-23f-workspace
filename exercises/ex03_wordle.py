"""My fourth COMP 110 program!! Structured Wordle!!"""
__author__ = "730658911"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Indicates whether a character is found at any given index in a word."""
    assert len(char) == 1
    i = 0
    while i < len(word):
        if word[i] == char:
            return True
        else: 
            i += 1 
    return False


def emojified(guess: str, secret: str) -> str:
    """Compares the letters of two equal-lengthed words and creates an array of colored blocks like wordle."""
    i = 0
    result = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            result = result + green_box
        elif contains_char(secret, guess[i]) is True:
            result = result + yellow_box
        else:
            result = result + white_box
        i = i + 1
    return result


def input_guess(idx: int) -> str:
    """Prompts the user for a word that is the length that they indicated."""
    wordd = (input(f"Enter a {idx} character word: "))
    while len(wordd) != idx:
        wordd = (input(f"That wasn't {idx} chars! Try again: "))
    return wordd


def main() -> None:
    """Basically combines all of our previous functions."""
    secret = "codes"
    turn = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        v = str(input_guess(len(secret)))
        wordle = emojified(v, secret)
        print(wordle)
        if v == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        else:
            turn += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()