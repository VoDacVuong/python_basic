#Function
import imp


def DTB(toan: float, ly: float, hoa: float):
    return (toan + ly + hoa)/ 3
# print(DTB(3.1, 5.6, 9.1))

#---------------------

#Lambda
add_one = lambda x, y: x + y
dtb_add_one = lambda func: func + 1
# print(dtb_add_one(DTB(1,2,3)))
# print(add_one(3, 4))

#---------------------

# args, **kwargs
#vd:1
l_a = lambda *args: sum(args) 
l_b = lambda **kwargs: sum(kwargs.values())
# print(l_a(1, 2, 3, 4))
# print(l_b(a = 1, b = 4, c = 5))

# vd:2
def demo1(*args):
    for x in args:
        print(x)

def demo2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

#---------------------

#unpack
x = (1, 2, 9)
y = {'x': 2, 'y': 4, 'z': 6}
# print(demo1(*x))
# print(demo2(**y))

#---------------------

#decorator
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

#Decorator nhiều lần
def decorator_1(func):
    def inner(*args, **kwargs):
        print('----------Decorator lần 1----------')
        func(*args, **kwargs)
        print('----------Decorator lần 1----------')
    return inner

def decorator_2(func):
    def inner(*args, **kwargs):
        print('----------Decorator lần 2----------')
        func(*args, **kwargs)
        print('----------Decorator lần 2----------')
    return inner
@decorator_1
@decorator_2
def print_mess(message):
    print(message)

# print_mess('Hello Decorator')
#output
# ----------Decorator lần 1----------
# ----------Decorator lần 2----------
# Hello Decorator
# ----------Decorator lần 2----------
# ----------Decorator lần 1----------


#--------------------
#Module and packages in python
from d_25_05_2022.oob import func_demo


func_demo("Day la function")

