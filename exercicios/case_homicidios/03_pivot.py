# %%
import pandas as pd

df = pd.read_csv("homicidios_consolidados.csv", sep=";")

# %%
df_stack = (df.set_index(["nome", "período"])
              .stack()
              .reset_index()
)
df_stack.columns = ["nome", "período", "metrica", "valor"]
df_stack
# %%
(df_stack.pivot_table(values="valor",
                     index=["nome", "período"],
                     columns="metrica")
                     .reset_index()
)
# %%
df_stack.pivot_table(values="valor",
                     index=["nome"],
                     columns="metrica",
                     aggfunc="mean")


# %%
