def odd_and_even(x: list[int]) -> list[int]:
    i: int = 0
    new_list: list[int] = []
    while i < len(x):
        if i % 2 == 0 and x[i] % 2 != 0:
            new_list.append(x[i])
        i += 1
    return new_list