# `/notebooks` — Exploración y Prototipos de Cálculo

## Sobre el Challenge
Este proyecto del equipo **Lunáticos 2026** (NASA Space Apps Challenge 2026) busca crear una herramienta intuitiva para comparar sitios y fechas de alunizaje en el polo sur lunar, visualizando la posición del Sol y la Tierra respecto del horizonte para evaluar generación de energía solar y ventanas de comunicación directa con la Tierra.

## Contenido de esta carpeta y conexión con los objetivos
En `/notebooks` se ubican los cuadernos interactivos de exploración de datos y validación de algoritmos antes de pasarlos a `/backend` o `/scripts`: pruebas con efemérides de JPL Horizons, análisis del efecto de la libración, trazado de perfiles de horizonte con topografía LOLA (sin refracción atmosférica) y detección de pendientes y cráteres con sombra permanente.
Se conecta directamente con:
- **Objetivo 2:** Flexibilidad de fecha/hora y cambios a lo largo de días lunares/estaciones.
- **Objetivo 3:** Visualización de Sol y Tierra sobre el horizonte; tiempo restante hasta puesta de Sol / de Tierra.
- **Objetivo 4:** Métricas: elevación solar, duración de luz, ventanas de visibilidad terrestre.

## Recursos relevantes
- **JPL Horizons:** https://ssd.jpl.nasa.gov/horizons/
- **Quickmap:** https://quickmap.lroc.asu.edu/
- **Moon Trek:** https://trek.nasa.gov/moon/

## Próximo paso sugerido
Crear un primer notebook que consulte JPL Horizons para una coordenada del polo sur lunar y grafique la curva de elevación del Sol y de la Tierra durante un día lunar o estación completa (librerías específicas **A definir por el equipo**).
