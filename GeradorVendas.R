
# Gerando um dataset de Vendas de Produtos do Zer081.
# Estes dados deverão conter apenas um dataset aleatório de Vendas!
# O dataset gerado aleatório das informações dos clientes é feito no Python.

library(tidyverse)
library(lubridate)

vendas <- read.csv('data/vendas_081.csv')
clientes <- read.csv('data/clientes.csv')
View(clientes)

# Definindo a quantidade total de vendas
n.vendas <- 3650

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

valores <- runif(n=n.produtos, min=5, max=30)
custos <- runif(n=n.produtos, min=1, max=10)


# Agora o endereço é uma informação definida já do cliente. Dessa forma, precisaremos importar o endereços
# dos clientes que já foram feitos em Python.
clients <- read.csv('./data/clientes.csv')
View(clientes)

enderecos <- clients$Endereco
#enderecos <- rep('Endereco', 10)
#enderecos <- paste(enderecos, c(1:10), sep = ' ')

# Definindo a quantidade de itens comprada no momento
#quantidades <- sample.int(5, n.produtos, replace=T)

x <- seq(1, n.vendas, 1)
quantidades <- round(1.5*sin(x/20) + 2.5 + runif(n=n.vendas, min = 0, max=2))

# Definindo os meios de pagamento
pagamentos <- c('Debito', 'Credito', 'Dinheiro')

# Definindo os meios de entrega
modalidades <- c('Delivery', 'Retirada', 'Local')

# Gerando 3 2 anos de datas a partir de 2021/01/01 - 2023/01/01

datas <- vector()
contador <- 1

for (day in 1:730){
  datas[day] <- as.Date(contador, origin="1970-01-01")
  contador <- contador + 1
}
datas <- as.Date(datas, origin='2021-01-01')


# Juntando todas as informações em um dataframe
vendas <- data.frame(Data = datas,
                 Produto = sample(produtos, size=n.vendas, replace=T),
                 Quantidade = quantidades,
                 #Custo = custos,
                 #Valor = valores,
                 Custo = sample(custos, size=n.vendas, replace=T),
                 Valor = sample(valores, size=n.vendas, replace=T),
                 Cliente = sample(clientes, size=n.vendas, replace=T),
                 Endereco = sample(enderecos, size=n.vendas, replace=T),
                 Pagamento = sample(pagamentos, size=n.vendas, replace=T),
                 Modalidade = sample(modalidades, size=n.vendas, replace=T))

vendas <- mutate(vendas, Total = Valor*Quantidade, Liquido = (Valor-Custo)*Quantidade)
View(vendas)

# Salvado os dados brutos
write.csv(vendas, './data/vendas_081.csv', row.names=F)

plot(as.Date(vendas$Data[0:365]), vendas$Quantidade[0:365], type='o',
     xlab='Mês',
     ylab='Quantidade de items')


plot(as.Date(vendas$Data[0:365]), vendas$Valor[0:365], type='o')
hist(vendas$Liquido)
