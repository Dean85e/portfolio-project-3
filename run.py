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
    driver_base_price = 0
    vehicle_base_price = 0
    # Vehicle information
    if vehicle_choice == 1:
        vehicle_base_price = 100
    elif vehicle_choice == 2:
        vehicle_base_price = 125
    elif vehicle_choice == 3:
        vehicle_base_price = 50
    # Vehicle year calculations
    if int(motor.year) >= 2000 or int(motor.year) <= 2010:
        vehicle_base_price = vehicle_base_price / 15 * 100
    elif int(motor.year) > 2010 or int(motor.year) <= 2015:
        vehicle_base_price = vehicle_base_price / 10 * 100
    elif int(motor.year) > 2015 or int(motor.year) <= 2022:
        vehicle_base_price = vehicle_base_price / 5 * 100
    # Engine capacity calculations
    if motor.engine_size >= 0.5 or vehicle_base_price <= 1.0:
        vehicle_base_price = vehicle_base_price / 3 * 100
    elif motor.engine_size > 1.0 or vehicle_base_price <= 1.5:
        vehicle_base_price = vehicle_base_price / 5 * 100
    elif motor.engine_size > 1.5 or vehicle_base_price <= 2.0:
        vehicle_base_price = vehicle_base_price / 7 * 100
    elif vehicle_base_price > 2.0 or vehicle_base_price <= 2.5:
        vehicle_base_price = vehicle_base_price / 10 * 100
    # Driver age calculations
    if int(driver.age) >= 18 or int(driver.age) <= 21:
        driver_base_price = vehicle_base_price / 25 * 100
    elif int(driver.age) > 21 or int(driver.age) <= 30:
        driver_base_price = vehicle_base_price / 15 * 100
    elif int(driver.age) > 30 or int(driver.age) <= 40:
        driver_base_price = vehicle_base_price / 10 * 100
    elif int(driver.age) > 40 or int(driver.age) <= 50:
        driver_base_price = vehicle_base_price / 5 * 100
    elif int(driver.age) > 50 or int(driver.age) <= 60:
        driver_base_price = vehicle_base_price / 2 * 100
    elif int(driver.age) > 60:
        driver_base_price = vehicle_base_price / 7 * 100

    print(driver_base_price)


def main():
    """
    Main function to run the application
    """
    driver = personal_details()
    vehicle_choice = get_vehicle_type()
    motor = vehicle_details()
    calculate_insurance(driver, motor, vehicle_choice)


main()