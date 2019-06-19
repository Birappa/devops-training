import re
def validate(password):
    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return True
    else:
        return False
    
pwd = input('Enter password: ')
if validate(pwd):
    print('Strong password')
else:
    print('weak password')