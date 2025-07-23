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

while True:
   user_input = input("enter the number of days!\n")
   if validate_input(user_input):
         break

 

# This code uses a while loop to continuously prompt the user for input until a valid number of days is entered. If the input is valid, it converts the days to hours and prints the result. If the input is invalid, it displays an error message and prompts again without terminating the program.