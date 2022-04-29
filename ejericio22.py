
#ejercicio22.py

vector_mochila_de_la_armadura = ["botella de aguna", "casco de darth vader", "kit de primeros auxilios",
 "juguete baby yoda", "sable de luz"]

print("MOCHILA anexada a la armadura:", vector_mochila_de_la_armadura)

cantidad_de_objetos = len(vector_mochila_de_la_armadura)

def usar_la_fuerza(mochila_de_la_armadura):
    if (len(mochila_de_la_armadura) == 0):
        return (False)

    elif(mochila_de_la_armadura[0] == "sable de luz"):
        return (True)   
    else:
        del mochila_de_la_armadura[0] 
        return usar_la_fuerza(mochila_de_la_armadura)


if (usar_la_fuerza(vector_mochila_de_la_armadura)):
    print("Se localizo elsable de luz")
    print("se sacaron: ", cantidad_de_objetos - len(vector_mochila_de_la_armadura), "objetos para localizarlo")
else:
    print("no hay ningun sable de luz")