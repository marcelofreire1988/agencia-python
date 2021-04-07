from conta import ContaCorrente, ContaPoupanca


class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Getter
    @property
    def nome(self):
        return self._nome

    def idade(self):
        return self._idade


class Cliente(Pessoa, ContaCorrente, ContaPoupanca):
    def __init__(self):
        pass
