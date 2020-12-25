def check_email(string):
    return all([' ' not in string, '@' in string, '.' in string[string.find('@') + 2:]])
