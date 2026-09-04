'''
age = "24"
age = int(age)
print(age)


price = "5000"
tax = 500
print(int(price) + tax)


# string parsing
user_input = "24"
value = int(user_input)
print(value + 10)

#handling diff numbers formats: Removing commas
price_with_comma = "2,500.00"
cleaned = price_with_comma.replace(",", "")
value = float(cleaned)
print(value)

# Removing currency symbols
price_with_currency = "#2500.00"
cleaned = price_with_currency.replace("#", "")
value = float(cleaned)
print(value)

# Handling whitespace
price_with_spaces = " 2500.50 "
cleaned = price_with_spaces.replace(" ", "")
value = float(cleaned)
print(value)

# parsing multiple numbers
numbers = "10 20 30 40"
parts = numbers.split()
print(parts)

#functions that handles multiple formats
def parse_nigerian_number(input_string):
    cleaned = input_string.replace(",", "")
    cleaned = cleaned.strip()
    try:
        return float(cleaned)
    except ValueError:
            cleaned = cleaned.replace("", "")
            return float(cleaned)
            print(parse_nigerian_number("₦2,500.00"))  # 2500.0
print(parse_nigerian_number("1,500.50"))   # 1500.5
print(parse_nigerian_number("3000"))       # 3000.0
print(parse_nigerian_number("  250  "))    # 250.0
'''

transactions = "5000 2500 10000"
transactions = transactions.split()
transactions = [int(amount) for amount in transactions]
print(transactions)