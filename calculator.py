# Basic Calculator Program
# Author: Created for xAI user query
# Date: August 09, 2025
# Description: Prompts user for two numbers and a mathematical operation (+, -, *, /) and displays the result

def calculator():
    try:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ").strip()

        # Perform the calculation based on operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation! Please use +, -, *, or /")

    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
if __name__ == "__main__":
    calculator()