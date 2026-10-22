print("======================= password analyzer =======================")
password= input("Enter your password: ")

def password_length(password):
    if len(password) < 8:
        return False
    else:
        return True
def password_upper(password):
    for letter in password:
        if letter.isupper():
            return True
        else:
            continue
    return False


def password_lower(password):
    for letter in password:
        if letter.islower():
            return True
        else:
            continue
    return False


def password_digit(password):
    for letter in password:
        if letter.isdigit():
            return True
        else:
            continue
    return False

def password_special(password):
    for letter in password:
        if letter in "!@#$%^&*?":
            return True
        else:
            continue
    return False



def password_analyzer(password):
    length_password = password_length(password)
    upper_password = password_upper(password)
    lower_password = password_lower(password)
    digit_password = password_digit(password)
    special_password = password_special(password)


    if not length_password or not upper_password or not lower_password or not digit_password or not special_password:
        print("error: \n")
    if not length_password:
        print("password length must be greater than 8")

    if not upper_password:
        print("password must contain uppercase letters")
    if not lower_password:
        print("password must contain lowercase letters")
    if not digit_password:
        print("password must contain digits")
    if not special_password:
        print("password must contain special characters")


password_analyzer(password)