# ### Problem Description

# You are given two numbers, stored in variables with the names `fuel` and `distance`. You must calculate the value of `required`, determined by the product of `fuel` and `distance`. If `required` is greater than 50, the output should indicate that you have enough fuel, otherwise, you should continue the journey.

# ### Input

# **Input Format:**

# A single line containing two values, representing the amount of fuel and the distance to be covered.

# **Constraints:**

# - Both numbers are less than 1000.

# ### Output

# **Output Format:**
# Print "Enough" if the `required` fuel is greater than 50, else print "Go On".

# --------------------------------------

# PsudoCode

# Read fuel, distance
# Calculate required = fuel * distance
# If required is greater than 50 then
#   Print "Enough"
# Else
#   Print "Go On"
# End

# ------------Code-----------------------

fuel = int(input('Enter fuel -'))
distance = int(input('Enter distance - '))

required = fuel*distance

if(required>50):
    print('Enough')
else:
    print('Go On')