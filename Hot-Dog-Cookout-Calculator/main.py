
# Alice J Black
# 2024SEP16
# Hot Dog Cookout Calculator Programming Project
# COSC1010
#
# 

# enter amount of people
number_of_people = int(input("Enter number of people: "))

# hotdogs per person
number_of_hotdogs_per_person = int(input("Enter number of hot dogs: "))
number_of_hotdogs_per_package = 10
number_of_buns_per_package = 8

# total number of hotdogs
total_number_of_hotdogs = number_of_people * number_of_hotdogs_per_person
number_of_hotdog_packages_needed = total_number_of_hotdogs // number_of_hotdogs_per_package
number_of_hotdog_buns_needed = total_number_of_hotdogs // number_of_buns_per_package
number_of_hotdogs_left_over = total_number_of_hotdogs % number_of_hotdogs_per_package
number_of_hotdog_buns_left_over = total_number_of_hotdogs % number_of_buns_per_package

print("Minimum number of hotdogs needed =", number_of_hotdog_packages_needed)
print("Minimum number of buns needed =", number_of_hotdog_buns_needed)
print("Number of hot dogs left over =", number_of_hotdogs_left_over)
print("Number of hot dogs buns left over =", number_of_hotdog_buns_left_over)
