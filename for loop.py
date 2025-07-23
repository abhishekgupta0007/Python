x = 24
unit = "hours"

def days_to_units(num_of_days):
    return(f"{num_of_days} days are {num_of_days * x} {unit}")



def validate_input(user_input):
    if user_input.isdigit():
      input_value = int(user_input)
      if input_value > 0:  
       result = days_to_units(input_value)
       print(result)
       return True
      else:
       print ("you entered value 0 please enter valid number")
       return False

    else:
     print("invalid value please enter a valid number")
     return False

user_input = input("enter the number of days!\n")
for num_of_days in user_input.split():
      validate_input(num_of_days)



# This code uses a for loop to process multiple inputs at once, allowing the user to enter several numbers separated by spaces. Each number is validated and converted to hours if valid. If an invalid input is detected, an error message is displayed without terminating the program.