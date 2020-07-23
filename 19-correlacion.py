import pandas as pd
import matplotlib.pyplot as plt
datos=pd.read_csv("data.csv")	

datos['health'].fillna(0,inplace=True)

df1=datos.loc[datos['school']=='GP']
df2=datos.loc[datos['school']=='MS']

cnt=len(df1[(df1['absences']>10)&(df1['failures']>2)])#si no utilizas len, te regresa un dataframe
print("Numero de casos:",cnt)
print('*'*20)
print(df1.loc[(df1['absences']>10)&(df1['failures']>2),('health','sex')])
print('*'*20)
x=df1[(df1['absences']>10)&(df1['failures']>2)].count()['failures']#otra forma de saber el numero de resultados
print(x)

print('*'*20)
print(df1[df1['age']>20].iloc[0]['guardian'])#con iloc te devuelve solamente el primer renglon
print('*'*20)
print("correlacion entre el tiempo de estudio y materias reprobadas")
print(df1['studytime'].corr(df1['failures']))

print('*'*20)

"""print('Indica las variables a correlacionar')
var1=input("variable 1")
var2=input("variable 2")
print(df1[var1].corr(df1[var2]))"""

dic={"Muy bajo":1, 'Bajo':2, 'Medio':3, 'Alto':4, 'Muy alto':5}
df1.Dalc.value_counts().plot(kind='pie',labels=None,autopct='%1.2f%%',shadow=True,startangle=180,fontsize=12,pctdistance=1.1,labeldistance=1.4)
plt.title("Consumo de alcohol")
plt.legend(loc="best",labels=dic)
plt.ylabel('')
plt.axis('equal')
#plt.show()
import seaborn as sns
sns.set(style='ticks',color_codes=True)
nuevo=datos[['G1','G2','G3']].copy()
g=sns.pairplot(nuevo,kind='reg')
plt.show()
