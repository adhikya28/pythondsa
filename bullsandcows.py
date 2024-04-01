def BandC():
    bc=0
    cc=0
    s=[int(x) for x in input().split()]
    g=[int(x) for x in input().split()]
    for i in range(len(s)):
        num=s[i]
    for j in g:
        num1=g[j]
    if num==num1:
        bc=bc+1
    elif num!=num1:
        cc=cc+1
    
print(BandC())
