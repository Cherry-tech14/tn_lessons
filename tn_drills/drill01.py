# Convert temperature
'''
def solution(celsius):
    celsius = float(celsius)
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)
    '''

# Convert length
def solution(meters):
    meters = float(meters)
    centimeters = meters * 100
    millimeters = meters * 1000

    return f"Centimeters: {centimeters}\nMillimeters: {millimeters}"

# convert weight
def solution(kilograms):
    kilograms = float(kilograms)
    grams = kilograms * 1000
    pounds = kilograms * 2.20462
    return round(kilograms * 2.20462, 2)

# reject bad input
def solution(value):
    try:
        number = float(value)
        return round(number * 2, 2)
    except ValueError:
        return "Invalid number"