import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def menu():
    print("\nMenu:")
    print("\t1. Trigonometric Functions")
    print("\t2. Exponential Function")
    print("\t3. Logarithmic Function")
    print("\t4. Polynomial Function")
    print("\t5. Print the menu again")
    print("\t6. Exit")

def get_parameters():
    while True:
        try:
            a = float(input("Enter the value of a: "))
            b = float(input("Enter the value of b: "))
            return a, b
        except ValueError:
            print("Please enter valid numbers.")

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

def integrate_function(func, lim_a, lim_b):
    result, error = quad(func, lim_a, lim_b)
    
    if np.isposinf(result):
        return float('inf'), 0.0
    elif np.isneginf(result):
        return float('-inf'), 0.0
    elif np.isclose(result, 0.0):
        return 0.0, 0.0
    else:
        return result, error

def print_results(result, error, lim_a, lim_b, func_name):
    if np.isinf(result):
        if result > 0:
            print(f"The integral for {func_name} from {lim_a} to {lim_b} diverges to +∞.")
        else:
            print(f"The integral for {func_name} from {lim_a} to {lim_b} diverges to -∞.")
    elif np.isclose(result, 0.0):
        print(f"The integral for {func_name} from {lim_a} to {lim_b} evaluates to 0.")
    else:
        print(f"The integral for {func_name} from {lim_a} to {lim_b} evaluates to {result} ± {error}")

def plot_function(func, lim_a, lim_b, title, func_name = ' '):
    x = np.linspace(lim_a, lim_b, 400)
    y = func(x)
    if func_name == 'tan':
        y = np.where(np.abs(y) > 10, np.nan, y)
    plt.plot(x, y, label=title)
    plt.fill_between(x, y, alpha=0.3)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()

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

def sin_function(x, a, b):
    x_mod = periodicity_check('sin', b, x)
    return a * np.sin(b * x_mod)

def cos_function(x, a, b):
    x_mod = periodicity_check('cos', b, x)
    return a * np.cos(b * x_mod)

def tan_function(x, a, b):
    x_mod = periodicity_check('tan', b, x)
    return a * np.tan(b * x_mod)

def exp_function(x, a, b):
    return a * np.exp(b * x)

def log_function(x, a, b):
    return a * np.log(b * x)

def poly_function(x, coeffs):
    return sum(c * x**i for i, c in enumerate(coeffs))

menu()

while True:
    choice = input("\nSelect an option (1-6): ")
    
    if choice == '1':
        print("\nTrigonometric Functions:")
        print("\t1. y = asin(bx)")
        print("\t2. y = acos(bx)")
        print("\t3. y = atan(bx)\n")

        trig_choice = input("Select a trigonometric function (1-3): ")

        if trig_choice == '1':
            func_name = 'sin'
            a, b = get_parameters()
            lim_a, lim_b = limit_input()
            lim_a1, lim_b1 = lim_a, lim_b
            x = np.linspace(lim_a, lim_b, 1000)
            x_mod = periodicity_check('sin', b, x)
            lim_a, lim_b = x_mod[0], x_mod[-1]
            func = lambda x: sin_function(x, a, b)
            result, error = integrate_function(func, lim_a, lim_b)
            print_results(result, error, lim_a1, lim_b1, f"{a} * sin({b} * x)")
            plot_function(func, lim_a1, lim_b1, f"{a} * sin({b} * x)")

        elif trig_choice == '2':
            func_name = 'cos'
            a, b = get_parameters()
            lim_a, lim_b = limit_input()
            lim_a1, lim_b1 = lim_a, lim_b
            x = np.linspace(lim_a, lim_b, 1000)
            x_mod = periodicity_check('cos', b, x)
            lim_a, lim_b = x_mod[0], x_mod[-1]
            func = lambda x: cos_function(x, a, b)
            result, error = integrate_function(func, lim_a, lim_b)
            print_results(result, error, lim_a1, lim_b1, f"{a} * cos({b} * x)")
            plot_function(func, lim_a1, lim_b1, f"{a} * cos({b} * x)")

        elif trig_choice == '3':
            func_name = 'tan'
            a, b = get_parameters()
            lim_a, lim_b = limit_input()
            lim_a1, lim_b1 = lim_a, lim_b
            x = np.linspace(lim_a, lim_b, 1000)
            x_mod = periodicity_check('tan', b, x)
            lim_a, lim_b = x_mod[0], x_mod[-1]
            print(lim_a, lim_b, np.pi/(2 * abs(b)))
            func = lambda x: tan_function(x, a, b)
            if np.isclose(np.pi/(2 * abs(b)), lim_b) and np.isclose(-np.pi/(2 * abs(b)), lim_a):
                result, error = integrate_function(func, lim_a, lim_b)
                print_results(result, error, lim_a1, lim_b1, f"{a} * tan({b} * x)")
            elif np.isclose(np.pi/(2 * abs(b)), lim_b):
                print(f"The integral for y = a{func_name}(bx) from {lim_a1} to {lim_b1} diverges to +∞.")
            elif np.isclose(-np.pi/(2 * abs(b)), lim_a):
                print(f"The integral for y = a{func_name}(bx) from {lim_a1} to {lim_b1} diverges to -∞.")
            plot_function(func, lim_a1, lim_b1, f"{a} * tan({b} * x)", func_name)
        
        else:
            print("\nInvalid choice. Please try again.")
    
    elif choice == '2':
        print("\ny = a * exp(bx)")
        print()
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))

        func = lambda x: exp_function(x, a, b)
        lim_a, lim_b = limit_input()
        result, error = integrate_function(func, lim_a, lim_b)

        print_results(result, error, lim_a, lim_b, f"{a} * exp({b} * x)")
        plot_function(func, lim_a, lim_b, f"{a} * exp({b} * x)")
    
    elif choice == '3':
        print("\ny = a * log(bx)")
        print()
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))

        if b <= 0:
            print("b must be positive for the logarithmic function.")
            continue

        func = lambda x: log_function(x, a, b)
        lim_a, lim_b = limit_input()
        result, error = integrate_function(func, lim_a, lim_b)

        print_results(result, error, lim_a, lim_b, f"{a} * log({b} * x)")
        plot_function(func, lim_a, lim_b, f"{a} * log({b} * x)")
    

    elif choice == '4':
        print("\nPolynomial Function: y = c0 + c1*x + c2*x^2 + ... + cn*x^n")
        print()
        degree = int(input("Enter the degree of the polynomial: "))
        coeffs = []
        for i in range(degree + 1):
            coeff = float(input(f"Enter coefficient for x^{i}: "))
            coeffs.append(coeff)

        func = lambda x: poly_function(x, coeffs)
        lim_a, lim_b = limit_input()
        result, error = integrate_function(func, lim_a, lim_b)

        print_results(result, error, lim_a, lim_b, "Polynomial Function")
        plot_function(func, lim_a, lim_b, "Polynomial Function")
    
    elif choice == '5':
        menu()
    
    elif choice == '6':
        print("\nExiting the program.")
        break

    else:
        print("\nInvalid choice. Please try again.")
