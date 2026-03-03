a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print("Result: ", a + b)

elif operation == "-":
    print("Result: ", a - b)

elif operation == "*":
    print("Result: ", a * b)

elif operation == "/":
    if b != 0:
        print("Result: ", a / b)
    else:
        print("Error cannot divede by zero")

else:    print("wrong  operation")    