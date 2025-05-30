"""
User manual..
EN:
DE:
"""


def main():
    expression = ""
    print_user_manual()
    
    i = 0
    #until  "enter" is pressed (bttn 16)
    while True:
        user_input = read_user_input(expression, i)
        #"27 + 6 "
        
        result = calculate(user_input)
        
        output_on_display(result)



def print_user_manual():
    x = 5


def read_user_input(expression, i):
    option = int(input("Press a button (0–9 = digits, 11–14 = ops, 15 = clear, 16 = enter): "))
    
    if option == 16:  #end input and calculate
        if expression == "":
            print("No input given!")
        else:
            expression += "="
            return expression
    
    elif option == 15:  #"delete" button
        print("Deleting all input")
        expression = ""
        continue

    
    elif 1 <= option <= 10: #buttons 1-10, but numbers 0-9
        expression += (str(option) - 1)
    
    
    elif option == 11:
        if expression != "" and expression != " ":
            if "+-*/" not in expression:
                expression += "+"

    elif option == 12:
        expression += "-"
        
    elif option == 13:
        expression += "*"
    elif option == 14:
        expression += "/"
        
    print(expression) #update each time any sign was added


#calculate
def calculate(user_input):
    try:
        result = eval(user_input)
        return result
    except Exception as e:
        print("Error in calculation:", e)
        return None


#output
def output_on_display(result):
    if result is not None:
        print(f"Result: {result}")
    else:
        print("Nope!")



if __name__ == '__main__':
    main()
