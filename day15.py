# with open('myfile.txt','r') as f:
#     print(type(f))
#     f.seek(10)
#     print(f.tell())
#     data = f.read(5)
#     print(data)


# # class-52(lamda functions)
# double = lambda x: x*2
# cube = lambda x: x*x*x
# avg = lambda x,y:(x+y)/2
# print(avg(4,6))
# print(cube(2))
# print(double(10))
    

# class-53(map,function,reduce)
# def cube(x):
#     return x*x*xl =[1,4,7,8,9]
# # newl=[]
# # for item in l:
# #     newl.append(cube(item))
# newl=list(map(cube,l))
# print(newl)

# filter
# l =[1,4,5,9,10]
# def new_function(a):
#     return a>4

# newl = list(filter(new_function,l))
# print(newl)
# print(type(new_function))