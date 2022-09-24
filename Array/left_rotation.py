def rotateLeft(d, arr):
    
    # Write your code here
    arr=arr[d:]+arr[:d]
    return arr

if __name__ == '__main__':

    first_multiple_input = input().strip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
    print(*result)
