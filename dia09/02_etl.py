# %%
import pandas as pd
import sqlalchemy

from sklearn import cluster

# %%
with open("etl.sql") as open_file:
    query = open_file.read()

print(query)
# %%
engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

df = pd.read_sql_query(query, con=engine)
df
# %%
kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[["totalproduct", "qtdTransacoes"]])

df["cluester"] = kmean.labels_
df
# %%
df.to_sql("transacao_cluster",
            con=engine,
            index=False,
            if_exists="replace")
# %%
