def sqr_sorted(l):
    Newl=[]
    for i in l:
      Newl.append(i**2)
    Newl.sort()
    return Newl
l=list(map(int,input().split()))
print(sqr_sorted(l))

    