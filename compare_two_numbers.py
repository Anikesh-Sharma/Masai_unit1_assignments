# ### Description

# Write the Psuedocode for below :

# You are given two numbers stored in two variables, with the name, `num1` and `num2`.

# Print the result of the following operations:
# 1. `num1 > num2` -> this operation prints true, if `num1` is greater than `num2`, otherwise it prints false

# 2. `num1 < num2` -> this operation prints true, if `num1` is smaller than `num2`, otherwise it prints false

# 3. `num1 == num2` -> this operation print true, if `num1` is equal to `num2`, otherwise it prints false

# You have to print the result of three operations in the order as shown above.
# ### Input
# The first and the only line of input contains the values stored in `num1` and `num2`.

# ----------------------------------

# Psuedocode

# Input num1
# Input num2
# If num1 > num2 then
#      Print true
# Else
#      Print false

# End

# If num1 < num2 then
#      Print true
# Else
#      Print false


# If num1 == num2 then
#     Print true
# Else
#     Print false
# End


# ----------------------------------

# Actual Code

num1 = int(input('Enter the value -'))
num2 = int(input('Enter the value -'))

if num1 > num2:
    print('true')
else:
    print('false')

if num1 < num2:
    print('true')
else:
    print('false')

if num1 == num2:
    print('true')
else:
    print('false')