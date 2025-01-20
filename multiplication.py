#This program prints the multiplication table (from 1 to 5) using nested while loops:\


i=1
while i<=5:
    j=1
    while j<=10:
        print(f"{i} * {j}=",i*j,  end="\t")
        j+=1

    print()
    i+=1