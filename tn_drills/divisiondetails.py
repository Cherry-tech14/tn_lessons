def division_details(a, b):
    return {
        "true_division": round(a / b, 2),
        "floor_division": a // b,
        "remainder": a % b
    }