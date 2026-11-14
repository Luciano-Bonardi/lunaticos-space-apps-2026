# 🌕 Lunáticos 2026 — NASA Space Apps Challenge 2026

> Herramienta intuitiva para que planificadores de misión, docentes y público general comparen sitios y fechas de alunizaje en el polo sur lunar, visualizando la posición del Sol y la Tierra respecto del horizonte para evaluar generación de energía solar y ventanas de comunicación directa con la Tierra.

---

## 🚀 El Desafío y Por Qué Importa

En el **polo sur lunar** (región clave por la presencia de agua congelada y objetivo de las misiones **CLPS** y **Artemis**), pequeños cambios de ubicación o de fecha alteran drásticamente las condiciones de iluminación solar y la visibilidad directa de la Tierra.

Las herramientas actuales (**Quickmap**, **Moon Trek**, **JPL Horizons**) son sumamente potentes, pero resultan difíciles de usar cuando se necesita **comparar múltiples escenarios rápidamente**. Nuestro proyecto busca cerrar esa brecha ofreciendo una experiencia ágil, visual y accesible tanto para especialistas como para docentes y público general.

---

## 🎯 Objetivos del Proyecto

1. **Selección y comparación de sitios:** Comparación lado a lado de sitios históricos y planificados (Apollo, CLPS, otros programas y coordenadas propias).
2. **Flexibilidad temporal:** Selección libre de fecha/hora y exploración de cambios a lo largo de días lunares y estaciones.
3. **Horizonte Sol y Tierra:** Visualización de la posición del Sol y la Tierra sobre el horizonte, indicando el tiempo restante hasta la puesta de Sol y de Tierra.
4. **Métricas clave:** Elevación solar, duración de luz solar y ventanas de visibilidad terrestre.
5. **Visualizaciones interactivas:** Vistas 2D/3D, animaciones y líneas de tiempo.
6. **Accesibilidad:** Interfaz clara y comprensible tanto para expertos en planificación de misiones como para público general y uso educativo.

---

## 🛰️ Consideraciones Técnicas

- **Efemérides:** Obtenidas vía **JPL Horizons** o mediante datasets precomputados.
- **Topografía real:** Uso de datos **LOLA** para modelar el horizonte real.
- **Física lunar:** Sin atmósfera → sin refracción atmosférica; el horizonte queda definido estrictamente por el terreno.
- **Dinámica y relieve:** Se contempla el efecto de la **libración lunar**, las **pendientes del terreno** y los **cráteres con sombra permanente**.

---

## 🔗 Recursos Oficiales

- **Quickmap (LROC):** https://quickmap.lroc.asu.edu/
- **Moon Trek (NASA):** https://trek.nasa.gov/moon/
- **JPL Horizons:** https://ssd.jpl.nasa.gov/horizons/
- **CSA Moon Exploration:** https://www.asc-csa.gc.ca/eng/astronomy/moon-exploration/

---

## 📂 Estructura del Repositorio

> 📖 **¿No sabés dónde guardar algo?** Leé el **[Manual de Organización del Repositorio](./docs/manual-organizacion-repo.md)** (especial para esta etapa de definición de idea, entorno y herramientas).

```text
├── ideas/       → 💡 Brainstorming, propuestas individuales, bocetos y opciones de stack (Fase actual)
├── docs/        → 📋 Documentación oficial, acuerdos unificados, manual del repo y estado de MCPs
├── data/        → 🗂️ Datasets limpios (efemérides precomputadas, perfiles LOLA, sitios curados)
├── backend/     → ⚙️ Cálculo de posiciones Sol/Tierra, horizonte y métricas
├── frontend/    → 🖥️ Interfaz de usuario y visualizaciones 2D/3D
├── notebooks/   → 🧪 Exploración de datos y prototipos de cálculo
└── scripts/     → 🛠️ Utilidades de descarga y preprocesamiento
```

Cada carpeta cuenta con su propio `README.md` explicando qué contiene, con qué objetivos se conecta y cuál es el próximo paso sugerido.

---

## ⚡ Cómo empezar en 5 minutos

### 1. Clonar el repositorio
```bash
git clone https://github.com/Luciano-Bonardi/lunaticos-space-apps-2026.git
cd lunaticos-space-apps-2026
```

### 2. Configurar variables de entorno
```bash
cp .env.example .env
```
*(Completá en `.env` las variables necesarias según tu rol; los valores específicos de APIs adicionales están **A definir por el equipo**).*

### 3. Instalar dependencias
- **Backend / Scripts / Notebooks (Python):** *(Gestor de paquetes y `requirements.txt` / `pyproject.toml` **A definir por el equipo**)*
  ```bash
  python -m venv .venv
  # Windows (PowerShell):
  .\.venv\Scripts\Activate.ps1
  # Linux / macOS:
  source .venv/bin/activate
  ```
- **Frontend (Node.js):** *(Framework y `package.json` **A definir por el equipo**)*
  ```bash
  cd frontend
  npm install
  ```

### 4. Correr el proyecto
- **Backend:** comando de ejecución en `/backend` (**A definir por el equipo**).
- **Frontend:** comando de desarrollo en `/frontend`, ej. `npm run dev` (**A definir por el equipo**).

Revisá [CONTRIBUTING.md](./CONTRIBUTING.md) antes de subir tu primera rama.

