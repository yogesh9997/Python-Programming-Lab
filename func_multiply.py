def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total
l=eval(input("enter the list : "))
print(multiply(l))
