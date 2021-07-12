import time
import datetime
import csv
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import math


file='./data/clientes.csv'


# ---- Gerando informações aleatórias de clientes
clientesid, nomes, sobrenomes, datas, enderecos, bairros = list(), list(), list(), list(), list(), list()


def Gerar_Clientes():
    for k in range(1, 11):
        # Gerando o ID
        clientesid.append(f'C{k}')

        # Gerando o nome
        nomes.append(f'Cliente {k}')

        # Gerando o sobrenome
        sobrenomes.append(f'Silva {k}')

        # Gerando datas de nascimento
        start_date = datetime.date(1970, 1, 1)  # Inicio
        end_date = datetime.date(2000, 1, 1)    # Fim
        interval = end_date - start_date        # Amplitude
        days_passed = interval.days             # Quantidade de dias
        # Gerando uma quantidade aleatoria de dias para o nth cliente
        random_number_of_days = random.randrange(days_passed)
        # Definindo a data aleatoria
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        datas.append(random_date)



# Criando o dataframe
def Criar_Dataframe():
    # Definindo o nome dos bairros
    bairros = ['Centro', 'Timbó', 'Caetés Velho', 'Caetés I', 'Caetés II', 'Caetés III', 'Zona Rural', 'Planalto',
               'Pitanga',
               'Fosfato']
    clientes = pd.DataFrame(list(zip(clientesid, nomes, sobrenomes, datas, bairros)), columns=['ClienteId', 'Nome', 'Sobrenome', 'DataNascimento', 'Bairro'])
    return clientes

# Extraindo a idade a partir da data de nascimento - subtrai a data x do dia de hoje e retira o dia/365
def Extrair_Idade(clientes):
    clientes['Idade'] = clientes['DataNascimento'].apply(lambda x: math.ceil((datetime.datetime.now().date() - x).days/365))
    return clientes

# Carregando alguns enderecos aleatórios do projeto de R
def Criar_Enderecos(clientes):
    enderecos = pd.read_csv('D:\\michel\\Universidade\\Mestrado\\disciplina\\repo\\2_VA\\ProjetoFinal/imoveis.csv', encoding='latin-1')

    # Filtrando 10 endereços diferentes em Paulista. Infelizmente todos eles ficam muito longe de Abreu e Lima
    # Talvez eu colete mais dados de Abreu e Lima
    enderecos = enderecos[(enderecos['Estado']=='PE') & (enderecos['Cidade'] == 'Paulista')].dropna()[:10]

    # Adicionando os endereços ao dataframe dos clientes
    clientes[['Endereco', 'lat', 'long']] = enderecos[['Endereco', 'lat', 'long']].values
    return clientes

# Salvando o novo dataset com endereços
def Salvar_Dataframe(clientes, path):
    clientes.to_csv(path, index=False, encoding='latin-1')

# Recarregando o dataset e adicionando informações de contato: Email e Telefone
def Load_Dataframe(path):
    clientes = pd.read_csv('./data/clientes.csv', encoding='latin-1')
    return clientes

# Gerando números de telefones aleatórios:
def Gerar_Contatos(clientes):

    # Gerando telefones
    clientes['Telefone'] = [int('9' + str(np.random.randint(10000000, 99999999))) for k in range(10)]

    # Gerando Emails aleatórios
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    emails = ['gmail.com', 'hotmail.com', 'yahoo.com.br', 'live.com', 'ufrpe.br']
    string = [[alfabeto[np.random.randint(0, len(alfabeto))] for k in range(8)] for l in range(10)]
    for i in range(10):
        string[i] = ''.join(string[i])
        string[i] = string[i] + '@' + emails[np.random.randint(len(emails))]
    clientes['Email'] = string

    # Gerando Sexos
    clientes['Sexo'] = [['F', 'M'][np.random.randint(2)] for h in range(10)]
    return clientes

# Executando o código

Gerar_Clientes()
clientes = Criar_Dataframe()
clientes = Extrair_Idade(clientes)
clientes = Criar_Enderecos(clientes)
clientes = Gerar_Contatos(clientes)
#clientes = Salvar_Dataframe(clientes, file)

print(clientes.head(10))