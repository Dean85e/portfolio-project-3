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


class Vehicle:
    """
    Class for vehicle
    """
    def __init__(self, make, model, year, engine_size):
        self.make = make
        self.model = model
        self.year = year
        self.engine_size = engine_size

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


def calculate_base_price(vehicle_choice):
    """
    Function to calculate the base price of the insurance premium.
    """
    base_price = 0
    # Vehicle information
    if vehicle_choice == 1:
        base_price = 350
    elif vehicle_choice == 2:
        base_price = 450
    elif vehicle_choice == 3:
        base_price = 250
    return base_price


def calculate_vehicle_age(motor, base_price):
    """ function to get Vehicle year """
    vehicle_yr = 0
    if int(motor.year) >= 2000 and int(motor.year) <= 2010:
        vehicle_yr = base_price * (90 / 100) + 200
    elif int(motor.year) > 2010 and int(motor.year) <= 2015:
        vehicle_yr = base_price * (60/100)
    elif int(motor.year) > 2015 and int(motor.year) <= 2022:
        vehicle_yr = base_price * (20/100)
    return vehicle_yr


def calculate_vehicle_cc(motor, base_price):
    """function to get Engine capacity of vehicle"""
    vehicle_cc = 0
    if motor.engine_size >= 0.5 and motor.engine_size <= 1.0:
        vehicle_cc = base_price * (30/100)
    elif motor.engine_size > 1.0 and motor.engine_size <= 1.5:
        vehicle_cc = base_price * (40/100)
    elif motor.engine_size > 1.5 and motor.engine_size <= 2.0:
        vehicle_cc = base_price * (70/100)
    elif motor.engine_size > 2.0 and motor.engine_size <= 2.5:
        vehicle_cc = base_price * (90/100) + 200
    return vehicle_cc


def calculate_driver_age(driver, base_price):
    """function to get Driver age which affects premium"""
    driver_age = 0
    young_driver_premium = 750
    if int(driver.age) >= 18 and int(driver.age) <= 21:
        driver_age = base_price * (90/100) + young_driver_premium
    elif int(driver.age) > 21 and int(driver.age) <= 30:
        driver_age = base_price * (70/100)
    elif int(driver.age) > 30 and int(driver.age) <= 40:
        driver_age = base_price * (45/100)
    elif int(driver.age) > 40 and int(driver.age) <= 50:
        driver_age = base_price * (20/100)
    elif int(driver.age) > 50 and int(driver.age) <= 60:
        driver_age = base_price * (10/100)
    elif int(driver.age) > 60:
        driver_age = base_price * (20/100)
    return driver_age


def calculate_pen_points(driver, base_price):
    """function to apply penalty points charge to premium."""
    points = 0
    if int(driver.p_point) >= 1 and int(driver.p_point) <= 3:
        points = base_price * (20/100)
    elif int(driver.p_point) > 3 and int(driver.p_point) <= 6:
        points = base_price * (40/100)
    elif int(driver.p_point) > 6 and int(driver.p_point) <= 12:
        points = base_price * (80/100)
    return points


def no_claim_bonus(driver, base_price):
    """function to calculate no claim bonus discount."""
    ncb = 0
    if driver.ncb == 5:
        ncb = base_price * (50/100)
    elif driver.ncb == 4:
        ncb = base_price * (40/100)
    elif driver.ncb == 3:
        ncb = base_price * (30/100)
    elif driver.ncb == 2:
        ncb = base_price * (20/100)
    elif driver.ncb == 1:
        ncb = base_price * (10/100)
    return ncb


def driver_address(driver, base_price):
    """Function to add to premium if customer lives in the city"""
    address = 0
    if driver.address.lower() == "city":
        address = base_price + 300
    else:
        address = base_price
    return address


def add(base_price, v_age, v_cc, d_age, pp, cb, d_ad):
    """
    Function to determine the total premium offered to the customer.
    """
    print("Your insurance quote is as follows...\n")
    total1 = base_price + v_age + v_cc
    total2 = d_age + pp + d_ad - cb
    total = total1 + total2
    return total


def quote(final, driver, vehicle_choice, motor):
    """
    Function to display quote information to user.
    """
    print(driver.f_name)


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

