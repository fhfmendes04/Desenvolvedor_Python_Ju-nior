from array import array

array_1 = array('B', [1,2,3,4,5,6,])

print(array_1)

for i in array_1:
    print(i)

# Inserir elemento

array_1.insert(2, 50)

print(array_1)

# remover elemento
array_1.remove(4)

print(array_1)

#Buscar elemento
print(array_1.index(50))

#Atualizar dados em um array
array_1[2] = 55

print(array_1)