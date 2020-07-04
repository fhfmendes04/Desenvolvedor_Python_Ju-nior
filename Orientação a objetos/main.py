import carro, moto, veiculo, pessoa

uno_vermelho = carro.Carro("vermelho","Flex", 1.0, 4)
uno_vermelho.ligar()

#uno_vermelho.qtd_combustivel = 200

uno_vermelho.abastecer(30)

uno_vermelho.pintar("preto")
print(uno_vermelho.cor)
#print(uno_vermelho.cor()) sem @property

#print(f"A quantidade de combustível do carro é: {uno_vermelho.qtd_combustivel}")

moto_vermelha = moto.Moto("vermelha", "Gasolina", 1.0, 2)
moto_vermelha.pintar("azul")
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)


#uno_veiculo = veiculo.Veiculo("vermelho","Flex", 1.0)
#uno_veiculo.ligar()


#help(uno_vermelho.abastecer)

#help(carro.Carro)

if isinstance(moto_vermelha, veiculo.Veiculo):
    print("A classe é um veículo")
else:
    print("A classe não é um veículo")

pessoa_sp = pessoa.Pessoa("Fábio")
if isinstance(pessoa_sp, veiculo.Veiculo):
    print("A classe é um veículo")
else:
    print("A classe não é um veículo")
