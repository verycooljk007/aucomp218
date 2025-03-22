def calculate_tax(income):
    tax_brackets = [
        (57375, 0.15),         # 15% on income up to $57,375
        (114750, 0.205),       # 20.5% on income over $57,375 up to $114,750
        (177882, 0.26),        # 26% on income over $114,750 up to $177,882
        (253414, 0.29),        # 29% on income over $177,882 up to $253,414
        (float('inf'), 0.33)   # 33% on income over $253,414
    ]

    tax = 0
    prev_limit = 0

    for limit, rate in tax_brackets:
        if income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income - prev_limit) * rate
            break

    return tax

# Get user input
try:
    income = float(input("Enter your total annual income: $"))

    if income < 0:
        print("Error: Income cannot be negative.")
    else:
        tax = calculate_tax(income)
        print(f"Total federal income tax owed: ${tax:,.2f}")

except ValueError:
    print("Error: Please enter a valid numerical income.")