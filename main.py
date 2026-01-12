import calculator

print("Welcome to CLI Calculator!", "Enter 'exit' to quit.", sep='\n')

user_input = 0
while True:
    user_input = input("Enter calculation: ")

    if not user_input != "exit":
        break

    user_input = user_input.split(" ")

    if len(user_input) != 3:
        print("Invalid input format. Use: number operator number")
        continue

    match user_input[1]:
        case '+':
            calc_output = calculator.add(float(user_input[0]), float(user_input[2]))
        case '-':
            calc_output = calculator.subtract(float(user_input[0]), float(user_input[2]))
        case '*':
            calc_output = calculator.multiply(float(user_input[0]), float(user_input[2]))
        case '/':
            calc_output = calculator.divide(float(user_input[0]), float(user_input[2]))
        case _:
            print("Invalid Operation")
            calc_output = ""

    if calc_output != "":
        print(calc_output)
