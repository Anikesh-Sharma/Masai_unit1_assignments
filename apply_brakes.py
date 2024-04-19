# ### Problem Description

# You are given two numbers representing `distance` and `time`. You need to calculate the `speed` using the formula `speed = distance/time` and determine whether to apply brakes or keep going based on the speed.
# ### Input
# **Input Format:**
# The first line contains two space-separated integers representing the distance travelled by car and the time taken to cover that distance.
# **Constraints:**
# - Distance < 1000
# - Time taken < 5

# ### Output

# **Output Format:**

# Print "Apply Brake" if the speed is greater than 40, otherwise print "Keep Going".

# ---------------------------------

# PsudoCode

# Input distance, time
# Calculate speed = distance / time
# If speed is greater than 40 then
#     Print "Apply Brake"
# Else
#     Print "Keep Going"
# End

# ---------------------------

distance = int(input('Enter the distance -'))
time = int(input('Enter the time -'))

speed = distance/time

if(speed>40):
    print('Apply break')
else:
    print('Keep Going')