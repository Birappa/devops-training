def dict(n):
    dictionary = {}
    for i in range(1,n+1):
        dictionary.update({i: i*i})
    print(dictionary)
num = int(input('Enter number: '))
dict(num)