message = "hello world"

def affiche(x):
    print(x)

affiche(message)
affiche("salut le monde ")
#  fonction locals() et globals() servent a regard tout ce qui se passe en local ou en global

# glabal

# def get_comment(note):
#     # global commentaire : on peu definir qu'une Vr utilisé ds une fonction se serve de celled efini en global
#     if note > 15:
#         commentaire = "Bravo !"
#     elif note > 10:
#         commentaire = "Peut mieux faire..."
#     elif note > 5:
#         commentaire = "Attention !"  

# commentaire = "Tu as tout faux"
# get_comment(20)
# print(commentaire) 

# ici ça ne marche pas puisque la Vr commentaire (local) et la Vr commentaire (global) sont deux Vr différente
# 
def get_comment(note):
    if note > 15:
        return "Bravo !"
    elif note > 10:
        return "Peut mieux faire..."
    elif note > 5:
        return "Attention !"
    else:
        return "Tu as tout faux"   

commentaire = get_comment(20)

print(commentaire) 

# ************************************* Classe ******************** 

class Voiture:
    marque = "Lamborghini"
    couleur = "rouge"
    vitesse = 200

print(Voiture.marque)
print(type(Voiture.vitesse))

