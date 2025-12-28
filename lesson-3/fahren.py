# Program to convert Fahrenheit to Celsius

inp = input("Enter Fahrenheit Temperature: ")

# Adding a try to check if we receive the correct input
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print("Please enter a number")
