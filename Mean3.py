# Program to find the mean of a list of values
# Version 3 - using sum instead of a loop
import statistics

# Calculate and return the mean of all the values in L
def arithmetic_mean(L):

    # set the initial value of total to zero
    total = 0 # running total of values in L

    # Now loop over the list
#    for v in L:
#        total = total + v # running total

    total = sum(L)
    
    # Divide by the total by the number of values in L
    return total/len(L)

# PYTHON STARTS EXECUTING FROM HERE ...

# Initialise a list of values
my_list = []
noOfValues = int(input("How many numbers do you want to find the mean of?\n"))
x = 0

while x < noOfValues:
  entry = int(input("Enter a number: \n"))
  my_list.append(entry)
  x = x + 1
  print(my_list)

print(my_list)
# Call the function
my_mean = arithmetic_mean(my_list)

# Display the answer
print("The mean is ", my_mean)
