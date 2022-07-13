#String Methods
import imp



from gettext import find
from itertools import count
import string
from turtle import pen
from unicodedata import digit, name


Name = "bro"

#Length Method. The Length Function Len For short this returns the length of our string can be used to find the length of dictionaries etc.

#Dictionary Method
myDict = {1: "hi",2 :"hi"}

print(len(myDict))

#VariableCharacterMethod

#Length Counts every single character even the ones you cant see.
print("Hey This Is The Len Function : " + str(len(Name)))

#Find Function.This finds the index of your string. This can be used to find Letters or words in a string.

#Computers always start at 0 so the output should be 0.

print("Hey This Is The Find Function : " + str(Name.find("b")))

#If The Character you're looking for doesn't exist it'll return negative

#Very Prices Case Sensitive.


#Next Function Capitalize.

#This function Capitalizes the first Character in a string
print("Hey This Is The capitalize Function : " + Name.capitalize())

#UpperCase Function.

#The UpperCase Function makes character in a string uppercase

print("Hey This Is The Upper Function : " + Name.upper())

#The Next Function the lower function Makes Everything in a string lowercase.

print("Hey This Is The Lower Function : " + Name.lower())

#Next Function The IsDigit Function. This Returns if your Variables Value is a number(digit) or a Letter if its a digit it will return true else false

Digit = "123"

NonDigit = "NonDigit"

print("Hey This Is The Digit Function : " + str(Digit.isdigit()) + " " + str(NonDigit.isdigit()))

#Next Function is the Is Alpha Function. Can use to check if A String Has Letter opposite of digit

print("Hey This Is The Alpha Function : " + str(Digit.isalpha()) + " " + str(NonDigit.isalpha()))

#Count Function. Counts how many of a specific character are in a string

# Case Sensitive
Count = "Heyooo"

print("This is the Count Function : " + str(Count.count("o")))

#Replace Method Can be used to Replace Specific character in a string

print(" Hey This Is The Replace Function :" + " " + Count.replace("o","a")*3)

#To replace multiple characters you should use the translate function and maketrans and str

Word2 = "Word"

print(Word2.translate(str.maketrans("Word","Made")))

#Using

Swear_Word = "Fuck"

def Swear_WordFilter(Word):
    if Word == "Fuck":
        NewWord = Word.translate(str.maketrans("Fuck", "####"))

        print("Hey no swearing!!! You have said : " + str(Word))
        
        print(NewWord)

Swear_WordFilter(Swear_Word)