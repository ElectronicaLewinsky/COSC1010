#
# Alice J Black
# 2024OCT21
# Average of Numbers Programming Project
# COSC 1010
#
#
#
# Define the amount of variables
print("Enter the Value of n: ")
n = int(input())
# Define variables
print("Enter " +str(n)+ " Numbers: ")
nums = []
for i in range(n):
    nums.insert(i, int(input()))
# Calculate average 
sum = 0
for i in range(n):
    sum = sum+nums[i]

avg = sum/n
print("\nAverage = ", avg)
