def flippingBits(n):
    return n^((1<<32)-1)
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        print(result)
