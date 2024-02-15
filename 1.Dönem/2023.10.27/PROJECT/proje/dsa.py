def list(items):
    numbers = 1

    for s in items:

       numbers *= s
    return numbers

print(list([1,45,19,-0.3]))