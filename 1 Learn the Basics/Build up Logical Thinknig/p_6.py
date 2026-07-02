n = int(input("Enter the no. "))


for i in range(n, 0, -1):
    for j in range(i):
        print(f"{j+1}", end="")
    print()