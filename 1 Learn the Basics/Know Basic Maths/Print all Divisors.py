import math
n = int(input("Enter no. "))

divisors = []

for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:
        divisors.append(i)
        if i != n // i:            # 6 x 6 case
            divisors.append(n // i)
        
print(divisors)