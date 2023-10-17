import random
r = input("range: ")
d = {}

def make_dict(r):
    c =0
##    L = []
    for i in range(int(r)):
        L = []
        name = f"LIST{c}"
        L.append(random.randint(0,100))
        L.append(random.randint(0,100))
        L.append(random.randint(0,100))
        L.append(random.randint(0,100))
        d[name] = L
        c += 1
    return L
    

##L = make_dict(r)
##print(L)
##
##prev = 0
##for item in L:
##    if prev:
##        d[item] = 1 + prev
##        prev = int(d[item])
##    else:
##        d[item] = 1 
##        prev = int(d[item])

make_dict(r)
print(d)

##
##x = d[L[4]]
##y = d[L[0]]
##z = d[L[5]]
