# `/scripts` — Utilidades de Descarga y Preprocesamiento

## Sobre el Challenge
Este proyecto del equipo **Lunáticos 2026** (NASA Space Apps Challenge 2026) desarrolla una herramienta intuitiva para que planificadores de misión, docentes y público comparen sitios y fechas de alunizaje en el polo sur lunar, evaluando generación de energía solar y ventanas de comunicación directa con la Tierra a partir de la posición del Sol y la Tierra sobre el horizonte.

## Contenido de esta carpeta y conexión con los objetivos
En `/scripts` se guardan las utilidades automatizadas para descargar efemérides desde JPL Horizons, recortar y preprocesar mapas de topografía LOLA del polo sur lunar, y precomputar perfiles de horizonte real y métricas para alimentar `/data` y `/backend`.
Se conecta directamente con:
- **Objetivo 1:** Selección y comparación de sitios (Apollo, CLPS, otros programas, coordenadas propias), lado a lado.
- **Objetivo 2:** Flexibilidad de fecha/hora y cambios a lo largo de días lunares/estaciones.
- **Objetivo 4:** Métricas: elevación solar, duración de luz, ventanas de visibilidad terrestre.

## Recursos relevantes
- **JPL Horizons:** https://ssd.jpl.nasa.gov/horizons/
- **Moon Trek:** https://trek.nasa.gov/moon/
- **Quickmap:** https://quickmap.lroc.asu.edu/

## Próximo paso sugerido
Escribir un script para descargar y guardar en `data/raw/` las efemérides de JPL Horizons para los sitios candidatos del polo sur lunar (formato de salida y parámetros de ejecución **A definir por el equipo**).
