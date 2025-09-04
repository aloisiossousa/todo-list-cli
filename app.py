tarefas = []

while True:

    print("---Menu To-Do List---")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Marcar tarefa como concluida")
    print("5 - Sair")

    escolha = input("Escolha uma opção: (1, 2, 3, 4, 5): ")
    
    if escolha == "1":
        print("\n---Suas tarefas---")
        if not tarefas:
            print("\nVocê não tem tarefas na lista")
        else:
            for i, tarefa in enumerate(tarefas):
                descricao = tarefa["descricao"]
                status = tarefa["status"]
                print(f" {i + 1}. {descricao} - [{status}")

    elif escolha == "2":
        nova_tarefa_desc = input("Digite a descrição da nova tarefa: ")

        nova_tarefa = {
            "descricao": nova_tarefa_desc,
            "status": "pendente"
        }

        tarefas.append(nova_tarefa)
        print(f"Tarefa '{nova_tarefa_desc}' adicionada com sucesso!")
    
    elif escolha == "3":
        print("\n----Remover tarefa----")
        if not tarefas:
            print("Você não tem tarefas para remover")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f" {i + 1}. {tarefa['descricao']} - [{tarefa['status']}]")

            try:
                indice_str = input("Digite o número da tarefa que deseja remover: ")
                indice_str = int(indice_str) -1

                tarefa_removida = tarefas.pop(indice_str)

                print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
            except ValueError:
                print("Erro: Digite um número válido")
            except IndexError:
                print("Erro: o número da tarefa não está na lista")                


    elif escolha == "4":
        print("\n---- Marcar tarefa como concluida ----")

        if not tarefas:
            print("Não há tarefas para marcar")

        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1}. {tarefa['descricao']} [{tarefa['status']}]")


            try:
                indice_str = input("Digite o número da tarefa que deseja marcar como concluida: ")
                indice_str = int(indice_str) -1

                if tarefas[indice_str]['status'] == "Concluido":
                    print("Essa tarefa já foi marcada como concluida.")
                
                else: 
                    tarefas[indice_str]['status'] = "Concluido"
                    print(f"Tarefa '{tarefas[indice_str]['descricao']}' marcada como concluida")

            except ValueError:
                print("Erro: Digite um número válido")
            except IndexError:
                print("Erro: o número da tarefa não está na lista")                


    elif escolha == "5":
        print("\n[Ação] - Obrigado por usar o To-Do List!")
        break
   