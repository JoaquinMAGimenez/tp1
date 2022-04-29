
#laberinto.py  

def salida_laberinto  (matriz , x , y , caminos=[]):
   if (x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz [ 0 ])-1):
     if  (matriz[x][y]==2):
       caminos.append([x , y])
       print ("saliste del laberinto")
       print (caminos)
       caminos.pop()
     elif(matriz[x][y]==1):
        matriz[x][y]=3
        caminos.append( [ x  , y ])

        salida_laberinto(matriz, x, y-1, caminos)
      
        salida_laberinto(matriz, x, y+1, caminos)
      
        salida_laberinto(matriz, x+1, y, caminos)
      
        salida_laberinto(matriz, x-1, y, caminos)
      
        caminos.pop()
        matriz [ x ] [ y ] = 1


experimento = [[ 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
       [ 0 , 0 , 0 , 0 , 0 , 0 , 1 ],
       [ 0 , 0 , 0 , 1 , 1 , 1 , 1 ],
       [ 0 , 0 , 0 , 1 , 1 , 1 , 2 ]]
    
salida_laberinto ( experimento , 0 , 0 )