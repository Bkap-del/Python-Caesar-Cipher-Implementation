import string

def Caesar_Cipher(text, shift_key, mode = 'enctpyt'):
    if mode == 'decrypt':
        shift_key = -shift_key
    cipher_text = []

    upper_alph = list(string.ascii_uppercase)
    lower_alph = list(string.ascii_lowercase)

    for letter in text:
        if not letter.isalpha():
            cipher_text.append(letter)
        elif letter.isupper():
            index = upper_alph.index(letter)
            index =  (index+shift_key) % len(upper_alph)
            cipher_text.append(upper_alph[index])
        else:
            index = lower_alph.index(letter)
            index =  (index+shift_key) % len(lower_alph)
            cipher_text.append(lower_alph[index])
    return ("".join(cipher_text))

secret = Caesar_Cipher("L-i-v-i-n", 4, 'encrypt')
print(f"The cipher text is: {secret}")
original = Caesar_Cipher(secret, 4, 'decrypt')
print(f"The original text was: {original}")
