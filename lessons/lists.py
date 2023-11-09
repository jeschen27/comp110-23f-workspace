"""Practice with lists."""
grocery_list: list[str] = list()

grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[1] = "cereal"
grocery_list.pop(2)
print(grocery_list)

cool_numbers: list[int] = list()
cool_numbers.append(2)
cool_numbers.append(3)
cool_numbers.pop(1)
print(len(cool_numbers))