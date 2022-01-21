## Output

name = "Francisco"
sentence = f"Hello {name}"

print(sentence)

name_1 = "Bob"
name_2 = "Juan"
sentence_2 = "Hello {} and {}. {}"
sentence_3 = sentence_2.format(name_1, name_2, "ready?")
print(sentence_2)
print(sentence_3)

## Input

ask = int(input("Whats your age?: "))
print(f"Your age is {ask}")
