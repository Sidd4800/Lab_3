
# Online Python - IDE, Editor, Compiler, Interpreter

num = int(input("Enter a no : "))
a = num//100
b = (num-(a*100))//10
c = (num-(a*100)-(b*10))
sum=(a+b+c) #Take sum
print(sum)
if sum%3==0:    
    print(sum,"is divisible by 3")
else:
    print(sum, "is not divisible by 3")


