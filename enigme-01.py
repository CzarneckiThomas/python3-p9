# nombre a 4 chiffre dont les 2 premiers ainsi que les 2 derniets atnat des carré a 2 chiffres
# liste qui contiendra nos reponses
resultats = []

# carré de 2 chiffres : 4 a 9  ( = 12 et 81)
carres_2_chiffres = []


for i in range(4,10):
    carres_2_chiffres.append(i ** 2)

# carre de 4 chiffres : 32  a 99

carres_4_chiffres = []

for i in range(32, 100):
    carres_4_chiffres.append(i ** 2)



# construisons des nombres a 4 chiffres

for i in carres_2_chiffres:
    for j in carres_2_chiffres:
        nombre = i * 100 + j

        if nombre in carres_4_chiffres:
            resultats.append(nombre)

print(resultats)

