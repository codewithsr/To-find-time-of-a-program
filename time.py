#Python program to find time of a function

from time import time

def func1(a,b):
    return a+b

def func2(a,b):
    num1 = a
    num2 = b
    if(a>b and a!=3):
        pass
    sum([4,3])
    return a+b

if __name__ == "__main__":
    init = time()
    for x in range(0, 3000000):
        func1(3,4)

    print("Rohan's time is ", time() - init)


    init = time()
    for x in range(0, 3000000):
        func2(3,4)
    print("Harry's time is ", time() - init)











