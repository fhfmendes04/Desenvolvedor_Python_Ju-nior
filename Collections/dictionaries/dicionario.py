meu_dicionario = {1:'Fabio', 2: "Maria", 3:"Joao", 4: "Jose"}
print(meu_dicionario)
print(type(meu_dicionario))

meu_dicionario_2 = dict({1:'Fabio', 2: "Maria", 3:"Joao", 4: "Jose"})

print(meu_dicionario[1])
print(meu_dicionario[4])

for chave, valor in meu_dicionario.items():
    print(f"chave: {chave} e o valor: {valor}")


