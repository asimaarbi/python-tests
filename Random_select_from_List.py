import random

foo = ['Shahid', 'Omer', 'Husnain', 'Bilal']
secure_random = random.SystemRandom()
print(secure_random.choice(foo))


