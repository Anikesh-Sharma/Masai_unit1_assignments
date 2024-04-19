# ### Title: Area and Perimeter
# ### Level: Level 1 - Easy
# ### Time to Solve the Problem: 5 Mins
# ### Problem Description
# Write the Psuedocode for below :
# You are provided with the dimensions of two rectangles. For the first rectangle, you have lengths L1 and B1, and for the second rectangle, you have lengths L2 and B2. You need to determine if the area of the first rectangle is greater than the second, and if the perimeter of the first rectangle is greater than the second.
# ### Input
# **Input Format:**
# The first line of input contains four space-separated integers representing the lengths and breadths of two rectangles: L1, B1, L2, B2.
# **Constraints:**
# - 1 ≤ L1, B1, L2, B2 ≤ 100
# ### Output
# **Output Format:**
# - On the first line, print "true" if the area of rectangle 1 is greater than the area of rectangle 2; otherwise, print "false".
# - On the second line, print "true" if the perimeter of rectangle 1 is greater than the perimeter of rectangle 2; otherwise, print "false"


# --------------------------------------

# PsedoCode

# Input L1, B1, L2, B2
# Calculate area1 = L1 * B1
# Calculate area2 = L2 * B2
# Calculate perimeter1 = 2 * (L1 + B1)
# Calculate perimeter2 = 2 * (L2 + B2)
# If area1 > area2 then
#     Print "true"
# Else
#     Print "false"
# End
#
# If perimeter1 > perimeter2 then
#   Print "true"
# Else
#   Print "false"
# End 

# Actual Code

L1 = int(input('Enter the length 1 -'))
L2 = int(input('Enter the length 2 -'))
B1 = int(input('Enter the breadth 1 -'))
B2= int(input('Enter the breadth 2 -'))

area1 = L1*L2
area2 = L2*L2
perimeter1 = 2 * (L1 + B1)
perimeter2 = 2 * (L2 + B2)

if area1 > area2:
    print('true')
else:
    print('false')

if perimeter1 > perimeter2:
    print('true')
else:
    print('false')