def enc(key, str):
    cipher=''
    for ch in str:
        if ch.isupper():
            cipher += chr(((ord(ch) - 65 + key) % 26) + 65)
        elif ch.islower():
            cipher += chr(((ord(ch) - 97 + key) % 26) + 97)
        else:
            cipher += ch
    return cipher


def dec(key, str):
    text=''
    for ch in str:
        if ch.isupper():
            text += chr(((ord(ch) - 65 - key) % 26) + 65)
        elif ch.islower():
            text += chr(((ord(ch) - 97 - key) % 26) + 97)
        else:
            text += ch
    return text


plain_txt = input('Enter a plain text:')
key = int(input('Enter a Key:'))
cipher_txt = enc(key, plain_txt)
print('cipher Text:', cipher_txt)

cipher_txt = input('Enter a cipher text:')
key = int(input('Enter a Key:'))
plain_txt = dec(key, cipher_txt)
print('Plain Text:', plain_txt)