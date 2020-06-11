#!/usr/bin/env python
# coding: utf-8

# # Análise de Correlação 

# ## Valor dólar e preço edifier w820bt

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[16]:


#Importação dos dados que estão numa planilha excel
dados = pd.read_excel('C:/Users/alexag/Documents/Alex/Cursos/Python/Dados_de_dolar_e_edifier.xlsx')


# In[17]:


#Leitura dos dados pra saber se está tudo ok
dados.head()


# In[18]:


#Declaração das variáveis, referenciando as colunas
mes = dados['Mês']
edifier = dados['Edifier']
dolar = dados['Dólar']


# <b>Variação do preço do headphone</b>

# In[13]:


plt.plot(mes,edifier)
plt.title("Preço do Headphone Edifier a partir de Maio")

plt.xlabel("Data")
plt.ylabel("Preço Edifier")

plt.show()


# Percebemos que o valor do fone cresce de forma consideravel com o tempo, partindo de 300 reais para 420 reais em dois meses.

# <b>Variação do preço do dólar</b>

# In[8]:


plt.plot(mes,dolar)
plt.title("Preço do Dólar a partir de Maio")

plt.xlabel("Data")
plt.ylabel("Preço do Dólar")

plt.show()


# Quanto ao valor do dólar, percebemos que ele cai também de forma considerável, partindo de 5,40 no início de Maio, chegando à aproximadamente 4,97.

# <b>Correlação entre o preço do headphone com o valor do dólar</b>

# In[14]:


plt.scatter(edifier,dolar)
plt.title("Correlação entre o preço do headphone com o valor do dólar")

plt.xlabel("Valor do headphone")
plt.ylabel("Valor do dólar")

plt.show()


# Identificamos que o valor do dólar não tem uma relação com o valor do fone onde percebe-se que o alto custo do fone aconteceu quando o dólar não estava tão alto, na casa de R$ 5,4.

# In[58]:


eixox = dados['Mês']
eixoy_1 = dados['Edifier']
eixoy_2 = dados['Dólar']

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel("Data")
ax1.set_ylabel('Preço do Headphone', color=color1)
ax1.plot(eixox, eixoy_1, color=color1)


#instancia o segundo eixo com o mesmo eixo x
ax2 = ax1.twinx() 

color = 'tab:blue'
ax2.set_ylabel('Valor do Dólar', color=color)
ax2.plot(eixox, eixoy_2, color=color)


plt.show()


# Aqui percebemos melhor o quanto os valores inverteram ao longo do tempo, onde o preço do headphone cresce e o valor do dólar cai.

# A conclusão é que o valor do headphone edifier w820bt não variou de preço de acordo com o valor do dólar, sendo esse não tendo influência no seu preço.
# Sendo assim, outros fatores podem ter ocasionados o aumento do preço do headphone.
