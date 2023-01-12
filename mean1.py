# Program to find the mean of a list of values
# Version 1

# Calculate and return the mean of all the values in L
def arithmetic_mean(L):

    # set the initial value of total to zero
    total = 0 # running total of values in L

    # Now loop over the list
    for v in L:
        total = total + v # running total

    # Divide by the total by the number of values in L
    return total/5

# PYTHON STARTS EXECUTING FROM HERE ...
# Initialise a list of values
my_list = [18, 27, 15, 13, 22]
# Call the function
my_mean = arithmetic_mean(my_list)
# Display the answer
print("The mean is ", my_mean)


# EXPERIMENT ...
# Check that the program is working? (i.e. actual result vs. expected result)
# Change the values in the list and see what happens?
# What happens if there were more (or less) than 5 values in the list?
# Change the variable names as see what happens
# Does this program work for a list of strings (e.g. ["Mary", "Andy", "Pat"])? Why/why not?

# TASKS FOR BREAKOUT
# Save this program as mean2.py
# Change the comment at the top of the program to say Version 2
# Modify the code so that it works for any number of values (not just 5)
# Modify the code so that it works without a loop
# Test each little change as you go

# EXTENSION EXERCISES (post-workshop tasks)
# Modify the code to get the mean of numbers entered by the end user
# HINT: Ask in advance how many numbers they will enter and use a for loop
# Modify the code to get the mean of numbers entered by the end user but instead of using a for loop, use a while loop and a loop guard to determine when to stop
# Modify the code to get the mean of numbers read in from a text (or csv) file

