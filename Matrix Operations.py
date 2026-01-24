import numpy as np 

def menu():
    print("\nMenu:")
    print("1. Addition of Matrices")
    print("2. Subtraction of Matrices")
    print("3. Multiplication of Matrices")
    print("4. Transpose of a Matrix")
    print("5. Determinant of a Matrix")
    print("6. Inverse of a Matrix")
    print("7. Rank of a Matrix")
    print("8. Trace of a Matrix")
    print("9. Eigenvalues and Eigenvectors of a Matrix")
    print("10. Show the Menu")
    print("11. Exit")

def input_matrix():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            matrix = []

            for i in range(rows):
                while True:
                    row = list(map(float, input(f"Enter row {i+1} ({cols} values): ").split()))
                    if len(row) == cols:
                        matrix.append(row)
                        break
                    else:
                        print(f"Please enter exactly {cols} values.")

            return np.array(matrix)

        except ValueError:
            print("Invalid input. Please enter numeric values.")

def get_single_matrix():
    print("\nEnter the matrix:")
    return input_matrix()

def determinant(M):
    if M.shape[0] != M.shape[1]:
        return None

    det = np.linalg.det(M)
    return 0 if abs(det) < 1e-10 else det # Treat very small values as zero (floating-point tolerance)

menu()

while True:
    try:
        n = int(input("\nPlease select an option from the menu (1-11): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if n == 1:
        print("\nEnter first matrix:")
        M1 = input_matrix()
        print("Enter second matrix:")
        M2 = input_matrix()

        if M1.shape == M2.shape:
            print("\nResult of addition:")
            print(M1 + M2)
        else:
            print("Matrices must have the same dimensions for addition.")

    elif n == 2:
        print("\nEnter first matrix:")
        M1 = input_matrix()
        print("Enter second matrix:")
        M2 = input_matrix()

        if M1.shape == M2.shape:
            print("\nResult of subtraction:")
            print(M1 - M2)
        else:
            print("Matrices must have the same dimensions for subtraction.")

    elif n == 3:
        print("\nEnter first matrix:")
        M1 = input_matrix()
        print("Enter second matrix:")
        M2 = input_matrix()

        if M1.shape[1] == M2.shape[0]:
            print("\nResult of multiplication:")
            print(M1 @ M2)
        else:
            print("Number of columns of first matrix must match number of rows of second matrix.")

    elif n == 4:
        get_single_matrix()
        print("\nTranspose of the matrix:")
        print(M.T)

    elif n == 5:
        get_single_matrix()

        det = determinant(M)
        if det is None:
            print("Determinant is only defined for square matrices.")
        else:
            print("Determinant:", det)

    elif n == 6:
        get_single_matrix()

        det = determinant(M)
        if det is None:
            print("Inverse is only defined for square matrices.")
        elif det == 0:
            print("The given matrix is non-invertible.")
        else:
            print("Inverse of the matrix:")
            print(np.linalg.inv(M))
    
    elif n == 7:
        get_single_matrix()
        print("Rank of the matrix:", np.linalg.matrix_rank(M))
    
    elif n == 8:
        get_single_matrix()
        M = input_matrix()
        if M.shape[0] != M.shape[1]:
            print("Trace is only defined for square matrices.")
        else:
            print("Trace of the matrix:", np.trace(M))
    
    elif n == 9:
        get_single_matrix()
        if M.shape[0] != M.shape[1]:
            print("Eigenvalues and Eigenvectors are only defined for square matrices.")
        else:
            eigenvalues, eigenvectors = np.linalg.eig(M)
            print("Eigenvalues:")
            print(eigenvalues)
            print("Eigenvectors (each column corresponds to the respective eigenvalue):")
            print(eigenvectors)

    elif n == 10:
        menu()

    elif n == 11:
        print("Thank you. Exiting program.")
        break

    else:
        print("Enter a valid option between 1 and 11.")
