
"""num = int(input("Enter a number to find its factorial: "))
factorial = 1
if num == 0:
    print("The factorial of 0 is 1.")
else:
    i = num
    while i > 1:
        factorial *= i
        i -= 1
    print(f"The factorial of {num} is {factorial}")"""
num=6
fact=1
if num==0:
    print("factorial is 1")
else:
    while num>1:
        fact=fact*num
        num=num-1
    print(fact)

print(6*5*4*3*2*1)