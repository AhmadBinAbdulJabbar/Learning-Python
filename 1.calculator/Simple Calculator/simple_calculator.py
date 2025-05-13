from msvcrt import getch
import sys, os

def display_calculator(display:str):
    print(" _____________________ ")
    print("|  _________________  |")
    print(f"| |{display:>17}| |")
    print("| |_________________| |")
    print("|  ___ ___ ___   ___  |")
    print("| | 7 | 8 | 9 | | / | |")
    print("| |___|___|___| |___| |")
    print("| | 4 | 5 | 6 | | * | |")
    print("| |___|___|___| |___| |")
    print("| | 1 | 2 | 3 | | - | |")
    print("| |___|___|___| |___| |")
    print("| | 0 | . | = | | + | |")
    print("| |___|___|___| |___| |")
    print("|_____________________|")

def get_input():
    key = getch()
    return key.decode()

operators = ['+', '-', '/', '*', '%'] 

def calculate(num1, operator: str, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error"
        return num1 / num2
    elif operator == '%':
        return num1 % num2

def calculate_expression(expression: str) -> str:
    cal = 0
    current_num_str = ""
    current_operator = ""

    if expression[0] == '-':
        current_num_str = '-'
        startIndex = 1
    else:
        startIndex = 0
    for c in expression[startIndex:]:
        if c not in operators:
            current_num_str += c
        elif c in operators:
            if current_operator in operators:
                if '.' in current_num_str:
                    cal = calculate(cal, current_operator, float(current_num_str))
                else:
                    cal = calculate(cal, current_operator, int(current_num_str))
            else:  
                if '.' in current_num_str:
                    cal = float(current_num_str)
                else:
                    cal = int(current_num_str)
            current_operator = c
            current_num_str = ""

    if '.' in current_num_str:
        cal = calculate(cal, current_operator, float(current_num_str))
    else:
        cal = calculate(cal, current_operator, int(current_num_str))      
    
    return str(cal)
        
def check_decimal(expression):
    last_number = ''
    for char in expression[::-1]:
        if char in operators:
            break
        last_number = char + last_number
    if '.' in last_number:
        return False
    else:
        return True

def handle_expression(expression: str, key: str) -> str:
    if(key == "A" or key == 'a'):
        sys.exit()
    elif(key == 'C' or key == 'c'):
        expression = ""
    elif key == '=' and expression and expression[-1] not in operators:
        expression = calculate_expression(expression)
    elif key.isdigit() and len(expression) < 17:
        expression += key
    elif key == '.' and check_decimal(expression):
        expression += key
    elif key in operators:
        if expression == "":
            if key == "-":
                expression += key
            else:
                return ""
        elif expression[-1] not in operators:
            expression += key
    elif key in ['\b', '\x08', '\x7f']: 
        expression = expression[:-1]
    
    return expression

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 100)   

def main():
    expression = ""
    while True:
        # clear_screen()
        display_calculator(expression)
        if expression == "Error":
            expression = ""
        key = get_input()
        expression = handle_expression(expression, key)
        


if __name__ == "__main__":
    main()


