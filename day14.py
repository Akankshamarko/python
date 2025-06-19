f = open('myfile.txt','r')
l=0
while True:
    l = l + 1
    
    line = f.readline()
    if not line:
        break
    m1 =  line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"marks of student{l} in maths is: {m1}")
    print(f"marks of student{l} in english is: {m2}")
    print(f"marks of student{l} in science is: {m3}")

    
   
    print(line)
