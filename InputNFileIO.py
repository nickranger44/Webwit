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


def website_saver(host, data, fname):
    """
    This function saves website data in order to be reused in the future.
    :param host: (string) target url
    :param data: (list) list of cookies
    :param fname: (string) file name
    :return: None
    """
    if not in_file(host, fname):
        # Append to the file
        f = open(fname, "a+")
        # Add the website to the file
        f.write(str({host: data}) + "\n")
        # Close the file
        f.close()


def in_file(host, fname):
    """
    This function checks to see if a website is already in the file.
    :param host: (string) target url
    :param fname: (string) file name
    :return: (bool) in file or not
    """
    # Read the file
    f = open(fname, "r+")
    # If the url exists in the file then return True
    for line in f:
        if host in line:
            print("That target is already saved")
            return True
    # Otherwise, return false
    return False


def load_from_file(fname):
    """
    Lists the contents of the file and allows you to choose which one you want to load into the script.
    :param fname: (string) file name
    :return: (dict) convert_entry(choice, fname)
    """
    # Read the file
    f = open(fname, "r+")
    # Counter keeps track of how many entries there are so it can be used with the int_input_getter function
    count = 1
    print("Saved websites:")
    # Prints a numbered list of all websites and their cookie data
    for i, line in enumerate(f):
        print(str(i+1) + ".", line[:-1])
        count += 1
    # Close the file
    f.close()
    # Get the user's input
    choice = int_input_getter("Which website would you like to load?: ", range(1, count))
    # Use the convert_entry function to get the final value to return
    return convert_entry(choice, fname)


def convert_entry(choice, fname):
    """
    This function searches the list of website entries and chooses and evaluates their choice to a dictionary.
    :param choice: (int) user's choice
    :param fname: (string) file name
    :return: (dict) entry to be loaded
    """
    # Read the file
    f = open(fname, "r+")
    # Search through the file
    for i, line in enumerate(f):
        # Once the script finds the entry that the user wants then it evaluates the string to dictionary
        if i == choice - 1:
            f.close()
            entry = eval(line[:-1])
            # Return the evaluated dictionary
            return entry
