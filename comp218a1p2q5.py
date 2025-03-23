def percentage_to_gpa(percentage):
    if 90 <= percentage <= 100:
        return 4.0
    elif 85 <= percentage <= 89:
        return 3.9
    elif 80 <= percentage <= 84:
        return 3.7
    elif 77 <= percentage <= 79:
        return 3.3
    elif 73 <= percentage <= 76:
        return 3.0
    elif 70 <= percentage <= 72:
        return 2.7
    elif 67 <= percentage <= 69:
        return 2.3
    elif 63 <= percentage <= 66:
        return 2.0
    elif 60 <= percentage <= 62:
        return 1.7
    elif 57 <= percentage <= 59:
        return 1.3
    elif 53 <= percentage <= 56:
        return 1.0
    elif 50 <= percentage <= 52:
        return 0.7
    else:
        return 0.0


# Get user input
try:
    percentage = float(input("Enter your percentage grade: "))

    if 0 <= percentage <= 100:
        gpa = percentage_to_gpa(percentage)
        print(f"Your GPA is: {gpa:.1f}")
    else:
        print("Error: Please enter a valid percentage between 0 and 100.")
except ValueError:
    print("Error: Please enter a numerical value.")
