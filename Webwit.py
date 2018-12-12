# Created By: Nick Lueth
# Date: 12/12/2018
# Webwit is a final project for CSI-160-01
# --------------------------------------------------------
# PLEASE DO NOT USE THIS CODE AND CLIAM IT TO BE YOUR OWN!
# --------------------------------------------------------
# Resources:
# https://dbader.org/blog/how-to-make-command-line-commands-with-python
# https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
# https://stackoverflow.com/questions/7164679/how-to-send-cookies-in-a-post-request-with-the-python-requests-library
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
# Black Hat Python by: Justin Seitz

import requests
import InputNFileIO
import MyASCII


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
            data = r.cookies
            for cookie in data:
                # parse the cookie data to clean up the out put a little.
                if str(cookie)[8:-1] not in cookies:
                    cookies.append(str(cookie)[8:-1])
            # Since we only opened the url to see if it works we just close it afterwards.
            r.close()
            print("Target set to: " + address)
            break
    return address


def view_cookies(target_host):
    """
    This function connects to the target host and views the cookie data of that site.
    :param target_host: (string) url of the website
    :return: (class) all of the cookie data
    """
    print("\n----------------------------------")
    r = requests.get(target_host)
    # Pull the cookie data from the web page
    data = r.cookies
    r.close()
    print("Cookies:")
    for i, cookie in enumerate(data):
        # parse the cookie data to clean up the out put a little.
        if str(cookie)[8:-1] not in cookies:
            cookies.append(str(cookie)[8:-1])
        print(str(i+1) + ".", str(cookie)[8:-1])
    print("----------------------------------")
    return data


def edit_cookie(host):
    """
    This function allows you to both view and edit cookies for a web page and to view the effects in the html once the
    cookie has been altered.
    :param host: (string) url
    :return: None
    """
    # Display cookies for target
    view_cookies(target)
    while True:
        # The user chooses a cookie to edit
        index = InputNFileIO.int_input_getter("Which cookie would you like to edit?: ", range(1, len(cookies) + 1))
        # Parse the cookie to only show the name of the cookie
        cookie_name = cookies[index - 1][:cookies[index - 1].index("=")]
        print("Chosen cookie:", cookie_name)
        # Allow the user to assign the cookie a value of their choice
        new_value = input("What do want to change that cookie's value to?: ")
        break
    # Craft the new cookie
    cookie = {cookie_name: new_value}
    # Send a post request to the web page with the new cookie
    r = requests.post(host, cookies=cookie)
    # Display the content of the web page with the cookie change
    print(str(r.content).replace('<', "\n<"))
    # Close the connection
    r.close()


def view_web_page(host):
    """
    This function is used to view the contents of a web page.
    :param host: (string) url
    :return: None
    """
    r = requests.get(host)
    # Makes a new line before the beginning of all HTML tags
    print(str(r.content).replace('<', "\n<"))
    r.close()


# Print random ASCII art
print(MyASCII.random_ascii())
# Global variables
menu = """
1. Set target host
2. View cookies
3. Edit cookies
4. View web page
5. Save website
6. Load website
7. Exit
"""
file_name = "WebPageData.txt"
target = ""
cookie_data = None
target_selected = False
cookies = []
website_saves = {}
# Program loop
while True:
    # Gets users input from the menu and manages errors
    user_choice = InputNFileIO.int_input_getter(menu, range(1, 8))
    # If they choose to "Set target host"
    if user_choice == 1:
        # Clear cookies
        cookies = []
        # Get target from the get_target() function
        target = get_target()
        # Set the global variable "target_selected" to True, this stops people from breaking the script by trying access
        # features that they can't without a valid target
        target_selected = True
    # If they choose to "View cookies"
    elif user_choice == 2:
        # If target is selected then view the cookie data for the target
        if target_selected is True:
            cookie_data = view_cookies(target)
        # Otherwise, tell the user that they need to select a target
        else:
            print("No target selected!")
    elif user_choice == 3:
        # If target is selected then allow the user to edit the cookie data for the target
        if target_selected is True:
            edit_cookie(target)
        # Otherwise, tell the user that they need to select a target
        else:
            print("No target selected!")
    elif user_choice == 4:
        # If target is selected then allow the user to view the web page
        if target_selected is True:
            view_web_page(target)
        # Otherwise, tell the user that they need to select a target
        else:
            print("No target selected!")
    elif user_choice == 5:
        # If target is selected then save web page and it's default cookie data
        if target_selected is True:
            InputNFileIO.website_saver(target, cookies, file_name)
        # Otherwise, tell the user that they need to select a target
        else:
            print("No target selected!")
    elif user_choice == 6:
        # Assign new_web to a line from the save file
        new_web = InputNFileIO.load_from_file(file_name)
        # The line is then parsed and redistributed across the global variables
        target = list(new_web.keys())[0]
        cookies = list(new_web.values())[0]
        # Reminds the script that a target has now been selected
        target_selected = True
    else:
        # If the user chose 7 (the only other possible input) then quit out of the script
        exit(0)
