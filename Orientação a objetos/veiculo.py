import abc, interface_veiculo

class Veiculo(interface_veiculo.Interface_veiculo, abc.ABC):
    """Essa é classe Carro. Esta classe é utilizada para instaciar novos carros"""
    def __init__(self, cor, tipo_combustivel, potencia):
        self.__cor = cor
        #self.qtd_portas = qd_portas
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0

    def __del__(self):
        print(f"Objeto removido da memória: {self.__cor}")

    @abc.abstractmethod
    def pintar(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self.__cor

    def abastecer(self, qtd_combustivel):
        """O método recebe como parâmetro combustivel"""
        self._qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            print("O veículo está ligado.")
        else:
            self.__is_ligado = True
            print("O veículo foi ligado.")

    def desligar(self):
        if self.__is_ligado == False:
            print("O veículo está desligado.")
        else:
            self.__is_ligado = False
            print("O veículo foi desligado.")

    def acelerar(self, velocidade=10):
        if self.__is_ligado:
            self.__velocidade += velocidade
            print(f"Velocidade do Carro: {self.__velocidade}")
        else:
            print("O veículo precisa estar ligado para ser acelerado")