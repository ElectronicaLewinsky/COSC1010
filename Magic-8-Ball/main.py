#
# Alice J Black
# 2024NOV5
# Magic 8 Ball Programming Project
# COSC 1010
#
#
#
#
# Import Random Module
import random
# Import Time Module
import time
# Define input or abort
question = input("Ask the magic 8 ball a question (press enter to abort): ") 
while question:
    if question == "quit":
        break
# Display text and define variables
    print("Let's see what your future holds")    
    for i in range(random.randrange(3,10)):
        print(". ",end=" ")
        time.sleep(1)
    print("\nYour answer is")
# Define result
    print("Your future is " +(random.choice(open("8_ball_responses.txt","r").read().splitlines())) + " .")
    question = input("Ask the magic 8 ball a question (press enter to quit): ")

print("byeee")
