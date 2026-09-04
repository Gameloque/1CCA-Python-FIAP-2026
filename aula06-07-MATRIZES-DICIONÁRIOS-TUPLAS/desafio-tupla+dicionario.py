#O programa deve:
#▪ Criar uma tupla com todos os nomes de usuário e exibir o primeiro e o último.
#▪ Trocar a ordem do primeiro e último nome de usuário usando atribuição de tupla (sem variável temporária).
#▪ Exibir o relatório final, por exemplo:
#▪ Relatório:
#▪ Quantidade de e-mails por domínio:
#▪ fiap.com.br: 3
#▪ Lista de usuários: ('ana.paula', 'joao.silva', 'maria.souza')
#▪ Após troca de posições: ('maria.souza', 'joao.silva', 'ana.paula')

# 1. Criar a tupla com todos os nomes de usuário
tupla_nomes = ('ana.paula', 'joao.silva', 'maria.souza')

# Exibir o primeiro e o último
print(f"Primeiro usuário: {tupla_nomes[0]}")
print(f"Último usuário: {tupla_nomes[-1]}")
print("-" * 30)

# 2. Trocar a ordem do primeiro e do último usando atribuição (via conversão para lista)
lista_nomes = list(tupla_nomes)
lista_nomes[0], lista_nomes[-1] = lista_nomes[-1], lista_nomes[0]
tupla_apos_troca = tuple(lista_nomes)


print("\nE-mails criados:")
for usuario in tupla_nomes:
    # Junta o nome do usuário com o domínio
    email = f"{usuario}@fiap.com.br"
    print(f"▪ {email}")

print(f"\n▪ Lista de usuários original: {tupla_nomes}")
print(f"▪ Após troca de posições: {tupla_apos_troca}")

# 3. Exibir o relatório final
print("Relatório:")
print(f"Quantidade de e-mails por domínio: {len(tupla_nomes)}")
for usuario in tupla_nomes:
    # Junta o nome do usuário com o domínio
    email = f"{usuario}@fiap.com.br"
    print(f"▪ {email}")
print(f"▪ Lista de usuários: {tupla_nomes}")
print(f"▪ Após troca de posições: {tupla_apos_troca}")
