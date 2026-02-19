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
# Quem teve mais transações de Streak?

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
produtos = pd.read_csv("../data/produtos.csv", sep=";")

cliente_transacao_produto = transacoes.merge(
    right=transacao_produto, 
    how="left", 
    left_on=["IdTransacao"], 
    right_on=["IdTransacao"],
)[["IdTransacao", "IdCliente", "IdProduto"]]

cliente_transacao_produto
# %%
df_full = cliente_transacao_produto.merge(
    right=produtos,
    how='left',
    on=['IdProduto'],
    )

df_full = df_full[df_full["DescNomeProduto"] == "Presença Streak"]

# %%

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)

# %%

produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"]

(transacoes.merge(
    right=transacao_produto, 
    on='IdTransacao',
    ).merge(produtos,
    on=["IdProduto"],
    how="right")
    .groupby(by="IdCliente")["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)
# %%
