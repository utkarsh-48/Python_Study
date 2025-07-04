def prime_number(num):
    if num <= 1:
        print(f"{num} is not a prime number ")
        return
    for i in range(2,int((num **0.5)+1)):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return
    print(f"{num} is a prime number")

while True:
   try:
    number = int(input("Enter Your Number: "))
    prime_number(number)
   except ValueError:
       print("Please Enter a Number")