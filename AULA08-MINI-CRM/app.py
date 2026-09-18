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
    leads = control.read_leads() # lista de dicts
    print(f"## | {"Nome":<10} | Email | Status")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<12}   | {lead["email"]} | ")

def search_lead():
    quarry = input("Bucar por: ").strip().lower()
    if not quarry:
        print("Consulta vazia")
        return
    # Chamar o control e passar nossa quarry (Busca)
    # o control irá verificar se existe a quarry no leads.json
    # e irá retornar os resultados da busca ´[]
    found_leads = control.read_leads_search(quarry)
    print(f"## | {"Nome":<10} | Email | Status")
    for i, lead in found_leads:
        print(f"{i:02d} | {lead["name"]:<12}   | {lead["email"]} | ")


def export_leads():
    path_csv = control.export_csv()
    if path_csv is None:
        print(" Não foi possível exportar os leads")
    else:
        print(f"\nExportando os leads para {path_csv}")
def main():
    while True:
        print('\n ---------- MINI CRM DE LEADS ---------- ')
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar lead(Nome/e-mail")
        print("[4] Exportar para CSV")
        print("[5] Remover lead")
        print("[0] Sair do Programa")
        print('-' * 40)

        opt = input("\nSelecione a opção desejada: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_lead()
        elif opt == "4":
            export_leads()
        elif opt == "5":
            print("lead removido com sucesso!")
        elif opt == "0":
            print("\nSaindo do Programa")
            break
        else:
            print("\nOpção Invalida, tente novamente!")
if __name__ == '__main__':
    main()
