import maya.cmds as cmds #can change cmds

cmds.polySphere(radius=1, subdivisionsX=20, subdivisionsY=20, axis=[0, 1, 0], cuv=2, ch=1)





name = "Timothy"
print(name)
print(type(name))

name = 4.5
print(name)
print(type(name))




# string ("str is shortform") : "timothy", "melissa"
                   # can also use single strokes 'timothy'
                   #"""timothy""" can also do that
                   # "you can do 'this'"
print('ya ta ta "woo"') # print("ya ta ta 'woo'")

# integer (int) : 35, 1234, -23523, 0 and etc

#float (float) : 25, 2.3, 234.345, -242.2424

#boolean (bool) : 1, or 0, True, or False

# collections  - like arrays
#   - list   : ["tim", "bob", "marie", "tim", "bob"]
#                ["tim", 35, True, ["Tina", 35], .343]
#               grades = [85, 73, 99, 35] is the same as grades = list((85, 73, 99, 35))
#   -tuple   :  ("tim", "bob", "marie")  
#               difference between list and tuple, after tuple is defined, cannot change it
#                ("tim", 35, True, ["Tina", 35], .343)
#              grades = (85, 73, 99, 35) is the same asgrades = tuple((85, 73, 99, 35))
#  - set     :    {"tim", "bob", "marie"}  sets are unordered, an unchangable. also no duplicate items, like lists
#                 grades = {85, 73, 99, 35} is the same as grades = tuple((85, 73, 99, 35))
#  - dictionary  :    pet = {"type" : "cat", "color" : "orange", "personality" : "aloof"}  same as pet = dict("type" : "cat", "color" : "orange", "personality" : "aloof")
                    #pet = {"type" : "cat", "color" : "orange", "personality" : "aloof"}
                    #pet["type"] = "dog"
                    #print (pet["type"])
# -NoneType (None)  :  None    its null in other languages




# Arithmetic Operators
# + : addition (5 + 3)
# - : subtraction (5 - 3)
# * : multiplication (5 * 3)
# / : Division (5 / 3)
# % : Modulus (5 % 3)  would return 2
# ** : exponentiation (5**3) == (5^3) (5 * 5 * 5)
# // : floor division (5 // 3) would return 1, rounds down to nearest whole value

#assignment operators
# = : assign right to left (name = "tim")
# += : add value on left to value on right and reasign variable on left
# -= : subtracts and reasigns
# *= : divides and reasigns
# %= : modulus and reasigns
# **/ : Exponentiates and reasigns
# //= : floor divides and reasigns


#comparison operators
# == : equal to, (3 == 3)
# != : not equal to, ( 3 != 5)
# > : Greater than, ( 5 > 3)
# < less than, ( 3 > 5)
# >= greater than or equal to, ( 5 >= 3, or 5)
# <= less than or equal to, (3 <= 5, or 3 )


#logical operators
# and : returns True if both statements are true, && in C#   (3 < 5 and 5 != 3)
# or : returns True if either statements are true, || in C#   (3 < 5 or 5 != 3)
# not : reverse result, return False if result is true, ! in C#   not(3 < 5 or 5 != 3)


#Identity operators
# is : returns True if both variables are the same object (x is y)
# is not : returns True if both variables are not the same object (x is not y)


#membership operators
# in : returns True if a sequence with the specified value is present in the object
# not in : returns True if a sequence with the specified value is not present in the object

if 13 in [13, 53, 7, "Hello"]:  # if 13 not in, etc
    print "got it"

if "rat" not in "Congratulations":
    print "got it"