import re

phoneNumberPattern = re.compile(r'(\d\d\d-\d\d\d\d-\d\d\d\d)')

phoneNumber = phoneNumberPattern.search('this is my phone number 123-4567-6789. my office number is 789-6543-1234')

print('phone number: '+phoneNumber.group())