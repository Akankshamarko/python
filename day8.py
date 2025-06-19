# a = 'akanksha'
# # print(a)
# tuple1 =(0,2,3,7,1,1,8)
# # res = tuple1.count(1)
# res= tuple1.index(3,1,8)
# print(res)


# # class-28(f-string)
# letter ="hey my name is {} and i am from"
# country ='india'
# name ='akanksha'
# # print(letter.format(country,name))
# print(f"hey my name is {name} and i am from {country}")
# print(f"hey my name is {{name}} and i am from {{country}}")
# print(type(name))

# # class-29(docstring and pep8)

# def square(n):
#     '''take a number n'''
#     print(n**2)
# square(6)

# # n= int(input("take a number of x: "))

# print(square.__doc__)
# # print(n



# # class-30(recursion)

# 
# factorial(n) = n*factorial(n-1)
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(4))
# fibonacci series

def fibonacci(n):
        #  if fibonacci(n==1):
        #          return 0
        #  if fibonacci(n==2):
        #          return 1
        #  else:
             return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))