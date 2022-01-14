import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC0a2f8b2342cb724b39be8b8b7ab1d18b"
# Your Auth Token from twilio.com/console
auth_token  = "7912ad7b409d5829e06ca5c0aac79f39"
client = Client(account_sid, auth_token)

# Como eu irei fazer a solução

# Abrir os 6 arquivos em exel
listas_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in listas_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5588983",
            from_="+19285648740",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)







# Para cada arquivo:

# Vamos verificar se algum valor na coluna de vendas daquele arquivo é maior que 55.000

# Se for maior que 55.000 -> Enviar um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja, não fazer nada

