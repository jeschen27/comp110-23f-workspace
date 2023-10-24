""" def input_guess(idx: int):
    wordd: input(f"Enter a {idx} letter word: ")
    while len(wordd) != idx:
        wordd: input(f"That wasn't {idx} chars. Try again: ")
    return wordd """

# ---------------------------------------------

# Loops Example 2
"""pets: list[str] = ["Louie","Bo","Bear"]
for name in pets:
    print(f"Good boy, {name}!")"""

# --------------------------------------------------
# Using rang() in a for ... in ... loop
"""names: list[str] = ["Alyssa","Janet","Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
    
    #ORRRRR

names: list[str] = ["Alyssa","Janet","Vrinda"]
for idx in range(0, len(names)):
    elem: str = names[idx]
    print(f"{idx}: {elem}")"""

# --------------------------------------------------

