# A program to find the median of a list of values
# Version 3 - using a function called myMedian

def myMedian(L):
  L.sort() 
  num_values = len(L)
  mid = num_values//2
  
  if (num_values %2 == 0):
    median = (L[mid]+L[mid-1])/2
  else:
    median = L[mid] # the median is in the middle

  return(median)
  
# Initialise a list of values
L = [18, 27, 15, 13, 22, 14]

# To find the median we need to sort the list

median = myMedian(L)

# Display the result
print("The median value is: %.1f" %median)
