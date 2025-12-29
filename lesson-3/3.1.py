# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly
# rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a
# rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and
# float() to convert the string to a number. Do not worry about error checking the user input - assume the user types
# numbers properly.

hours = input("Enter hours: ")
hours_float = float(hours)

rate = input("Enter Rate: ")
rate_float = float(rate)

normal_pay = hours_float * rate_float
overtime_rate = 1.5 * rate_float
full_time_pay = 40.0 * rate_float
full_time_hours = 40.0
overtime_pay = full_time_pay + ((hours_float - full_time_hours) * overtime_rate)

if hours_float > 40.0:
    print(overtime_pay)
else:
    print(normal_pay)
