def find_ans(h1,h2,h3):
    sum1=sum(h1)
    sum2=sum(h2)
    sum3=sum(h3)
    while True:
        m=min(sum1,sum2,sum3)
        if m==0:
            return 0
        if sum1>m:
            sum1-=h1.pop()
        if sum2>m:
            sum2-=h2.pop()
        if sum3>m:
            sum3-=h3.pop()
        if(sum1==sum2==sum3):
            return sum1
if __name__ == '__main__':
    N=list(map(int,input().split()))
    h1=list(map(int,input().split()))
    h2=list(map(int,input().split()))
    h3=list(map(int,input().split()))
    h1=h1[::-1]
    h2=h2[::-1]
    h3=h3[::-1]
    result=find_ans(h1,h2,h3)
    print(result)