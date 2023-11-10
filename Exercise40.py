a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if (a == b == c):
        print("Equilateral triangle ") 
elif (a == b or a == c or b == c):
    print("Isosceles triangle") 
else:
    print("Scalene triangle")