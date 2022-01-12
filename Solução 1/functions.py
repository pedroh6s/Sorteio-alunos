def lista_chamada(alunos, opcoes):
    """Cria uma lista informando presença ou falta para cada aluno.

    Args:
        alunos (lista): lista com o nome dos alunos da turma.
        opcoes (lista): lista com as opções.

    Retorno:
        [lista]: retorna a lista criada.
    """
    lista_presenca = []
    print(f'{"ALUNO":^40}{"PRESENÇA":^10}')
    for i in alunos:
        while True:
            try:
                print(f'{i:^40}', end='')
                presenca = input('    ')
                if presenca in opcoes:
                    break
                else:
                    print('Digite uma opção válida!')
            except:
                print('Erro!')
        lista_presenca.append(presenca)
    return lista_presenca


def listar_alunos_presentes(alunos, presenca):
    """Cria uma nova lista apenas com os alunos presentes.

    Args:
        alunos (lista): lista com o nome dos alunos da turma.
        presenca (lista): lista com as presenças dos alunos.

    Retorno:
        [lista]: retorna a lista criada.
    """
    alunos_presentes = [nome for nome in alunos if presenca[alunos.index(nome)] == 'P']
    return alunos_presentes


def sortear_aluno(alunos):
    """Sorteia um aluno da lista informada.
    
    Args:
        alunos (lista): lista com o nome dos alunos da turma.
    
    Retorno:
        [string]: retorna o aluno sorteado.
    """
    from random import choice
    import random
    n1 = choice(alunos)
    return n1


def sortear_lista(alunos):
    """Sorteia aleatoriamente os alunos da lista em uma nova ordem.

    Args:
        alunos (lista): lista com o nome dos alunos da turma.

    Retorno:
        [lista]: retorna a lista criada.
    """
    from random import shuffle
    lista = alunos.copy()
    shuffle(lista)
    return lista


def sorteio_duplas(sorteio):
    """Sorteio em pares os alunos da lista.

    Args:
        sorteio (lista): lista com o nome dos alunos da turma.
    """
    for i in sorteio:
        if sorteio.index(i) % 2 == 0:
            print(f'{i} Vs ', end='')
        else:
            print(f'''{i}
            ''')


def print_sorteio(sorteio):
    """Imprime em pares todos os alunos da lista informada.

    Args:
        lista_sorteio (lista): lista com o nome dos alunos da turma.
    """
    if len(sorteio) % 2 == 0:
        sorteio_duplas(sorteio)
    else:
        from random import choice
        lista = sorteio.copy()
        aluno = choice(lista)
        lista.remove(aluno)
        sorteio_duplas(lista)
        print(f'''O aluno {aluno} ficou sem dupla
        ''')

