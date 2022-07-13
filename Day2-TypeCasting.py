#Type Casting, To ConvertData into Another Type of data.

from hashlib import new
from lib2to3.pytree import convert
from multiprocessing.connection import wait

z = "1"

def ConvertVar(Target,Type):
    if Type == "Int" or Type == "int" or Type == "Integer":
        Target = int(Target)
        print("Your Target Has Succesfully Been Converted to a : " + Type,type(Target)) 
        return Target
    elif Type == "String":
        Target = str(Target)
        print("Your Target Has Succesfully Been Converted to a : " + Type,type(Target)) 
        return Target

    elif Type == "Float":
        Target = float(Target)
        print("Your Target Has Succesfully Been Converted to a : " + Type,type(Target)) 
        return Target
    
    
    
--print(ConvertVar(z,"Float"))