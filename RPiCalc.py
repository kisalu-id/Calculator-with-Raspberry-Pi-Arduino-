
def main():
    expression = ""
    print_user_manual()
    
    #until  "enter" is pressed (btn 16)
    while True:
        expression = read_user_input(expression)
        #"27+6="
        expression = expression.strip()
        if expression.endswith("="):
            expression = expression[:-1] #remove "="
            if any(op in expression for op in "+-*/"):
                result = calculate(expression)
                
                print(result)
                expression = ""
                #output_on_display(result)
            else:
                expression = "" #reset



def print_user_manual():
    print("""
    ==============================
    USER MANUAL / BENUTZERHANDBUCH
    ==============================

    ENG:
    ---------
    Use the 16-key keyboard to enter a simple expression and calculate it.
    - Keys 0–9     → Enter digits 0–9
    - Key 11       → Addition (+)
    - Key 12       → Subtraction (-)
    - Key 13       → Multiplication (*)
    - Key 14       → Division (/)
    - Key 15       → Clear expression
    - Key 16       → Calculate result (Enter)
    - You see the expression build up live on screen.

    DE:
    ---------
    Benutze die 16-Tasten-Tastatur, um einen einfachen Ausdruck einzugeben und zu berechnen.
    - Tasten 0–9   → Ziffern 0–9 eingeben
    - Taste 11     → Addition (+)
    - Taste 12     → Subtraktion (-)
    - Taste 13     → Multiplikation (*)
    - Taste 14     → Division (/)
    - Taste 15     → Ausdruck löschen
    - Taste 16     → Ergebnis berechnen (Enter)
    - Du siehst den Ausdruck live auf dem Bildschirm entstehen.
    """)



def read_user_input(expression):
    #option = int(input("Press a button (0–9 = digits, 11–14 = ops, 15 = clear, 16 = enter): "))
    
    #code for RPi
    # if option == 16:  #end input and calculate
    #     if expression == "":
    #         print("No input given!")
    #     else:
    #         expression += "="
    #         return expression
    
    # elif option == 15:  #"delete" button
    #     print("Deleting all input")
    #     expression = ""
    #     return expression

    
    # elif 1 <= option <= 10: #buttons 1-10, but numbers 0-9
    #     #code for RPi 
    #     #expression += str(option - 1)
    #     expression += str(option)
    
    
    # elif option == 11:
    #     if expression != "" and expression != " ":
    #         if "+-*/" not in expression:
    #             expression += "+"

    # elif option == 12:
    #     expression += "-"
        
    # elif option == 13:
    #     expression += "*"
        
    # elif option == 14:
    #     expression += "/"
    # else:
    #     print("Invalid option.")
    
    
    #for now testing the program on PC
    
    option = input("Press a key (0-9, +, -, *, /, = to calculate, c to clear): ").strip()
    
    if len(option) != 1:
        print("Please enter exactly one key.")
        return expression
    
    if option == "=":  #end input and calculate
        if expression.strip() == "":
            print("No input given!")
        else:
            expression += "="
    
    elif option.lower() == "c":  #"delete" button
        print("Deleting all input")
        expression = ""
        return expression

    
    elif str(option) in "0123456789": #numbers 0-9
        expression += str(option)
    
    
    elif option == "+":
        if expression != "" and expression != " ":
            if "+-*/" not in expression:
                expression += "+"

    elif option == "-":
        expression += "-"
        
    elif option == "*":
        expression += "*"
        
    elif option == "/":
        expression += "/"
    else:
        print("Invalid option.")
    
    print(expression) #update each time any sign was added
    return expression



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
