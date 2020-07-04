import abc

class Interface_veiculo(abc.ABC):
    @abc.abstractmethod
    def abastecer(self, qtd_combustivel):
        pass #nenhum tipo de implemetação

    @abc.abstractmethod
    def ligar(self):
        pass
    @abc.abstractmethod
    def desligar(self):
        pass

    @abc.abstractmethod
    def acelerar(self, velocidade=10):
        pass

    @abc.abstractmethod
    def pintar(self, cor):
        pass