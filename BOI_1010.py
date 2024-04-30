def factorial(n):
    num = 1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            num *= i
        return num
    
def combination(m,n):
    return int(factorial(m)/(factorial(n)*factorial(m-n)))

N = int(input())

for _ in range(N):
    n,m = map(int,input().split())
    print(combination(m,n))
