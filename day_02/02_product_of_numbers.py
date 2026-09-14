"""
write a program to display product of number from  1 to n
"""
def product(n):

    product = 1

    for num in range(1,n+1):

        product = product * num

    return product

print(product(10))

