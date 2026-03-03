# Simple Calculator
print("Welcome to Calculator!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose (1/2/3/4): ")

if choice == "1":
    print(f"Result: {num1 + num2}")
elif choice == "2":
    print(f"Result: {num1 - num2}")
elif choice == "3":
    print(f"Result: {num1 * num2}")
elif choice == "4":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid choice!")

input("\nPress Enter to exit...")  # This keeps window open