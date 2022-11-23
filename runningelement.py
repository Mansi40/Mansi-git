def sum_inn(l):
    ans=[l[0]]
    for i in l[1:]:
        ans.append(ans[-1]+i)
    print(ans)
sum_inn([1,2,3,4,5])