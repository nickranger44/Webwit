# Created By: Nick Lueth
# Webwit is a final project for CSI-160-01

import requests
# import curl
# import thread
# import time


def view_cookies(target_host):
    """
    This function connects to the target host and views the cookie data of that site.
    :param target_host: (string) url of the website
    :return: (class) all of the cookie data
    """
    # TODO: Find a way to include session cookies.
    print("\n----------------------------------")
    r = requests.get(target_host)
    data = r.cookies
    print(type(data))
    r.close()
    print("Cookies:")
    for i, cookie in enumerate(data):
        # parse the cookie data to clean up the out put a little.
        print(str(i+1) + ".", str(cookie)[8:-1])
    print("----------------------------------")
    return data


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
    """
    This function helps to set the target host.
    :return: (string) The address of the target
    """
    while True:
        # The strip is added just in case extra white space is added
        address = input("Enter target URL: ").strip()
        try:
            # See if the address can be accessed
            r = requests.get(address)
        except requests.exceptions.MissingSchema:
            print("Invalid URL!")
        else:
            # Since we only opened the url to see if it works we just close it afterwards.
            r.close()
            print("Target set to: " + address)
            break
    return address


print("""
'|| '||'  '|'         '||                   ||    .   
 '|. '|.  .'    ....   || ...  ... ... ... ...  .||.  
  ||  ||  |   .|...||  ||'  ||  ||  ||  |   ||   ||   
   ||| |||    ||       ||    |   ||| |||    ||   ||   
    |   |      '|...'  '|...'     |   |    .||.  '|.' 

Created by: Nick Lueth""")
menu = """
1. Set target host
2. View cookies
3. Edit cookies
4. Craft login crack
5. Exit
"""
target = ""
cookie_data = None
target_selected = False
while True:
    user_choice = int_input_getter(menu, range(1, 6))
    if user_choice == 1:
        target = get_target()
        target_selected = True
    elif user_choice == 2:
        if target_selected is True:
            cookie_data = view_cookies(target)
        else:
            print("No target selected!")

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

# For 2: View all of the cookies of the website using the request cookiejar or something of the sort

# For 3: Using curl module or something make post request using a handcrafted value for a cookie

# For 4: Take in a password file, or username file, login page path, host IP/domain name, port, fail text, allow
# for multi-threading
# I will offer these options for the login cracker. (Not exactly this order)
# 1. Select word list
# 2. Select port
# 3. Select fail string
# 4. Set username
# 5. Set request format
# 6. Set path
# 7. Set threads
# 8. Set form data

# At this point I don't know what all of my functions will be so I'm keeping what I have right now for this update.
