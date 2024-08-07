
from calc_func import do_addition, do_subtraction
def main():
    print('welcome to the calculator')
    print(''''
          \nSelect the function from the five option
          1. ADD
          2. SUBTRACT
          ''')
    
    user_input = input('select function')
    a = int(input('value of A '))
    b = int(input('value of B '))
    
    if user_input == '1':
        result = do_addition(a, b)
    elif user_input == '2':
        result = do_subtraction(a, b)
        
    print('Result:', result)
    
if __name__ == '__main__':
    main()