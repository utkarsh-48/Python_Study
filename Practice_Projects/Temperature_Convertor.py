option = int(input("Choose the conversion \n"
               "1. Celsius to Fahrenheit "
               "2. Fahrenheit to Celsius : "))
if option == 1:
    cel = float((input("Enter Temperature in Celsius: ")))
    fah = (cel * 9 / 5) + 32
    print(f"Temperature in Fahrenheit: {fah}")
else:
    fah = float((input("Enter Temperature in Fahrenheit: ")))
    cel = (fah - 32) * 5/9
    print(f"Temperature in Celsius: {cel}")