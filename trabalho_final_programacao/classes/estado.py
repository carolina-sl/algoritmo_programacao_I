class Estado:
    nome_estado: str
    sigla: str
    pais: str
    qt_estado: int

    def __init__(self, nome_estado, sigla):
        self.nome_estado = nome_estado
        self.sigla = sigla
        self.pais = 'Brasil'
        self.qtd_estado = 0  # é a soma dos qt_casos da classe Cidade

    def __str__(self):
        return '> ' + self.nome_estado + '.............. - total de casos: ' + str(self.qtd_estado) + ' - País: ' + self.pais

    def adicionar_casos(self, novos_casos):
        self.qtd_estado += novos_casos




