# Function to perform addition
def perform_addition(x, y):
    return x + y

# Function to perform subtraction
def perform_subtraction(x, y):
    return x - y

# Function to perform multiplication
def perform_multiplication(x, y):
    return x * y

# Function to perform division
def perform_division(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator function
def calculator():
    print("Welcome to My Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    user_choice = input("Enter choice (1/2/3/4): ")

    input_num1 = float(input("Enter first number: "))
    input_num2 = float(input("Enter second number: "))

    if user_choice == '1':
        result = perform_addition(input_num1, input_num2)
        print("Result:", result)
    elif user_choice == '2':
        result = perform_subtraction(input_num1, input_num2)
        print("Result:", result)
    elif user_choice == '3':
        result = perform_multiplication(input_num1, input_num2)
        print("Result:", result)
    elif user_choice == '4':
        result = perform_division(input_num1, input_num2)
        print("Result:", result)
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4).")

# Run the calculator
calculator()
