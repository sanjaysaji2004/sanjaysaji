from itertools import permutations

# Get input from user
digits = input("Enter three digits: ")

# Create a list of all permutations of the input digits
combinations = list(permutations(digits))

# Print the combinations
for combination in combinations:
    print("".join(combination))
