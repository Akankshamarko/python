# # we learn about string in this day
# name = "akanksha"
# anothername = 'singh'
# name1= '''' 
# hello 
# my 
# name is akanksha
# '''
# print("hello",name,name1)
# print(name[0])
# # looping throung the string
# print("lets loop for\n another charecter find withut write multiple index")
# for charecter in name1:
#     print(charecter)

#     # string method  class12
 
# naam ="akanksha,singh"
# print(len(naam))
# print(naam[0:8])
# print(naam[1:14])
# # negative
# print(naam[0:-4])
# print(naam[-1:-4])


# # class 13
a = "  akanksha  "
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("akanksha","singh"))
print(a.split(" "))
blogHeading = "introdece to python"
print(blogHeading.capitalize())
str = "welcome"
print(str.center(20))
print(str.endswith("!!!"))
print(str.endswith("to",4,6))
print(str.find("el"))
print(str.index("come"))
print(str.isalnum())
print(str.isalpha())
str2 = "hey my name is akanksha"
print(str2.isprintable())
str3 =" "
print(str3.isspace())
print(str3.swapcase())


# # class 14 
# a = "akanksha"
# print(a)
# # decision making condition statement
# b = int(input("enter your age: "))
# print("your age is:  ",b)
# if(b>18):
#     print("you can drive")
#     print("yes")
# else:
#     print("you can not ")

# apple = 200
# budget = 210
# if(apple<= budget):
#     print("yes you can buy")
# else:
#     print("no you can't buy")

# if(budget - apple >50):
#     print("you can buy")
# elif(budget-apple>90):
#     print("do not buy")

# nested  
# age =19
# has_id = True
# if age >= 18:
#     if has_id:
#         print("access granted")
#     else:
#         print("id request for verification")
# else:
#     print("access denied- underage")


#     # class-15
# execersie:

import time
timestamp =time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp= time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)

