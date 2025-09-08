print("Welcome to the fahrenheit to celsius converter!")
while True:
    ask = input("What would you like to do? \n 1. Convert fahrenheit to celsius \n 2. Convert celsius to fahrenheit \n ")
    if ask == "1":
        while True:
            fahrenheit = float(input("Enter the temperature in fahrenheit: "))
            if fahrenheit < -459.67:
                print("That temperature is below absolute zero (-459.67) and is not possible.")
                continue
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit} degrees fahrenheit is equal to {celsius}° degrees celsius.")
            break
    elif ask == "2":
        while True:
            celsius = float(input("Enter the temperature in celsius: "))
            if celsius < -273.15:
                print("That temperature is below absolute zero (-273.15) and is not possible.")
                continue
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} degrees celsius is equal to {fahrenheit}° degrees fahrenheit.")
            break
    else:
        print("Please enter a valid option (1 or 2).")