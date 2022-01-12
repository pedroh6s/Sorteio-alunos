def titulo(msg):
    """Imprime uma mensagem em caixa alta, centralizado em 50 caracteres.

    Args:
        msg (string): mensagem para imprimir.
    """
    print(f'{msg:-^50}'.upper())
    print()


def linhas_sleep(linhas, segundos):
    """Imprime uma quantidade de linhas vazias e aguarda uma quantidade de segundos.

    Args:
        linhas (integer): quantidade de linhas.
        segundos (integer): quantidade de segundos.
    """
    from time import sleep
    for c in range (0, linhas):
        print()
    sleep(segundos)


def sleep_linhas(segundos, linhas):
    """Aguarda uma quantidade de segundos e imprime uma quantidade de linhas vazias.

    Args:
        segundos (integer): quantidade de segundos.
        linhas (integer): quantidade de linhas.
    """
    from time import sleep
    sleep(segundos)
    for c in range (0, linhas):
        print()


def menu(opcoes):
    """Imprime um menu com base em uma lista, recebe um integer como input e o retorna.

    Args:
        opcoes (lista): lista com as opções do menu.

    Returns:
        [integer]: o número da opção desejada.
    """
    print('''Escolha a opção desejada: 
    ''')
    for i in opcoes:
        print(f'[{opcoes.index(i)+1}] {i}')
    print('''
    Sua opção: ''', end='')
    while True:
        try:
            option = int(input())
            break
        except:
            print('Digite um número!', end=' ')
    return option


def submenu(opcoes, turmas):
    """Imprime um menu com base em uma lista, recebe um integer como input e o retorna.

    Args:
        opcoes (lista): lista com as opções do menu.

    Returns:
        [integer]: o número da opção desejada.
    """
    print('''Escolha a opção desejada: 
    ''')
    for i in opcoes:
        print(f'[{opcoes.index(i)+1}] {i}')
    print('''
    Sua opção: ''', end='')
    while True:
        try:
            option = int(input())
            break
        except:
            print('Digite um número!', end=' ')
    return turmas[option - 1]


