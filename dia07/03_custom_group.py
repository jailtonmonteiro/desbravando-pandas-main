# %%
import pandas as pd
import numpy as np
# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
def amp_diff(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media)**2)

def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

idades = pd.Series([42, 7, 65, 19, 34, 58, 27, 71, 14, 50, 22, 9, 39, 60])
amp_diff(idades)
# %%
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
            .agg({
                "IdTransacao": ["count"],
                "QtdePontos": ["sum", "mean", amp_diff],
                "DtCriacao": [life_time]
            }))
# %%
summary.columns = ["IdCliente","qtdeTransaca","totalPontos","mediaPontos","ampDiffPontos","lifeTime"]
summary