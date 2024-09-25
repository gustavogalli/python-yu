def format_name(f_name, l_name):
    """Take a first and a last name and format it
    to return the capitalized version of the name."""
    
    if f_name == '' or l_name == '':
        return 'You did\'t provide valid inputs!'

    name = str(f_name).capitalize()
    surname = str(l_name).capitalize()
    return f'{name} {surname}'


print(format_name(input("What's your fist name? "),
      input("What is your last name? ")))
