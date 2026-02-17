# %%
import pandas as pd

idades = [42, 7, 65, 19, 34, 58, 3, 27, 71, 14, 50, 22, 9, 39, 60]
idades = pd.Series(idades)
idades
# %%
idades.describe()
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes
# %%
clientes["flTwitch"].sum()
# %%
redes_sociais =["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
clientes[redes_sociais].mean()
# %%
num_columns = clientes.dtypes[~(clientes.dtypes == "str")].index.tolist()
clientes[num_columns].describe()
# %%
