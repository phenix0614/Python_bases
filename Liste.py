# methode .append(Vl) permet d'ajouter une valeur a la list
liste = []
Slist = [1,2,3]
liste.append(5)
# attent en argument une list
# liste.extend([1,2,3])
liste.extend(Slist)
# retire le 1er element en parametre 
liste.remove(2) 
print(liste)
#  retiré un elem de la list par son index
liste.pop(-1) 
print(liste)



langage = ["JavaScript", "PhP", "C#", "Python", "Ruby"]
print(langage[3])

# les Slices permet de recuperer une plage de donnée ds a liste
print(langage[0:2])

# .index(VL) retourne la position ds la liste de la Vl ciblé
print(langage.index("PhP"))
# .count(vl) retourne le nmbrs d'occurence Vl dans la liste
# list.sort() trie directement la liste par ordre alpha 
# liste-trié = sorted(List) n'ecrase pas la liste de depart puisque contenu ds une variable 
langage_trie =  sorted(langage)
langage.sort()
print(langage_trie)
print(langage)
# list.reverse() inverse l'ordre de la list
# list.clear() vide la list
# " ".join(list) dans une CC insert entre les Vl de la lsite
# verifier qu'1 Vr est ds une list 
print("C#" in langage) 