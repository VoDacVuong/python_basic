#Function
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
from distutils.log import Log
import message
# from . import message as ms

# print(message.CONTACT_ADMIN_FOR_SUPPORT)
# print(ms.CONTACT_ADMIN_FOR_SUPPORT)

# importing module

#Logger, Errors and Exception Handling
import logging
# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
 
# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

# Exception Handling
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occurred.")
#         print("Next entry.")
#         print()
# print("The reciprocal of", entry, "is", r)

#vd:2
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)