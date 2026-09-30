# Exploratory Data Analisys
# Profesor: Carlos Alfaro Díaz

# Para que Python funcione tendremos que construir un 'Virtual Environment' .venv
# Para que Python funcione tendremos que instalar 'Dependencias'
# Para instalar las 'Dependencias' de una sola vez el analista contruye un archivo 'requirements.txt'
# El archivo 'requeriments.txt' contiene el nombre de todas las dependencias que se deben instalar.

# Determinar cuál el el vínculo al archivo planilla google con los datos, lo llamaremos link
link = "https://docs.google.com/spreadsheets/d/1d00npDQFBoya7pS5SO6G79A9g3ub3pc_iDzBAdB_TUg/edit?usp=sharing"

# Construiremos un dataframe con todos los valores en 12 filas y 23 columnas
# En las columnas 11, 13, 19 los indicadores están invertidos hay que rectificar 

# Existen dos 'Constructos Separados', 
# 1ro el constructo para los que sí realizaron la evaluación
# 2do el constructo para los que no realizaron la evaluación

# Construiremos un data frame para el constructo 1
# Construiremos un data frame para el constructo 2

# Determinamos las estadísticas a realizar
# Determinamos las gráficas a construir

# En esta zona se realizará el llamado a las 'Dependecias'
import pandas as pd
import numpy as np
import pingouin as pg
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


# URL modificada para exportación directa a CSV
# link = "https://docs.google.com/spreadsheets/d/1d00npDQFBoya7pS5SO6G79A9g3ub3pc_iDzBAdB_TUg/edit?usp=sharing"
# url  = "https://docs.google.com/spreadsheets/d/1d00npDQFBoya7pS5SO6G79A9g3ub3pc_iDzBAdB_TUg/export?format=csv"

url = "https://docs.google.com/spreadsheets/d/1d00npDQFBoya7pS5SO6G79A9g3ub3pc_iDzBAdB_TUg/export?format=csv"

# Crear el DataFrame base 'golden_df'
golden_df = pd.read_csv(url)

# Verificar los datos cargados
# print(golden_df.head(1))
# print(golden_df.info())

# Deseo un ditionary de encabezados del golden_df
# Muestra en consola el diccionario con formato listo para renombrar
print("column_mapping = {")
for col in golden_df.columns:
    print(f"    '{col}': '{col}',")
print("}")

# Copiar y renombrar
column_mapping = {
    'Marca temporal': 'timestamp',
    'P0.1. ¿Rindió usted la Evaluación 1 de Ayudantía y recibió la retroalimentación cualitativa correspondiente?': 'P0_e1rendida',
    'La retroalimentación de 600 caracteres que recibí por correo fue lo suficientemente específica para entender mis errores técnicos.  ': 'AD1_entender_error',
    'Los comentarios recibidos me permitieron identificar con claridad las brechas entre mi respuesta y la respuesta perfecta esperada. ': 'AD1_identific_brecha',
    'El feedback que recibí aporta más a mi aprendizaje que solo haber conocido la nota final numérica. ': 'AD1_aporta_aprendizaje',
    'Siento que mis respuestas fueron evaluadas con el mismo estándar de exigencia que las de mis compañeros (imparcialidad). ': 'AD2_imparcial',
    'Considero que la evaluación fue objetiva y basada estrictamente en los contenidos teóricos abordados en la asignatura.': 'AD2_objetiva',
    'La pauta de "Respuesta Perfecta" me pareció un criterio claro y transparente para juzgar el desempeño.': 'AD2_transparente',
    'El tiempo transcurrido entre la entrega de mi trabajo y la recepción del resultado/retroalimentación fue óptimo.': 'AD3_tiempo',
    'El uso del formato digital (Word) facilitó la claridad y lectura de mis respuestas en comparación con una prueba en papel.': 'AD3_legibilidad',
    'Siento que el uso de Inteligencia Artificial para apoyar la evaluación reduce el esfuerzo o compromiso del profesor hacia el curso.-': 'AD4N_mayor_compromiso',
    'Reconozco que el profesor mantiene el control técnico y la autoridad académica sobre la calificación final recibida.': 'AD4_mayor_controltecnico',
    'Percibo que el profesor delega en la máquina la tarea que debería hacer él manualmente.-': 'AD4N_no_revision_manual',
    'Considero que un docente que domina e integra la IA en sus evaluaciones muestra mayor innovación y competencias profesionales.': 'AD4_mayor_innovacion',
    'Me siento cómodo(a) sabiendo que el profesor utiliza herramientas de IA para apoyar el proceso de revisión.': 'AD5_comodidad',
    'Preferiría que las próximas evaluaciones de desarrollo sigan utilizando este sistema de retroalimentación asistido por IA.': 'AD5_seguir_usando',
    'Considero que recibir una retroalimentación escrita detallada de 600 caracteres sería útil para entender mis errores en las evaluaciones de desarrollo. ': 'BD1_util_mejor_retralim',
    'Creo que el uso de un formato digital (Word) facilitaría la entrega y corrección de mis trabajos en comparación con el papel. ': 'BD1_mejor_correccion',
    'Me preocupa que el uso de IA por parte del profesor reduzca la dedicación o el compromiso hacia la corrección de nuestros trabajos.-': 'BD2N_mayor_compromiso',
    'Considero que el profesor debe mantener siempre el control técnico y la revisión final sobre las notas asignadas por una IA. ': 'BD2_mayor_controltecnico',
    'Valoro positivamente que un docente incorpore tecnologías avanzadas de IA para innovar en sus métodos de enseñanza y evaluación. ': 'BD2_mayor_innovacion',
    'Me gustaría participar en las próximas evaluaciones del curso bajo esta modalidad de revisión asistida por IA. ': 'BD3_deseo_revision_asistida',
    'Confío en que un sistema supervisado por el profesor puede ser imparcial y justo al corregir trabajos escritos. ': 'BD3_confio_revision_asistida',
}

# Aplicar el renombrado en el mismo DataFrame (inplace=True)
work_df = golden_df
work_df.rename(columns=column_mapping, inplace=True)

print("☄️work_df info\n")
work_df.info()

# 4. Verificar el resultado
print("🐲--- Nuevos nombres de columnas ---")
print(work_df.columns.tolist())

print("\n🐈--- Vista previa con las columnas renombradas ---")
print(work_df[['timestamp', 'P0_e1rendida']].head())

# Muestra en consola el diccionario con nombre de columnas de work_df
print("💕")
print("column_mapping2 = {")
for col in work_df.columns:
    print(f"    '{col}',")
print("}")

# imprimir algunas columnas para revisarlas
columnas_interes = [
    'AD4N_mayor_compromiso',
    'AD4N_no_revision_manual',
    'BD2N_mayor_compromiso'
]

print("\n☄️ Columnas de interés por tener valores invertidos")
print(work_df[columnas_interes])

# Cambia los valores de columnas invertidas
posiciones = [10, 12, 18]

# Aplica la fórmula sobre las columnas especificadas (0-indexado)
work_df.iloc[:, posiciones] = 6 - work_df.iloc[:, posiciones]

# imprimir algunas columnas para revisarlas
print("🍢 Estado de las columnas de interés")

# imprimir algunas columnas para revisarlas
columnas_interes = [
    'AD4N_mayor_compromiso',
    'AD4N_no_revision_manual',
    'BD2N_mayor_compromiso'
]

print(work_df[columnas_interes])

# Cambiar columna P0_e1rendida a si y no
# imprimir algunas columnas para revisarlas
print("🍅 Estado inicial de P0_e1rendida")
print(work_df["P0_e1rendida"])

# Posición 1 (segunda columna)
# Si el valor es exacto a 'No', asigna 'no'. De lo contrario, asigna 'si'.
# import numpy as np 
work_df.iloc[:, 1] = np.where(work_df.iloc[:, 1] == 'No', 'no', 'si')

# Ordenar todo el work_df según la columna P0_e1rendida
# Orden ascendente (de A a Z / de menor a mayor)
# work_df = work_df.sort_values(by='P0_e1rendida', ascending=False).reset_index(drop=True)
work_df = work_df.sort_values(by='P0_e1rendida').reset_index(drop=True)

print("🧩 Salida")
print(work_df["P0_e1rendida"])

# Exporta a CSV usando utf-8-sig para que Excel reconozca correctamente los acentos y la 'ñ'
# work_df.to_csv('revisar_datos.csv', index=False, encoding='utf-8-sig', sep=';')


##################################################
#       A L F A    D E    C R O N B A C H        #
##################################################

# 1. Definir los mapas de dimensiones (ítems por dimensión)
dims_A = {
    'AD1_retralim_util': ['AD1_entender_error', 'AD1_identific_brecha', 'AD1_aporta_aprendizaje'],
    'AD2_evaluac_justa': ['AD2_imparcial', 'AD2_objetiva', 'AD2_transparente'],
    'AD3_revisa_oportuna': ['AD3_tiempo', 'AD3_legibilidad'],
    'AD4_docen_comprometid': ['AD4N_mayor_compromiso', 'AD4_mayor_controltecnico', 'AD4N_no_revision_manual', 'AD4_mayor_innovacion'],
    'AD5_aceptacion': ['AD5_comodidad', 'AD5_seguir_usando']
}

dims_B = {
    'BD1_expectativa': ['BD1_util_mejor_retralim', 'BD1_mejor_correccion'],
    'BD2_docen_comprometid': ['BD2N_mayor_compromiso', 'BD2_mayor_controltecnico', 'BD2_mayor_innovacion'],
    'BD3_confianza': ['BD3_deseo_revision_asistida', 'BD3_confio_revision_asistida']
}

# 2. Filtrar las submuestras df_A y df_B desde work_df
df_A = work_df[work_df['P0_e1rendida'] == 'si']
df_B = work_df[work_df['P0_e1rendida'] == 'no']


# 3. Función para evaluar Consistencia Interna y Validez Convergente sin Warnings
def evaluar_validez_dimensiones(df_grupo, mapa_dimensiones, nombre_grupo):
    print(f"\n==========================================")
    print(f" EVALUACIÓN DE VALIDEZ INTERNA: {nombre_grupo}")
    print(f"==========================================")
    
    resultados = []
    for dim_nombre, cols in mapa_dimensiones.items():
        # Tomar columnas válidas que existan en el DataFrame y tengan respuestas
        cols_reales = [c for c in cols if c in df_grupo.columns and df_grupo[c].notna().sum() > 0]
        
        if len(cols_reales) > 1:
            df_sub = df_grupo[cols_reales].dropna()
            
            if len(df_sub) > 1:
                # Alfa de Cronbach
                alpha, _ = pg.cronbach_alpha(data=df_sub)
                
                # Matriz de correlación
                corr_matrix = df_sub.corr()
                
                # Extraer solo el triángulo superior (excluyendo la diagonal de 1.0)
                mask = np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
                corrs = corr_matrix.where(mask).stack().values
                
                # Filtrar posibles NaNs por varianza cero o constantes
                corrs_validas = corrs[~np.isnan(corrs)]
                
                # Promedio seguro de correlación inter-ítem
                if len(corrs_validas) > 0:
                    avg_corr = np.mean(corrs_validas)
                    str_corr = f"{round(avg_corr, 3)}"
                else:
                    str_corr = "N/A (Varianza 0)"
                
                resultados.append({
                    'Dimensión': dim_nombre,
                    'N° Ítems': len(cols_reales),
                    'Muestra (N)': len(df_sub),
                    'Alfa Cronbach': round(alpha, 3),
                    'Corr. Inter-Ítem Media': str_corr,
                    'Estado Confiabilidad': 'Aceptable' if alpha >= 0.7 else 'Revisar / Bajo'
                })
    
    df_res = pd.DataFrame(resultados)
    print(df_res.to_string(index=False))
    return df_res

# 4. Ejecutar análisis limpio para ambos constructos
res_A = evaluar_validez_dimensiones(df_A, dims_A, "CONSTRUCTO A (Sí rindieron - N=9)")
res_B = evaluar_validez_dimensiones(df_B, dims_B, "CONSTRUCTO B (No rindieron - N=4)")

#####################################################
#       C O M P R O M I S O    D O C E N T E        #
#####################################################

# 1. Calcular el puntaje promedio de compromiso por estudiante
# Constructo A (Sí rindieron, N=9)
items_AD4 = ['AD4N_mayor_compromiso', 'AD4_mayor_controltecnico', 'AD4N_no_revision_manual', 'AD4_mayor_innovacion']
df_A['AD4_promedio'] = df_A[items_AD4].mean(axis=1)

# Constructo B (No rindieron, N=4)
items_BD2 = ['BD2N_mayor_compromiso', 'BD2_mayor_controltecnico', 'BD2_mayor_innovacion']
df_B['BD2_promedio'] = df_B[items_BD2].mean(axis=1)

def probar_compromiso_docente_scipy(series_datos, nombre_grupo, punto_neutro=3.0):
    print(f"\n==========================================")
    print(f" PRUEBA DE HIPÓTESIS (95% CI): {nombre_grupo}")
    print(f"==========================================")
    
    # Prueba t de 1 muestra en SciPy
    stat, p_val = stats.ttest_1samp(series_datos, popmean=punto_neutro, alternative='greater')
    
    media = series_datos.mean()
    std = series_datos.std()
    
    print(f"Muestra (N): {len(series_datos)}")
    print(f"Media observada: {media:.3f} (DE: {std:.3f})")
    print(f"Estadístico t: {stat:.3f}")
    print(f"Valor p (p-value): {p_val:.4f}")
    
    if p_val < 0.05:
        print("✅ CONCLUSIÓN: Se RECHAZA H0. Con un 95% de confianza, el docente SÍ es percibido como comprometido.")
    else:
        print("❌ CONCLUSIÓN: No hay evidencia suficiente para afirmar con 95% de confianza que es percibido como comprometido.")
    
# Ejecutar la prueba estadistica
ttest_A = probar_compromiso_docente_scipy(df_A['AD4_promedio'], "CONSTRUCTO A (Sí rindieron - N=9)")
ttest_B = probar_compromiso_docente_scipy(df_B['BD2_promedio'], "CONSTRUCTO B (No rindieron - N=4)")

# Insertar espacios
print("\n\n")

# GRAFICA DE BARRAS

# Ejemplo con seaborn para promedios por ítem
plt.figure(figsize=(10, 6))
sns.barplot(data=df_A[items_AD4], orient='h', palette='Blues_r', errorbar=None)
plt.axvline(3, color='red', linestyle='--', label='Punto Neutro (3.0)')
plt.title('Percepción de Compromiso Docente (Constructo A - N=9)')
plt.xlim(1, 5)
plt.xlabel('Escala Likert (1 a 5)')
plt.legend()
plt.tight_layout()
plt.show()


# GRAFICA CAJA Y BIGOTES

# Unir datos para gráfico comparativo
df_A_comp = pd.DataFrame({'Grupo': 'Sí rindieron (N=9)', 'Compromiso': df_A['AD4_promedio']})
df_B_comp = pd.DataFrame({'Grupo': 'No rindieron (N=4)', 'Compromiso': df_B['BD2_promedio']})
df_total = pd.concat([df_A_comp, df_B_comp])

plt.figure(figsize=(8, 5))
sns.boxplot(x='Grupo', y='Compromiso', data=df_total, palette='Set2', width=0.4)
sns.stripplot(x='Grupo', y='Compromiso', data=df_total, color='black', jitter=0.2, size=8)

# Línea de referencia del punto neutro de la prueba de hipótesis
plt.axhline(3.0, color='red', linestyle='--', label='Punto Neutro (H0: μ = 3.0)')
plt.ylim(1, 5.5)
plt.title('Comparación de la Percepción del Compromiso Docente')
plt.ylabel('Puntaje Promedio (Escala 1-5)')
plt.legend()
plt.tight_layout()
plt.show()

# GRAFICA RADAR

# Proporción de las 5 dimensiones de A
labels = ['Feedback', 'Justicia', 'Eficiencia', 'Compromiso', 'Aceptación']
valores = [
    df_A[dims_A['AD1_retralim_util']].mean().mean(),
    df_A[dims_A['AD2_evaluac_justa']].mean().mean(),
    df_A[dims_A['AD3_revisa_oportuna']].mean().mean(),
    df_A['AD4_promedio'].mean(),
    df_A[dims_A['AD5_aceptacion']].mean().mean()
]

# Configuración de los ángulos del radar
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
valores += valores[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, valores, color='teal', alpha=0.25)
ax.plot(angles, valores, color='teal', linewidth=2)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_ylim(1, 5)
plt.title('Perfil Multidimensional de Percepción (Grupo Sí Rindió)', y=1.1)
plt.show()