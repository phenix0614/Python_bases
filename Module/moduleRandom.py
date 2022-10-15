# import de module voulu
import random
# import de la fonction pprint qui liste dir() par ligne
from pprint import pprint
# fonction qui liste toutes les methode d'un module
methode_list = dir(random)
# print(methode_list)
# pprint(methode_list)
#  collable(fonction) verifie si une fonction est appelable


# fonction help(methode) retourne une aide de la methode ciblé 
help(random.randint)

# on stock une  methode de random dans une V
# ici la methode randint(min,max) retourne un int aleat dans la plage
r= random.randint(1,10)
print(r)
# methode .uniform(min,max) retourne un float
# methode .randrange(min, max*,pas) retourne un int dans la plage avc un pas

