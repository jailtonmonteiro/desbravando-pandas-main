# %%
import pandas as pd
# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
transacoes.groupby(by="IdCliente").count()
# %%
transacoes.groupby(by="IdCliente", as_index=False)[["IdTransacao"]].count()
# %%
summary = (transacoes.groupby(by="IdCliente", as_index=False)
                     .agg({"IdTransacao": ["count"],
                            "QtdePontos": ["sum", "mean"]}))
summary
# %%
summary[("QtdePontos", "mean")]
# %%
summary.columns = ["IdCliente", "qtdeTransacao", "totalPontos", "avgPontos"]
summary