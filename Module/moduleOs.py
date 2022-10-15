import os

chemin = "/CODE/python/bases"
# methode pour creer un nouveau chemin pour le nouveau dossier
dossier = os.path.join(chemin, "Module")

# methode pour creer le dossier 
#  os.mkdir() peu crée qu'un seul dossier
 
# methode ppur créer dossier et sous dossier 
os.makedirs(dossier)
# os.makedirs(dossier, exist_ok=true) permet de creer le dossier si il n'existe pas deja
# methode pour effacé un dossier 
# os.removedirs(dossier )

