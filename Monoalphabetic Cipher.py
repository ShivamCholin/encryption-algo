letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def set_key(in_key):
    key = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    in_key = in_key.upper()
    if in_key!=None and len(in_key)==26:
        key = in_key
    return key


def enc(key, str):
    key = set_key(key)
    cipher = ''
    for ch in str:
        if ch.isupper():
            cipher += key[letters.find(ch)]
        elif ch.islower():
            cipher += key.lower()[letters.find(ch.upper())]
        else:
            cipher += ch
    return cipher


def dec(key, str):
    key = set_key(key)
    text = ''
    for ch in str:
        if ch.isupper():
            text += letters[key.find(ch)]
        elif ch.islower():
            text += letters.lower()[key.find(ch.upper())]
        else:
            text += ch
    return text


plain_txt = input('Enter a plain text:')
key = input('Enter a Key:')
cipher_txt = enc(key, plain_txt)
print('cipher Text:', cipher_txt)

cipher_txt = input('Enter a cipher text:')
key = input('Enter a Key:')
plain_txt = dec(key, cipher_txt)
print('Plain Text:', plain_txt)