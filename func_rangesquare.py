def printValues(ll,ul):
	l = list()
	for i in range(ll,ul+1):
		l.append(i**2)
	print(l)
ll=int(input("enter the lower limit "))
ul=int(input("enter the max limit"))
printValues(ll,ul)
