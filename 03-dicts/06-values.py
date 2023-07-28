# Podemos separar solo los valores de un diccioanrio utilizando su método .values() 
english_to_spanish = {"hi": "hola", "bye": "chao" }

values = english_to_spanish.values()
for val in values:
    print(val)