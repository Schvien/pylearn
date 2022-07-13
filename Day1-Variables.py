#Variables = a container for a value. So if A was my value and i did print(A) it would print A

from ast import If
import re


name = "Bro"

print(name)

#To Combine A String With A variable you would do

print("Hello "+name)



#To find the data type of a variable you need to use the type function as shown here

String_Type = type(name)

#You cannot combine variables of different classes you cant do V1 = 1 V2 = "J" print(v1+v2)

first_name = "Sean"

#Instead of adding a space before the variable you can add a Blank quotation between your 2 vars
last_name = "Constable"

full_name = first_name + " " +  last_name

#Combining multiple variables with A print function
print("Hello "+full_name)


# Numbers -- Ints Onlt take whole number

age = 21

age +=1 


print(age)
print(type(age))

#Conversion Variables

print("Your Age is : "+str(age)) ##This Converts your string into a string

#you can also store the string conversion as a variable

converted = str(age)

print("Hello This Is Conversion And Our Converted Number is" + " " + converted)


##Float Data Types are Data types that can store Decimals unlike Ints that can store Whole numbers only.

## You cant use space character trick before number that are being converted just figured that out
Height = 250.5 #This Is a float number

print("Your Height is : "+str(Height) + " " + "Centimeters")
#print(type(Height))


#Boolean Values are values that can only store true or false values

# When Creating FUNCTIONS ALWAYS ADD THE :
Active = False

print(type(Active))

print("PlayerHigh = "+str(Active))
def Check():
    if Active == False:
        return "The Value is false"
    elif Active == True:
        return "Value is true"

print(Check())

## MISC --The + operator concatenates strings and the * operator creates multiple copies. The result of 2 * (s + t) is 'foobarfoobar', which does contain the string 'barf'.

#RunDown Of Day 1, I got basic stuff done, Made myself a little function now got to know strings n stuff now i feel abit smarter

#Why are varibles Useful? Variables can be useful because they can store values and make it easier to find things and print out instead of constantly typing it out raw