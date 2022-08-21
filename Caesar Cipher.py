# Caesar Cipher problem from ProgrammingExpert.io

def caesar_cipher(string, offset):

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_string = list(string)

    for character in range(len(new_string)):
        idx = alphabet.index(new_string[character])
        new_idx = idx - offset
        new_letter = alphabet[new_idx]
        new_string[character] = new_letter

    joined_string = "".join(new_string)

    return joined_string

# Test case
print(caesar_cipher("bowling", 3))