text = "foo bar baz"
splitted_text = text.split(" ")

print(splitted_text)
print(len(splitted_text))
print(splitted_text[0])
print(splitted_text[1])
print(splitted_text[2])
# print(splitted_text[3]) #erreur
# splitted_text[3] = 123 # erreur car pas possible d'ecrader une valeur qui n'existe pas


splitted_text.append(123)
print(splitted_text)

# help(splitted_text.append)


# [start:end:step]

result = splitted_text[0:2] # choisi les element de 0 a 2 exclus
print(result)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae luctus nunc. Vivamus at nisl vitae orci blandit imperdiet in at mauris. Nulla gravida eu ex at fringilla. Proin finibus metus eu laoreet porttitor. Nam tincidunt enim dui, tristique rhoncus est condimentum vitae. Sed sit amet odio vitae tortor tempor ultricies. Cras interdum, justo quis luctus varius, neque velit scelerisque ex, id iaculis tellus diam at elit."


text = text.replace(".", "")  # pour remplacer les point par un espace vide , 1ere methode

splitted_text = text.split(",") # permet d'enlever la virgule dans le texte    2e methode
text = "".join(splitted_text) 

splitted_text = text.split(".") # la virgule est remplacé par un espace vide
text = "".join(splitted_text)


splitted_text = text.split(" ")
print(len(splitted_text))

# tous les mots de l'index 3 inclus a l'index 7 exclus
partial_list = splitted_text[3:7]
print(partial_list)
print(splitted_text)


partial_list = splitted_text[3:7:2] # ici l' index start = 3, index end = 7 ,le 3e chiffre permet de sauter les mots, de 2 en 2 ici
print(partial_list)
print(splitted_text)

# tout les mots de l'index 7 inclus a l'index 3 exclus
# ne fonctionne pas dans l'autre sens
# l'index start doit etre strictement inferieur a l'index end
partial_list = splitted_text[7:3] # ne fonctionne pas
print(partial_list)
print(splitted_text)

start = 7
end = 3

if start >= end:
    start, end = end, start

print(start, end)
partial_list = splitted_text[start:end]

partial_list = splitted_text[-7:-3:2]
print(splitted_text)
print(partial_list)

#Execercice
# 1.recuperer dans splitted_text les mots de l'index 35 a 49 inclus
# 2. Afficher le numero du dernier index
# 3.recuperer 1 mot sur 2 de l'index 0 au dernier index
# Attention, utiliser le dernier index calculé dans l'etape 2


#1
print(splitted_text[35:50]) # ma reponse

# reponse
start= 35 
end = 49
result = splitted_text[start:end+1]

#2

last_index = (len(splitted_text)-1)
print(last_index)


#3
result = (splitted_text[0:last_index+1:2])


# 4. creer 3 listes contenant:
# - le premier mot sur 3
# - le deuxieme mot sur 3
# - le troisieme mot sur 3

# Exemple : 
# liste_originale = ['foo', 'bar', 'baz','lorem','ipsum']
# liste_partielle1 == ['foo', 'lorem']
# liste_partielle2 == ['bar', 'ipsum']
# liste_partielle3 == ['baz']


list1 = splitted_text[0:last_index+1:3]
list2 =splitted_text[1:last_index+1:3]
list3 = splitted_text[2:last_index+1:3]


# copie de tout les elements 
# valeurs par defaut : 
 # start = 0
 # end = len()
 # step = 1
splitted_text[::] 

# copie de tout les elements en ordre inverse
result = splitted_text[::-1]

#copie de tout les elements a partir de start jusqu'a la fin
result = splitted_text[start:]

# copie de tout les elements du debut jusqu'a end
end = 10
result = splitted_text[:end]


a = 42
b = 123

a, b = b, a # inversion  de valeur dans une liste (version python)

splitted_text[0] = 42
splitted_text[1] = 123

splitted_text[0], splitted_text[1] = splitted_text[1], splitted_text[0]

 # inversion de valeur dans une version plus classique
#  tmp = splitted_text[0]
#  splitted-text[0] = splitted_text[1]
#  splitted_text[1] = tmp



my_list = []
print(list)

# mode Pile d'assiete
# equivalent d'un push ()
my_list.append("foo")
print(list)
my_list.append(123)
print(list)
my_list.append(3.14)
print(list)


last_element = my_list.pop()  
print(my_list)
print(last_element)


# mode File d'attente
my_list = ["toto", " titi", "tata", "tutu"]
client = my_list.pop(0) # pop(0) supprime l'index 0 , pop(1) surppime l'index 1,etc
print(my_list)
print(client)


# mode liste
print(my_list[0])
del(my_list[0])
print(my_list)

# ajouter un element a la liste
my_list.insert(0, "mémé") # ajout de mémé a l'index 0
print(my_list)


# concatenation de 2 listes
list_a = ["a","b","c"]
list_b = [1, 2, 3]

list_c = list_a + list_b

print(list_c)

# fusion de listes (modification de l'originale)
list_a.extend(list_b)
print(list_a)





