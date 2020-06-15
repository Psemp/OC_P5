
def InputChecker(usage, minimum, maximum, input_text):
    user_input = ""
    valid_input = False
    if usage == "ls_ind":
        while valid_input is False:
            user_input = IntChecker(user_input, minimum, maximum)
            if user_input >= minimum and user_input <= maximum:
                return user_input
                # valid_input = True  # Return user_input is better
            else:
                user_input = input(f"""Please enter a value between {minimum} and {maximum} : """)

    if usage == "y_n":
        while valid_input is False:
            user_input = input(input_text)
            if user_input == "y" or user_input == "n":
                valid_input = True  # Useless
                return user_input
            else:
                user_input = input("Please answer y or n : ")


def IntChecker(user_input, minimum, maximum):
    type_check = False
    error_message = "Please Enter a number"
    while type_check is False:
        user_input = input(f"""Please enter a value between {minimum} and {maximum} : """)
        try:
            int(user_input)
            type_check = True
            return int(user_input)
        except ValueError:
            print(error_message)
