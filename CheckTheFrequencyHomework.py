test_dict = {"Guddu": 9, "Gamerz": 4, "is": 3, "the": 3, "best": 4, "gaming": 0, "channel": 1, "ever": 1}

print("The original dictionary : " + str(test_dict))

G = 9
M = 0
L = 4
K = 3

# Initialize separate result variables for each frequency count
res = 0
res1 = 0
res2 = 0
res3 = 0

# Loop through the dictionary and check each condition separately
for key in test_dict:
    if test_dict[key] == K:
        res += 1
    if test_dict[key] == L:
        res1 += 1
    if test_dict[key] == M:
        res2 += 1
    if test_dict[key] == G:
        res3 += 1

# Output the frequencies
print("Frequency of K is =", res)
print("Frequency of L is =", res1)
print("Frequency of M is =", res2)
print("Frequency of G is =", res3)