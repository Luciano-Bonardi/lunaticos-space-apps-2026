# `/data` — Datasets (Efemérides, Topografía LOLA y Sitios Curados)

## Sobre el Challenge
Este proyecto del equipo **Lunáticos 2026** (NASA Space Apps Challenge 2026) consiste en desarrollar una herramienta intuitiva para que planificadores de misión, docentes y público comparen sitios y fechas de alunizaje en el polo sur lunar. Permite visualizar la posición del Sol y la Tierra sobre el horizonte para evaluar generación de energía solar y ventanas de comunicación directa con la Tierra, superando la complejidad de comparar escenarios rápidamente en las herramientas actuales.

## Contenido de esta carpeta y conexión con los objetivos
En `/data` se almacenan los datasets precomputados de efemérides, modelos de elevación digital de topografía LOLA (para calcular el horizonte real definido por el terreno, pendientes y cráteres con sombra permanente) y el catálogo de sitios de alunizaje curados. Los datos crudos pesados deben ubicarse en `data/raw/` (ignorado por Git).
Se conecta directamente con:
- **Objetivo 1:** Selección y comparación de sitios (Apollo, CLPS, otros programas, coordenadas propias), lado a lado.
- **Objetivo 2:** Flexibilidad de fecha/hora y cambios a lo largo de días lunares/estaciones.
- **Objetivo 3:** Visualización de Sol y Tierra sobre el horizonte; tiempo restante hasta puesta de Sol / de Tierra.
- **Objetivo 4:** Métricas: elevación solar, duración de luz, ventanas de visibilidad terrestre.

## Recursos relevantes
- **JPL Horizons** (efemérides del Sol, la Tierra y libración lunar): https://ssd.jpl.nasa.gov/horizons/
- **Quickmap** (consulta de topografía LOLA, pendientes y cráteres del polo sur): https://quickmap.lroc.asu.edu/
- **Moon Trek** (capas cartográficas y modelos de terreno LOLA): https://trek.nasa.gov/moon/
- **CSA Moon Exploration** (contexto de misiones lunares): https://www.asc-csa.gc.ca/eng/astronomy/moon-exploration/

## Próximo paso sugerido
Armar el archivo inicial de sitios curados (coordenadas de misiones Apollo, CLPS y polo sur lunar) y definir la resolución/recorte del dataset LOLA y el formato de almacenamiento (**A definir por el equipo**).

