def add(*args):
    total = 0
    for argument in args:
        total += argument
    return total


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))