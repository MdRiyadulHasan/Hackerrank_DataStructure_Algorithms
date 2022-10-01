# main logic :- a+b = a^b +a&b
def sumXor(n):
    result=1
    while(n):
        b=n&1
        if b==0:
            result=result*2
        n=n>>1
    return result
if __name__ == '__main__':
    n = int(input().strip())
    result = sumXor(n)
    print(result)

    