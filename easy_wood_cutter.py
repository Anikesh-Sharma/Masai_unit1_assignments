
# Write the Psuedocode for below 

# You are given a number, stored in a variable named `N`. Your task is to determine whether `N` is divisible by 3. A number that is divisible by 3 will be evenly divisible, meaning no remainder or fractional part after division.

# **Input Format:**
# A single line that contains the length of the wood, represented by the integer `N`.
# **Constraints:**
# - `1 ≤ N < 1000`
# ### Output
# **Output Format:**

# Print "Yes" if `N` is divisible by 3; otherwise, print "No".

# -------------------------------------

# input N
# If N % 3 == 0 then
#   Print "Yes"
# Else
#   Print "No"
# End

N = int(input('Enter the value -'))

if N % 3 == 0:
    print('Yes')
else:
    print('No')