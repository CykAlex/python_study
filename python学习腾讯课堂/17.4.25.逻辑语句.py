# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:06:55 2017

@author: chenyongkang
"""


1.逻辑语
#elif
age = 1
if age>=18:
    print("old")
elif age<=4:
    print("haha")
else:
    print("young")

#or/and
number = 5
if number<0 or number>8:
    print("TRUE")
else:
    print("FALSE")
    
number = 52
if (number>=0 and number<=8) or (number>=10 and number<=15):
    print("TRUE")
else:
    print("FALSE")

#input
a=int(input())
if a>10:
    print("OK")
else:
    print("NO")

#while循环
sum=0
x=0
while x<=100:
    sum+=x
    x=x+2
print (sum)

sum = 0
for a in range(1,101):
    if a%2 ==0:
        continue
    else:
        sum = sum + a
print(sum)

a = 1
while True:
    if a>2:
        print("ok")
    else:
        print("no")

for a in "python":
    if a == "y":
        break
    print(a)












