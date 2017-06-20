x=16
ans=0
while ans*ans<=x:
    ans +=1
print(ans)

##x=10
##ans=0
##if x >= 0:
##    while ans*ans < x:
##        ans +=1
##        #print('ans = ',ans)
##    if ans*ans != x:
##        print(x,'is not a perfect square')
##    else:
##        print(ans)
##else:
##    print(x,'is a negative number')

##x=10
##i=1
##while i<x:
##    if x%i == 0:
##        print('divisor',i)
##    
##    i+=1
##
##x=10
##for i in range(1,x):
##    if x%i == 0:
##        print('divisor',i)

##sumDigits = 0
##for C in str(1952):
##    sumDigits +=int(C)
##print(sumDigits)

#第四课*********************抽象与递归
##def sqrt(x):
##    ans=0
##    if x>=0:
##        while ans*ans<x:
##                ans=ans+1
##        if ans*ans!=x:
##                return None
##        else:return ans
##    else:return None
##def f(x):
##    x=x+1
##    return x

##def fib(x):
##    if x==0 or x==1:return 1
##    else:return fib(x-1)+fib(x-2)
    
##def factorial(n):
##    if n==0 or n==1:
##        return 1
##    else:
##        return n*factorial(n-1)



