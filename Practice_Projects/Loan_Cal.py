def calculate_loan(principal, interest, years):
    rate = interest / 100 / 12
    months = years * 12
    payment = float(principal * rate / (1 - (1 + rate) ** -months))
    return payment

principal = float(input("Enter the principal: "))
Interest = float(input("Enter the Interest: "))
Years = float(input("Enter the Years: "))

payment = calculate_loan(principal,Interest, Years)
print(f"{payment:.2f}")

