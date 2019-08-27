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


cipher_txt = input('Enter a cipher text:')
print('Plain Text:')
for key in range(26):
    plain_txt = dec(key+1, cipher_txt)
    print('Key:'+str(key+1)+'\tText:'+plain_txt)
