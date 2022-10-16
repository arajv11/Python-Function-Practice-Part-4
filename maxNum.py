def max_num(x, y, z):
    if (x > y and x > z):
        return f"{x} is the max"
    elif (y > x and y > z):
        return f"{y} is the max"
    elif (z > x and z > y):
        return f"{z} is the max"
    elif (x == y > z): 
        return f"{x} and {y} are the max"
    elif (x == z > y): 
        return f"{x} and {z} are the max"
    elif (y == z > x): 
        return f"{y} and {z} are the max"
    else:
        return "No max"


print(max_num(999, 0, 0))
print(max_num(0, 999, 0))
print(max_num(0, 0, 999))

print(max_num(999, 999, 0))
print(max_num(999, 0, 999))
print(max_num(0, 999, 999))

print(max_num(0, 0, 0))