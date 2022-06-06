
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


# p2 = Pessoa.por_ano_nascimento('João', 1990)
p2 = Pessoa('João', 30)
print(p2)
print(p2.nome, p2.idade)
p2.get_ano_nascimento()
