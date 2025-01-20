#This program calculates the sum of digits for each number in a list using nested while loops.

number=[10,56,865,345,456,23,234]

i=0
while i<len(number):
    num=number[i]
    addition=0

    while num>0:
        addition=addition+num%10
        num//=10
    print(f"The sum of digits in {number[i]} is {addition}")
    i+=1