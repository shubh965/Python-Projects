import numpy as np
import matplotlib.pyplot as plt

def menu():
    print("\nMenu:")
    print("\t1. Basic Projectile Motion for n projectiles at differing heights and starting points.")
    print("\t2. Check which of the given projectiles hit a target.")
    print("\t3. Plot Range vs Angle for a given velocity.")
    print("\t4. Print Menu again.")
    print("\t5. Exit")

def take_input(n):
    v = float(input(f"Enter the velocity for {n} projectile in m/s: "))
    while True:
        theta = np.radians(float(input(f"Enter the angle for {n} projectile in degrees: ")))
        if 0 <= theta <= np.pi/2:
            break
        else:
            print("Please enter a valid angle between 0 and 90 degrees.")
    x = float(input(f"Enter the starting x-coordinate for {n} projectile in m: "))
    while True:
        y = float(input(f"Enter the starting y-coordinate for {n} projectile in m: "))
        if y >= 0:
            break
        else:
            print("Projectile can't be below ground.")

    return np.abs(v), theta, x, np.abs(y)

def simulation(n, v, theta, ch = 1, x = 0.0, y = 0.0, dt = 0.01):
    a_x = 0.0
    a_y = -9.81

    v_x = v * np.cos(theta)
    v_y = v * np.sin(theta)

    x_array = []
    y_array = []

    t = 0.0
    t_array = []

    while True:
        if y < 0:
            break
        v_x += a_x * dt
        v_y += a_y * dt

        x += v_x * dt
        y += v_y * dt

        t += dt

        x_array.append(x)
        y_array.append(y)
        t_array.append(t)
    
    x_array = np.array(x_array)
    y_array = np.array(y_array)
    t_array = np.array(t_array)

    if ch!= 3:
        print(f"\nRange of the {n} projectile: {x_array[-1]:.2f} m")
        print(f"Maximum Height of the {n} projectile: {np.max(y_array):.2f} m")
        print(f"The Time Taken by the {n} projectile is: {t_array[-1]:.2f} s")
    return x_array, y_array

def plot_trajectory(x, y):
    plt.legend()
    plt.title("Projectile Motion")
    plt.xlabel("Distance (m) -------->")
    plt.ylabel("Height (m) --------->")
    if x < 0:
        plt.xlim(left = x)
    else:
        plt.xlim(left = 0)
    plt.ylim(bottom = 0)
    plt.show()

plt.style.use('dark_background')
menu()
while True:
    ch = int(input("\nEnter your choice (1-5): "))

    if ch == 1:
        n = int(input("\nEnter the number of projectiles: "))
        v = []
        theta = []
        x = []
        y = []
        
        for i in range(n):
            vn, thetan, xn, yn = take_input(i + 1)
            v.append(vn)
            theta.append(thetan)
            x.append(xn)
            y.append(yn)
        
        v = np.array(v)
        theta = np.array(theta)
        x = np.array(x)
        y = np.array(y)

        for i in range(n):
            x_array, y_array = simulation(i + 1, v[i], theta[i], ch, x[i], y[i])
            plt.plot(x_array, y_array, label=f'Projectile {i+1}')
        
        plot_trajectory()
    
    elif ch == 2:
        v, theta, x, y = take_input(1)

        target_x = float(input("Enter the x-coordinate of the target in m: "))
        target_y = float(input("Enter the y-coordinate of the target in m: "))

        x_array, y_array = simulation(1, v, theta, ch, x, y)
        plt.plot(x_array, y_array, label='Projectile path')
        plt.plot(target_x, target_y, 'rx', label='Target')
        plot_trajectory()

        distance = np.sqrt((x_array - target_x)**2 + (y_array - target_y)**2)
        if np.any(distance < 0.1):
            print("The projectile hits the target.")
        else:
            print("The projectile does not hit the target.")


    elif ch == 3:
        v = float(input("Enter the velocity in m/s: "))
        angles = np.radians(np.arange(0, 91, 1))
        ranges = []

        for theta in angles:
            x_array, y_array = simulation(1, v, theta, ch)
            ranges.append(x_array[-1])

        plt.plot(np.degrees(angles), ranges)
        plt.title("Range vs Angle")
        plt.xlabel("Angle (degrees) -------->")
        plt.ylabel("Range (m) --------->")
        plt.grid()
        plt.show()
    
    elif ch == 4:
        menu()
    
    elif ch == 5:
        print("Exiting the program.")
        break