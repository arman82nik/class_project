import re




def email_checker(email):
    if re.match (r"^[\w\.-]+@[\w\.-]+\.\w+$",email):
        print("email is  Exist")
        return True
    else:
        print("Email Does Not Exist")
        return False

def name_checker(name):
    if re.match(r"^[a-zA-Z\s{4,30}]$",name):
        print("name is  Exist")
        return True
    else:
        print("Name Does Not Exist")
        return False

def family_checker(family):
    if re.match(r"^[a-zA-Z\s{3,30}]$",family):
        print("Family  Exist")
        return True

    else:
        print("family Does Not Exist")
        return False

def code_checker(code):
    if re.match(r"^[0-9]{3,15}$",code):
        print("code is Exist")
        return True
    else:
        print("Code Does Not Exist")
        return False

def postalcode_checker(postalcode):
    if re.match(r"^[0-9]{3,}$",postalcode):
        print("postalcode is Exist")
    else:
        print("Postalcode Does Not Exist")
        return False

def mobile_checker(mobile):
    if re.match(r"^0[0-9]{11}$", mobile):
        print("Mobile Number is Valid")
        return True
    else:
        print("Mobile Number is not Valid")
        return False

