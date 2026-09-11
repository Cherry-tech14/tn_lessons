# python is dynamically typed
'''
name = "Alex"
age = 20
score = 85.5

print(type(name))
print(type(age))
print(type(score))


value = 10
print(type(value))

value = "Hello"
print(type(value))

# type hint
name: str = "Alex"
age: int = 20

print(name)
print(age)


# The optional type
from typing import Optional
email: Optional[str] = None
print(email)

from typing import Optional
email: Optional[str] = None
print(email)

email = "alex@example.com"
print(email)


# optional with a function
from typing import Optional

def find_email(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "alex@example.com"

    return None

print(find_email(1))
print(find_email(2))
'''

# type hints for variables
student_name: str = "Alex"
student_age: int = 20
student_score: float = 87.5
is_passed: bool = True

print(student_name)
print(student_age)
print(student_score)
print(is_passed)
