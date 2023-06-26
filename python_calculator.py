import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    if num1 != 0 or num2 != 0:
        return num1 / num2
    else:
        return "error cannot divide by a zero, try again"
        
def square_root(num):
    if num > 0:
        return math.sqrt(num)
    else:
        print("Cannot Square Root A Negative Number")
        
def power(base, exponent):
    return math.pow(base, exponent)
    
def remainder(num1, num2):
    return num1 % num2
    
def log_function(num, base):
    return math.log(num, base)
    
def calculate_sin(angle):
    return math.sin(angle)

def calculate_cos(angle):
    return math.cos(angle)
    
def calculate_tan(angle):
    return math.tan(angle)




def calculator_screen():
    print("Welcome To The Calculator Screen")
    print("Enter two numbers first, to be able to acess the calculator menu")
    
    
    while True: 
        num1 = float(input("Enter Your First Number: "))
        num2 = float(input("Enter your Second Number: "))
        
        print("1. ADDITION")
        print("2. Subtraction")
        print("3, Multiplication")
        print("4, Division")
        print("5, Square Root")
        print("6, Exponent")
        print("7, Remainder")
        print("8, logarithim")
        print("9, Sine")
        print("10, Cosine")
        print("11, Tangent")
        print("12, EXIT")
        
        
        choice = int(input("Navigate The Menu With Numbers 1-8: "))
        
        
        if choice == 1:
            result = add(num1, num2)
            print(f"End Result: '{result}'")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"End Result: '{result}'")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"End Result: '{result}'")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"End Result: '{result}'")
        elif choice == 5:
            num = float(input("Enter a positive Whole Number: "))
            result = square_root(num)
            print(f"End Result: '{result}'")
        elif choice == 6:
            base = float(input("Type In the base(bottom number): "))
            exponent = float(input("Type in the exponent(Top Number): "))
            result = power(base, exponent)
            print (f"The result is '{result}'")
        elif choice == 7:
            result = remainder(num1, num2)
            print(f"The Result is '{result}'")
        elif choice == 8:
            num = float(input("Enter A number: "))
            base = float(input("Enter the base: "))
            result = log_function(num, base)
            print(f"The Result is '{result}'")
        elif choice == 9:
            angle = math.radians(float(input("Enter an angle number(sine): ")))
            result = calculate_sin(angle)
            print(f"The Result is '{result}'")
        elif choice == 10:
            angle = math.radians(float(input("Enter an angle number(cosine): ")))
            result = calculate_cos(angle)
            print(f"The Result is '{result}'")
        elif choice == 11:
            angle = math.radians(float(input("Enter an angle number(tangent): ")))
            result = calculate_tan(angle)
            print(f"The Result is '{result}'")
        elif choice == 12:
            print("You Have Chosen To Exit The Program Goodbye")
            break
        else:
            print("Invalid Option Selected, try again")
    
          
    
calculator_screen()