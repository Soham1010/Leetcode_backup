num = int(input("Enter times: "))


def recursive_fn(num, current=1, total=0):
    if current > num:
        print(total)
        return

    recursive_fn(num, current=current + 1, total=total + current)

    
recursive_fn(num)