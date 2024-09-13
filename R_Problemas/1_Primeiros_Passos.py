# 1. Processamento dos Dados

## 1° Leitura e Processamento dos dados
dados_contatos = [
    "João Silva;28;joao.silva@gmail.com;São Paulo",
    "Maria Oliveira;35;maria.oliveira@gmail.com;Rio de Janeiro",
    "Carlos Pereira;22;carlos.pereira@outlook.com;São Paulo",
    "Ana Costa;30;ana.costa@yahoo.com;Belo Horizonte"
]

## 2° Armazenamento das Informações
contatos = []

for i in dados_contatos:
   dado = i.split(';')
   contatos.append({
      'nome': dado[0],
      'idade': int(dado[1]),
      'email': dado[2],
      'cidade': dado[3]
   })
   print(f"Dados de {dado[0]} adicionado. ")

# 2. Análise de Dados

## 1° Listagem de Dados

nomes = []

for i in contatos:
   nomes.append(i['nome'])
   print(f"{i['nome']} adicionado a lista!")
nomes

## 2° Extração de Domínios de E-mail

dominios = []

for contato in contatos:
    dominio = contato['email'].split('@')[1]  
    dominios.append(dominio) 
    print(f"Dominio {dominio} adicionado à lista!")

print("Lista de domínios:", dominios)

## 3° Filtragem por Cidade

clientes_sao_paulo = []

for contato in contatos:
    if contato['cidade'] == 'São Paulo':
        clientes_sao_paulo.append(contato['nome'])

print(f"Clientes que moram em São Paulo: {clientes_sao_paulo[0]} e {clientes_sao_paulo[1]}")

## 4° Manipulação de Strings

def extrair_nome_e_dominio(email):
    for contato in contatos:
        if contato['email'] == email:
            nome = contato['nome']  
            dominio = email.split('@')[1]  
            return nome, dominio
    return "Email não encontrado!"   

extrair_nome_e_dominio("joao.silva@gmail.com")
