groceries = {"bananas": 5, "oranges": 3}

print(groceries["bananas"])

print(groceries.get("bananas")) # whitout an error if doesnt exits

contacts = {
    "Joe": ["123 456 789", "joe@example.com"],
    "Jane": ["987 654 321", "jane@example.com"]
}

print(contacts.get("Jane"))

contacts = {
    "Joe": {"phone": "123 456 789", "email": "joe@example.com"},
    "Jane": {"phone": "987 654 321", "email": "jane@example.com"}
}

print(contacts.get("Jane").get("email"))

sentence = "I like the name Aaron beacause the name Aaron is best"

word_counts = {
    "I": 1,
    "like": 1,
    "the": 3
}

# dict.items() returs key-values in a tuple
print(word_counts.items())
print(list(word_counts.items()))

# dict.keys() returs a list of keys
print(word_counts.keys())

# dict.values() returs a list of values
print(word_counts.values())

word_counts.pop("I")
print(word_counts)

# dict.popitem() pop the last item

word_counts["Aaron"] = 2

# dict.clear() empties the dictionary

print(sorted(list(word_counts.values())))
