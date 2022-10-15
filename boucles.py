# boucle for 
# langage = ["JavaScript", "PhP", "C#", "Python", "Ruby","CSS","JAVA"]

# for i in langage :
#     print(i)

# # boucle while tant que
# a = 0
# while a < 11 :
#     print(f"salut {a} ")
#     a += 1


# # fonction range(VL) crée une list avec plage de [0,VL]
# b = 0
# for i in range(11) :
    
#     print(f"hello {b} ")
#     b += 1 

#  compréhension de list
# nombres = [1,21,5,44,4,9,5,83,29,31,25,38]
# print(nombres)
# # boucle for pour sortir les nbrs pairs
# # nombres_pairs = []
# # for i in nombres:
# #   if i % 2 == 0:
# #       nombres_pairs.append(i)
# # i:valeur de sortie--- for i in nombres:boucle/list   if... :condition
# nombre_pairs = [i for i in nombres if i % 2 == 0]  
# print(nombre_pairs)
# for i in range(10):
#     print(f"Utilisateur {i+1} ")

# exo list de course
liste = []
choix= 0
while  int(choix) != 5:
    print("choisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: vider la liste")
    print("5: Quitter")
    choix = input("     votre choix : ")
    incrt = 0
    if int(choix) == 1:
        article = input("     Ajouter votre article : ")
        liste.append(f"{article}")
        # correction pour incrementé : fonction enumerate(liste,1)
        print(liste)
    elif int(choix) == 2:
        article = input("     élément à retiré : ")
        if article in liste:
            liste.remove(article)
            print(liste)
            
        else:
            print("élement non présent dans la liste")
    elif int(choix) == 3:
        for i in liste:
            print(i)
    elif int(choix) == 4:
        liste.clear()

print("*" * 50)        
              
# else:
#     print("à bientot")            
#     # elif int(choix) == 4:
#     #     liste = []                   

        

     











 
