tarefas = []

while True:

    print("n\---Menu To-Do List---")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

    escolha = input("Escolha uma opção: (1, 2, 3, 4): ")
    
    if escolha == "1":
        if not tarefas:
            print("Você não tem tarefas na lista")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f" {i + 1}. {tarefa}")

    elif escolha == "2":
        nova_tarefa = input("Digite a descrição da nova tarefa: ")
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{nova_tarefa}'adicionada com sucesso!")
    
    elif escolha == "3":
        print("\n----Remover tarefa----")
        if not tarefas:
            print("Você não tem tarefas para remover")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f" {i + 1}. {tarefa}")

            try:
                indice_str = input("Digite o número da tarefa que deseja remover: ")
                indice_str = int(indice_str) -1

                tarefa_removida = tarefas.pop(indice_str)

                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            except ValueError:
                print("Erro: Digite um número válido")
            except IndexError:
                print("Erro: o número da tarefa não está na lista")                


    elif escolha == "4":
        print("\n[Ação] - Obrigado por usar o To-Do List!")
        break
    else:
        print("\n[Ação] - Opção inválida! Tente novamente.")