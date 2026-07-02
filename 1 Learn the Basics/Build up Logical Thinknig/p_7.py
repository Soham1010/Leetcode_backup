n = int(input("Enter the no. "))

sp = n-1
star = 1

for i in range(n):
    # Space
    print(" "*sp, end="")
    # Star
    print("*"*star, end="")
    # empty line
    print()
    sp-=1
    star+=2