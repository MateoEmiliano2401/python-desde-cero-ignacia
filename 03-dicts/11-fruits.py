fruits_prices = {
    "paltas":4200,
    "platano": 800,
    "piña": 2000,
    "mangos": 1000,
    "bambino": 1100,
    "limones": 850,
    "lechugas": 1200
}

# Se pide crear un programa que muestre el precio por kilo de la verdura o fruta solicitada

# 1 pedir que ingrese la fruta a buscar
search = input("¿Que precio quieres saber?")
# 2 mostrar el precio si existe
if search in fruits_prices:
    print("El precio de", search, "es",fruits_prices[search] )
# 3 mostrar que no tiene ese vegetal