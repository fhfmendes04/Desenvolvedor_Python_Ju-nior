lista_simples_inteiro = [1, 2, 3, 8, 14,  4, 5]

meu_iter = iter(lista_simples_inteiro)

#print(next(meu_iter))
#print(next(meu_iter))

#for i in lista_simples_inteiro:
#    print(i)

while True:
    try:
        elemento = next(meu_iter)
        print(elemento)
    except StopIteration:
        break