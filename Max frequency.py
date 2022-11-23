def max_freq(l):
    d={}
    for i in l:
        if  i in d:
           d[i]+=1
        else:
            d[i]=1
    d=list(sorted(d.items(),key=lambda x:x[1]))
    print(d[-1][0])
l=[1,3,3,2]
max_freq(l)