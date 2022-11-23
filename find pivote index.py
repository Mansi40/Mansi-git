def pivote_index(l):
    for i in l:
        if sum(l[:i])==sum(l[i+1:]):
            return i
l=list(map(int,input().split()))      
print(pivote_index(l))
        

