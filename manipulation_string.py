# *************************** manipulation de string ****************

# print("hello world")
# bonjour="hello world i'm Phenix"
# print(bonjour)
# print(type(bonjour))
# # Place en mémoire 
# print(id(bonjour))
# # tout en majuscule
# print(bonjour.upper())
# # tout en minuscule
# print(bonjour.lower())
# # Maj sur le 1er mot
# print(bonjour.capitalize())
# # Maj sur chaque mot 
# print(bonjour.title())
# #  methode is renvoi un boolen 
# # islower , istitle etc 
# # isdigit bool regarde si le string represente un int 
# # count("") compte 
# # .endswith("") et startswith("")  bool cherche la fin et le debut d'une chaine charactere


# salut=" bonjour "
# print(salut)
# # remplace old/new
# print(salut.replace("jour","soir"))
# # retire les charactère demander par defaut "espace"
# print(salut.strip())
# # de GàD et de DàG
# print(salut.strip(" ujor"))
# # da DàG
# print(salut.rstrip(" ujor"))
# print(salut.lstrip(" ujor"))

# # ********************************Concatenation *************************************

# # exo 
# # on ne concatène que les String
# a ="j'ai une classe de" +" "+ str(30)+" "+"eleves"
# b =str(10) + " " + "+" + " " + "5"+" " + "est egal à" + " " + str(15)
# c =10+int("5")
# d ="l'addition de 10 + 5 est egal à"+" "+str(10+5)
# print(a)
# print(b)
# print(c)
# print(d)

# # creation input
# prenom = input("votre prenom : ")
# age = input("votre age : ")
# # methode format(V) tres m odulable avc les indice et les variable dans la CC
# phrase = "Vous avez {} ans".format(age)
# #  les f-String
# print(f"bonjour {prenom}, {phrase} ")




# #  séprer et joindre des String 
# Lnbr= "1, 2, 3, salut, copain, @"
# print(Lnbr)
# print(Lnbr.split(", "))
# print("-".join(Lnbr.split(", ")))

# # ajouter des 0 à un nombre 
# print("9".zfill(4))

# # calculatrice
# fnbr=input("entrer un 1er nombre : ")
# snbr=input("entrer un second nombre : ")
# result=int(fnbr) + int(snbr)
# text="Le résultat de l'addition de {} avec {} est égal à {} "
# print(text.format(fnbr,snbr,result ))
# print(f"le résultat de l'addition de {fnbr} avec {snbr} est égale à {int(fnbr)+int(snbr)}  ")

# exo Password 
mdp = input("Entrez votre password :  ")
mdp_trop_court = "votre mot de passe est trop court."

if len(mdp) == 0 :
    print(mdp_trop_court.upper())
elif len(mdp) <= 8 :
    print(mdp_trop_court.capitalize())
elif mdp.isdigit() :
    print(mdp_trop_court.replace(" est trop court."," ne contient que des nombres").capitalize()) 
else :
    print("inscription terminée")      

