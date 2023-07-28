#Escribir un programa que imprima una lista de los estudiantes o promedios superior a 6

averages = {
    "seba":5,
    "gaby":6.5,
    "fran":7,
    "jose":6.4,
    "coni";6.2,
    "gonza":4.8
}

# 1 crear un diccionario vacio
approved = []
# 2 recorrer las llaves del diccionario
for key in averages.keys():

# 3 revisar si el valor de la llave es superior a 6
if averages[key]> 6:
# 4 agregar la llave a la lista 
approved.append(key)

# 5 imprimir la lista
print(approved)