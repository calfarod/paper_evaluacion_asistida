# Rediseño de la Evaluación Universitaria mediante Inteligencia Artificial Generativa: Optimización del Feedback Formativo y Eficiencia Docente en la Enseñanza de Investigación de Mercados

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.es)
[![License: MIT](https://img.shields.io/badge/Code_License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Research](https://img.shields.io/badge/Status-Active_Research-blue.svg)](#)

---

## 📌 Descripción del Proyecto

Este repositorio alberga el trabajo de investigación, datos anonimizados, instrumentos de medición y flujos de trabajo metodológicos vinculados al proyecto **"Rediseño de la Evaluación Universitaria mediante Inteligencia Artificial Generativa"**. 

La investigación analiza la implementación de un modelo evaluativo sumativo y formativo asistido por el modelo de IA Generativa Gemini en la asignatura de **Investigación de Mercados**. El procedimiento integra la generación automatizada de preguntas de alta complejidad cognitiva, el establecimiento de pautas de "Respuesta Perfecta" y el procesamiento automatizado de informes en formato digital para entregar retroalimentación formativa cualitativa personalizada de 600 caracteres.

```text
  +-------------------------------------------------------------+
  | 1. Provisión de Material y Generación de Preguntas          |
  +-------------------------------------------------------------+
                                |
                                v
  +-------------------------------------------------------------+
  | 2. Construcción del Estándar ("Respuesta Perfecta")         |
  +-------------------------------------------------------------+
                                |
                                v
  +-------------------------------------------------------------+
  | 3. Aplicación Digital (Word) y Recepción de Entregas        |
  +-------------------------------------------------------------+
                                |
                                v
  +-------------------------------------------------------------+
  | 4. Procesamiento Asistido por IAG y Generación de Feedback  |
  +-------------------------------------------------------------+
                                |
                                v
  +-------------------------------------------------------------+
  | 5. Conversión a Escala 1-7 y Registro Institucional         |
  +-------------------------------------------------------------+

```

# 🎯 Objetivos de la InvestigaciónEficiencia Temporal: 

Cuantificar la reducción de la carga operacional docente en el proceso de corrección y feedback de evaluaciones de desarrollo (alcanzando un 82% de ahorro de tiempo).   Evaluación de Impacto Formativo: Analizar el rendimiento académico alcanzado por los estudiantes (promedio del 89,2% de logro).   Validación del Constructo PEA-IA: Medir la percepción del estudiante mediante un cuestionario multidimensional estructurado en torno a 5 dimensiones (Utilidad del Feedback, Justicia Evaluativa, Eficiencia Operativa, Legitimidad y Rol Docente, y Confianza en la IA).

📁 Estructura del Repositorio
```Plaintext
.
├── paper/
│   ├── paper_evaluacion_asistida.docx     # Manuscrito principal del paper
│   └── figura_proceso_evaluativo.png      # Diagrama del flujo metodológico
├── instrument/
│   ├── cuestionario_PEA_IA.md             # Instrumento de medición (Rama A y Rama B)
│   └── ficha_tecnica_instrumento.md       # Caracterización metodológica y escalas
├── data/
│   ├── datos_evaluacion_anonimizados.csv  # Matriz de rendimiento académico (N=10)
│   └── respuestas_cuestionario_pea_ia.csv # Respuestas recabadas de la percepción
├── scripts/
│   ├── recodificacion_items_inversos.py   # Script de tratamiento de preguntas inversas (6 - X)
│   └── analisis_eficiencia_tiempo.py     # Cálculos comparativos de carga horaria
├── LICENSE                                # Archivo de licencias (CC BY-NC 4.0 / MIT)
└── README.md                              # Presentación general del proyecto

```

# 📐 Constructo Teórico e Instrumento (PEA-IA)

El cuestionario PEA-IA (Percepción del Estudiante sobre la Evaluación Asistida por IA) utiliza una escala Likert de 5 puntos y se bifurca mediante una pregunta filtro ($P0.1$):   

**Rama A (Evaluados):** Mide la experiencia real en 5 dimensiones (incluyendo el análisis de posible menosprecio al docente en la Dimensión 4 mediante ítems inversos)[cite: 4].

**Rama B (No Evaluados):** Diagnostica motivos de no participación y explora expectativas/sesgos previos[cite: 4].

## Tratamiento de Ítems Inversos

Para los ítems redactados en sentido inverso (ej. ítems 9 y 11), se aplica la regla de transformación previa al análisis multivariado[cite: 4]:

> **Puntaje Recodificado = 6 - Puntaje Original**


# 👤 Autoría y Filiación
Autor Principal: Prof. Carlos Alfonso Alfaro Díaz
Rol: Profesor Universitario / Consultor en Desarrollo Digital y Analítica
Institución / Afiliación: Universidad Santo Tomás / CAAD Consulting
Ubicación: Iquique, Tarapacá, Chile
Contacto: calfarod@gmail.com

# 📖 Cita / Citation
Si utilizas esta metodología, el cuestionario PEA-IA o los datos de este repositorio en tus investigaciones o innovaciones docentes, por favor cita este trabajo como:

Fragmento de código
@misc{alfaro2026rediseno,
  author       = {Alfaro D'iaz, Carlos Alfonso},
  title        = {Redise\~no de la Evaluaci\'on Universitaria mediante Inteligencia Artificial Generativa: Optimizaci\'on del Feedback Formativo y Eficiencia Docente en la Ense\~nanza de Investigaci\'on de Mercados},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {[https://doi.org/10.5281/zenodo.XXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXX)}
}

# 📄 Licencia
Este repositorio se distribuye bajo un esquema dual de licenciamiento:

Contenido Académico, Documentos, Cuestionarios y Datos: Licenciado bajo Creative Commons Atribución-NoComercial 4.0 Internacional (CC BY-NC 4.0).

Permitido: Copiar, redistribuir, mezclar, transformar y crear a partir del material en cualquier medio o formato.

Condiciones: Debe dar el crédito correspondiente (autoría), proporcionar un enlace a la licencia e indicar si se realizaron cambios. No puede hacer uso del material con fines comerciales.

scripts, código fuente todos los derechos reservados Carlos Alfonso Alfaro Díaz