def menu(opcao):
    print('------------------------------------\n')

    print(' [1] Adicionar uma tarefa')
    print(' [2] Listar todas as tarefas')
    print(' [3] Remover a última tarefa')
    print(' [4] Desfazer a remoção da última tarefa')
    print(' [5] Sair\n')

    print('------------------------------------\n')

# ADICIONAR TAREFA NO ARQUIVO
def adicionar_tarefa(input_tarefa):
    with open('tarefas.txt', 'a') as file:
        file.write(f'[TAREFA]: [{input_tarefa}]\n')
        file.close()

# LISTAR TAREFAS ADICIONADAS ANTERIORMENTE
def listar_tarefas():
    with open('tarefas.txt', 'r') as file:
        file.seek(0)
        print(file.read())
        file.close()


# DELETAR ULTIMA TAREFA ADICIONADA
def deleta_tarefa():
    # BACKUP DO ARQUIVO DE TAREFAS ATUAL
    with open('tarefas.txt', 'r') as file_1, open('tarefas_bkp.txt', 'w') as file_2:
        for i in file_1:
            file_2.writelines(i)
            print()

    # LEITURA E ESCRITA REMOVENDO A ÚLTIMA TAREFA
    with open('tarefas_bkp.txt') as tasks:
        tasks = tasks.readlines()
    with open('tarefas.txt', 'w') as file:
        file.writelines(tasks[:-1])

# DESFAZER ÚLTIMA TAREFA (RETORNAR O ÚLTIMO ITEM REMOVIDO)
def desfaz():
    with open('tarefas_bkp.txt', 'r') as file_2:
        ultima_tarefa = file_2.readlines()[-1]
    with open('tarefas.txt', 'a') as file_1:
        file_1.writelines(ultima_tarefa)

opcao = '0'
while opcao == '0':
   menu(opcao)
   opcao = input(f'Selecione a opção desejada conforme a lista acima:  \n')

   if opcao == '1':
       while True:
           tarefa = input('Adicione a tarefa desejada:\n')
           adicionar_tarefa(tarefa)
           print(f'Tarefa: [{tarefa}] adicionada com sucesso!\n')
           opcao_2 = input('Deseja adicionar mais uma tarefa? [s/S - Sim] [digite qualquer tecla - Não]\n')
           if opcao_2 == 's' or opcao_2 == 'S':
               continue
           elif opcao_2 != 's' or opcao_2 != 'S':
               opcao = '0'
               break
               menu(opcao)

   elif opcao == '2':
       while True:
           listar_tarefas()
           opcao = '0'
           break
           menu(opcao)

   elif opcao == '3':
       while True:
           deleta_tarefa()
           opcao = '0'
           break
           menu(opcao)

   elif opcao == '4':
       while True:
           desfaz()
           opcao = '0'
           break
           menu(opcao)

   elif opcao == '5':
       break


