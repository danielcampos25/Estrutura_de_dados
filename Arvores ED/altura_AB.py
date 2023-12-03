def altura(raiz):
    hleft = 0
    hright = 0
    if raiz[1]:
        hleft = altura(raiz[1])
    if raiz[2]:
        hright = altura(raiz[2])

    if hright>hleft:
        return hright+1
    else:
        return hleft+1