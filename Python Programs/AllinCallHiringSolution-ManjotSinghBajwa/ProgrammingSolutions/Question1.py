num = input('Enter a Mobile No : ')
if len(num) == 10:
    if num[0] == '7' or num[0] == '8' or num[0] == '9':
        if num.isdigit():
            print('VALID')
        else:
            print('NOT VALID')
    else:
        print('NOT VALID')
else:
    print('NOT VALID')

