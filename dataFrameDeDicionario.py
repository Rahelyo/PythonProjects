import pandas as pd

dados = {
    "Nome": ["Ana","Bruno","Carlos"],
    "Idade": [30, 22, 28],
    "Cidade": ["Fortaleza","São Paulo","Salvador"]
}
df = pd.DataFrame(dados)
print(df)
print(df.head())
print(df.describe())
print(df["Nome"])
print(df["Idade"] > 25)

df["Profissao"] = ["Engenheira","Designer","Medico"]

nova_pessoa = pd.DataFrame([{
    "Nome": "Daniela",
    "Idade": 30,
    "Cidade": "Recife",
    "Profissao": "Advogada"
}])

df = pd.concat([df, nova_pessoa], ignore_index=True)
print(df)

df.to_csv("pessoas.csv", index=False)
print("Arquivo salvo com sucesso!")

df_carregando = pd.read_csv("pessoas.csv")