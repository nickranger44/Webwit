# Created By: Nick Lueth
# Webwit is a final project for CSI-160-01
# Resources:
# https://dbader.org/blog/how-to-make-command-line-commands-with-python

#!/usr/bin/env python
import requests
import InputGetter


def view_cookies(target_host):
    """
    This function connects to the target host and views the cookie data of that site.
    :param target_host: (string) url of the website
    :return: (class) all of the cookie data
    """
    print("\n----------------------------------")
    r = requests.get(target_host)
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


def edit_cookie(host):
    """
    This function allows you to both view and edit cookies for a web page and to view the effects in the html once the
    cookie has been altered.
    :param host: (string) url
    :return: None
    """
    view_cookies(target)
    while True:
        index = InputGetter.int_input_getter("Which cookie would you like to edit?: ", range(1, len(cookies)+1))
        cookie_name = cookies[index - 1][:cookies[index - 1].index("=")]
        print("Chosen cookie:", cookie_name)
        new_value = input("What do want to change that cookie's value to?: ")
        break
    cookie = {cookie_name: new_value}
    r = requests.post(host, cookies=cookie)
    print(str(r.content).replace('<', "\n<"))
    r.close()


def view_web_page(host):
    r = requests.get(host)
    print(str(r.content).replace('<', "\n<"))
    r.close()


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
4. View web page
5. Save website
6. List saved websites
7. Exit
"""
target = ""
cookie_data = None
target_selected = False
cookies = []
website_saves = {}
while True:
    user_choice = InputGetter.int_input_getter(menu, range(1, 7))
    if user_choice == 1:
        cookies = []
        target = get_target()
        target_selected = True
    elif user_choice == 2:
        if target_selected is True:
            cookie_data = view_cookies(target)
        else:
            print("No target selected!")
    elif user_choice == 3:
        if target_selected is True:
            edit_cookie(target)
        else:
            print("No target selected!")
    elif user_choice == 4:
        if target_selected is True:
            view_web_page(target)
        else:
            print("No target selected!")
    else:
        exit(0)

# TODO: implement file i/o and make people be able to use old saved websites.
