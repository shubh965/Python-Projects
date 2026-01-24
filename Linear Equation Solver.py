import numpy as np

while True:
    try:
        n = int(input("Enter number of variables: "))
        if n <= 0:
            print("n must be positive.")
            continue
        break
    except ValueError:
        print("Please enter a positive integer.")

A = []
B = []

print("Enter the coefficients of the equations:")
for i in range(n):
    row = []
    while len(row) != n:
        print(f"Please enter exactly {n} coefficients.")
        try:
            row = list(map(float, input(f"Equation {i+1}: ").split()))
        except ValueError:
            print("Enter only numbers.")
    A.append(row)

print("Enter the constants of the equations:")
for i in range(n):
    while True:
        try:
            value = float(input(f"Constant for equation {i+1}: "))
            break
        except ValueError:
            print("Enter a valid number.")
    B.append(value)

A = np.array(A)
B = np.array(B)

if abs(np.linalg.det(A)) < 1e-10:
    print("System has no unique solution.")
    exit(1)

try:
    solution = np.linalg.solve(A, B)
    print("Solution:")
    for i in range(n):
        print(f"x{i+1} = {solution[i]}")
except np.linalg.LinAlgError as e:
    print("Error solving the system of equations:", e)
