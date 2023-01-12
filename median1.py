# A program to find the median of a list of values
# Version 1

# Initialise a list of values
L = [18, 27, 15, 13, 22]

# To find the median we need to sort the list
L.sort() # the values are sorted 'in place'

# The next step is to find the index of the middle value
num_values = len(L)
mid = num_values//2

median = L[mid] # the median is in the middle

# Display the result
print("The median value is: %.2f" %median)


# EXPERIMENT ...
# Change the values in the list and see what happens?
# What happens if there was an even number of values?
# Ask students how they know the program is working? (i.e. actual result vs. expected result)
# Investigate the difference between 'sort()' and 'sorted()'?
# Does this program work for a list of strings (e.g. ["Mary", "Andy", "Pat"])? Why/why not?

# TASKS FOR BREAKOUT
# Save this program as median2.py
# Change the comment at the top of the program to say Version 2
# Modify the code so that it works for an even number of values
# Incorporate the code into a function (name it median2)
# Test each little change as you go