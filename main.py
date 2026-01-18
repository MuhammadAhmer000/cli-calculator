import calculator

print("Welcome to CLI Calculator!", "Enter 'exit' to quit.", sep='\n')

while True:

    user_input = input("Enter calculation: ")

    if user_input == "exit":
        break

    user_input = user_input.split(" ")

    if len(user_input) != 3:
        print("Invalid input format. Use: number operator number")
        continue

    try:
        a = float(user_input[0])
        b = float(user_input[2])
    except ValueError:
        print("Invalid Number")
        continue

    match user_input[1]:
        case "+":
            calc_output = calculator.add(a, b)
        case "-":
            calc_output = calculator.subtract(a, b)
        case "*":
            calc_output = calculator.multiply(a, b)
        case "/":
            calc_output = calculator.divide(a, b)
        case _:
            print("Invalid Operation")
            calc_output = None

    if calc_output is not None:
        print(calc_output)
