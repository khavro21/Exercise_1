# First exercise

# sum all integers from 1 to n( included) that can be divided by 3 or 5


# input_list = []

# while True:
#    try:
#        user_input = int(input("Write a number here:"))
#    except ValueError:
#        print('This is not an integer')

"""
def inputNumber(number):
    while True:
        try:
            user_input = int(input("Write a number here:"))
        except ValueError:
            print("This is not a valid number, please try again.")
            user_input = int(input("Write a number here:"))
            continue
        if user_input == 0:
            print("The program was ended.")
            break

"""

# if isinstance(user_input, int):
#   print('Its an int')
# else:
#   print('Its not an int')

input_list = []
user_input = input("Enter any integer number or type 'exit' to close the program.")
while user_input != 'exit' or 'Exit':
        try:
            user_input = int(input("Write an integer number here or write 'exit' to exit:"))
            input_list.append(user_input)
            if user_input == 'exit' or 'Exit':
                break
            else:
                continue
        except ValueError:
            print("Please enter a valid integer number.")
    


  """
if user_input == 'exit' or 'Exit':
    print("The program was ended by your request.")
    while user_input != 'exit':
        try:
            user_input = int(input("Write an integer number here or write 'exit' to exit:"))
            input_list.append(user_input)
        except ValueError:
            print("Please enter a valid integer number.")
"""
print(input_list)
