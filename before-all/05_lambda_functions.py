# Implementation
function = lambda x, y: x * y
print(function(3, 4))

# Scalar values
(lambda x, y: x * y)(5, 9)
# print((lambda x,y : x*y)(5,9))

list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# List
filter(lambda x: x % 2 == 0, list_values)
print(list(filter(lambda x: x % 2 == 0, list_values)))

# Map
map_values = map(lambda x: x ** 3, list_values)
print(list(map_values))
