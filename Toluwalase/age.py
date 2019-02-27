print('Sho mo age mi?')
min = 10
max = 100

while True:
    guess = int((min+max)/2)
    print('Is your age', guess,'?')
    a = input('Enter yes/high/low:\n')
    if a == 'yes':
      print('Mo mo age e!')
      break
    elif a == 'low':
      max= guess-1
    elif a == 'high':
      min = guess+1
    else:
        print('Ko ye mi!')
