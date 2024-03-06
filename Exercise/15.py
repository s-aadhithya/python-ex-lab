def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                raise ValueError("Invalid operation. Please enter '+', '-', '*', or '/'.")

            print(f"Result: {result}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            try_again = input("Do you want to perform another calculation? (y/n): ").lower()
            if try_again != 'y':
                break

if __name__ == "__main__":
    calculator()
