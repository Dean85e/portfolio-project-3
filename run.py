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

    # Get address increase / discount
    def get_address_modifier(self):
        """Function to add to premium if customer lives in the city"""
        price_modifier = 0
        if self.address.lower() == "city":
            price_modifier = 1.15
        else:
            price_modifier = 0.90
        return price_modifier

    # Get no claims bonus increase / discount
    def get_ncb_modifier(self):
        """function to calculate no claim bonus discount."""
        price_modifier = 0
        if self.ncb == 5:
            price_modifier = 0.60
        elif self.ncb == 4:
            price_modifier = 0.70
        elif self.ncb == 3:
            price_modifier = 0.80
        elif self.ncb == 2:
            price_modifier = 0.80
        elif self.ncb == 1:
            price_modifier = 0.90
        else:
            price_modifier = 1.15
        return price_modifier

    # Get penalty points increase / discount
    def get_pen_points_modifier(self):
        """function to apply penalty points charge to premium."""
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

    # Get persons age increase / discount
    def get_age_modifier(self):
        """function to get self age which affects premium"""
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
    def __init__(self, make, model, year, engine_size):
        self.vehicle_type = int(vehicle_type)
        self.make = make
        self.model = model
        self.year = year
        self.engine_size = engine_size
    # Get a base price from the vehicle type.
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

    # Get Engine size discount / increase
    def get_cc_modifier(self):
        """function to get Engine capacity of vehicle"""
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

    # Get Vehicle Age discount / increase
    def get_age_modifier(self):
        """ function to get Vehicle year """
        price_modifier = 0
        if int(self.year) >= 2000 and int(self.year) <= 2010:
            price_modifier = 1.50
        elif int(self.year) > 2010 and int(self.year) <= 2015:
            price_modifier = 1.25
        elif int(self.year) > 2015 and int(self.year) <= 2022:
            price_modifier = 1
        return price_modifier


class InsuranceCalculator:
    """
    Class for calculating insurance
    """
    def __init__(self, person, vehicle):
        self.person = person
        self.vehicle = vehicle


def personal_details():
    """
    Get personal details from the user.
    """
    print("Welcome to python insurances.")
    print("Please proceed for an insurance quote.\n")
    f_name = details_validation_str("Please enter your first name?.\n")
    l_name = details_validation_str("Please enter your last name?.\n")
    location_choices = ['City', 'County']
    address = validate_input_choice(location_choices, "Do you live in the city or county?\n")
    age = details_validation_int("Please enter your age ?.\n")
    ncb = details_validation_int("How many years NCB do you have?.\n")
    p_point = details_validation_int("How many penalty points do you have?.\n")
    return Person(f_name, l_name, address, age, ncb, p_point)


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


def details_validation_float(message):
    """
    Input validation of float for engine size.
    """
    valid_input = False
    user_input_num = 0
    while valid_input is False:
        user_input_num = input(message)
        try:
            float(user_input_num)
            valid_input = True
        except ValueError:
            print("Invalid option please enter a decimal number.\n")
            print("Example 1.0 , 1.5 , 2.0")
    return user_input_num


def details_validation_str(message):
    """
    Input validation of string personal details.
    """
    valid_input = False
    user_input_str = 0
    while valid_input is False:
        user_input_str = input(message)
        try:
            int(user_input_str)
            print("Invalid input! please try again.")
        except ValueError:
            if len(user_input_str.strip()) == 0:
                valid_input = False
                print("Please input")
            else:
                valid_input = True
    return user_input_str


def get_vehicle_details():
    """
    Get vehicle details from the user.
    """
    print("Thank you now we need to get your vehicle details.\n")

    valid_Vehicles = ['1', '2', '3']
    vehicle_type = validate_input_choice(valid_Vehicles, "Please select a vehicle category:\nOption 1: Car\nOption 2: Van\n Option 3: Motorbike\n")

    make = details_validation_str("Please enter the make of your vehicle?.\n")
    model = details_validation_str("Please enter the model ?.\n")
    year = details_validation_int("What year is your vehicle?.\n")
    engine_size = float(details_validation_float("Enter vehicle engine size?.\n"))
    return Vehicle(vehicle_type, make, model, year, engine_size)


def main():
    """
    Main function to run the application
    """
    driver = personal_details()
    vehicle_choice = get_vehicle_type()
    motor = vehicle_details()
    base_price = calculate_base_price(vehicle_choice)
    calculate_base_price(vehicle_choice)
    v_age = calculate_vehicle_age(motor, base_price)
    calculate_vehicle_age(motor, base_price)
    v_cc = calculate_vehicle_cc(motor, base_price)
    calculate_vehicle_cc(motor, base_price)
    d_age = calculate_driver_age(driver, base_price)
    calculate_driver_age(driver, base_price)
    pp = calculate_pen_points(driver, base_price)
    calculate_pen_points(driver, base_price)
    cb = no_claim_bonus(driver, base_price)
    no_claim_bonus(driver, base_price)
    d_ad = driver_address(driver, base_price)
    driver_address(driver, base_price)
    add(base_price, v_age, v_cc, d_age, pp, cb, d_ad)
    final = add(base_price, v_age, v_cc, d_age, pp, cb, d_ad)
    quote(final, driver, vehicle_choice, motor)


main()

