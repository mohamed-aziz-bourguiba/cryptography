def encrypt(txt,key):
    global t
    cipher_list=[]
    for l in txt :
        position = ord(l)
        new_letter = chr(position+int(key))
        cipher_list.append(new_letter)

    t =''.join(cipher_list)
    print(t)

def decrypt(t,key):
    dcipher_list=[]
    for i in t :
        position = ord(i)
        new_letter = chr(position-int(key))
        dcipher_list.append(new_letter)

    y=''.join(dcipher_list)
    print(y)

text=input("give me your string to encrypt =")
key=input("give me the key please= ")
encrypt(text,key)
decrypt(t,key)