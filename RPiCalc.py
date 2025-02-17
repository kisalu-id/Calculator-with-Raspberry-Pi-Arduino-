def main():
    expression = ""
    i = 0
    user_input = read_user_input(expression, i)
    #"27 + 6 "
    
    divided_user_input = user_input.split(" ")
    a = int(divided_user_input[0])
    operator = divided_user_input[1]
    b = int(divided_user_input[2])
    
    result = calculate(user_input)
    
    output_on_display(result)
    

#user input
def read_user_input(expression, i):
    option = "here is user input"

    match option:
        case 1:
            expression += "1"
        case 2:
            expression += "2"
        case 3:
            expression += "3"
        case 4:
            expression += "4"
        case 5:
            expression += "5"
        case 6:
            expression += "6"
        case 7:
            expression += "7"
        case 8:
            expression += "8"
        case 9:
            expression += "9"
        case 10:
            expression += "0"
        case 11:
            print("Addition")
            expression += "+"
        case 12:
            print("Substraction")
            expression += "-"
        case 13:
            print("Multiplication")
            expression += "*"
        case 14:
            print("Division")
            expression += "/"
        case 15:
            print("Case 15 executed")
        case 16:
            print("Input ended, next input")
            expression += " "
            i += 1
            if i > 1:
                return expression
            else:

                read_user_input(expression, i)
        case _:
            print("Invalid option")

#calculate
def calculate(user_input):
    result = 5
    return result


#output
def output_on_display(result):
    x = 6