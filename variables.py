# foo
# bar
# baz


nombre = 123
print(nombre)
print(type(nombre))

nombre = -3.14
print(nombre)
print(type(nombre))

nombre = "foo bar baz"
print(nombre)
print(type(nombre))

nombre = "-123"
print(nombre)
print(type(nombre))

text = "lorem ipsum"
print(text)

is_day = True
print(is_day)
print(type(is_day))

has_sugar = False
print(has_sugar)

has_accepted_ula = None
print(has_accepted_ula)
print(type(has_accepted_ula))

html_code = '<h1>Titre de mon blog</h1>'
print(html_code)

nickname = "John \"Dead\"Doe"
print(nickname)

multiline_text = "foo\nbar\nbaz"
print(multiline_text)

multiline_text = """foo
bar
baz"""
print(multiline_text)


# pour changer le type d'une fonction de string a integer
nombre = "5"
print(nombre)
print(type(nombre))
nombre = int(nombre)
print(nombre)
print(type(nombre))


#pour changer le type d'une fonction de string a float
nombre = "2.71"
print(nombre)
print(type(nombre))
nombre = float(nombre)
print(nombre)
print(nombre)
print(type(nombre))

nombre = 3.14
print(nombre)
print(type(nombre))
nombre = int(nombre)
print(nombre)
print(type(nombre))

texte = str(nombre)
print(texte)
print(type(texte))

#conversion en booleen ==> toute les valeur sauf 0 donne True, 0 donne False
my_var = 0
my_var = bool(my_var)
print(my_var)

my_var = 1
my_var = bool(my_var)
print(my_var)

my_var = 123
my_var = bool(my_var)
print(my_var)

my_var = -1
my_var = bool(my_var)
print(my_var)

my_var = -123
my_var = bool(my_var)
print(my_var)

my_var = " "
my_var = bool(my_var)
print(my_var)



my_var = [123, "abc", False]
my_var = bool(my_var)
print(my_var)
 
my_var = [False]
my_var = bool(my_var)
print(my_var)

my_var = []
my_var = bool(my_var)
print(my_var)

my_var = [None]
my_var = bool(my_var)
print(my_var)

n = 34.14
n = bool(int(n))
print(n)

#swap (interchanger les valeurs)
a = 42
b = 123

# interdit de faire a = 123 et b=42
# methode classique
c = a 
a = b
b = c

#methodr arythmetique
a = a + b # a = (42 + 123)
b = a - b # b = (42 + 123) - 123
a = a - b # a = (42 + 123) - 42 = 123

#destructured assignement
# pour python, js mais pas pour php
a, b = b, a 

if a == 123 and b == 42:
    print("vous avez reussi à inverser les valeurs des variables")

#arrondi
import decimal 
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

print(Decimal("0.5").quantize(Decimal("1"))) # Decimal('1')
print(Decimal("1.5").quantize(Decimal("1"))) # Decimal('2')

