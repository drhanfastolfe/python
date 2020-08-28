t = (0, 1, 3)
print(t[2])

credit_card = (4444333322221111, 'Joe Rogan', '11/20', 123)
credit_card2 = (1111222233334444, 'Joe Rogan', '12/22', 456)

credit_cards = [credit_card, credit_card2]

print(credit_cards)

person1 = ('Nancy', 25, 'Pizza')
person2 = ('Joe', 22, 'Pasta')

people = [person1, person2]

# (name, age, favfood) = person

# print(name)
# print(age)
# print(favfood)

for name, age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()
    
for i in range(len(people)):
    print(people[i])
    print()
    
for i in range(len(person1)):
    print(person1[i])