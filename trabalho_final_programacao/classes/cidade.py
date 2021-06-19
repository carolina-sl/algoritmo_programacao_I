from classes.estado import Estado


class Cidade:
    nome: str
    qt_casos: int
    estado: Estado

    def __init__(self, nome):
        self.nome = nome
        self.qt_casos = 0
        self.estado = None  # vai receber a classe Estado

    def __str__(self):
        return '--> ' + self.nome + '......... - Casos Registrados: ' + str(self.qt_casos) + \
               ' - Estado: ' + str(self.estado.sigla)

    def setEstado(self, estado):
        self.estado = estado

    def adicionar_casos(self, novos_casos):
        self.qt_casos += novos_casos
        self.estado.adicionar_casos(novos_casos)


