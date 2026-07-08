# Datathon SUNASS 2026 — Reto Operacional (Finalista Nacional)

Solución de ciencia de datos para optimizar la operación de una EPS de saneamiento con +300,000 conexiones activas: de la limpieza de datos a la priorización de sectores críticos y la optimización de rutas de reparación.

## Contexto

Una EPS gestiona miles de fugas y roturas al mes con cuadrillas limitadas. Sin priorización basada en datos ni ruteo eficiente, aumentan el agua no facturada, los tiempos de reparación y los costos operativos.

## Objetivo

Construir un pipeline reproducible que limpie los datos operativos, identifique los sectores críticos y asigne y rutee de forma óptima las reparaciones para minimizar desplazamiento y costos.

## Arquitectura

```mermaid
flowchart LR
    A[Datos operativos EPS] --> B[Limpieza<br/>dedup, IQR, geo-coords]
    B --> C[Indicadores por sector<br/>roturas/km, fugas/mil conex.]
    C --> D[Clustering K-Means<br/>sectores criticos]
    D --> E[Asignacion a 3 cuadrillas<br/>distancia euclidiana min.]
    E --> F[Ruteo diario TSP]
    F --> G[Plan operativo + mapas Folium]
```

## Stack

| Categoría | Herramientas |
|---|---|
| Lenguaje | Python |
| Datos | pandas, NumPy |
| ML / optimización | scikit-learn (K-Means), SciPy (TSP) |
| Geo / visualización | Folium, Matplotlib |
| Entorno | Jupyter Notebook |

## Estructura del proyecto

```
datathon-sunass-2026/
├── solucion_lima_SCC07.ipynb                   # Pipeline completo
├── presentacion_solucion_lima_SCC07.pptx       # Presentación de la solución
├── Datathon_SUNASS_2026_Reto_Operacional.pdf   # Enunciado del reto
└── README.md
```

## Ejecución

1. Clona el repositorio: `git clone https://github.com/Alvaro192023/datathon-sunass-2026.git`
2. Instala dependencias: `pip install pandas numpy scikit-learn scipy matplotlib folium`
3. Abre `solucion_lima_SCC07.ipynb` en Jupyter y ejecuta las celdas en orden.

## Resultados e impacto

- **Finalista Nacional** de la Datathon SUNASS 2026.
- Limpieza robusta: deduplicación, estandarización de sectores, corrección de outliers (IQR) y de coordenadas geográficas invertidas.
- Indicadores operativos por sector (roturas/km, fugas/mil conexiones, tiempos de reparación) y **clustering K-Means** para priorizar sectores críticos.
- **Asignación óptima** de fugas a 3 cuadrillas por distancia euclidiana mínima y **ruteo diario con TSP** para minimizar desplazamiento y costo.

## Próximos pasos

- Ruteo con ventanas de tiempo (VRPTW) y capacidad por cuadrilla.
- Modelo predictivo de aparición de fugas por sector.
- Dashboard operativo para el despacho diario de cuadrillas.

## Licencia y contacto

MIT. Álvaro Villanueva Kobayashi — alvarovillakoba515@gmail.com · [GitHub](https://github.com/Alvaro192023)
