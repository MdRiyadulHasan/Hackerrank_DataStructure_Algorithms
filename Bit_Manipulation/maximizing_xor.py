def maximizingXor(l, r):
    max_xor=0
    for i in range(l,r+1):
        for j in range(l,r+1):
            max_xor=max(max_xor,i^j)
    return max_xor

if __name__ == '__main__':
    l = int(input().strip())
    r = int(input().strip())
    result = maximizingXor(l, r)
    print(result)
