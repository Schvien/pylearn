from ast import Slice
from telnetlib import theNULL
from matplotlib.pyplot import step


def SliceASite(Target,type,Step,WhatStep):
    if type == "Index":
        if Step != False and WhatStep != False:
            NewStringStep = Target[8:-4:WhatStep]
            return NewStringStep
        else:
            NewStringNoStep = Target[8:-4]
            return NewStringNoStep
    elif type == "Slice":
        if Step != False and WhatStep != False:
            NewSlice = slice(8,-4,WhatStep)
            NewTarget = Target[NewSlice]
            return NewTarget
        else:
            NewSlice = slice(8,-4)
            NewTarget2 = Target[NewSlice]
            return NewTarget2

print(SliceASite("https://google.com","Slice",False,False))

        

