class person:
    def __init__(self, f_name, l_name, address, age, ncb, p_point):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.age = age
        self.ncb = ncb
        self.p_point = p_point


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
    f_name = details_validation_str("Please enter your first name?.\n")
    l_name = details_validation_str("Please enter your last name?.\n")
    while True:
        address = input("Do you live in the city or county?.\n")
        if address.lower() == "city" or address.lower() == "county":
            address = str(address)
            break
        else:
            print("Please choose city or county")
    age = details_validation_int("Please enter your age ?.\n")
    ncb = details_validation_int("How many years NCB do you have?.\n")
    p_point = details_validation_int("How many penalty points do you have?.\n")
    return person(f_name, l_name, address, age, ncb, p_point)


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


def get_vehicle_type():
    """
    Get vehicle type from the user.
    """
    print("Please select a vehicle category:\n")
    print("Option 1 for cars.")
    print("Option 2 for vans.")
    print("Option 3 for motorbike.\n")
    while True:
        vehicle_type = input("Please select your vehicle type.\n")
        try:
            vehicle_type = int(vehicle_type)
        except ValueError:
            print("")
        if vehicle_type == 1:
            print("Your vehicle is a car\n")
            break
        elif vehicle_type == 2:
            print("Your vehicle is a van\n")
            break
        elif vehicle_type == 3:
            print("Your vehicle is a motorbike\n")
            break
        else:
            print("Invalid input please choose a number from the menu\n")
    return vehicle_type


def vehicle_details():
    """
    Get vehicle details from the user.
    """
    print("Thank you now we need to get your vehicle details.\n")
    make = details_validation_str("Please enter the make of your vehicle?.\n")
    model = details_validation_str("Please enter the model ?.\n")
    year = details_validation_int("What year is your vehicle?.\n")
    engine_size = float(input("Enter vehicle engine size?.\n"))
    return vehicle(make, model, year, engine_size)


def calculate_insurance(driver, motor, vehicle_choice):
    """
    Function to calculate insurance premium.
    """
    print("Your insurance quote is as follows...\n")
    young_driver_premium = 750
    base_price = 0
    vehicle_year = 0
    vehicle_cc = 0
    driver_age = 0
    ncb_discount = 0
    pen_point = 0
    # Vehicle information
    if vehicle_choice == 1:
        base_price = 350
    elif vehicle_choice == 2:
        base_price = 450
    elif vehicle_choice == 3:
        base_price = 250
    # Vehicle year calculations
    if int(motor.year) >= 2000 and int(motor.year) <= 2010:
        vehicle_year = base_price * (90 / 100) + 200
    elif int(motor.year) > 2010 and int(motor.year) <= 2015:
        vehicle_year = base_price * (60/100)
    elif int(motor.year) > 2015 and int(motor.year) <= 2022:
        vehicle_year = base_price * (20/100)
    # Engine capacity calculations
    if motor.engine_size >= 0.5 and motor.engine_size <= 1.0:
        vehicle_cc = base_price * (30/100)
    elif motor.engine_size > 1.0 and motor.engine_size <= 1.5:
        vehicle_cc = base_price * (40/100)
    elif motor.engine_size > 1.5 and motor.engine_size <= 2.0:
        vehicle_cc = base_price * (70/100)
    elif motor.engine_size > 2.0 and motor.engine_size <= 2.5:
        vehicle_cc = base_price * (90/100) + 200
    # Driver age calculations
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
    # Penalty points charge.
    if int(driver.p_point) >= 1 and int(driver.p_point) <= 3:
        pen_point = base_price * (20/100)
    elif int(driver.p_point) > 3 and int(driver.p_point) <= 6:
        pen_point = base_price * (40/100)
    elif int(driver.p_point) > 6 and int(driver.p_point) <= 12:
        pen_point = base_price * (80/100)
    # No claim bonus discounts.
    if driver.ncb == 5:
        ncb_discount = base_price * (50/100)
    elif driver.ncb == 4:
        ncb_discount = base_price * (40/100)
    elif driver.ncb == 3:
        ncb_discount = base_price * (30/100)
    elif driver.ncb == 2:
        ncb_discount = base_price * (20/100)
    elif driver.ncb == 1:
        ncb_discount = base_price * (10/100)
    total = (vehicle_year + vehicle_cc + driver_age + base_price + pen_point)
    print(total - ncb_discount)


def main():
    """
    Main function to run the application
    """
    driver = personal_details()
    vehicle_choice = get_vehicle_type()
    motor = vehicle_details()
    calculate_insurance(driver, motor, vehicle_choice)


main()