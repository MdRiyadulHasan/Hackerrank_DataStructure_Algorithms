from collections import deque
if __name__== '__main__':
    n=int(input())
    q=deque()
    for _ in range(n):
        val =list(map(int,input().strip().split()))
        if val[0]==1:
            q.append(val[1])
        elif val[0]==2:
            q.popleft()
        else:
            print(q[0])