def max_index(a):
    max = a[0]
    for i in range(1,len(a)-1):
	if a[i] > max :
	    max = a[i]
	return a.index(max)

a = [17,92,18,33,58,7,33,42]
print(max_index(a))


