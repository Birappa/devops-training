name = input('Enter your name: ')
age = int(input('Enter your age: '))
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, Kiddo')
elif age > 100:
    print('You are not Alice, Granny')
elif age > 2000:
    print('You are Vampire')
else:
    exit