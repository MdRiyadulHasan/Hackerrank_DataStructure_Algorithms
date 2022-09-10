def swap_case(s):
    x=''
    for c in s:
        if c.islower():
            c=c.upper()
        else:
            c=c.lower()
        x=x+''.join(c)
        
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)