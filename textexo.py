import random


numbers = []

# 1er tirage
n = random.randint(1, 5)
numbers.append(n)

# 2ème ,3e et 4e tirage , code a reproduire 3 fois, mais beaucop trop lourd



while True:
    n = random.randint(1, 5)

    # condition d'arrêt
    if n not in numbers:
        # le nombre n'a pas encore été tiré au hasard
        # on peut sortir de la boucle
        break
    
numbers.append(n)
print(numbers)

# 2e, 3e et 4eme tirage , code de facon optimisée

while True:
    n = random.randint(1, 5)

    # condition d'arrêt
    if n not in numbers:
        # le nombre n'a pas encore été tiré au hasard
        # on peut sortir de la boucle
        break
    
numbers.append(n)
print(numbers)



