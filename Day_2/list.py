girls = ["Anna", "Maria", "Eva"]
print(girls)

girls.append("Brenda")
print(girls)

print (girls[3])

girls.sort(reverse = True)
print(girls)
print('\n')
boys = ["George", "Bello", "Joel", "Bankey"]
print(boys)
boys.sort(reverse=True, key=len)
print(boys)