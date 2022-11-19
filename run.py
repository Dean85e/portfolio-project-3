def get_personal_details():
    """
    Get personal details from the user.
    """
    print("Welcome to python insurances.")
    print("Please proceed for an insurance quote.\n")
    f_name = details_validation_str("Please enter your first name ?.\n")
    l_name = details_validation_str("Please enter your last name ?.\n")
    address = details_validation_str("Do you live in the city or county ?.\n")
      
    age = details_validation_int("Please enter your age ?.\n")
    no_claim_bonus = details_validation_int("How many years no claim bonus do you have ?.\n")
    penalty_points = details_validation_int("How many penalty points do you have ?.\n")
        
        
    get_vehicle_type()


def details_validation_int(message):
    """
    Input validation of integer personal details.
    """
    valid_input = False
    user_input_num = 0
    
    while valid_input == False:
        user_input_num = input(message)
        try:
            int(user_input_num)
            valid_input = True

        except ValueError:
            print("Invalid option please enter a number.")     

    return user_input_num



def details_validation_str(message):
    """
    Input validation of string personal details.
    """
    valid_input = False
    user_input_str = 0
    
    while valid_input == False:
        user_input_str = input(message)
        try:
            int(user_input_str)
            print("Invalid option please enter a number.")

        except ValueError:    
            valid_input = True
    
    return user_input_str


def get_vehicle_type():
    """
    Get vehicle type from the user.
    """
    print("Please select a vehicle category:")
    print("Option 1 for cars.")
    print("Option 2 for trucks.")
    print("Option 3 for motorbike.")


get_personal_details()