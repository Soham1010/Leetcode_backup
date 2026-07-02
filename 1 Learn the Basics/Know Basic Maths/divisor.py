n = int(input("Enter no. "))

divisors = []

for i in range(n//2):
    if n % (i+1) == 0:
        divisors.append(i+1)

divisors.append(n)
print(divisors)
    
