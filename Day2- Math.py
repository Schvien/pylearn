#Math And Function

import math
from turtle import pen

from numpy import absolute, mat

pi = math.pi

x = 1

y = 2

z = 3

#Round Function, Rounds a variable or number for you
def RoundFunction():
    print("New Number Is : " +  str(round(math.pi)) + " Old Number Is " + str(math.pi))

#Ceiling Function, Rounds up to the nearest integer

def CeilingMath():
    print("New Number Is : " +  str(math.ceil(math.pi)) + " Old Number Is " + str(math.pi))

#Floor Function, Rounds to the lowest integer
def FloorMath():
    print("New Number Is : " +  str(math.floor(math.pi)) + " Old Number Is " + str(math.pi))


#Absolute Value, Shows how far a number is from zero. abs()

def AbsoluteMath():
    
    pi1 = math.pi*2
    pi2 = math.pi-pi1
   
    print("AbsoluteMath",abs(pi2))

AbsoluteMath()

#Exponents / To the power of, pow()
def PowerMath():
    
    print(pow(math.pi,2))

#Sqrt of a numba

def SquareRootMath():

    print(math.sqrt(math.pi))

#Max Value Between Numbers

def MaxMath(x,y,z):
    print(max(x,y,z))

#Min number finds the lowest number between numbers

def MinMath(x,y,z):
    print(min(x,y,z))


#When you wake up make a calculator.