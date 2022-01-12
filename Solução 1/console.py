import functions
import menus


#Lista dos alunos
turma_1 = ['aluno 1', 'aluno 2', 'aluno 3', 'aluno 4', 'aluno 5',
          'aluno 6', 'aluno 7', 'aluno 8', 'aluno 9', 'aluno 10']
turma_2 = ['aluno 1', 'aluno 2', 'aluno 3', 'aluno 4', 'aluno 5',
          'aluno 6', 'aluno 7', 'aluno 8', 'aluno 9']
lista_presenca = []


#Listas dos menus e opções
lista_menu = ( 'ESCOLHER TURMA', 'LISTA DE CHAMADA', 'SORTEAR TURMA', 'SORTEIO SIMPLES', 'SAIR')
lista_turmas = ['TURMA 1', 'TURMA 2']
turmas = [turma_1, turma_2]
options_presenca = ['P', 'F']


print('Seja bem vindo!')

#ABRE O MENU ESCOLHER TURMA
menus.titulo(lista_menu[0])
turma_escolhida = menus.submenu(lista_turmas, turmas)
print(turma_escolhida)
#ABRE O MENU LISTA DE CHAMADA
menus.titulo(lista_menu[1])
lista_presenca = functions.lista_chamada(turma_escolhida, options_presenca)
alunos_presentes = functions.listar_alunos_presentes(turma_escolhida, lista_presenca)
#ABRE O MENU PRINCIPAL

while True:
    menus.linhas_sleep(1, 1)
    option = menus.menu(lista_menu)
    menus.sleep_linhas(1, 1)
    if option == 1:
        menus.titulo(lista_menu[0])
        turma_escolhida = menus.submenu(lista_turmas, turmas)
        print(turma_escolhida)
    elif option == 2:
        menus.titulo(lista_menu[1])
        lista_presenca = functions.lista_chamada(turma_escolhida, options_presenca)
        alunos_presentes = functions.listar_alunos_presentes(turma_escolhida, lista_presenca)
    elif option == 3:
        menus.titulo(lista_menu[2])
        sorteio = functions.sortear_lista(alunos_presentes)
        functions.print_sorteio(sorteio)
    elif option == 4:
        menus.titulo(lista_menu[3])
        print(f'O aluno sorteado foi: {functions.sortear_aluno(alunos_presentes)}')
    elif option == 5:
        menus.titulo(lista_menu[4])
        break
    else:
        print('Digite uma opção válida do menu!')
print('Tchau.')
