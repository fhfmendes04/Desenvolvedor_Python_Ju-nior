lista_simples_inteiro = [1, 2, 3, 3, 4, 5]

nova_lista = []

for i in lista_simples_inteiro:
    nova_lista.append(i * i)
print(nova_lista)

nova_lista_elegante = [i * i for i in lista_simples_inteiro]

print(nova_lista_elegante)