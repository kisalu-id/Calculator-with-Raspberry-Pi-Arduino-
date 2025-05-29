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
    

#calculate
def calculate(user_input):
    return eval(user_input) 


#output
def output_on_display(result):
    x = 6
