# `/backend` — Cálculo de Posiciones Sol/Tierra y Horizonte

## Sobre el Challenge
Este proyecto del equipo **Lunáticos 2026** (NASA Space Apps Challenge 2026) busca crear una herramienta intuitiva para comparar sitios y fechas de alunizaje en el polo sur lunar. Dado que en el polo sur pequeños cambios de lugar o fecha alteran drásticamente la iluminación solar y la visibilidad terrestre, este módulo resuelve los cálculos orbitales y topográficos necesarios para evaluar energía solar y comunicación directa con la Tierra.

## Contenido de esta carpeta y conexión con los objetivos
En `/backend` vive la lógica de consulta o lectura de efemérides (vía JPL Horizons o datasets precomputados), el cálculo del horizonte real a partir de la topografía LOLA (considerando que no hay atmósfera ni refracción, el efecto de la libración lunar, las pendientes y los cráteres con sombra permanente) y la exposición de métricas hacia la interfaz.
Se conecta directamente con:
- **Objetivo 1:** Selección y comparación de sitios (Apollo, CLPS, otros programas, coordenadas propias), lado a lado.
- **Objetivo 2:** Flexibilidad de fecha/hora y cambios a lo largo de días lunares/estaciones.
- **Objetivo 3:** Visualización de Sol y Tierra sobre el horizonte; tiempo restante hasta puesta de Sol / de Tierra.
- **Objetivo 4:** Métricas: elevación solar, duración de luz, ventanas de visibilidad terrestre.

## Recursos relevantes
- **JPL Horizons** (efemérides y posiciones aparentes Sol/Tierra): https://ssd.jpl.nasa.gov/horizons/
- **Quickmap** (referencia de topografía LOLA e iluminación): https://quickmap.lroc.asu.edu/
- **Moon Trek** (datos de terreno LOLA): https://trek.nasa.gov/moon/

## Próximo paso sugerido
Implementar el servicio o módulo que calcule la elevación del Sol y de la Tierra sobre el perfil de horizonte LOLA para una coordenada y rango de fechas dados, definiendo previamente el lenguaje y framework del servidor (**A definir por el equipo**).
