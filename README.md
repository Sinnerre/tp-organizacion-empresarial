# TP Organización Empresarial

## Integrantes
P1 (Hugo): Organización del repositorio y estructura inicial
P2 (Paco): Desarrollo del análisis de datos
P3 (Luis): Revisión, documentación y control de calidad

## Escenario elegido
Análisis de Ventas

## Estructura del proyecto

/datos
    sales_sample_2024.csv

/scripts
    analisis.py

/resultados
    resumen.txt
    ventas_por_mes.png

## Tecnologías utilizadas

- Python
- Git
- GitHub
- Jira
- Google Colab

## Dataset

Se utilizó el dataset del punto 10.3 del TP, con las siguientes columnas:

id
sales_date
sales_amount

Este dataset permite realizar un análisis temporal de ventas.

## Script

El script realiza:

Carga del dataset
Conversión de fechas
Cálculo de métricas:
Ventas totales
Promedio de ventas
Valor máximo y mínimo
Agrupación de ventas por mes
Generación de gráfico de evolución mensual

## Como ejecutar el script

-1: Clonar el repositorio.

En Colab:
!git clone https://github.com/Sinnerre/tp-organizacion-empresarial.git

-2: Entrar al proyecto

%cd tp-organizacion-empresarial

-3: Ejecutar el script

!python scripts/analisis.py

Luego de esto, se generan automáticamente:

/resultados/resumen.txt
/resultados/ventas_por_mes.png
