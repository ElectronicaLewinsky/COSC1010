# Alice J Black
# 2024SEP16
# Areas of Rectangles Programming Project
# COSC1010
#
# Local variables

# Calculate area A

# Calculate area B

# Print area comparison using if-elif-else statements

# Get length A
length_1 = float(input('Enter length #1: '))

# Get width A
width_1 = float(input('Enter width #1: '))

# Get area A
area_1 = length_1 * width_1

# Get length B
length_2 = float(input('Enter length #2: '))

# Get width A
width_2 = float(input('Enter width #2: '))

# Get Area 2
area_2 = length_2 * width_2

#Calculate areas A and B
if area_1 > area_2:
print('Rectangle #1 has the greatest area at', area_1, 'inches.')
elif area_2 > area_1:
print('Rectangle #2 has the greatest area at', area_2, 'inches.')
elif area_1 == area_2:
print('Rectangles #1 and #2 have the SAME area at', area_1+area_2, 'inches.')
