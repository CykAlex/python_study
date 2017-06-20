# -*- coding:utf-8 -*-
##一、python中__str__和__repr__
##如果要把一个类的实例变成str，就需要实现特殊方法__str__():
# class Person(object):
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#     def __str__(self):
#         return '(Person:%s,%s)'%(self.name,self.gender)
#     __repr__ = __str__
# p = Person('Bob','Male')
# print p

##二、python中__cmp__
##对int、str等内置数据类型排序时，python的sorted()按照默认的比较函数cmp排序，但是，
##如果对一组Student类的实例排序时，就必须提供我们自己的特殊方法__cmp__():
# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def __str__(self):
#         return '(%s,%s)'%(self.name,self.score)
#     __repr__ = __str__
#
#     def __cmp__(self,s):
#         if self.name < s.name:
#             return -1
#         elif self.name > s.name:
#             return 1
#         else:
#             return 0
# L = [Student('Tim','99'),Student('Bob',100),Student('Alice','77')]
# print sorted(L)

##请修改 Student 的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。
# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def __str__(self):
#         return '(%s,%s)'%(self.name,self.score)
#     __repr__ = __str__
#
#     def __cmp__(self,s):
#         if self.score == s.score:
#             return cmp(self.name,s.name)
#         return -cmp(self.score,s.score)
# L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
# print sorted(L)

##三、python中__len__
##如果一个类表现的像一个list，要获取多少个元素，就得用len()函数
# class Student(object):
#     def __init__(self,*args):
#         self.names = args
#     def __len__(self):
#         return len(self.names)
# s = Student('Bob','Alice','Tim')
# print len(s)

##任务，斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。
# 请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
#
# def fibs(num):
#     result=[0,1]
#     for i in range(num-2):
#         result.append(result[-2]+result[-1])
#     return result
# print fibs(10)

# class Fib(object):
#     def __init__(self, num):
#         a, b, L = 0, 1, []
#         for n in range(num):
#             L.append(a)
#             a, b = b, a + b
#         self.numbers = L
#
#     def __str__(self):
#         return str(self.numbers)
#
#     __repr__ = __str__
#
#     def __len__(self):
#         return len(self.numbers)
#
# f = Fib(10)
# print f
# print len(f)

##四、python中数学运算
# class Rational(object):
#     def __init__(self, p, q):
#         self.p = p
#         self.q = q
#     def __add__(self, r):
#         return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
#     def __str__(self):
#         return '%s/%s' % (self.p, self.q)
#     __repr__ = __str__
#
# r1 = Rational(1, 3)
# r2 = Rational(1, 2)
# print r1 + r2

# def gcd(a,b):
#     if b == 0:
#         return a
#     return gcd(b,a%b)
# class Rational(object):
#     def __init__(self,p,q):
#         self.p = p
#         self.q = q
#     def __add__(self,r):
#         return Rational(self.p * r.q + self.q * r.p,self.q * r.q)
#     def __sub__(self,r):
#         return Rational(self.p * r.q - self.q * r.p,self.q * r.q)
#     def __mul__(self,r):
#         return Rational(self.p * r.p,self.q * r.q)
#     def __div__(self,r):
#         return Rational(self.p * r.q,self.q * r.p)
#     def __str__(self):
#         g = gcd(self.p,self.q)
#         return '%s/%s'%(self.p/g,self.q/g)
#     __repr__ = __str__
# r1 = Rational(1, 2)
# r2 = Rational(1, 4)
# print r1 + r2
# print r1 - r2
# print r1 * r2
# print r1 / r2

##五、python中类型转换,要把有理数转换为int
# class Rational(object):
#     def __init__(self,p,q):
#         self.p = p
#         self.q = q
#     def __int__(self):
#         return self.p//self.q
#     def __float__(self):
#         return float(self.p)/self.q
# print int(Rational(7,2))
# print float(Rational(7,2))

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#     @property
#     def score(self):
#         return self.__score
#     @score.setter
#     def score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.__score = score
#
# s = Student('Bob', 59)
# s.score = 60
# print s.score


