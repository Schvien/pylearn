# logical operators are stuff like (and, or , not,!)

import asyncio
from types import coroutine


x = 2


def Not():
    if not x == 1 : 
        #The operator basically mean if that x is not = to 1 it'll do your bidding
        print("uno")



def And():
    # and function is basically your first thing like if this thing exists and this thing exists it does whatever

    if x and x==2:
        print("dos")


def Or():
    if x==1 or x==2:
        #the or function is like if x is this or this it'll do that
        print("tres")



def Exclamation():
    if x!=1:
        #! means doesnt equal so if x doesnt equal 1 it does that
        print("cuatro")
