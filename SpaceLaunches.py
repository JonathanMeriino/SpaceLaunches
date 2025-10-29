import pandas as pd


#Lectura del CSV
df0 = pd.read_csv('SpaceLaunches.csv')

"""Exploracion inicial del dataframe"""

print(df0.columns)
print(df0.head())
df0.info()
print(df0.shape)

#Eliminar columnas inecesarias
df = df0.drop (['Unnamed: 0.1','Unnamed: 0','Detail'], axis=1)

#Renombrar dataset

df.rename(columns={'Company Name': 'company',
                   'Location': 'loc',
                   'Datum': 'date',
                   'Status Rocket': 'rocket_status',
                   ' Rocket':'cost',
                   'Status Mission':'mission_status'
                   }, inplace=True)



#Crear columna con la ubicación del lanzamiento, a partir del centro de lanzamiento
df['launch_location'] = df['loc'].str.split(', ').str[-1]



#Eliminar los caracteres UTC de los registros de fecha
df['date'] = df['date'].str.replace(' UTC', '')

#Debido a que hay formatos combinados en los registros de fecha se crea una función para poder convertirlos a tipo datetime
def date_formator(date):
    if ':' in date:
        return pd.to_datetime(date, format='%a %b %d, %Y %H:%M')
    else:
        return pd.to_datetime(date, format='%a %b %d, %Y')
    
#Aplicar formato a la fecha   
df['date'] = df['date'].apply(date_formator)

#Crear la columa de año y mes
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

#Eliminar columnas inecesarias
df= df.drop(['loc','date'], axis=1)

df.to_excel('SpacheLaunchesProcessed.xlsx')
