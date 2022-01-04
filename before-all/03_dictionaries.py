friends = [
    {
    "name": "Rolf Smith", 
    "age": 31
    },
    {
    "name": "Sam With", 
    "age": 29
    },
    {
    "name": "George Brown", 
    "age": 30
    },
]

for f in friends:
    print(f)
    
for f in friends: 
    for key in f.keys():
        print(key)

for f in friends: 
    for value in f.values():
        print(value)

for f in friends: 
    for key, value in f.items():
        print(f"{key}-{value}")

for f in friends: 
    print(f.get("name", "No es"))
    
print(dir([]))
print(dir({}))
print(dir(()))
print(dir(''))