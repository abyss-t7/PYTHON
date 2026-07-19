n= ["a", "b", "c", "d"]
def lust(k):
    if k==[]:
        return
    print (k[0])
    lust(k[1:])

lust(n)