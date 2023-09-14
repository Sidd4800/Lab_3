
# Online Python - IDE, Editor, Compiler, Interpreter

num = int(input("Enter the number : "))
hundred = num//100
tens = (num-(hundred*100))//10
ones = (num-(hundred*100)-(tens*10))

num_arm = (hundred**3)+(tens**3)+(ones**3)
if num==num_arm:
    print("Armstrong number")
else:
    print("Not an armstrong number")






