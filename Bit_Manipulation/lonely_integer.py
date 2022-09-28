def lonelyinteger(a):
    result=0
    for num in a:
        result=result^num
    return result

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    result = lonelyinteger(a)
    print(result)
