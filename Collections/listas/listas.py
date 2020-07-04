lista_simples_inteiro = [1,2,3,3, 4,5]

lista_simples_string = ["oi", "Olá"]

lista_simples_mesclada = [1,2 ,3, "oi"]

nested_list = [[1,2], ["oi", "olá" ]]

print(lista_simples_inteiro)
print(nested_list)

# Len()
print(len(lista_simples_inteiro))
print(len(nested_list))

# Append()
lista_simples_inteiro.append(6)
print(lista_simples_inteiro)

# Insert()
lista_simples_inteiro.insert(2, 0)
print(lista_simples_inteiro)

# Remove()
lista_simples_inteiro.remove(1)
print(lista_simples_inteiro)

# Index()
print(lista_simples_inteiro.index(3))

# Count()
count = lista_simples_inteiro.count(3)
print(count)

# Sort()
lista_simples_inteiro.sort(reverse=False)
print(lista_simples_inteiro)

lista_simples_inteiro.sort(reverse=True)
print(lista_simples_inteiro)
