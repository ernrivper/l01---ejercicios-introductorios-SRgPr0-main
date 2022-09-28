from calificaciones import *

#Ejercicio1
aciertos=int(input("Escribe el numero de aciertos: "))
fallos=int(input("Escribe el numero de fallos: "))
total_respuestas=int(input("Escribe el numero total de respuestas: "))

print("n\La nota de tu test es de:",calcula_nota(aciertos,fallos,total_respuestas))

#Ejercicio2
c1=int(input("Escribe la nota del primer cuestionario: "))
c2=int(input("Escribe la nota del segundo cuestionario: "))
c3=int(input("Escribe la nota del tercer cuestionario: "))
nota_cuestionarios=(c1,c2,c3)
nota_práctico=int(input("Escribe la nota del examen práctico: "))
nota_proyecto=int(input("Escribe la nota del proyecto: "))

print(calcula_nota_cuatrimestre(nota_cuestionarios,nota_práctico,nota_proyecto))


