import random



#if True: 
   # print("ce message sera toujours affiché")

#if False: 
   # print("ce message ne sera jamais affiché")



# # if True: 
# #     print("ce message sera toujours affiché (if True)")
# # else:
# #     print("ce message ne sera jamais affiché (if True)")

# # if False: 
# #     print("ce message sera toujours affiché (if False)")
# # # else:
# # #     print("ce message ne sera jamais affiché (if False)")

# # # fruits = ['bananas','cherries','apples']
# # # if 'apples' in fruits:
# # #    print("il y a des pommes")
# # # else:
# # #     print("il n'y a pas de pommes")

# # # if 'orange' in fruits:
# # #     print("il y a des oranges")
# # # else: 
# # #     print("il n'y a pas d'oranges")


# # # is_authenticated = True
# # # if is_authenticated:
# # #       print("L'utilisateur peut acceder aux backoffices")

# # user_password_in_form = "123"
# # user_password_in_db = "abc"

# # if user_password_in_form == user_password_in_db:
# #     print("L'utilisateur peut acceder aux backoffices")
# # else :
# #     print("Le login ou le mot de passe est incorrect")

# # user_in_db = ['toto','titi','tata','tutu']
# # tutu_password_in_db = "abc"

# # user_name_in_form = 'tutu'
# # user_password_in_form = "123"

# # #les parenthese en dessous ne sont pas obligatoire. Python calcul dabord "in" puis "==" puis "and"
# # if (user_name_in_form in user_in_db) and (user_password_in_form == tutu_password_in_db):
# #     print("L'utilisateur peut acceder aux backoffices")
# # else : 
# #     print("le login ou le mot de passe est incorrect")

# # if ("tutu") and user_password_in_form == user_password_in_db:
# #     print("L'utilisesateur peut acceder aux bacoffices")
# # else:
# #     print("Le login ou le mot de passe est incorrect")



# # is_authenticated = True
# # user_in_db = ['toto','titi','tata','tutu']
# # tutu_password_in_db = "abc"

# # user_name_in_form = 'tutu'
# # user_password_in_form = "abc"


# # # quand on melange des or et des and, il faut mettre des parenthese (comme pour les calculs avec des multiplication)
# # if is_authenticated or (user_name_in_form in user_in_db and user_password_in_form == tutu_password_in_db):
# #     print("L'utilisateur peut acceder aux backoffices")
# # else : 
# #     print("le login ou le mot de passe est incorrect")



# #boo(random.randint(0, 1)) permet de generer soit un false soit un true
# electricity_is_off = bool(random.randint(0, 1))
# water_is_off = bool(random.randint(0, 1))
# gas_is_off = bool(random.randint(0, 1))

# print("electricity:", electricity_is_off)
# print("water:", water_is_off)
# print("gas:", gas_is_off)

# #verifier que toutes les soures sont coupées
# #si c'est le cas,affichez le message "Vous pouvez partir en week end"
# #sinon,affichez le message "il reste des sources a couper"
# # si c'est True , c'est coupé
# #si c'est false, c'est pas coupé

# if electricity_is_off and water_is_off and gas_is_off:
#  print("Vous pouvez partir en week end")
# else : 
#  print("Il reste des sources à couper")


# if electricity_is_off == True and water_is_off == True and gas_is_off == True:
#     print("Vous pouvez partir en we")
# else: "il reste des sources à couper"

# foo = True 
# print(foo == True)
# foo = True



# if electricity_is_off and water_is_off and gas_is_off:
#  print("Vous pouvez partir en week end")
# else : 
#  print("Il reste des sources à couper")
#  if not electricity_is_off:
#      print("coupez l'electricité")

# if not water_is_off:
#     print("coupez l'eau")

# if not gas_is_off:
#     print("coupez le gaz")

#if not_electricity_is_on and not water_is_on and not gas_is_on:
#else:
#if electricity_is_on
# #print(couper l'electricité)

# has_cash = bool(random.randint(0, 1))
# has_card = bool(random.randint(0, 1))
# has_check = bool(random.randint(0, 1))
# print("has_cash:", has_cash)
# print("has_cash:", has_card)
# print("has_cash:", has_check)


# # verifier qu'au moins un moyen de paiement est disponible
# # si c'est le cas, affichez le message " Vous pouvez partir faire les courses"
# #sinon affichez le message "Vous n'avez aucun moyen de paiement"

# if has_cash or has_card or has_check:
#     print("Vous pouvez partir faire les courses")
#     if has_cash:
#         print("Vous avez du liquide")
#     if has_card:
#         print("Vous avez une CB")
#     if has_check:
#         print("vous avez un chequier")
# else: 
#     print("Vous n'avez aucun moyen de paiement")

age = random.randint(0, 100)

# 0-5 bébé
# 6-11 enfant
# 12-25 ado, jeune adulte
# 26-59 adulte
# 60+ seniot

if age <= 5:
    print("bébé")
elif 6 <= age <=11:
    print("enfant")   
elif 12 <= age <=25:
    print("ado, jeune adulte") 
elif 26 <= age <=59:
    print("adulte") 
    # on peut aussi faire un else pour intercepter les cas ou l'age >= 60
elif age >= 60:
    print("senior") 

if 123:
    #s'affichera car le bool(123) == True
    print("il y a une valeur numerique")

if 0: 
    #le message ne s'affichera pas car bool(0) == false .
    print("il y a une valeur nulle")

    



