
from hashlib import new
from operator import ne, truediv
import random 

firstname = "toto"
lastname = "pop"
number = 2

# quand on fait une concatenation, il faut ajouter str au nombre pour le transformer en strings
email = firstname + "." + lastname + str(number) + "@exemple.com"
print(email)

new_emails = random.randint(0, 3)

if new_emails == 0:
    print("Vous n'avez pas de nouveaux mails")
elif new_emails == 1:
    print("Vous avez recu <strong>1</strong> nouveau mail")
else:
    print("Vous avez recu <strong>" + str(new_emails) + "</strong> nouveaux mails")


# f-strings
stock = random.randint(0, 15)

if stock == 0:
    print("Stock epuisé")
elif stock == 1:
    print("stock en tension : 1 Piece")
elif 1 < stock < 5:
    print(f"stock en tension : {stock} pieces")
elif 5 < stock < 10:
    print(f"stock confortable : {stock} pieces")
elif 10 <= stock:
    print(f"Stock en surnombre : {stock} pieces")


temperature = 10.1 + 0.1 + 0.1
print(temperature)
# interpolation
# .2f ca explique a Python comment afficher la varibale (nombre decimal, exadecimal, etc. ICI c'est 2 chiffres apres la virgule)
print(f"La temperature actuelle est de {temperature:.2f}° C")

#ne pas faire d'interpolation de variable booleenne si votre apli n'est pas en anglais
electricite = True
if electricite:
    print("electricite: vrai")
else: 
    print("electricité: faux")


print(f"le nombre tiré au hasard est : {random.randint(0, 10)}")



texte = "foo bar baz"
 # len == lenght == longueur
print(len(texte))


texte = " Bnjour   Toto"
texte = texte.replace("Bnjour", "Bonjour")
texte = texte.replace("   ", " ")
texte = texte.replace("Toto", "Titi")
print(texte)


# find() renvoie a un nombre entier
# find () renvoie un nombre entier >= 0 si le texte est trouvé
# find () renvoie a un nombre entier < 0 si le texte n'est pas trouvé

print(texte.find("baz"))
print(texte.find("ba"))
# recherche a partir du 5e caractere
print(texte.find("ba", 5))
print(texte.find("banana"))

#-----------------------------------------------------------------------
#exercice 
texte = "bonjour toto"

keyword = "toto"
keyword = " titi"

# rediger un bloc if qui indique si le keyword est present ou non dans la chaine de caractere
#afficher "trouvé" si le keyword est présent
#sinon afficher "non trouvé"
keyword = "toto"

print(texte.find(keyword))

if texte.find(keyword) >= 0:
    print("Trouvé")
else:
    print("Non trouvé")




# rediger un bloc if qui indique si le keyword est present ou non dans la chaine de caractere
#afficher "trouvé" si le keyword est présent
#sinon afficher "non trouvé"
keyword = "titi"


print(texte.find(keyword))


if texte.find(keyword) >= 0:
    print("Trouvé")
else:
    print("Non trouvé")

#---------------------------------------------------------