 #!/usr/bin/python
 # -*- coding: utf-8 -*-
pokemon=open("pokemon.txt","r")
lista=pokemon.readline().split(" ")
#Comprueba que la ultima linea no sea el final del fichero
while lista[-1]!="":
        #elimina el salto de linea "\n" de la ultima linea
        lista[-1]=lista[-1][0:-1]
        #añade la nueva linea a la lista
        for x in pokemon.readline().split(" "):
                lista.append(x)
#elimina toda linea vacia
lista=[i for i in lista if i != ""]
cadena,candidata=[],[]
for x in range(len(lista)):
		#actualiza la cadena mas larga encontrada hasta el momento
        if len(cadena)<len(candidata):
                cadena=candidata
		#machaca la cadena ya comprobada(y guardada en el caso de ser la mayor) con el primer elemento de la siguiente candidata
        candidata=[lista[x]]
		#la busqueda empezará por el elemento siguiente
        y=x+1
		#comprobación inicial de que el elemento siguiente no se salga del rango, en cuyo caso vuelve al inicio de la lista
        if y>=len(lista):
                y=0
        while y!=x:
				#comprueba si la letra inicial de la palabra candidata se corresponde con la ultima letra de la palabra final de 
				#la cadena, en cuyo caso la enlaza
                if lista[x][-1]==lista[y][0]:
                        candidata.append(lista[y])
                        x=y
                        break
                y=y+1
				#realiza un movimiento circular de busqueda hasta alcanzar el elemento inicial
                if y>=len(lista):
                        y=0
print("La cadena mas larga es de longitud", len(cadena),"y esta compuesta por:\n",cadena)
