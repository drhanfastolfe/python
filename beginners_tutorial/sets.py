s = {"blueberry", "raspberry"}

s.add("strawberry")
s.add("4")
s.add("blueberry")

print(s)

list_of_numbers = [1, 2, 3, 4, 4, 5, 4, 1, 1]

no_duplicate_set = set(list_of_numbers)

print(no_duplicate_set)

list_of_numbers = list(no_duplicate_set)

print(list_of_numbers)

library_1 = {"Harry Potter", "Hunger Games", "Lord of the Rings"}
library_2 = {"Harry Potter", "Romeo and Juliet"}

library_3 = library_1.union(library_2)

print(library_3)

library_3 = library_1.intersection(library_2)

print(library_3)

library_3 = library_1.difference(library_3)

print(library_3)