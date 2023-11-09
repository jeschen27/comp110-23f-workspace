def value_exists(test_dict: dict[str, int], test_val: int) -> bool:
    for elem in test_dict:
        if test_dict[elem] == test_val:
            return True
    return False

test_dict: dict[str, int] = {"a": 2, "b": 4, "c": 7, "d": 1}
test_val: int = 4
print(value_exists(test_dict, test_val))