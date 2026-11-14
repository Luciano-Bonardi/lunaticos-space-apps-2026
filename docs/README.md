# `/docs` — Documentación y Decisiones

## Sobre el Challenge
Este proyecto del equipo **Lunáticos 2026** (NASA Space Apps Challenge 2026) busca crear una herramienta intuitiva para que planificadores de misión, docentes y público general comparen sitios y fechas de alunizaje en el polo sur lunar. En esta región (clave por el agua congelada y las misiones CLPS/Artemis), pequeños cambios de ubicación o fecha alteran drásticamente la iluminación y la visibilidad de la Tierra. La herramienta visualiza la posición del Sol y la Tierra respecto del horizonte real del terreno para evaluar generación de energía solar y ventanas de comunicación directa.

## Contenido de esta carpeta y conexión con los objetivos
En `/docs` se centraliza la documentación oficial del desafío, la **[Bitácora de Contexto: Cosas Charladas y Pendientes](./bitacora-y-pendientes.md)**, las decisiones de arquitectura ya consensuadas (que nacen en `/ideas`), el **[Manual de Organización del Repositorio](./manual-organizacion-repo.md)**, la guía de **[APIs de la NASA y Contexto Técnico](./apis-nasa-y-contexto.md)** y el estado de las integraciones ([mcp-status.md](./mcp-status.md)).
Se conecta transversalmente con todos los objetivos del challenge:
- **Objetivo 1:** Selección y comparación de sitios (Apollo, CLPS, otros programas, coordenadas propias), lado a lado.
- **Objetivo 2:** Flexibilidad de fecha/hora y cambios a lo largo de días lunares/estaciones.
- **Objetivo 3:** Visualización de Sol y Tierra sobre el horizonte; tiempo restante hasta puesta de Sol / de Tierra.
- **Objetivo 4:** Métricas: elevación solar, duración de luz, ventanas de visibilidad terrestre.
- **Objetivo 5:** Visualizaciones 2D/3D, animaciones y líneas de tiempo.
- **Objetivo 6:** Accesible para expertos y para público general.

## Recursos relevantes
- **Quickmap (LROC):** https://quickmap.lroc.asu.edu/
- **Moon Trek (NASA):** https://trek.nasa.gov/moon/
- **JPL Horizons:** https://ssd.jpl.nasa.gov/horizons/
- **CSA Moon Exploration:** https://www.asc-csa.gc.ca/eng/astronomy/moon-exploration/

## Próximo paso sugerido
Documentar la lista inicial de sitios de alunizaje a comparar (Apollo, CLPS y otros programas) y definir el alcance del MVP junto con el stack técnico exacto (**A definir por el equipo**).

