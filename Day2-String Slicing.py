# Slicing is creating a substring by extracting elements from another string
#       indexing[] or slice()
#       [starti:stop:step]
#the slice function has these function depending on where and how we want to slice


from ast import Slice
from hashlib import new


name = "Schvien Onan"

#First Name is using the start function and removing the zero and keeping the coollin means 0,end number

first_name = name[:7]

#Funk is using the step function it doesnt count anything but the numbers you put
funky_name = name[::1]

reversed_name = name[::-1]

last_name = name[7:]
print(reversed_name)



#Step is how much we're increasing index by between starting and stopping
#Basically counts every other thing




#Slice Function, This can be used to make a sliced object

#Trying to slice everything but google would be tricky

# So we need negative indexing to go backwards (doesnt start at 0)
website1 = "http://google.com"

website2 = "https://youtube.com"

slice = slice(8,-4)

print(website2[slice])

def SliceWebsite(website):
    new=website[slice]
    return new 

print(SliceWebsite("https://wikipedia.com"))