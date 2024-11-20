import pandas as pd
import scipy.stats as stats
# %%
# Cargar el archivo CSV
archivo_csv = 'heart.csv'      # Defino el nombre del archivo con datos que voy a leer
df = pd.read_csv(archivo_csv)  # Leo datos usando librería Pandas
# %%

# Crear un diccionario para almacenar los resultados
resultados = {}

# Calcular promedio, desviación estándar, mediana y moda para cada columna
for columna in df.columns:
    if pd.api.types.is_numeric_dtype(df[columna]):
        promedio = df[columna].mean()
        desviacion_estandar = df[columna].std()
        mediana = df[columna].median()
        moda = df[columna].mode()[0] if not df[columna].mode().empty else None

        resultados[columna] = {
            'Promedio': promedio,
            'Desviación Estándar': desviacion_estandar,
            'Mediana': mediana,
            'Moda': moda
        }

# Imprimir los resultados
for columna, stats in resultados.items():
    print(f"Columna: {columna}")
    print(f"  Promedio: {stats['Promedio']}")
    print(f"  Desviación Estándar: {stats['Desviación Estándar']}")
    print(f"  Mediana: {stats['Mediana']}")
    print(f"  Moda: {stats['Moda']}")
    print()


##########################historygram

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo_csv = 'heart.csv'
df = pd.read_csv(archivo_csv)

# Dibujar histogramas para cada columna numérica
for columna in df.columns:
    if pd.api.types.is_numeric_dtype(df[columna]):
        plt.figure(figsize=(10, 6))
        plt.hist(df[columna], bins=30, edgecolor='k', alpha=0.7)
        plt.title(f'Histograma de {columna}')
        plt.xlabel(columna)
        plt.ylabel('Frecuencia')
        plt.grid(True)
        plt.show()
        


##########################Scatter plots
import pandas as pd
import matplotlib.pyplot as plt
import itertools

# Cargar el archivo CSV
archivo_csv = 'heart.csv'
df = pd.read_csv(archivo_csv)

# Obtener las columnas numéricas
columnas_numericas = df.select_dtypes(include='number').columns

# Crear scatter plots para cada par de columnas numéricas
for col1, col2 in itertools.combinations(columnas_numericas, 2):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[col1], df[col2], alpha=0.7)
    plt.title(f'Scatter Plot: {col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.grid(True)
    plt.show()


######################3 box_plots
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo_csv = 'heart.csv'
df = pd.read_csv(archivo_csv)

# Identificar la columna categórica y las columnas numéricas
columna_categorica = 'GENERO'  # Cambia esto por el nombre real de tu columna categórica
columnas_numericas = df.select_dtypes(include='number').columns

# Crear box plots para la columna categórica versus cada columna numérica
for columna in columnas_numericas:
    plt.figure(figsize=(10, 6))
    df.boxplot(column=columna, by=columna_categorica)
    plt.title(f'{columna} por {columna_categorica}')
    plt.suptitle('')  # Elimina el título por defecto de pandas
    plt.xlabel(columna_categorica)
    plt.ylabel(columna)
    plt.grid(True)
    plt.show()


#########################################scatter plot category
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
archivo_csv = 'heart.csv'
df = pd.read_csv(archivo_csv)

# Identificar la columna categórica y las columnas numéricas
columna_categorica = 'GENERO'  # Cambia esto por el nombre real de tu columna categórica
columnas_numericas = df.select_dtypes(include='number').columns

# Crear scatter plots para la columna categórica versus cada columna numérica
for columna in columnas_numericas:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=columna, y=columna_categorica, hue=columna_categorica, palette='Set1')
    plt.title(f'Scatter Plot: {columna} vs {columna_categorica}')
    plt.xlabel(columna)
    plt.ylabel(columna_categorica)
    plt.legend(title=columna_categorica)
    plt.grid(True)
    plt.show()
    
################################# frec-table
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo_csv = 'heart.csv'
df = pd.read_csv(archivo_csv)

# Identificar la columna categórica
columna_categorica = 'GENERO'  # Cambia esto por el nombre real de tu columna categórica

# Crear la tabla de frecuencias
tabla_frecuencias = df[columna_categorica].value_counts().reset_index()
tabla_frecuencias.columns = [columna_categorica, 'Frecuencia']

# Imprimir la tabla de frecuencias
print(tabla_frecuencias)

# Crear un gráfico de barras para la tabla de frecuencias
plt.figure(figsize=(10, 6))
plt.bar(tabla_frecuencias[columna_categorica], tabla_frecuencias['Frecuencia'], color='skyblue')
plt.title(f'Tabla de Frecuencias de {columna_categorica}')
plt.xlabel(columna_categorica)
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

################################33-scatter category
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import seaborn as sns
print(sns.__version__)

# Leer el archivo CSV
df = pd.read_csv('heart.csv')

# Scatter plot: Weight vs Length1, coloreado por Species 
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='EDAD', y='ENFERMEDAD CARDIACA', hue='GENERO', palette='viridis')
plt.xlabel('Edad')
plt.ylabel('ENFERMEDAD CARDIACA')
plt.title('Scatter Plot of EDAD vs ENFERMEDAD CARDIACA for heart GENERO')
plt.legend(title='Genero')
plt.show()

# Pair plot: Relaciones entre todas las variables numéricas, coloreado por Species
sns.pairplot(df, hue='GENERO', palette='viridis')
plt.suptitle('Pair Plot of Persona Measurements by GENERO', y=1.02)
plt.show()




