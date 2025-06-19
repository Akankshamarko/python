# class-34(dic-method)
# student={106:53,124:53,141:48}
# student1={142:47,147:51}
# student.update(student1)
# print(student)
# student.popitem()
# del student[124]
# print(student)

# class-35(else in loop)

# for i in range(5):
# i =0
# while i<7:
#     print(i)
#     i = i + 1
#     # if i ==4:
#         # break
# else:
#     print("sorry no i")


# class-36(Exceptionhandling)

# a = input("enter the number ")
# print(f"multiplaction table of {a} is :")
# try:
#   for i in range (1,11):
#     print(f"{int(a)}x{i} = {int(a)*i}")
# except Exception as e:
#   print("invalid input")

# print("some imp lines in code")
# print("end of code")

# try:
#     num = int(input("enter the integer: "))
#     a= [6,3]
#     print(a[num])
# except ValueError:
#     print("this is not integer")
# except IndexError:
#     print("index error")


# class-37(finally keywords)

# def fun1():
#     try:
#      l = [4,7,8,9]
#      i = int(input("enter the index : "))
#      print(l[i])
#      return 1
#     except:
#      print("some error occurred")
#      return 0
#     finally:
#      print("executed in every situation")
# x = fun1()
# print(x)


# class-38(custom errors)
a = int(input("enter any value b/w 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")
