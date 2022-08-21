import os
import string
os.system("clear")

# Create Strings From Characters problem from ProgrammingExpert.io

def create_strings_from_characters(frequencies, string1, string2):
    string3 = string1 + string2
    can_create_string1 = can_create_strings(frequencies, string1)
    can_create_string2 = can_create_strings(frequencies, string2)
    can_create_string3 = can_create_strings(frequencies, string3)

    if (not can_create_string1) or (not can_create_string2):
        if can_create_string1 or can_create_string2:
            return 1
        return 0

    elif  not can_create_string3:
        return 1
    return 2


def can_create_strings(dict, string):
    for letter in set(string):
        if string.count(letter) > dict.get(letter, 0):
            return False

    return True

# Test case
frequencies = {
    "h": 2, 
    "e": 1, 
    "l": 3, 
    "r": 4, 
    "a": 3, 
    "o": 1, 
    "d": 1, 
    "w": 1
    }
        
string1 = "hello"
string2 = "world"

print(create_strings_from_characters(frequencies,string1, string2))