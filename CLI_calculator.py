def calculator():
    try:
        a = float(input("\nEnter first number: "))
        b = float(input("Enter second number: "))

        print("\nSelect operation:")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")

        op = input("Enter operator: ")

        match op:
            case "+":
                result = a + b
            case "-":
                result = a - b
            case "*":
                result = a * b
            case "/":
                if b == 0:
                    print("❌ Cannot divide by zero")
                    return
                result = a / b
            case _:
                print("❌ Invalid operator")
                return

        print(f"✅ Result: {result}")

    except ValueError:
        print("❌ Please enter valid numbers")


while True:
    calculator()

    again = input("\nDo you want another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("Calculator closed 👋")
        break