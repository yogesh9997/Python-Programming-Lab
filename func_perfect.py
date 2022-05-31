def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
n=int(input("enter the no."))
print(perfect_number(n))
© 2022 GitHub, Inc.
Terms
Privacy
Security
