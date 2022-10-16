def num_within(n, min, max):
    if (min <= n <= max):
        return True
    else:
        return False

print(num_within(5, 1, 9))
print(num_within(0, 1, 9))
print(num_within(10, 1, 9))