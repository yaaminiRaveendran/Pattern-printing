string = input("enter a string:")
length=len(string)
for i in range(length):
    for j in range(length-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(string[j], end= " ")
    print()
