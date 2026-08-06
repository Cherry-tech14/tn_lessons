#creating a single tuple
'''
good_single = ("Vanilla",)
print(type(good_single))

#indexing in tuple
signature = ("Vanilla", "Caramel", "Hazelnut")
print(signature[1])
print(signature[-1])

#immutability in tuple
signature_blend = ("Vanilla", "Caramel", "Hazelnut")

print(f"To make the House Blend, use: {signature_blend[0]} and {signature_blend[1]}")

#tuple unpacking
dimensions = (12, 8)
width, height = dimensions
print(width)
print(height)
'''
person = ("Chuks", 30)
name, age = person
print(name)
print(age)

student = ("Mary", "course", 100)
name, course, score = student
print(name)
print(course)
print(score)




