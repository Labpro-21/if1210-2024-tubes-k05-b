def encode(cipher:str)->str:
    alfabeth_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alfabeth_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    for letter in cipher:
        if letter in alfabeth_lower:
            message += alfabeth_lower[alfabeth_lower.index(letter)+13]
        elif letter in alfabeth_upper:
            message += alfabeth_upper[alfabeth_upper.index(letter)+13]
        else:
            message += letter
    return message

def decode(cipher:str)->str:
    alfabeth_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alfabeth_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    for letter in cipher:
        if letter in alfabeth_lower:
            message += alfabeth_lower[alfabeth_lower.index(letter)-13]
        elif letter in alfabeth_upper:
            message += alfabeth_upper[alfabeth_upper.index(letter)-13]
        else:
            message += letter
    return message