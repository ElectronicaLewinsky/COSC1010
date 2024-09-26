#
# Alice J Black
# 2024SEP24
# Bug Collector Programming Project
# COSC 1010
#
#
#otal bugs
total_bugs = 0
#
# Loop for a specific number of days 
for day in range(1, 6):
    # Ask the user to enter amount collected
    bugs_collected = int(input(f"Enter the amount of bugs collected on day {day}: "))

    # Add amount to total
    total_bugs += bugs_collected

# Display the total number of bugs collected
print("Total bugs collected:", total_bugs)