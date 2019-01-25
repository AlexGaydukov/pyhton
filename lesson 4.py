__author__ = 'Гайдуков Александр Михайлович'


# hw04_easy 1

a = [4,3,5]
b = [i**2 for i in a]
print (b)

# hw04_easy 2

z = 1
a1 = ['киви', 'груши', '2']
a2 = ['киви', 'киви', 'яблоки']
a3 = [i for i in a1 for j in a2 if i ==j]
print (a3)

# hw04_easy 3

s = [3,12,9,7,45,95,-276,94]
k = [a for a in s if a%3==0 if a >0 if a%4!=0]
print (k)

# hw04_normal 1

import re
line = 'mtMmEZUOmcqfkejfZosMijdijfEkjj'
s = re.split(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]', line)
print (s)











































