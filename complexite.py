# complexité == efficacité
# efficacité :
# - temp d'execution
# - espace memoire

# notation de Landau : O()    lettre O , pas chiffre 0
# pas une fonction mais un ensemble

# O(c)   (c == constante)
# O(1)
# + - * / // **2 
result = 123 + 42
print(result)




#recherche par dicothomie dans une liste
# recherche d'un fruit dont la lettre demarre par une lettre
# O(n * log(n))
# log == logarithme naturel

words = ["ananas", "bananas", " cerise", "durian", "kiwi", "orange", "pomme"]



# O(n)
# n est la quantité de données a traiter
numbers = [123, 42, 3.14]

for number in numbers:
    result = number * 2
    print(result)


# O(n * m)   == O(n²)
# n est la quantité de donées a traiter de la premiere liste
# m est la quantitité de donnée a traiter de la deuxieme liste
numbers = [123, 42, 3.14]
more_numbers= [2.71, 3.14, 0, 53]
common_numbers = []

for number in numbers:
    for more_number in more_numbers:
        if number == more_number:
            common_numbers.append(number)

# O(n²)
matrix = [ 
    [123, 42, 3.14]
    [2.71,3.14,0]
    [1,2,3]
]
    
for line in matrix:
    for number in line:
        result = number * 2
        print(result)

# O(n3)   ===> O( n * n * n)
cube = [
    [
        ["a1", "a2", "a3"],
        ["a4", "a5", "a6"],
        ["a7", "a8"," a9"],
    ],
[
        ["b1", "b2", "b3"],
        ["b4", "b5", "b6"],
        ["b7", "b8"," b9"],
    ],
[
        ["c1", "c2", "c3"],
        ["c4", "c5", "c6"],
        ["c7", "c8"," c9"],
    ],

]

for square in cube:
     for line in square:numbers = [4, 10, 42, 3.14]
my_list = []

for n in numbers:
     #puissance 2
     result = n ** 2
     my_list.append(result)

# algo pas efficace du tout :
# O(n ** n)
# O(n!) == O(n* (n -1) * (n -2) * ... *2)
# 5! == 5 * 4 * 3 * 2 * 1

#exemple d'optimisation
#O(n)
numbers = [4, 10, 42, 3.14]
#initialisation du compteur
i = 0
#verification de la condition de continuation
while i < len(numbers):
    #action a repeter
    print(number[i])
    #incrementation du compteur
    i += 1


# exo 1 ;  determiner la complexité algorithmique de ce programme
numbers = [4, 10, 42, 3.14]
my_list = []

for n in numbers:
     #puissance 2
     result = n ** 2
     my_list.append(result)

# exo 2: determinez la complexité algo de ce programme
 

numbers = [4, 10, 42, 3.14]
my_list = []

while True:
    number = numbers.pop()
    my_list.append(number)

    if len(numbers) == 0:
        break

