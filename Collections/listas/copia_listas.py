import copy
nested_list = [[1,2], ["oi", "olá" ]]

# Deep Copy
nova_lista = copy.deepcopy(nested_list)
nova_lista[0][1] = "A"
print(nova_lista)

# Shallow Copy - endereço de memória
outra_lista = copy.copy(nested_list)
nested_list[0][1] = "B"
print(outra_lista)
print(nested_list)

