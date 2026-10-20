NormaliseCode
Instructions
Codes arrive messy and must be cleaned before they can be matched. Implement normalise_code(raw) and return the code with the surrounding spaces trimmed, all letters in lower case, and every remaining space removed. Methods return new strings, so you can chain them in one line: trim, then lower, then remove spaces. The code AL PHA with stray spaces becomes alpha.

# Solution
def normalise_code(raw):
    return raw.strip().lower().replace(" ", "")
print(normalise_code(" AL PHA "))