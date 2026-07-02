n = 5  # Number of rows

for i in range(1, n + 1):
    for j in range(i):
        # 65 is 'A', 66 is 'B', etc.
        print(chr(65 + j), end="")
    print() 