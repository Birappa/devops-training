harshad = int(input('Enter number: '))
def isHarshad(n):
    digit1 = n%10
    digit2 = round(n/10)
    if (n%(digit1 + digit2)) == 0:
        print('Given number is harshad')
    else:
        print('Given number is not harshad')
isHarshad(harshad)
