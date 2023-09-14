
# Online Python - IDE, Editor, Compiler, Interpreter

a=float(input("Enter side of triangle : "))
b=float(input("Enter side of triangle : "))
c=float(input("Enter side of triangle : "))

if (a+b>c or b+c>a or c+a>b) and (a+b!=c and a+c!=b and c+b!=a):
    print(("Yes, it is possible."))
else:
    print(("No, it is not possible."))



