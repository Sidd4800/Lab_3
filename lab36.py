
# Online Python - IDE, Editor, Compiler, Interpreter

num = int(input("Enter the number : "))
x=num//10000
y=(num-(a*10000))//1000
z=(num-(a*10000)-(b*1000))//100
w=(num-(a*10000)-(b*1000)-(c*100))//10
v=(num-(a*10000)-(b*1000)-(c*100)-(d*10))
print(x,y,z,w,v)
num_rev = ((v*10000)+(w*1000)+(z*100)+(y*10)+v)
if num==num_rev:
    print("Palindrome")
else:
    print("Not a Palindrome")


