import string

def alphabet_position(letter):
    if letter.islower() == True:
        pos = list(string.ascii_lowercase).index(letter)

    if letter.isupper() == True:
        pos = list(string.ascii_uppercase).index(letter)

    return pos

def rotate_character(char, rot):
    lo = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_int = (alphabet_position(char) + rot) % 26
    if char.islower() == True:
        return lo[new_int]
    if char.isupper() == True:
        return up[new_int]

def encrypt(text, rot):
    output = ""
    for i in text:
        if i.isalpha() == True:
            lett = rotate_character(i, rot)
            output += lett
        else:
            output += i
    return output
