#Caser Cipher project
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift, alphabet):
    encrypt_text =""
    for i in text:
        if i in alphabet:
            idx = alphabet.index(i)
            idx += shift
            if (idx > 26):
                idx = idx % 26
            encrypt_text += alphabet[idx]
        else:
            encrypt_text += i
    print(f"Here's the encoded result: {encrypt_text}")

def decrypt(text, shift , alphabet):
    decrypt_text =""
    for i in text:
        if i in alphabet:
            idx = alphabet.index(i)
            idx -= shift
            if idx < 0:
                idx = 26 + idx
            decrypt_text += alphabet[idx]
        else:
            decrypt_text += i

    print(f"Here's the decoded result: {decrypt_text}")

repeat = 'yes'

while repeat == 'yes' :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    if direction == 'encode':
        encrypt(text,shift, alphabet)
    elif direction == 'decode':
        decrypt(text, shift, alphabet)
    else:
        print("wrong input direction!")

    rep = input("Type 'yes' if you want to go again, Otherwise type 'no'.\n").lower()
    if rep != repeat:
        repeat = "no"


