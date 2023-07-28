#La forma mas fercuente de recorrer una list es utilizando for o loop

activities = ("sleep", "eat", "study")

#Utilizamos el for para recorrer directamente en la lista
for activity in activities:
    print(activity.title())

#ATENCION
# Lo anterior funciona bien su queremos utilizar directamente los valores existentes, pero si queremos actualizar algun valor, necesitamos los indices.
print("------------------------")
# Utilizamos el for sobre un rango desde cero hasta la ultima posicion de la lista. En todo momento es un rango de NÚMEROS 
#Podemos utilizar esos números como indices para acceder a los elementos de la lista.
for position in range(len(activities)):
    print(activities[position].title())

print("---------------------------")
print(activities)


cities = ["bogotá", "caracas","lima","la paz","san josé"]

for city in cities:
  print(city.title())

for position in range(len(cities)):
  cities[position] = cities[position].title()

print(cities)

# ["Bogotá", "Caracas","Lima", "La Paz", "San José"]

numbers = [4,3,5,6,7,4,3,5,6,7]

for n in range(len(numbers)):
  numbers[n] = numbers[n] * 2

print(numbers)


# [8,6,10,12,14,8,6,10,12,14]