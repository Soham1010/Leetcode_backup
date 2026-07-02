n = int(input("Enter the no. "))
 
acc = 1

for i in range(n):
    for j in range(i+1):
        print(acc, end="")
        acc+=1
    print()
        
