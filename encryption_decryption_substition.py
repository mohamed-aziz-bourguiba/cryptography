def crypto(c):
    global alphabet
    global melange
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","W","X","W","Z"]
    melange=["y","k","c","o","d","m","f","j","g","z","a","x","r","n","b","u","t","q","i","p","h","w","e","s","v","l"]

    if c in alphabet:
        y=alphabet.index(c)
        print(melange[y])
    else:
        print("element not in list")



def ch_phrase(phrase):
    l=[]
    w=[]
    z=p.split()
    print(z)
    for i in z:
        print(i)

        for j in range(len(i)):

                l.append(i[j])
    print(l)
    for x in l:
        q=alphabet.index(x)
        f=melange[q]
        w.append(f)
    print(w)
    print(''.join(w))

def dec_phrase(p):
    l = []
    w = []
    z = p.split()
    print(z)
    for i in z:
        print(i)

        for j in range(len(i)):
            l.append(i[j])
    print(l)
    for x in l:
        q = melange.index(x)
        f = alphabet[q]
        w.append(f)
    print(w)
    print(''.join(w))






c = input("write your alphabet= ")
p=input("write your phrase= ")
d=input("write your phrase for decrypt= ")
crypto(c)
ch_phrase(p)
dec_phrase(d)