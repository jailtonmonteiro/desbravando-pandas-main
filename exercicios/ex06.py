# %%
import pandas as pd
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%
# Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?

redes_sociais =["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
clientes[redes_sociais].describe()
# %%
#Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.groupby(by="IdCliente")[["IdTransacao"]].count().sort_values(by="IdTransacao", ascending=False).head(10)
# %%
# Qual usuário teve maior quantidade de pontos debitados?
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
produtos = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacoes
produtos
(transacoes.merge(
    right=produtos, 
    how="inner", 
    left_on=["IdTransacao"], 
    right_on=["IdTransacao"]
).groupby(by='IdCliente')[["vlProduto"]]
    .sum()
    .sort_values(by="vlProduto")
    .head(1))
# %%
