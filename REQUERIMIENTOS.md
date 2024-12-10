# Documento de Requerimientos para un Reto Técnico Empresarial basado en Inteligencia Artificial

Este documento detalla los requerimientos para desarrollar y entregar una solución técnica basada en inteligencia artificial que resuelva un problema empresarial específico. La solución debe ser técnicamente sólida, estar alineada con los objetivos de negocio y ser escalable, garantizando su aplicabilidad en un entorno real. Además, se espera que el proyecto incluya una documentación clara, un código modular y métricas que respalden su impacto en el problema planteado.

## Tabla de Contenidos
1. [Definición y Enfoque del Problema](#1-definición-y-enfoque-del-problema)
    - [Definición Problema](#definición)
    - [Impacto Empresarial](#impacto-empresarial)
2. [Solución Técnica](#2-solución-técnica)
    - [Modelos y Algoritmos](#modelos-y-algoritmos)
    - [Desempeño del Modelo](#desempeño-del-modelo)
    - [Datos](#datos)
        - [Descripción de los Datos](#descripción-de-los-datos)
        - [Preparación y Limpieza de los Datos](#preparación-y-limpieza-de-los-datos)
        - [Ética y Legalidad](#ética-y-legalidad)
3. [Implementación y Escalabilidad](#3-implementación-y-escalabilidad)
    - [Reproducibilidad](#reproducibilidad)
    - [Escalabilidad](#escalabilidad)
    - [Automatización](#automatización)
4. [Entregables](#4-entregables)
    - [Estructura del Proyecto](#estructura-del-proyecto)
        - [Descripción General](#descripción-general)
        - [Estructura de Carpetas](#estructura-de-carpetas)
        - [Archivos Principales](#archivos-principales)
        - [Cómo Ejecutar](#cómo-ejecutar)
        - [Notas Finales](#notas-finales)
    - [Documentación Técnica](#documentación-técnica)
    - [Código y GitHub](#código-y-github)
    - [Presentación](#presentación)
5. [Criterios de Selección](#5-criterios-de-selección)
    - [Claridad y Alineación](#claridad-y-alineación)
    - [Calidad Técnica](#calidad-técnica)
    - [Documentación y Reproducibilidad](#documentación-y-reproducibilidad)
    - [Innovación y Creatividad](#innovación-y-creatividad)
    - [Viabilidad y Escalabilidad](#viabilidad-y-escalabilidad)

---

## 1. Definición y Enfoque del Problema

### Definición
El problema debe estar claramente definido y contextualizado dentro del dominio empresarial relevante, especificando los desafíos y oportunidades que presenta. Se debe detallar el objetivo del proyecto, indicando cómo la solución de inteligencia artificial abordará el problema planteado. Es necesario incluir una sección que describa el impacto esperado de la solución en términos empresariales, como reducción de costos, mejora en la eficiencia operativa o incremento en ingresos.

### Impacto Empresarial
Es necesario cuantificar el impacto potencial de la solución en términos de métricas empresariales clave. Se deben incluir casos de uso específicos que demuestren cómo la solución puede ser aplicada al negocio.

---

## 2. Solución Técnica

### Modelos y Algoritmos
La solución debe incluir una descripción del modelo de IA seleccionado, con justificación técnica que explique por qué es el más adecuado para resolver el problema. Es importante implementar el modelo con una arquitectura clara, alineada con el objetivo empresarial. Se valorará la innovación técnica, ya sea a través de adaptaciones de metodologías existentes o el uso de técnicas avanzadas.

### Desempeño del Modelo
La evaluación del modelo debe incluir métricas relevantes que midan el éxito de la solución en el contexto del problema, como `accuracy`, `precision`, `recall`, `RMSE` u otras específicas del dominio. La solución debe superar benchmarks tradicionales o soluciones anteriores, demostrando una mejora significativa. Es importante garantizar que el modelo sea robusto y capaz de manejar variaciones en los datos de entrada.

### Datos

#### Descripción de los Datos
Los datos utilizados deben ser representativos del problema empresarial y se requiere una descripción detallada de las fuentes de datos, las variables incluidas y su relevancia para el problema.

#### Preparación y Limpieza de los Datos
Los datos utilizados deben ser representativos del problema empresarial y se requiere un preprocesamiento adecuado, incluyendo la eliminación de valores atípicos, imputación de datos faltantes y normalización o estandarización de variables. La selección de características debe estar alineada con los objetivos del modelo, identificando variables clave que aporten al desempeño.

#### Ética y Legalidad
Los datos utilizados deben cumplir con las regulaciones de privacidad y protección de datos aplicables, como `GDPR` u otras normativas relevantes. Es necesario documentar cómo se abordaron posibles sesgos en los datos y garantizar que la solución sea equitativa y no discriminatoria.

---

## 3. Implementación y Escalabilidad

### Reproducibilidad
El código entregado debe ser modular y estar bien documentado, con scripts separados para tareas como preprocesamiento, entrenamiento y evaluación del modelo. El repositorio debe incluir un archivo `README` con instrucciones detalladas para reproducir la solución.

### Escalabilidad
La solución debe ser capaz de manejar grandes volúmenes de datos de manera eficiente, considerando estrategias de optimización para modelos y procesamiento de datos. Se debe incluir un plan o prototipo de despliegue, como una API o contenedor Docker, que permita su implementación en un entorno empresarial.

### Automatización
La solución debe incorporar pasos automatizados para el pipeline de datos y el ciclo de vida del modelo, incluyendo la actualización de datos, el entrenamiento y la evaluación.

---

## 4. Entregables

### Estructura del Proyecto

#### Descripción General
Este proyecto está diseñado para resolver un problema técnico empresarial utilizando técnicas de Inteligencia Artificial. La estructura facilita la organización de datos, scripts, modelos y resultados para asegurar un flujo de trabajo eficiente y reproducible.
#### Estructura de Carpetas

```
Reto_Tecnico_IA/
│
├── .venv/              # Entorno virtual para las dependencias del proyecto
├── data/               # Carpeta para almacenar datos sin procesar y procesados
├── notebooks/          # Carpeta para notebooks exploratorios
├── src/                # Carpeta para scripts principales
│   ├── main.py         # Script principal para ejecutar el pipeline
│   ├── preprocessing.py # Script para limpieza y preprocesamiento de datos
│   ├── training.py     # Script para entrenar el modelo
│   ├── evaluation.py   # Script para evaluar el modelo
├── models/             # Carpeta para almacenar los modelos entrenados
├── outputs/            # Carpeta para los resultados y visualizaciones
├── kerastuner/         # Carpeta para almacenar configuraciones y resultados de Keras Tuner
├── tensorboard/        # Carpeta para almacenar logs de TensorBoard
├── .env                # Archivo para secretos y credenciales
├── .gitignore          # Archivo para ignorar archivos y carpetas en Git
├── README.md           # Documentación del proyecto
├── requirements.txt    # Lista de dependencias del proyecto
```

#### Archivos Principales

##### 1. **`src/main.py`**
Este script es el punto de entrada principal para ejecutar el pipeline del proyecto. Su propósito es coordinar las tareas de preprocesamiento, entrenamiento y evaluación.

##### 2. **`src/preprocessing.py`**
Este módulo contiene las funciones para la limpieza y preprocesamiento de datos.

##### 3. **`src/training.py`**
Este módulo gestiona el entrenamiento del modelo con los datos procesados.

##### 4. **`src/evaluation.py`**
Este módulo realiza la evaluación del modelo entrenado, generando métricas y reportes.

##### 5. **`requirements.txt`**
Lista de dependencias necesarias para ejecutar el proyecto.

##### 6. **`.env`**
Archivo para almacenar secretos y credenciales necesarios para el proyecto.

##### 7. **`.gitignore`**
Archivo para especificar qué archivos y directorios deben ser ignorados por Git.

##### 8. **`README.md`**
Para facilitar la creación de un archivo `README.md` efectivo y profesional, se recomienda utilizar plantillas disponibles en [Readme Templates](https://www.readme-templates.com/). Estas plantillas proporcionan una estructura clara y completa que puede ser adaptada a las necesidades específicas de tu proyecto.

#### Cómo Ejecutar

1. Clona este repositorio o descarga el archivo ZIP.
2. Crea y activa el entorno virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows usa `.venv\Scripts\activate`
    ```
3. Instala las dependencias desde el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4. Configura las variables de entorno en el archivo `.env`.
5. Ejecuta el pipeline desde el script principal:
    ```bash
    python src/main.py
    ```
6. Los resultados generados se almacenarán en la carpeta `outputs`.

#### Notas Finales
Este proyecto es modular y está diseñado para ser fácilmente escalable y reproducible.

### Documentación Técnica
La entrega debe incluir un informe detallado que describa el enfoque metodológico, las decisiones técnicas y los resultados obtenidos. Se deben proporcionar visualizaciones que respalden los hallazgos y faciliten la comprensión de la solución.

### Código y GitHub
El código debe incluir comentarios claros que expliquen las secciones más importantes, facilitando la comprensión y modificación por parte de otros desarrolladores. Debe estar versionado en un repositorio de GitHub.

### Presentación
La entrega debe incluir una presentación de no más de 5-6 diapositivas que resuma el problema, la solución propuesta, los resultados obtenidos y el impacto empresarial esperado.


---
## 5. Criterios de Selección

### Claridad y Alineación
La solución debe estar claramente alineada con el problema empresarial planteado, demostrando una comprensión profunda del mismo.
**Ponderación: 20%**

### Calidad Técnica
Se evaluará la calidad técnica del modelo y el procesamiento de datos, incluyendo la robustez y precisión del modelo.
**Ponderación: 30%**

### Documentación y Reproducibilidad
La documentación debe ser completa y el código debe ser fácilmente reproducible por otros desarrolladores.
**Ponderación: 20%**

### Innovación y Creatividad
Se valorará la innovación y creatividad en la solución propuesta, incluyendo el uso de técnicas avanzadas y enfoques novedosos.
**Ponderación: 15%**

### Viabilidad y Escalabilidad
La solución debe ser viable y escalable en un entorno empresarial real, demostrando su potencial para ser implementada y utilizada de manera efectiva.
**Ponderación: 15%**



| Criterio                   | Ponderación | Importancia y Justificación |
|----------------------------|--------------|-----------------------------|
| Claridad y Alineación      | 20%          | Es crucial que la solución esté claramente alineada con el problema empresarial planteado, demostrando una comprensión profunda del mismo. |
| Calidad Técnica            | 30%          | La calidad técnica del modelo y el procesamiento de datos es fundamental para asegurar la robustez y precisión del modelo, lo cual es esencial para su éxito. |
| Documentación y Reproducibilidad | 20%    | Una documentación completa y un código fácilmente reproducible son vitales para que otros desarrolladores puedan entender y replicar la solución. |
| Innovación y Creatividad   | 15%          | La innovación y creatividad en la solución propuesta son valoradas, ya que pueden ofrecer enfoques novedosos y técnicas avanzadas que mejoren el resultado. |
| Viabilidad y Escalabilidad | 15%          | La solución debe ser viable y escalable en un entorno empresarial real, demostrando su potencial para ser implementada y utilizada de manera efectiva. |

