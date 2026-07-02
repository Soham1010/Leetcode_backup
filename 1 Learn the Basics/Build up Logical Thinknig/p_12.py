n = int(input("Enter the no. "))
 
num = 1
sp = (2*n)-2

for i in range(n):
    for sub_1 in range(i+1):
        print(num, end="")
        num+=1
    print(" "*sp, end="")
    for sub_2 in range(i+1):
        print(num, end="")
        num-=1
    sp-=2
    print()