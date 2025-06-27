def perform(function,x):
    return function(x)


def addFive(n):
    return n + 5

# Example 1:
print(perform(lambda x: x**2,2))

# Example 2:
print(perform(lambda x: addFive(x),10))
