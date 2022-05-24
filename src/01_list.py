

# Crear una lista 
# name_list = ["valores", "separados", "por", "comas"]

list_str = ["uno", "dos", "tres"]
print(list_str)

list_n = [1, 2, 3, 4]
print(list_n)

# acceder a los valores de una lista mediante su index
# el indice comienza en 0 desde el primer elemento de la lista

print(list_str[0] , "es el primer elemento de list_str ")

print(list_n[1], "es el segundo elemento de list_n")

# para conocer el indice de un elemento se usa el método index()

print(list_n.index(4), "es el indice del elemento 4")

# se pueden usar asignaciones como en cualquier variable
list_n[3] = 5
print("list_n[3] = 5 \nahora el indice 3 de list_n es: \n", list_n[3])

# para saber la longitud de una lisra se usa el metodo len()
my_list = [0,1,2,3,4,5,6,7]
print()
print("uso de len()")
print("my_list =", my_list)
print("len(my_list) da como resultado:", len(my_list))

# remove

print()
print("remove")
print("my_list =", my_list)
my_list.remove(5)
print("my_list.remove():", my_list)

