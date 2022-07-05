# un artilleur dispose de boulets de canon répartis dans un carré parfait. Pour réduire l'encombrement
# au sol, l'artilleur réussit à empiler ses boulets pour former une belle pyramide à base carrées.
# Quel est le plus petit nombre de boulets possible dont dispose l'artilleur ?

# complexité algorithmique O(n+ n*n) == O(n*(1+n))


# liste en comprehension
#on demare a 2 pour eviter que la boucle for principale trouve 1 comme resultat
#de plus sa evite de faire un if qui verifi que le resultat est different de 1 a chaque iteration
squares = [i ** 2 for i in range(2, 101)]




# meme code mais differement
# squares = []

# for i in range(1, 101):
#     squares.append(i ** 2)


#Comme les carré pré-calculé demare a 1, il faut pré-compter ce boulet dans la pyramdide
pyramid= 1

for bullet in squares:
    pyramid += bullet

    if pyramid in squares:
        print(pyramid)
        break



