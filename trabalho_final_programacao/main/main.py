from classes.estado import Estado
from classes.cidade import Cidade
import csv

# =================================================================
# LISTAS


list_estado = []

list_cidade = []

# =================================================================

# FUNÇÕES


def buscar_estado(sigla_estado):
    for estado in list_estado:
        if estado.sigla.upper() == sigla_estado.upper():
            return estado

    return None


def carregar_estados():
    # print(__file__)
    str_caminho_raiz = str(__file__).replace('main/main.py', '')
    # print(str_caminho_raiz)
    reader = csv.reader(open(str_caminho_raiz + 'arquivos/estados.csv', 'r'), delimiter=";")
    next(reader, None)  # skip primeira linha
    for row in reader:
        # print('Estado:', row[0], 'Sigla:', row[1])
        list_estado.append(Estado(row[0], row[1]))


def carregar_cidades():
    str_caminho_raiz = str(__file__).replace('main/main.py', '')

    reader = csv.reader(open(str_caminho_raiz + 'arquivos/cidades.csv', 'r'), delimiter=";")

    next(reader, None)  # skip primeira linha
    for linha_cidade in reader:

        # buscar o estado da cidade da lista
        estado = buscar_estado(linha_cidade[1])

        # instanciar a variavel cidade
        cidade = Cidade(nome=linha_cidade[0])

        # setar o estado da cidade
        cidade.setEstado(estado)

        # apendar a cidade na lista
        list_cidade.append(cidade)


# ======================================================================================================

def cad_estado():
    """
    Cadastra o Estado e a sigla do Estado e adiciona na lista [list_estado]
    :return:
    """

    print(' ## CADASTRO DE ESTADO ## ')
    nome_estado = input('Digite o Estado que deseja cadastrar: ').upper()
    sigla = input('Digite a sigla do Estado: ').upper()

    for est in list_estado:
        if est.nome_estado.upper() == nome_estado:
            print(' ===== Estado já cadastrado. ==== ')
            return True
        if est.sigla.upper() == sigla:
            print('===== Sigla já cadastrada. ====')
            return True

    list_estado.append(Estado(nome_estado.upper(), sigla))
    return False


def relatorio_estados():
    """
    Imprime um relatório dos estados cadastrados
    :return:
    """
    print(' ## RELATÓRIO DOS ESTADOS ## ')
    for estado in list_estado:
        print(estado) # imprime o bjeto


def cad_cidade():  # aqui vai se vincular a classe cidade com a classe estado:
    """
    Cadastra as cidades e adiciona na lista [list_cidades]
    :return:
    """

    print(' ## CADASTRO DE CIDADE ## ')
    nome = input('Digite o nome da cidade: ').upper()

    for cid in list_cidade:
        if cid.nome.upper() == nome:
            print(' ===== Cidade já cadastrada. ====')
            return True

    estados_cadastrados()
    escolha_estado = input('Escolha um estado: ').upper()
    estado_escolhido = None

    # Busca o estado pelo atributo [sigla]
    estado_escolhido = buscar_estado(escolha_estado)

    if estado_escolhido is None:
        print('Estado não cadastrado!')
        return False

    # vincula o estado à cidade
    nova_cidade = Cidade(nome)
    nova_cidade.setEstado(estado_escolhido)

    # adiciona a cidade na lista
    list_cidade.append(nova_cidade)


def relatorio_cidades():
    """
    Imprime um relatório de cidades cadastradas
    :return:
    """
    print(' ## RELATÓRIO DAS CIDADES ## ')
    for cidade in list_cidade:
        print(cidade) # imprime o objeto


def estados_cadastrados():
    """
    Imprime um relatório de estados, pela sigla
    :return:
    """
    print('## ESTADOS CADASTRADOS: ##')
    for estado in list_estado:
        print('>>>>>', estado.sigla) # imprime o atributo [sigla]


def atualizar_casos():
    """
    Atualiza a quantidade de casos na classe cidade
    :return:
    """

    print(' ## ATUALIZAR OS DADOS DA CIDADE: ##')
    print('Selecione uma cidade pelo indice: ')
    for ind, cid in enumerate(list_cidade):
        print('[', ind, '] - ', cid.nome)

    ind_escolha = int(input('Escolha uma opção pelo indice entre colchetes: '))

    for ind, cid in enumerate(list_cidade):
        if ind == ind_escolha:
            print('Quantidade atual: ', cid.qt_casos)
            qtd_novos_casos = int(input('Digite a quantidade de novos casos: '))
            if qtd_novos_casos < 0:
                print(' ..... A capacidade não pode ser negativa, digite novamente.')
                return True

            cid.adicionar_casos(qtd_novos_casos)
            return False


# =================================================================
# PROGRAMA PRINCIPAL


if __name__ == '__main__':
    carregar_estados()
    carregar_cidades()

    while True:
        escolha = input('''MENU
        0 - Finalizar o programa:
        1 - Cadastrar Estados:
        2 - Cadastrar Cidades:
        3 - Relatórios de Estados
        4 - Relatório de cidades:
        5 - Atualizar número de casos:
        Escolha: ''')

        if escolha not in ('0', '1', '2', '3', '4', '5'):
            print(' >>>> Opção inválida. Digite uma das opções do menu.')

        if escolha == "0":
            print('Saindo do programa...')
            break
        if escolha == "1":
            cad_estado()
        if escolha == "2":
            cad_cidade()
        if escolha == "3":
            relatorio_estados()
        if escolha == "4":
            relatorio_cidades()
        if escolha == "5":
            atualizar_casos()

