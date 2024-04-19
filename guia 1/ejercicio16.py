#s = ruta c = autonomia
#estrategia miro si tengo que cargar para llegar a la siguiente estacion
# si no hace falta avanzo, sino cargo
# en 0 siempre hay una estacion y siempre empiezo con el tanque vacio
def ruta_eficiente(s,c):
    tanque = 0
    paradas = []
    # for i  in range(len(s)):
    for i in range(len(s)-1):
        distancia = s[i+1] - s[i]
        if(tanque >= distancia):
            tanque -= distancia
        else:
            tanque = c
            tanque -= distancia
            paradas.append(s[i])
    return paradas

print(ruta_eficiente([0,2,8,11,20,25],10))
print(ruta_eficiente([0,2,8,10,20,25],10))