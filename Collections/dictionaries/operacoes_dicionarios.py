meu_dicionario = {1:'Fabio', 2: "Maria", 3:"Joao", 4: "Jose"}

#get()
print(meu_dicionario.get(2))
print(meu_dicionario[2])

#len()
print(len(meu_dicionario))

# pop()
meu_dicionario.pop(2)
print(meu_dicionario)

# clear()
meu_dicionario.clear()
print(meu_dicionario)

meu_dicionario_2 = {1:'Fabio', 2: "Maria", 3:"Joao", 4: "Jose"}

#keys
print(meu_dicionario_2.keys())

# adicionando elementos
meu_dicionario[5] = 'Joaquina'
meu_dicionario.update({1: 'Mendes'})
print(meu_dicionario)
