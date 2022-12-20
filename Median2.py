# A program to find the median of a list of values
# Version 2 - This will work for an even number of values

# Initialise a list of values
L = [18, 27, 15, 13, 22, 14]

# To find the median we need to sort the list
L.sort() # the values are sorted 'in place'
print(L)

# The next step is to find the index of the middle value
num_values = len(L)
mid = num_values//2

if (num_values %2 == 0):
    median = (L[mid]+L[mid-1])/2
else:
    median = L[mid] # the median is in the middle

# Display the result
print("The median value is: %.1f" %median)

