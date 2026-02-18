# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%
transacoes.merge(
    right=clientes,
    how='left',
    on=['IdCliente'],
    suffixes=["Transacao","Cliente"]
    )
# %%
df_1 = pd.DataFrame({
    "trasacao":[1,2,3,4,5],
    "idCliente":[1,2,3,2,2],
    "valor":[10,45,32,17,87],
})

df_2 = pd.DataFrame({
    "id":[1,2,3,4],
    "nome":["que","jota","ka","te"],
})
# %%
df_1.merge(
    right=df_2, 
    how="inner", 
    left_on=["idCliente"], 
    right_on=["id"]
)
# %%
