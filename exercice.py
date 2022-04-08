import random

# Exo 1.1
# Affichez le type de donnée des variables a et b.

a = 3.14
b = 3

# Réponse 1.1

print(type(a))
print(type(b))

# Exo 1.2
# En utilisant les variables a et b, affichez les chiffres après la virgule de la variable a.

a = 3.14
b = 3

# Réponse 1.2

print(round (a-b, 2))

# Exo 1.3
# Affichez le type de données de la variable n.

n = random.randint(10, 99) / 10

print(type(n))

# Réponse 1.3

# Exo 1.4
# Convertissez n en un nombre entier, stockez le résultat dans une variable et affichez le résultat.

n = random.randint(10, 99) / 10
n = int(n)
print(n)


# Réponse 1.4

# Exo 1.5
# Affichez :
# - les nombres avant la virgule de la variable n
# - les nombres après la virgule de la variable n

n = random.randint(10, 99) / 10

# Réponse 1.5
print(n)
n_integer = int(n)
print(n_integer)
print(n - n_integer)




# Exo 1.5
# Stockez dans une variable si la variable n est un nombre entier ou non.

n = random.randint(10, 99) / 10

# Réponse 1.5




#exo 2.
# Affichez le texte "foo" si la variable n est inferieur a 5

n = random.randint(0, 9)
print(n)

if n < 5:
    print("foo") 

# exo 2.2 tirez un nombre au hasard compris entre 0 et 9 inclus sans le stocker dans une variable
# et afficher le texte "foo", si le nombre est inferieur a 5
# Vous pouvez utiliser random.randint(0, 9) pour tirer le nombre au hasard


if random.randint(0, 9) < 5:
     print("foo") 



# 2.3 Affichez le texte "foo" tant que vous tirez au hasard un nombre compris entre 0 et 9 inclus, plus petit que 5
# Vous pouvez utiliser random.randint(0, 9) pour tirer le nombre au hasard


#avec une condition de continuation
while random.randint(0, 9) < 5:
    print("foo")


#avec une condition d'arret
while True:
    if random.randint(0, 9) < 5:
        print("foo")
    else:
        break



