#Ejercicio 1
tonelada_cereal = [12,24,16,15,20,18,6,10,12,11,15,12]

#Sumar los datos del arreglo y Divirlos entre el total de elementos
promedio_total = sum(tonelada_cereal)/len(tonelada_cereal)
print(promedio_total)

#Realizar una comparacion de todos los valores vs promedio
promsuper = [tonelada for tonelada in tonelada_cereal if tonelada > promedio_total]
superior = (len(promsuper))
print(superior)

#Realizar una comparacion de todos los valores vs promedio
prominfe = [tonelada for tonelada in tonelada_cereal if tonelada < promedio_total]
inferior = (len(prominfe))
print(inferior)






