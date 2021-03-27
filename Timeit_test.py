# -*- coding: utf-8 -*-
import timeit

mycode1 = '''
def loop1():
    mylist = [0]*1000
    for i in range(1000):
        mylist[i] = i
'''

mycode2 = '''
def loop2():
    mylist = [0]*1000
    i = 0
    while i < 1000:
        mylist[i] = i
        i += 1
'''

mycode3 = '''
def loop3():
    mylist = [0]*1000
    for i, c in enumerate(mylist):
        c = i
'''

mycode4 = '''
def loop4():
    mylist = [0]*1000
    i = 0
    for c in mylist:
        c = i
        i += 1
'''

mycode5 = '''
def check1():
    mylist = [0]*1000
    for i in range(1000):
        if mylist[i] <= 0:
            mylist[i] = i
'''

mycode6 = '''
def check2():
    mylist = [0]*1000
    for i in range(1000):
        try:
            assert mylist[i] <= 0
            mylist[i] = i
        except:
            pass
'''

mycode7 = '''
def check3():
    mylist = [0]*1000
    for i in range(1000):
        try:
            assert mylist[i] > 0
        except:
            mylist[i] = i
'''

numlist = [100, 10000, 1000000, 100000000]
for num in numlist:
    print("\n\nCurrent test num: ", num)
    print("for range: ", timeit.timeit(stmt = mycode1, number = num))
    print("while: ", timeit.timeit(stmt = mycode2, number = num))
    print("for enumerate: ", timeit.timeit(stmt = mycode3, number = num))
    print("for in: ", timeit.timeit(stmt = mycode4, number = num))
    print("if else: ", timeit.timeit(stmt = mycode5, number = num))
    print("try except: ", timeit.timeit(stmt = mycode6, number = num))
    print("try except 2: ", timeit.timeit(stmt = mycode7, number = num))

