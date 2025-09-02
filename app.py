tarefas = []

while True:

    print("n\---Menu To-Do List---")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Sair")

    escolha = input("Escolha uma opção: (1, 2, 3): ")
    
    if escolha == "1":
        if not tarefas:
            print("Você não tem tarefas na lista")
        else:
            for tarefa in tarefas:
                print(f" - {tarefa}")

    elif escolha == "2":
        nova_tarefa = input("Digite a descrição da nova tarefa: ")
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{nova_tarefa}'adicionada com sucesso!")


    elif escolha == "3":
        print("\n[Ação] - Obrigado por usar o To-Do List!")
        break
    else:
        print("\n[Ação] - Opção inválida! Tente novamente.")