import string

def Caesar_Cipher():
    #prompt user for text and key to be shifted by
    text = list(input("Enter your text to be shifted via Casear Cipher (pls no spaces rn): "))
    shift_key = int(input("Enter your shift key: "))
    cipher_text = []

    upper_alph = list(string.ascii_uppercase)
    lower_alph = list(string.ascii_lowercase)

    for letter in text:
        if letter.isupper():
            index = upper_alph.index(letter)
            index =  (index+shift_key) % len(upper_alph)
            cipher_text.append(upper_alph[index])
        else:
            index = lower_alph.index(letter)
            index =  (index+shift_key) % len(lower_alph)
            cipher_text.append(lower_alph[index])
    print ("".join(cipher_text))

Caesar_Cipher()
