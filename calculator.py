def add(n,p):
    return(n+p)
def subtract(n,p):
    return(n-p)
def multiply(n,p):
    return(n*p)
def divide(n,p):
    return(n/p)

choice= input("choose a= addition, b=subtraction, c=multiplication, or d= division: ")
num1= int(input("Choose value for first number: "))
num2= int(input("Choose value for second number: "))

if choice=="a":
    print(add(num1,num2))
elif choice=="b":
    print(subtract(num1,num2))
elif choice=="c":
    print(multiply(num1,num2))
elif choice=="d":
    print(divide(num1,num2))
else:
    print("Invalid Result")