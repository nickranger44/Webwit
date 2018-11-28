# Import requests
import requests


def view_cookies(target_host):
    print("\n----------------------------------")
    r = requests.get(target_host)
    data = r.cookies
    r.close()
    print("Cookies:")
    for i, cookie in enumerate(data):
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
    while True:
        address = input("Enter target URL: ").strip()
        try:
            r = requests.get(address)
        except requests.exceptions.MissingSchema:
            print("Invalid URL!")
        else:
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

# For 2: View all of the cookies of the website using cookiejar or something of the sort

# For 3: Using curl module or something make post request using a handcrafted value for a cookie

# For 4: Take in a password file, or username file, login page path, host IP/domain name, port, fail text, allow
# for multi-threading