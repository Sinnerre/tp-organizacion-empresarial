
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/sales_sample_2024.csv")

# Convertir fecha
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Estadísticas generales
ventas_totales = df["sales_amount"].sum()
venta_promedio = df["sales_amount"].mean()
venta_maxima = df["sales_amount"].max()
venta_minima = df["sales_amount"].min()

# Ventas por mes
df["mes"] = df["sales_date"].dt.to_period("M")
ventas_mes = df.groupby("mes")["sales_amount"].sum()

# Guardar resumen
with open("resultados/resumen.txt", "w", encoding="utf-8") as f:
    f.write("RESUMEN DE VENTAS\n")
    f.write("=================\n\n")
    f.write(f"Ventas totales: {ventas_totales}\n")
    f.write(f"Venta promedio: {venta_promedio:.2f}\n")
    f.write(f"Venta máxima: {venta_maxima}\n")
    f.write(f"Venta mínima: {venta_minima}\n")

# Gráfico
plt.figure(figsize=(10,5))
ventas_mes.plot(kind="bar")
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto de Ventas")
plt.tight_layout()

plt.savefig("resultados/ventas_por_mes.png")

print("Análisis finalizado.")
