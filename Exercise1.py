x = int(input("Enter the Starting number: "))
y = int(input("Enter the ending number: "))
count = 0
for number in range(x, y):
    if number % 2 == 0:
        print(number)
        count += 1
    # else:
    #     print("odd")
print("Number of even numbers:", count)  # my answer
# print(f"We have {count} even numbers") *** mosh answer**
