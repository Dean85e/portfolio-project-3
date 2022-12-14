"""
Insurance calculator
"""


class Person:
    """
    Class for driver.
    """
    def __init__(self, f_name, l_name, address, age, ncb, p_point):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.age = age
        self.ncb = ncb
        self.p_point = p_point

    def get_person_price(self, vehicle_price):
        """
        Function to determine the cost of insurance depending on the,
        drivers : age, address, no claims bonus and penalty points.
        """
        # Add modifier for location
        vehicle_price = vehicle_price * self.get_address_modifier()
        print(f"Driver Address | {self.get_address_modifier()} | "
              f"{vehicle_price}")
        # Add modifier for age
        vehicle_price = vehicle_price * self.get_age_modifier()
        print(f"Drivers  Age   | {self.get_age_modifier()}    |"
              f" {vehicle_price}")
        if int(self.age) >= 18 and int(self.age) <= 21:
            # Add young driver premium
            vehicle_price = vehicle_price+400
            print(f"Age | Young Driver Premium | {vehicle_price}")
        # Add modifier for No claims
        vehicle_price = vehicle_price * self.get_ncb_modifier()
        print(f"No claim bonus | {self.get_ncb_modifier()}  | {vehicle_price}")
        # Add modifier for penalty points
        vehicle_price = vehicle_price * self.get_pen_points_modifier()
        print(f"Penalty points | {self.get_pen_points_modifier()}  | "
              f"{vehicle_price}")
        print("")
        return round(vehicle_price, 2)

    def get_address_modifier(self):
        """Function to add to premium if customer lives in the city,
           return price modifier"""
        price_modifier = 0
        if self.address.lower() == "city":
            price_modifier = 1.15
        else:
            price_modifier = 0.90
        return price_modifier

    def get_ncb_modifier(self):
        """function to calculate no claim bonus discount,
           return price modifier."""
        price_modifier = 0
        if int(self.ncb) == 5:
            price_modifier = 0.60
        elif int(self.ncb) == 4:
            price_modifier = 0.70
        elif int(self.ncb) == 3:
            price_modifier = 0.80
        elif int(self.ncb) == 2:
            price_modifier = 0.80
        elif int(self.ncb) == 1:
            price_modifier = 0.90
        elif int(self.ncb) == 0:
            price_modifier = 1.15
        return price_modifier

    def get_pen_points_modifier(self):
        """function to apply penalty points charge to premium,
           return price modifier."""
        price_modifier = 0
        if int(self.p_point) >= 1 and int(self.p_point) <= 3:
            price_modifier = 1.30
        elif int(self.p_point) > 3 and int(self.p_point) <= 6:
            price_modifier = 1.60
        elif int(self.p_point) > 6 and int(self.p_point) <= 12:
            price_modifier = 1.90
        else:
            price_modifier = 0.9
        return price_modifier

    def get_age_modifier(self):
        """function to get self age & return price modifier"""
        price_modifier = 0
        if int(self.age) >= 18 and int(self.age) <= 21:
            price_modifier = 1.5
        elif int(self.age) > 21 and int(self.age) <= 30:
            price_modifier = 1.1
        elif int(self.age) > 30 and int(self.age) <= 40:
            price_modifier = 1
        elif int(self.age) > 40 and int(self.age) <= 50:
            price_modifier = 0.9
        elif int(self.age) > 50 and int(self.age) <= 60:
            price_modifier = 0.85
        elif int(self.age) > 60:
            price_modifier = 0.95
        return price_modifier


class Vehicle:
    """
    Class for vehicle
    """
    def __init__(self, vehicle_type, make, model, year, engine_size):
        self.vehicle_type = int(vehicle_type)
        self.make = make
        self.model = model
        self.year = year
        self.engine_size = engine_size

    def get_vehicle_price(self):
        """
        Function to calculate the total cost of the vehicle price,
        including year and engine size.
        """
        print("Category Tag   |  %   | Price")
        # Determine base price from Vehicle Type
        base_price = self.get_base_price()
        print(f"Vehicle Base   | 0.00 | {(base_price)}")
        # Add engine size price % modifier
        base_price = base_price * self.get_cc_modifier()
        print(f"Engine size    | {self.get_cc_modifier()} | {base_price}")
        # Add vehicle Year mondifier
        base_price = base_price * self.get_age_modifier()
        print(f"Vehicle Year   | {self.get_age_modifier()}    | {base_price}")
        return base_price

    def get_base_price(self):
        """
        Get a base price from the vehicle type
        """
        if self.vehicle_type == 1:
            return 350
        elif self.vehicle_type == 2:
            return 450
        elif self.vehicle_type == 3:
            return 250

    def get_cc_modifier(self):
        """function to get Engine capacity of vehicle return price modifier"""
        price_modifier = 0
        if self.engine_size >= 0.5 and self.engine_size <= 1.0:
            price_modifier = 0.7
        elif self.engine_size > 1.0 and self.engine_size <= 1.5:
            price_modifier = 1
        elif self.engine_size > 1.5 and self.engine_size <= 2.0:
            price_modifier = 1.25
        elif self.engine_size > 2.0 and self.engine_size <= 2.5:
            price_modifier = 1.60
        return price_modifier

    def get_age_modifier(self):
        """ function to get Vehicle year and return price modifier"""
        price_modifier = 0
        if int(self.year) >= 2000 and int(self.year) <= 2010:
            price_modifier = 1.50
        elif int(self.year) > 2010 and int(self.year) <= 2015:
            price_modifier = 1.25
        elif int(self.year) > 2015 and int(self.year) <= 2022:
            price_modifier = 1
        return price_modifier


class InsuranceCalculation:
    """
    Class for calculating insurance
    """
    def __init__(self, person, vehicle):
        self.person = person
        self.vehicle = vehicle

    def get_vehicle_price(self):
        """
        Function to get returned value from vehicle.
        """
        return self.vehicle.get_vehicle_price()

    def get_personal_price(self, vehicle_price):
        """
        Function to get returned value from person.
        """
        return self.person.get_person_price(vehicle_price)

    def get_total_insurance_cost(self):
        """
        Function to put driver price and vehichle price together
        to return a value in final price.
        """
        vehicle_price = self.get_vehicle_price()
        final_price = self.get_personal_price(vehicle_price)
        return final_price


def get_personal_details():
    """
    Function get personal details from the user.
    """
    f_name = details_validation_str("Please enter your first name?.\n")
    l_name = details_validation_str("Please enter your last name?.\n")
    # Array for valid address choices.
    location_choices = ['City', 'County']
    address = validate_input_choice(
        location_choices, "Do you live in the city or county?\n")
    age_input = range(18, 81)
    age = validate_input_details(
        age_input, "Please enter your age from 18 to 80 ?.\n")
    ncb_input = range(0, 6)
    ncb = validate_input_details(
        ncb_input, "Enter no claim bonus from 0 to 5 .\n")
    pp_input = range(0, 13)
    p_point = validate_input_details(
        pp_input, "Enter penalty points from 0 to 12.\n")
    return Person(f_name, l_name, address, age, ncb, p_point)


def get_vehicle_details():
    """
    Function to get vehicle details from the user.
    """
    print("Thank you now we need to get your vehicle details.\n")
    # Array for valid vehicles
    valid_vehicles = ['1', '2', '3']
    vehicle_type = validate_input_choice(
        valid_vehicles,
        "Choose a vehicle:\n 1 for: Car\n 2 for: Van\n 3 for: Motorbike\n")

    make = details_validation_str("Please enter the make of your vehicle?.\n")
    model = details_validation_str("Please enter the model ?.\n")
    year_input = range(2000, 2023)
    year = validate_input_details(
        year_input, "Enter vehicle year between 2000 to 2022.\n")
    min_cc = 0.5
    max_cc = 2.5
    engine_size = float(
        validate_float(min_cc, max_cc, "Enter engine size from 0.5 to 2.5\n"))
    return Vehicle(vehicle_type, make, model, year, engine_size)


def validate_input_details(valid_details, message):
    """
    'Valid_details' is going to check for input in range,
     anything inside the range set can be considerd a valid choice.
     .strip will check for an empty field.
    """
    valid_input = False
    user_input = 0
    while valid_input is False:
        user_input = input(message)
        try:
            if len(str(user_input).strip()) == 0:
                valid_input = False
                print("Please input")
            elif user_input == str(user_input):
                valid_input = False
            for details in valid_details:
                if int(details) == int(user_input):
                    valid_input = True
        except ValueError:
            print("Enter a number")
    return user_input


def details_validation_int(message):
    """
    Input validation of integer personal details.
    """
    valid_input = False
    user_input_num = 0
    while valid_input is False:
        user_input_num = input(message)
        try:
            int(user_input_num)
            valid_input = True
        except ValueError:
            print("Invalid option please enter a number.")
    return user_input_num


def validate_input_choice(valid_choices, message):
    """
    'ValidChoices' is going to be an array,
     anything inside the array can be considerd a valid choice.
    """
    valid_input = False
    user_input = ""
    while valid_input is False:
        user_input = input(message)
        for choice in valid_choices:
            if choice.lower() == user_input.lower():
                valid_input = True
                return user_input
        print("Invalid input! please try again.")


def validate_float(min_cc, max_cc, message):
    """
    Input validation of float for engine size,
    with a minimun and maximum value passed in.
    """
    valid_input = False
    user_float = 0
    while valid_input is False:
        user_float = input(message)
        try:
            if float(user_float) < min_cc or float(user_float) > max_cc:
                print("Invalid input!")
                valid_input = False
            else:
                valid_input = True
        except ValueError:
            print("Invalid option please enter a decimal number.\n")
            print("Example 1.0 , 1.5 , 2.0")
    return user_float


def details_validation_str(message):
    """
    Input validation of string personal details,
    the .strip method will check for empty strings.
    and will check for inputs less than 2 or greater than 10.
    """
    valid_input = False
    user_input_str = 0
    while valid_input is False:
        user_input_str = input(message)
        try:
            int(user_input_str)
            print("Invalid input! please try again.")
        except ValueError:  # Ensure user does not leave an input field blank.
            if len(user_input_str.strip()) == 0:
                valid_input = False
                print("Please input")
            elif len(user_input_str.strip()) < 2:
                valid_input = False
                print("Please enter between 2 to 10 letters")
            elif len(user_input_str.strip()) > 10:
                valid_input = False
                print("Please enter betweem 2 or 10 letters")
            elif user_input_str.isalpha():
                valid_input = True
            else:
                print("Please use letters only")
    return user_input_str


def main():
    """
    Main function to run the application
    """
    print("Welcome to python insurances.")
    print("Please proceed for an insurance quote.\n")

    person_details = get_personal_details()
    vehicle_details = get_vehicle_details()
    insurance_calculator = InsuranceCalculation(
        person_details, vehicle_details)
    print("")
    print("")
    print(f"Hello {person_details.f_name} "
          f"{person_details.l_name} your quote for vehicle "
          f"{vehicle_details.make} {vehicle_details.model} is as follows:\n")
    print("Details entered are:\n")
    print(f"Address: {person_details.address}")
    print(f"Age: {person_details.age}")
    print(f"No claim bonus: {person_details.ncb}")
    print(f"Penalty points: {person_details.p_point}")
    print(f"Vehicle year: {vehicle_details.year}")
    print(f"Engine capacity: {vehicle_details.engine_size}")
    print("")
    print("Premium Breakdown:")
    print("")
    print("Your total premium is: " + str(
        insurance_calculator.get_total_insurance_cost()))


# Main function call.
main()
