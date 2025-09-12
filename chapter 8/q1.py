a = 32
b = 23
c = 12 

def greatest():
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > b and c > a:
        return c
    print(greatest(a,b,c))