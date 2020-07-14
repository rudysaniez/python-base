import sys

print("Hello World")  
print(sys.copyright)
print(sys.path)

# Concaténation Str an Int
age=40
yearAdding=1;now=age+yearAdding;
print("J'ai maintenant " + str(now))
print("J'ai toujours %s ans" % (now))
print("J'ai toujours et encore {} ans".format(now))

#Type de variables et opérateurs de comparaison sur l'objet de type <class 'int'>
print("Age est de type : " + str(type(age)))
print(str(age.__lt__(20)) + " -- " + str(age.__eq__(40)))