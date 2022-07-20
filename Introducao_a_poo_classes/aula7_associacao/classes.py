class Escritor:
    def __init__(self, nome):
        self.__nome = nome  # ATRIBUTO PRIVADO QUE NÃO ESTÁ ACESSÍVEL FORA DA CLASSE

    @property               # GETTER PARA SER POSSÍVEL UTILIZAR O METODO FORA DA CLASSE
    def nome(self):
        return self.__nome