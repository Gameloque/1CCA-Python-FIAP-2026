from model import model_lead
import control


def add_lead():
    name = input("\nInforme o nome do Lead: ")
    email = input("\nInforme o email do Lead: ")
    status = input("\nInforme o status do Lead: ")
    # validar os dados
    print("\nNome do Lead: ", name)
    print("Email do Lead: ", email)
    print("Status do Lead: ", status)
    #depois de validar
    #preciso modelar eles né (model.py)
    print(model_lead(name, email, status))
    # Depois de modelar, precisa enviar para o leads.json
    # o control.py irá auxiliar a enviar os dados para o json
    control.create_lead(model_lead(name, email, status))
    # Resolver o do pq não tá salvando no json
    print("\nLead Adicionado com Sucesso!")


def list_leads():
    leads = control.read_leads()
    print(leads)
    # Printar como uma tabela/painel2
def main():
    while True:
        print('\n ---------- MINI CRM DE LEADS ---------- ')
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Remover lead")
        print("[0] Sair do Programa")
        print('-' * 40)

        opt = input("\nSelecione a opção desejada: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            print("\nLead Removido")
        elif opt == "0":
            print("\nSaindo do Programa")
            break
        else:
            print("\nOpção Invalida, tente novamente!")
if __name__ == '__main__':
    main()
