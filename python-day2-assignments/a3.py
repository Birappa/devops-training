name = ''
while name == '':
    name = input('who are you:')
    if name != 'joe':
        continue
    else:
        password = input('hello, joe. what is the password?(it is a fish)')
        if password == 'swordfish':
            break
        else:
            continue
print('access granted')
