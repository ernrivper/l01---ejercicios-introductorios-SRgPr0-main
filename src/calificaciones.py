
#Ejercicio 1
def calcula_nota(a,f,t):
    res=(a*10/t)-(f*10/(50-t))
    if res<0:
        res=0
    return res

#Ejercicio2
def calcula_nota_cuatrimestre(cuestionarios,practico,proyecto):
    res=cuestionarios[0]+cuestionarios[1]+cuestionarios[2]
    return res


