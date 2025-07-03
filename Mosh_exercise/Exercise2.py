def fizz_buzz(num):
    if (num % 5 ==0) and (num % 3 ==0):
        return "fizz_buzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"

    return num


number = int(input("Enter the number: "))
print(fizz_buzz(number))