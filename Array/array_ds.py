def reverse_array(a):
    n=len(a)
    new_arr=[]
    for i in range(n-1,-1,-1):
        new_arr.append(a[i])
    return new_arr


if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().strip().split()))
    res=reverse_array(arr)
    print(res)