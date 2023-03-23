
def countCharacter(chr):
    chr2 =chr.lower()
    c = {}

    for i in chr2:
        if i in c:
            c[i] +=1
        else:
            c[i]=1
    return c

cStrings = input("Enter String :")

print(countCharacter(cStrings))
