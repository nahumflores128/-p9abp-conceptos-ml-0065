# Nahum flores NC 0065
import pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
datos21 = {
    'distancia_km': [2.2, 4.6, 1.6, 5.3, 3.7],
    'trafico_nivel': [2, 1, 3, 2, 1],
    'edad_repartidor': [26, 35, 24, 41, 30],
    'tiempo_entrega_min': [18, 32, 15, 45, 25]
}

df = pd.DataFrame(datos21)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("Nahum flores NC 0065")


# Nahum Flores NC 0065
import pandas as pd

# 1. Crear un dataset de ejemplo similar al planteamiento del hospital
datos = {
    'id_paciente': [101, 102, 103, 104, 105],
    'edad': [45, 23, 60, 35, 50],
    'nivel_glucosa': [140, 85, 180, 95, 130],
    'presion_arterial': [80, 70, 90, 75, 85],
    'indice_masa_corporal': [28.5, 21.0, 33.2, 24.1, 29.8],
    'diagnostico_diabetes': [1, 0, 1, 0, 1]  # Target (1: Sí, 0: No)
}

df = pd.DataFrame(datos)

# 2. Eliminar la columna no útil ('id_paciente')
df_limpio = df.drop(columns=['id_paciente'])

# 3. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df_limpio[['edad', 'nivel_glucosa', 'presion_arterial', 'indice_masa_corporal']]  # Features / Entradas
y = df_limpio['diagnostico_diabetes']                                                  # Target / Salida

# 4. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
print("Nahum flores NC 0065")
