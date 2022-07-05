 #2. Carré formé de deux nombres consécutifs

# 183 184 est le carré a six chiffres de 428. On remarque que ses trois
# premiers chiffres et ses trois derniers forment deux nombres consécutifs
# 183 et 184.
# Trouver 1'unique carré a huit chiffres tel que ses quatre premiers
# chiffres et ses quatre derniers représentent deux nombres consécutifs.

for i in range(1000, 10000 ):
    print(i,i ** 2)  # pour trouver le plus petit chiffre dont le carré nous permzt d'obteniur 8 chiffres
 
 #limite inferieur = 3163 ** 2 = 10004569
 #limite superieur = 9999 ** 2 = 99980001

for i in range(3163, 9999 + 1):
     carre = i ** 2

     premier_nombre = carre // 10000 # pour recuperer les 4 premier chiffres
     dernier_nombre = carre % 10000 # pour recuperer les 4 derniers chiffres
    #  print(carre,premier_nombre, dernier_nombre)

     if premier_nombre + 1 == dernier_nombre:
         print(i,carre,premier_nombre, dernier_nombre)

