'''
Question
implement receipt_formatter(name, quantity, price)
calculate:
* subtotal = quantity * price
* tax = 7.5% of subtotal
* total = subtotal + tax
return a four-line receipt containing:
* customer
* subtotal
* tax
* total

Round monetary values to exactly 2 decimal places
if quantity is zero or negative, return: invalid quantity.
if price is negative, return: invalid price.


#solution
def receipt_formatter(name, quantity, price):

    subtotal = quantity * price
    tax = subtotal * 0.075
    total = subtotal + tax

    if quantity <= 0:
        return "Invalid quantity"
    if price < 0:
        return "Invalid price"

    return f"Customer: {name} \nSubtotal: {subtotal:.2f}\nTax: {tax:.2f}\nTotal: {total:.2f}"
print(receipt_formatter("Mariam", 2, 2000))


# Question 2
implement validate_pass(pass_code) using guard clauses.
return immediately for each invalid case in this order:
* Empty pass "no pass"
* Less than 5 characters "too short"
* Doesnt start with "P" "invalid prefix"
* Contains a space "invalid format"
* Otherwise "valid"
'''
def validate_pass(pass_code):
    if pass_code == "":
        return "no pass"
    elif len (pass_code) < 5:
        return "too short"
    elif pass_code[0] != "P":
        return "invalid prefix"
    elif " " in pass_code:
        return "invalid format"
    else:
        return "valid"
print(validate_pass(""))
print(validate_pass("Pa1"))
print(validate_pass("hello123"))
print(validate_pass("P123 45"))
print(validate_pass("P12345"))    
                  