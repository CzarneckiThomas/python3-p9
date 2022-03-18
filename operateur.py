# + - * 

from doctest import OutputChecker


result = 123 + 4.14
print(result)


#  ()
result = (1+2) * 3


# / // % **

# Division entiere   pour arrondir
result = 1 // 3   
print(result)

# modulo
# 10 % 3  c'est 3+3+3 => reste 1   donc modulo = 1
result = 10 % 3
print(result)

result = 14 % 2 
print(result)

# verification de la devisibilité
result = 7685923 % 7
print(result)

# Puissance
# dans certains language c'est : ^, pow()
result = 3 ** 2
print(result)

# racine carré
result = 9 ** (1 / 2)
print(result)

#  racine  cubique
result = 9 ** (1 / 3)
print(result)

# operateur composé

       #n'existe pas en python
# c++ <=> c = c + 1

number = 42
# number = number + 1
n = 1
number += n

# Operateur Booleen "and"
result = True and True # True
result = False and True # False
result = True and False  # False
result= False and False # False

# S'il n'y a que des "and", l'ordre n'est pas important
result = True and True and False and False  #False

# Operateur Booleen "or"
result = True or True # True
result = False or True # True
result = True or False  # True
result= False or False # False

# S'il n'y a que des "or", l'ordre n'est pas important
result = True and True and False and False  # True

# pour dire l'inverse
result = not True
print(result)

is_user_majeur = True
result = is_user_majeur == False 
result = not is_user_majeur # la meme chose que la ligne au dessus


#  == != < > <= >= 
# ===  
a = 123
b = 42
result = a == b
print(result)

# different
result = a != b
print(result)

# inferieur ou egal
result = a <= b
print(result)


# l'operateur fait office de comparaison d'identité
a = "123"
b = 123
result = a == b
print(result)

# n'exite pas en python
# === !==

# operateur de test d'inclusion
fruits = ["apple", "banana", "cherry"] 
result = "banana" in fruits
print(result)


result = type(123) is float
print(result)


# encadrement
import random
a = 42
b = 123

c = random.randint(1, 100)

result = a < 50 < b
print(result)

result = a < c < b
print(c)
print(result)





