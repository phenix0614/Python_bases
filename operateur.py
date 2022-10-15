# incrementation

# i += 1 somme
# i -= 1 soustraction
# i *= 1 multiplication
# i /= 1 division float
# i %= 1 modulo recupere le reste d'une division
# i //= 1 division entiere
# i **= 1 puissance

#  place en memoire  
a= [1,2,3]
b= [1,2,3]
c= a 
# on verifie l'egalité des valeur 
print(a == b)
print(a == c)
# on verifie l'egalité des variable 
print(a is b)
print(a is c)
# adresse en mémoir 
print(id(a))
print(id(b))
print(id(c))

# pour des raison d'opti les entiers entre -5 et 256
# ont la même place memoir du coup deux variable qui 
# pointe la même valur ds cet ecart son true
# a=256
# b=256
# print(id(a))
# print(id(b))

# print(a is b)
# a=38000
# b=38000
# print(id(a))
# print(id(b))
# print(a is b)
#  apreciser 


