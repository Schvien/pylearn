

import time

System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)

# Multiple Assignment is assigning multiple variables in 1 line of code.

#Multiple Assignment isn't very hard its really just using one line of code to define multiple variables etc.

AccountCreationDate,PlayerName,IsFat = System_time1,"Schvien",False

print("System Time is : ",AccountCreationDate,"PlayerName is : " + PlayerName,"Is The PlayerFat? : " + str(IsFat))

#Another Method is that if everything is the same value you can do all of them in 1 line of code and set it to that value

V1 = V2 = V3 = V4 = 30

print(V1,V2,V3,V4)


#Multiple Assignment is Good For Saving Space and reducing file size