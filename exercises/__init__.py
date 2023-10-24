"""test"""
name: str = input("Name? ")

if len(name) > 6:
    print("Do you have a nickname")
elif name == "Jess": 
    print("I love COMP 110")
else:
    print("Nice to meet you, " + name)