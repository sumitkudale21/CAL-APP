
from calc_func import do_addition, do_subtraction
from area import cal_area_rectangle
from multiply import do_multiplication
def main():
    print('welcome to the calculator')
    print(''''
          \nSelect the function from the five option
          1. ADD
          2. SUBTRACT
          3. MULTIPLY
          4. AREA
          ''')
    
    user_input = input('select function')
    a = int(input('value of A '))
    b = int(input('value of B '))
    
    if user_input == '1':
        result = do_addition(a, b)
    elif user_input == '2':
        result = do_subtraction(a, b)
    elif user_input == '3':
        result = do_multiplication(a, b)
    elif user_input == '4':
        result = cal_area_rectangle(a, b)
        
    print('Result:', result)
    
if __name__ == '__main__':
    main()