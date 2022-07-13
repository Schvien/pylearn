#While loops will run indefinetly until you break as long as the condition remains true

from asyncio import coroutine


def RawWhileTrueLoop():
    #Method 1, if you want a block of code to run forever without needing a condition you would do ..
    while True:
        print("hi")

#You can Also use Logical operators with while loops to create a condition

def ConditionWhileLoop():
    x , y , z =  1 , 2 , 3

    #Basically if statements that run forever
    while x == 1:
        print("X is Equal to "+ str(x))

    while x == 1 and y == 2:
        print("X and Y are equal to 1 and 2")
