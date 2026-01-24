import numpy as np
import scipy.integrate as spi

def menu():
    print("\nMenu:")
    print("\t1. y = asin(bx)")
    print("\t2. y = acos(bx)")
    print("\t3. y = atan(bx)")
    print("\t4. Print the menu again")
    print("\t5. Exit")

def limit_input():
    while True:
        try:
            lim_a = float(input("\nEnter the lower limit of integration: "))
            lim_b = float(input("Enter the upper limit of integration: "))
            if lim_a > lim_b:
                print("Lower limit must be less than or equal to upper limit.")
                continue
            return lim_a, lim_b
        except ValueError:
            print("Please enter valid numbers.")

def get_parameters():
    while True:
        try:
            a = float(input("Enter the value of a: "))
            b = float(input("Enter the value of b: "))
            return a, b
        except ValueError:
            print("Please enter valid numbers.")

def periodicity_check(func_name, b, x):
    period_dict = {
        'sin': 2 * np.pi / abs(b) if b != 0 else np.inf,
        'cos': 2 * np.pi / abs(b) if b != 0 else np.inf,
        'tan': np.pi / abs(b) if b != 0 else np.inf,
    }
    
    if func_name == 'tan':
        period = period_dict['tan']
        x_mod = ((x + period / 2) % period) - period / 2
    else:
        period = period_dict[func_name]
        x_mod = x % period

    return x_mod

def integrate_function(func, lim_a, lim_b):
    result, error = spi.quad(func, lim_a, lim_b)

    print(result)
    
    if np.isclose(result, 0.0):
        print(f"The integral for y = a{func_name}(bx) from {lim_a} to {lim_b} evaluates to 0.")
    else:
        print(f"The integral for y = a{func_name}(bx) from {lim_a} to {lim_b} evaluates to {result} ± {error}")

    return result, error

def sin_function(x, a, b):
    x_mod = periodicity_check('sin', b, x)
    return a * np.sin(b * x_mod)

def cos_function(x, a, b):
    x_mod = periodicity_check('cos', b, x)
    return a * np.cos(b * x_mod)

def tan_function(x, a, b):
    x_mod = periodicity_check('tan', b, x)
    return a * np.tan(b * x_mod)

menu()

while True:
    choice = input("\nSelect an option (1-5): ")
    
    if choice == '1':
        func_name = 'sin'
        a, b = get_parameters()
        lim_a, lim_b = limit_input()
        x = np.linspace(lim_a, lim_b, 1000)
        x_mod = periodicity_check('sin', b, x)
        lim_a, lim_b = x_mod[0], x_mod[-1]
        func = lambda x: sin_function(x, a, b)
        integrate_function(func, lim_a, lim_b)

    elif choice == '2':
        func_name = 'cos'
        a, b = get_parameters()
        lim_a, lim_b = limit_input()
        x = np.linspace(lim_a, lim_b, 1000)
        x_mod = periodicity_check('cos', b, x)
        lim_a, lim_b = x_mod[0], x_mod[-1]
        func = lambda x: cos_function(x, a, b)
        integrate_function(func, lim_a, lim_b)

    elif choice == '3':
        func_name = 'tan'
        a, b = get_parameters()
        lim_a, lim_b = limit_input()
        x = np.linspace(lim_a, lim_b, 1000)
        x_mod = periodicity_check('tan', b, x)
        lim_a, lim_b = x_mod[0], x_mod[-1]
        '''if lim_b == np.pi/(2 * abs(b)):
            lim_b -= 1e-6'''
        print(lim_a, lim_b, np.pi/(2 * abs(b)))
        func = lambda x: tan_function(x, a, b)
        if np.isclose(np.pi/(2 * abs(b)), lim_b) and np.isclose(-np.pi/(2 * abs(b)), lim_a):
            integrate_function(func, lim_a, lim_b)
        elif np.isclose(np.pi/(2 * abs(b)), lim_b):
            print(f"The integral for y = a{func_name}(bx) from {lim_a} to {lim_b} diverges to +∞.")
        elif np.isclose(-np.pi/(2 * abs(b)), lim_a):
            print(f"The integral for y = a{func_name}(bx) from {lim_a} to {lim_b} diverges to -∞.")

    elif choice == '4':
        menu()

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
        continue
