#ejercicio_5


valores={"I":1, "V":5 ,"X":10, "L":50, "C":100, "D":500, "M":1000} 
cadena="IL"

def convertir_romano_a_decimal(cadena):
    if (len(cadena)==1):
        return valores[cadena[0]]
    elif (valores[cadena[0]]>=valores [cadena[1]]):
       return valores [cadena[0]]+convertir_romano_a_decimal(cadena[1])
        
    else:
        return -valores [cadena[0]]+convertir_romano_a_decimal(cadena[1:])


print (convertir_romano_a_decimal(cadena))
#I=1
#V=5
#X=10
#L=50
#C=100
#d=500
#M=1000