# Exercise 1
# Creating a list with user input
list1 = []
while True:
    try:
        user_input = int(input("Write a valid integer number here or type '0' to end the program:"))
        if user_input == 0:
            print(list1)
            break
        else:
            list1.append(user_input)
    except ValueError:
        print("This is not a valid number. Please try again.")
        continue

# checking for numbers in list1 that are divisible by 3 or 5, and sum them
final_list = []
for i in list1:
    if i > 0 and i % 3 == 0 or i % 5 == 0:
        final_list.append(i)

# printing the final result which is a sum of the numbers from list1 that are divisible by 3 and 5
print(sum(final_list))

