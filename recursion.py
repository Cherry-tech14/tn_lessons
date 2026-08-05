'''
def wash_stack(mugs):
    print("Washing one mug")
    wash_stack(mugs) 
    
# The base and recursive case
def wash_mugs(stack_size):
    if stack_size == 0:
        print("All mugs are washed")
        return
    print(f"Washing mug {stack_size}")
    wash_mugs(stack_size - 1)
wash_mugs(3) 
 
def calculate_water(mugs):
     if mugs <= 0:
        return 0
     return 10 + calculate_water(mugs - 1)
stack_size = 3
total_water_ml = calculate_water(stack_size)
print(total_water_ml)  
'''
def sum_stack(mugs):
    if mugs <= 0:
        return 0
    return mugs + sum_stack(mugs - 1)
print(sum_stack(4))
