class person:
    def __init__(self, f_name, l_name, address, age, no_claim_bonus, penalty_points):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.age = age
        self.no_claim_bonus = no_claim_bonus
        self.penalty_points = penalty_points

class vehicle:
    def __init__(self, make, model, year, engine_size):
        self.make = make
        self.model = model
        self.year = year
        self.engine_size = engine_size
       

def personal_details():
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
    return person(f_name, l_name, address, age, no_claim_bonus, penalty_points)

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


def vehicle_details():
    """
    Get vehicle details from the user.
    """
    print("Thank you now we need to get your vehicle details.\n")
    make = details_validation_str("Please enter the make of your vehicle?.\n")
    model = details_validation_str("Please enter the model ?.\n")
    year = details_validation_int("What year is your vehicle?.\n")
    engine_size = details_validation_int("What size engine has your vehicle got?.\n")
     
    return vehicle(make, model, year, engine_size)


def calculate_insurance(p, v):   




p = personal_details()
v = vehicle_details()
calculate_insurance(p, v)


personal_details()