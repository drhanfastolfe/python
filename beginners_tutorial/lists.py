l = [1, 2, 3]

l2 = [1, "string", "slkd", 4.3, True, [1, 2, 3]]
print(l2)

print(l2[0])
print(l2[1])
print(l2[2])
print(l2[3])
print(l2[4])
print(l2[5])

names = ["Joe", "John", "James"]
print(names)

names.append("Gary")
print(names)

names.insert(0, "Jesus")
print(names)

names.remove("Joe")
print(names)

numbers = [5, 1, 2, 9, 6, 1]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

for n in numbers:
    print(n)