
   
def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        print("PRIME NO.")
    else:
        print("NOT PRIME")

n=int(input("enter the no."))
prime(n)
