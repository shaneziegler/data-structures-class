def nfact(x):
    if x == 0:
        return 1
    return x * nfact(x-1)

c = nfact(4)
print(c)