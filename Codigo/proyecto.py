'''
Proyecto final de Programcion de lenguajes estadisticos
'''
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
#Primer Punto

#segundo punto
Datos = pd.read_excel("PrecioExternoAnualCivil.xlsx")
column = Datos.columns[0]
column2 = Datos.columns[1]
column3 = Datos.columns[2]
column4 = Datos.columns[3]
column6 = Datos.columns[5]

print("----")

Lista1 = []
Lista2 = []
Lista3 = []
Lista4 = []
Lista5 = []
Lista6 = []
for index, row in Datos.iterrows():
    Lista1.append(row[column])
    Lista2.append(row[column2])
    Lista3.append(str(row[column3]))
    Lista4.append(row[column4])
    

fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('PRECIO ANUAL CIVIL')
#Colocamos una etiqueta en el eje X
ax.set_title('Año')
plt.bar(Lista1, Lista2)
plt.savefig('punto2_A.png')
plt.show()

fig, at = plt.subplots()
#Colocamos una etiqueta en el eje Y
at.set_ylabel('PRECIO ANUAL CAFETERO')
#Colocamos una etiqueta en el eje X
at.set_title('Año')
plt.bar(Lista3, Lista4)
plt.savefig('punto2_b.png')
plt.show()
#tercer punto
Precio = pd.read_excel("Precios.xlsx")#lectura del doc
Ano_c =Precio.columns[0]
valor = Precio.columns[3]
ano_Calendario = []
Valores_decada1=[]
for index, row in Precio.iterrows():
    ano_Calendario.append(row[Ano_c])
    if float(row[Ano_c]) > 2000 and float(row[Ano_c])<2011:
        Valores_decada1.append(row[valor])
ano_Calendario =list( map(int, ano_Calendario))

Valor_ano_estandar =[]
Valores_decada2=[]
for index, row in Precio.iterrows():
    Valor_ano_estandar.append(row[valor])
    if float(row[Ano_c]) > 2010 and float(row[Ano_c])<2021:
        Valores_decada2.append(row[valor])
fig, hist = plt.subplots()
#Colocamos una etiqueta en el eje Y
hist.set_ylabel('PRECIOS ESTANDARIZADOS AL DÍA DE HOY')
#Colocamos una etiqueta en el eje X
hist.set_title('AÑOS')
plt.bar(ano_Calendario,Valor_ano_estandar)
plt.savefig('punto3.png')
plt.show()
#cuarto punto
ano1=" Decada 2001-2010 "
ano2=" Decada 2011-2020 "
Valores_decada1_1 = np.mean(Valores_decada1)
print(Valores_decada1_1)
Valores_decada2_1 = np.mean(Valores_decada2)
print(Valores_decada2_1)
fig, hist1 = plt.subplots()
#Colocamos una etiqueta en el eje Y
hist1.set_ylabel('PRECIOS ESTANDARIZADOS AL DÍA DE HOY')
#Colocamos una etiqueta en el eje X
hist1.set_title('Decada 2001-2010 vs Decada 2011-2020')
plt.bar(ano1,Valores_decada1_1)
plt.bar(ano2,Valores_decada2_1)
plt.savefig('punto4.png')
plt.show()


#quinto punto

df = pd.read_excel("df.xlsx")#lectura del doc
df.keys()
df.plot('Años',"Totalvolumen",kind="scatter")
plt.savefig('punto5_1.png')
df.plot('Preciomensual',"Totalvolumen",kind="scatter")
plt.savefig('punto5_2.png')
#Correlación
matriz_de_correlacion = df.corr()
matriz_de_correlacion
sns.heatmap(matriz_de_correlacion,square=True)
plt.savefig('punto5_2.png')
#sexto punto
