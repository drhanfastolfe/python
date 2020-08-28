digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(digits[3])

print(digits[-2])

print(digits[0:1])

print(digits[-1:-5:-1])

print(digits[0:10:2])

print(digits[::-1])

for i in range(len(digits)):
    print(digits[-i::-1])
    
window_size = 5
for i in range(len(digits)):
    print(digits[i:i+window_size])
    if i + window_size == len(digits):
        break
