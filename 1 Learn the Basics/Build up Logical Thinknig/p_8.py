n = int(input("Enter the no. "))

sp = 0
star = (2*n)-1

for i in range(n,0,-1):
    # Space
    print(" "*sp, end="")
    # Star
    print("*"*star, end="")
    # empty line
    print()
    sp+=1
    star-=2