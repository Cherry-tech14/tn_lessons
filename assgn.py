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
'''

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