#
# Alice J Black
# 2024OCT21
# Average of Numbers Programming Project
# COSC 1010
#
#
# 
# Open file
loop_count = 0
total = 0
data = open("/Users/main/Documents/COSC1010/COSC1010-main/Average-of-Numbers/numbers.txt","r")
# Read data
for line in data.readlines():
    # Calculate average
    total = total + int(line)
    loop_count += 1
avg = total/loop_count
# Display average
print (avg)
