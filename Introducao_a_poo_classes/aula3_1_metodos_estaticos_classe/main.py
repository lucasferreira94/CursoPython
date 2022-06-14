# Tech With TIM >> ClassMethod and StaticMethod: https://www.youtube.com/watch?v=pUGyU-hxw5E

class Person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):                # É UM METODO QUE NÃO PRECISA DE UM PARAMETRO PARA FUNCIONAR. É SEMELHANTE A UMA FUNÇÃO DEF COMUM
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')


#  INSTANCE METHOD
newPerson = Person('Lucas', 18)  # CRIAMOS UM OBJETO E CHAMAMOS A CLASSE PASSANDO OS PARÂMETROS
print(newPerson.display())

# CLASS METHOD
print(Person.getPopulation())    # CHAMAMOS A CLASSE SEM CRIAR UM OBJETO PARA UTILIZAR ESSE MÉTODO PORQUE É UM "CLASSMETHOD"

# STATIC METHOD
print(Person.isAdult(15))
print(Person.isAdult(20))