import calculator

print("Welcome to CLI Calculator!", "Enter 'exit' to quit.", sep='\n')

user_input = 0
while user_input != "exit":
    print("Enter calculation: ")
    user_input = input()
    user_input = user_input.split(" ")

    match user_input[1]:
        case '+':
            calculator.add(user_input[0], user_input[2])
        case '-':
            calculator.subtract(user_input[0], user_input[2])
        case '+':
            calculator.multiply(user_input[0], user_input[2])
        case '/':
            calculator.divide(user_input[0], user_input[2])



