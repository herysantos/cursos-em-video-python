days = int(input('Say how nuch days you used the car:'))
kms = float(input('Now, say how much km\'s you ran with the car:'))
print('The total you have to pay is R$ {:.2f}'.format((days * 60) + (kms * 0.15)))

