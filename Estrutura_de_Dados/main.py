from listas import lista_ligada, lista_duplamente_ligada
from vetores import vetor
from pilhas import pilha
from filas import fila

from array import array

#vetores_inteiros = array('b', [1,2,3])

#print(vetores_inteiros)

#vetores_inteiros.insert(3, 4)

#print(vetores_inteiros)

#print(vetores_inteiros.index(2))


print(30*"-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")
print("3. Listas Duplamente Ligadas ")
print("4. Pilhas")
print("5. Filas")

menu = int(input("Digite a 1opção do Menu: "))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)
    vetor_teste.inserir_elemento_posicao(3, 2)
    vetor_teste.inserir_elemento_posicao(4, 2)

    #vetor_teste.inserir_elemento_final(1)
    #vetor_teste.inserir_elemento_final(2)
    #vetor_teste.inserir_elemento_final(3)
    vetor_teste.inserir_elemento_final(5)

    print(vetor_teste)

    #print(vetor_teste.listar_elemento(0))
    #print(vetor_teste.listar_elemento(1))
    #print(vetor_teste.listar_elemento(2))
    #print(vetor_teste.listar_elemento(3))

    #vetor_teste.remover_elemento_posicao(1)
    vetor_teste.remover_elemento(7)
    print(vetor_teste.tamanho_vetor())
    print(vetor_teste)

    #print(vetor_teste.contem(2))
    #print(vetor_teste.indice(2))
elif menu == 2:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2,10)
    print(lista_teste)
    #print(lista_teste.contem(4))
    #print(lista_teste.indice(7))
    #print(lista_teste.recuperar_elemento_no(3))
    #lista_teste.remover_posicao(1)

    lista_teste.remover_elemento(15)
    print(lista_teste)

elif menu == 3:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2,10)
    print(lista_teste)
    #print(lista_teste.contem(4))
    #print(lista_teste.indice(7))
    #print(lista_teste.recuperar_elemento_no(3))
    #lista_teste.remover_posicao(3)

    lista_teste.remover_elemento(15)
    print(lista_teste)

elif menu == 4:
    pilha_teste = pilha.Pilha()
    pilha_teste.empilhar(5)
    pilha_teste.empilhar(6)
    pilha_teste.empilhar(7)
    print(pilha_teste.desempilhar())

elif menu == 5:
    fila_teste = fila.Fila()
    fila_teste.enfileirar(1)
    fila_teste.enfileirar(2)
    fila_teste.enfileirar(3)
    print(fila_teste)

    fila_teste.desenfileirar()
    print(fila_teste)

else:
    print("Opção inválida")

