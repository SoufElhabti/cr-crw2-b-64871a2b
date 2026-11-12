def add(a, b):
    return a + b


def mul(a, b):
    result = 0
    for _ in range(b):
        result = result + a
    return result
