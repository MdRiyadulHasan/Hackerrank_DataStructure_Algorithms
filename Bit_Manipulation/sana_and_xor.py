def sansaXor(arr):
    l=len(arr)
    result=0
    if(l&1==0):
        return 0
    else:
        for i in range(0,l,2):
            result=result^ arr[i]
    return result
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = sansaXor(arr)
        print(result)