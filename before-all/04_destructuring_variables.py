x, y = 10, 20
print(x, y)

x, y = (10, 20)
print(x, y)

# Tuple
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# List
example_list = ["A", "B", "C", "D"]
for counter, value in enumerate(example_list):
    print(f"{counter}-{value}")

# Values
person = ("Bob", 42, "Mechanic")
name, _, proffesion = person
print(name, proffesion)

# Collect values
first, *rest = [1, 2, 3, 4, 5, 6, 7]
print(first)
print(*rest)

*head, tail = [1, 2, 3, 4, 5]
print(head)  # [1, 2, 3, 4]
print(tail)  # 5

head, *middle, tail = [1, 2, 3, 4, 5]
print(head)  # 1
print(middle)  # [2, 3, 4]
print(tail)  # 5

first, second, third, *rest = [1, 2, 3, 4, 5]
