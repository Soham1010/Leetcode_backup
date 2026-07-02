num = int(input("Enter times: "))
thing = input(f"Enter what to print {num} times: ")



def recursive_fn(num, val, ret_val=0):
    buf = ret_val
    if buf == num:
        print()
        return
    else:
        print(f"{val} ", end="")
    buf+=1
    recursive_fn(num, val, buf)
    
recursive_fn(num, thing)