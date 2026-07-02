num = int(input("Enter times: "))


def recursive_fn(count, rec_hlp=0):
    buf = rec_hlp
    if buf == count:
        print()
        return
    else:
        print(f"{buf+1} ", end="")
    buf+=1
    recursive_fn(count, buf)
    
recursive_fn(num, )