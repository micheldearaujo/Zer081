import time
import datetime
import csv
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import math

# ---- Gerando informações aleatórias de clientes
# clientesid, nomes, sobrenomes, datas, enderecos, bairros = list(), list(), list(), list(), list(), list()
#
# for k in range(1, 11):
#     clientesid.append(f'C{k}')
#     nomes.append(f'Cliente {k}')
#     sobrenomes.append(f'Silva {k}')
#
#     start_date = datetime.date(1970, 1, 1)
#     end_date = datetime.date(2000, 1, 1)
#     interval = end_date - start_date
#     days_passed = interval.days
#     random_number_of_days = random.randrange(days_passed)
#     random_date = start_date + datetime.timedelta(days=random_number_of_days)
#     datas.append(random_date)
#
# bairros = ['Centro', 'Timbó', 'Caetés Velho', 'Caetés I', 'Caetés II', 'Caetés III', 'Zona Rural', 'Planalto', 'Pitanga',
#            'Fosfato']
#
# data = np.array([clientesid, nomes, sobrenomes, datas, bairros])
# clientes = pd.DataFrame(data.transpose(), columns=['ClienteId', 'Nome', 'Sobrenome', 'DataNascimento', 'Bairro'])
#
# # Extraindo a idade a partir da data de nascimento
# clientes['Idade'] = clientes['DataNascimento'].apply(lambda x: math.ceil((datetime.datetime.now().date() - x).days/365))
#

clientes = pd.read_csv('./data/clientes.csv', encoding='latin-1')
# Carregando alguns enderecos aleatórios do projeto de R
enderecos = pd.read_csv('D:\\michel\\Universidade\\Mestrado\\disciplina\\repo\\2_VA\\ProjetoFinal/imoveis.csv', encoding='latin-1')

# Filtrando 10 endereços diferentes em Paulista. Infelizmente todos eles ficam muito longe de Abreu e Lima
# Talvez eu colete mais dados de Abreu e Lima
enderecos = enderecos[(enderecos['Estado']=='PE') & (enderecos['Cidade'] == 'Paulista')].dropna()[:10]

# Adicionando os endereços ao dataframe dos clientes
clientes[['Endereco', 'lat', 'long']] = enderecos[['Endereco', 'lat', 'long']].values

# Salvando o novo dataset com endereços
clientes.to_csv('./data/clientes.csv', index=False, encoding='latin-1')


# Recarregando o dataset e adicionando informações de contato: Email e Telefone
clientes = pd.read_csv('./data/clientes.csv', encoding='latin-1')

# Gerando números de telefones aleatórios:
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

# Salvando o novo dataset
clientes.to_csv('./data/clientes.csv', index=False, encoding='latin-1')
clientes.to_excel('./data/clientes2.xlsx', index=False, encoding='latin-1')