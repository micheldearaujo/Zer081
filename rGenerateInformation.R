
# Generating fake data to amaze Zer081

library(tidyverse)

clientes <- rep('Cliente', 10)
clientes <- paste(clientes, c(1:10), sep=' ')


produtos <- rep('Produto', 5)
produtos <- paste(produtos, c(1:5), sep=' ')
valores <- sample.int(n=50, size=5)
custos <- sample.int(n=30, size=5)

enderecos <- rep('Endereco', 10)
enderecos <- paste(enderecos, c(1:10), sep = ' ')

quantidades <- sample.int(5, 5, replace=T)

pagamentos <- c('Debito', 'Credito', 'Dinheiro')

modalidades <- c('Delivery', 'Retirada', 'Local')


df <- data.frame(Data = as.POSIXlt("2021-06-20 18:00:00") + rnorm(1000, 0, 432000),
                 Produto = sample(produtos, size=100, replace=T),
                 Quantidade = sample(quantidades, size=100, replace=T),
                 Custo = sample(custos, size=100, replace=T),
                 Valor = sample(valores, size=100, replace=T),
                 Cliente = sample(clientes, size=100, replace=T),
                 Endereco = sample(enderecos, size=100, replace=T),
                 Pagamento = sample(pagamentos, size=100, replace=T),
                 Modalidade = sample(modalidades, size=100, replace=T))

df <- mutate(df, Total = Valor*Quantidade, Liquido = (Valor-Custo)*Quantidade)

View(df)
names(df)
# Salvado os dados brutos
write.csv(df, 'vendas_081.csv', row.names=F)


