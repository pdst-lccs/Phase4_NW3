# A program to find the mode of a list of values
# Version 3 - no mode or multiple modes

# Initialise a list of values
L = [38, 16, 17, 20, 19, 28, 27]

# Build up a list of unique values
unique_values = []
for value in L:
    if value not in unique_values:
        unique_values.append(value)

# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = L.count(value)
    frequencies.append(frequency)

# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]

print("Mode is", mode)
print("Frequency of the mode =", max_frequency)

# The statement list(set(L)) returns a list of unique elements in L. Use this information to shorten the code
print(list(set(L)))

# The program works if the list has a single mode. Modify the code so that it ....
# - works if there is no mode e.g. L = [18, 16, 17, 21, 19, 16, 22]



# - works if there are multiple modes e.g. L = [18, 16, 17, 18, 17, 18, 17]
