prenom=input("prenom : ")

if prenom == "stephane" :
    print(f"hello {prenom} le beau gosse ")
else :
    print(f"bonjour {prenom} ")   

# différence avc elif 
user = input(" compte : ")
if user =="admin" :
    print(f"Acces autorisé {user} ")
elif user == "modo" :
    print(f"Acces autorisé {user} ") 
else :
    print("Accès refusé ")  
# WARNING !! else ne marche qu'avc le 1er if
#  au dessus de lui    

#  operateur de comparaison AND OR NOT 

