def min_fee(pages_to_print):
    pages_to_print = sorted(pages_to_print)
    j=0
    s=0
    su=[]
    for i in range(len(pages_to_print)):
       if j==i:
           s = s + pages_to_print[i]
           su.append(s)
           j += 1
    return sum(su) 

print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
