def manual_index(n, a):
    for i in range(len(a)):
        if n == a[i]:
            return i
    return -1

def encode(cipher:str) -> str:
    alphabet_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    for letter in cipher:
        if letter in alphabet_lower:
            index = manual_index(letter, alphabet_lower)
            message += alphabet_lower[index + 13]
        elif letter in alphabet_upper:
            index = manual_index(letter, alphabet_upper)
            message += alphabet_upper[index + 13]
        else:
            message += letter
    return message

def decode(cipher:str) -> str:
    alphabet_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    for letter in cipher:
        if letter in alphabet_lower:
            index = manual_index(letter, alphabet_lower)
            message += alphabet_lower[index - 13]
        elif letter in alphabet_upper:
            index = manual_index(letter, alphabet_upper)
            message += alphabet_upper[index - 13]
        else:
            message += letter
    return message