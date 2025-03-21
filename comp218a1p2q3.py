# Program to calculate employee's pay based on work hours and day type

# Constants for pay rates
weekday_rate = 15
overtime_rate = 21
weekend_rate = 21
standard_hours = 8

# Input from the user for the type of day and hours worked
day_type = input("Is it a 'weekday' or 'weekend'? ").lower()
hours_worked = float(input("Enter the number of hours worked: "))

# Initialize the pay variable
pay = 0

# Calculate pay for weekdays
if day_type == "weekday":
    if hours_worked <= standard_hours:
        pay = hours_worked * weekday_rate
    else:
        # Regular pay for the first 8 hours and overtime for extra hours
        pay = (standard_hours * weekday_rate) + ((hours_worked - standard_hours) * overtime_rate)

# Calculate pay for weekends (all hours at weekend rate)
elif day_type == "weekend":
    pay = hours_worked * weekend_rate

# Output the calculated pay
print(f"The employee should be paid: ${pay:.2f}")