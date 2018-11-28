# Import requests
import requests


def int_input_getter(prompt, num_range):
    """
    This function takes a prompt and displays it until the user chooses a valid option.
    :param prompt: (string) Prompt for user selection
    :param num_range: (range) Range of integer values that are available
    :return: choice (int) The user's selection
    """
    while True:
        # Test for errors.
        try:
            choice = int(input(prompt))
        # If there is a value error pass so the loop can restart.
        except ValueError:
            pass
        # Otherwise, test to see if the number chosen is available.
        else:
            # If the number is available then return that number.
            if choice in num_range:
                return choice
            # Otherwise, pass so the loop can restart.
            else:
                pass


def get_target():
    while True:
        address = input("Enter target URL: ")
        try:
            r = requests.get(address)
        except requests.exceptions.MissingSchema:
            print("Invalid URL!")
        else:
            print("Target set to: " + address)
            break
    return address


menu = """
'|| '||'  '|'         '||                   ||    .   
 '|. '|.  .'    ....   || ...  ... ... ... ...  .||.  
  ||  ||  |   .|...||  ||'  ||  ||  ||  |   ||   ||   
   ||| |||    ||       ||    |   ||| |||    ||   ||   
    |   |      '|...'  '|...'     |   |    .||.  '|.' 
                                                  
Created by: Nick Lueth                                                      

1. Set target host
2. View cookies
3. Edit cookies
4. Craft login crack
5. Exit
"""
target = ""
user_choice = int_input_getter(menu, range(1, 6))
if user_choice == 1:
    target = get_target()
else:
    exit(0)
# Program plan:
# Start with cool ASCII Art of title. (THIS IS A MUST)
# Display menu
# 1. Set target host
# 2. View cookies
# 3. Edit cookies
# 4. Craft login crack
# 5. Exit


# For 1: Set target_host equal to a valid IP address or link

# For 2: View all of the cookies of the website using cookiejar or something of the sort

# For 3: Using curl module or something make post request using a handcrafted value for a cookie

# For 4: Take in a password file, or username file, login page path, host IP/domain name, port, fail text, allow
# for multi-threading
