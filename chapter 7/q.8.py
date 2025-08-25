n = int(input("enter a number:"))
for i in range(1,n+1):
    print(" " * (2*i-1), end="")
    print("*" * i, end=" ")
    print("")
