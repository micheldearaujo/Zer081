
# Gerando um dataset de Vendas de Produtos do Zer081.
# Estes dados deverão conter apenas um dataset aleatório de Vendas!
# O dataset gerado aleatório das informações dos clientes é feito no Python.

library(tidyverse)
library(lubridate)


# Gerando n clientes
n.clientes <- 10
clientes <- rep('Cliente', 10)
clientes <- paste(clientes, c(1:10), sep=' ')

# Gerando n quantidades de produtos vendidos
n.produtos <- 10
produtos <- rep('Produto', 10)
produtos <- paste(produtos, c(1:n.produtos), sep=' ')

# Gerando n quantidades de valores de produtos e de custos. Nesse caso, aqui é
# ainda a mesma quantidade de produtos, pois estamos criando um banco de dados dos produtos
valores <- sample.int(n=50, size=n.produtos)
custos <- sample.int(n=30, size=n.produtos)

# Agora o endereço é uma informação definida já do cliente. Dessa forma, precisaremos importar o endereços
# dos clientes que já foram feitos em Python.
clients <- read.csv('./data/clientes.csv')
View(clientes)

enderecos <- clients$Endereco
#enderecos <- rep('Endereco', 10)
#enderecos <- paste(enderecos, c(1:10), sep = ' ')

# Definindo a quantidade de itens comprada no momento
quantidades <- sample.int(5, n.produtos, replace=T)

# Definindo os meios de pagamento
pagamentos <- c('Debito', 'Credito', 'Dinheiro')

# Definindo os meios de entrega
modalidades <- c('Delivery', 'Retirada', 'Local')

# Gerando Datas aleatórias. Vou criar um ano inteiro de vendas
n.vendas <- 3650
datas <- as.POSIXlt("2021-01-01 00:00:00") + rnorm(n.vendas, 0, 31536000)

# Juntando todas as informações em um dataframe
df <- data.frame(Data = datas,
                 Produto = sample(produtos, size=n.vendas, replace=T),
                 Quantidade = sample(quantidades, size=n.vendas, replace=T),
                 Custo = sample(custos, size=n.vendas, replace=T),
                 Valor = sample(valores, size=n.vendas, replace=T),
                 Cliente = sample(clientes, size=n.vendas, replace=T),
                 Endereco = sample(enderecos, size=n.vendas, replace=T),
                 Pagamento = sample(pagamentos, size=n.vendas, replace=T),
                 Modalidade = sample(modalidades, size=n.vendas, replace=T))

df <- mutate(df, Total = Valor*Quantidade, Liquido = (Valor-Custo)*Quantidade)

View(df)
names(df)
# Salvado os dados brutos
write.csv(df, 'vendas_081.csv', row.names=F)


vendas <- read.csv('./data/vendas_081.csv')
View(vendas)

plot(vendas$Data, vendas$Quantidade, type='o')
