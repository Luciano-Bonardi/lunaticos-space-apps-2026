# 📋 Bitácora de Contexto: Cosas Charladas, Definidas y Pendientes

> **Objetivo de este documento:** Que todo el equipo **Lunáticos 2026** (y los agentes de IA con los que trabajemos en cada computadora) comparta un **único contexto vivo**. Cada vez que avancemos en un chat o reunión, volcamos acá qué quedó resuelto, qué se charló y qué sigue abierto para decidir entre todos.

---

## ✅ 1. Lo que ya está definido y listo (Contexto Base)

### 🎯 Problema y Enfoque del Challenge
- **Qué construimos:** Una herramienta intuitiva para comparar sitios y fechas de alunizaje en el **polo sur lunar**, visualizando la posición del **Sol** y de la **Tierra** respecto del horizonte para evaluar **generación de energía solar** y **ventanas de comunicación directa con la Tierra**.
- **Valor diferencial:** Las herramientas actuales (Quickmap, Moon Trek, JPL Horizons) son muy potentes pero complejas para comparar múltiples escenarios rápido. Nuestro foco es la **comparación ágil lado a lado** accesible tanto para expertos como para docentes y público general.

### 🛰️ Datos y APIs de la NASA (Ya probados en el repo)
- **Efemérides (Sol y Tierra):** Usamos la API REST pública de **JPL Horizons** (`https://ssd.jpl.nasa.gov/api/horizons.api`), que **no requiere API Key**.
  - Observador en superficie lunar: `CENTER='coord@301'`, `COORD_TYPE='GEODETIC'`, `SITE_COORD='lon,lat,alt_km'`.
  - Cuerpos: Sol (`COMMAND='10'`) y Tierra (`COMMAND='399'`).
  - Magnitud: `QUANTITIES='4'` devuelve **Azimut (`Azi_(a-app)`)** y **Elevación (`Elev_(a-app)`)** aparentes sin refracción atmosférica.
  - Script funcional disponible: [scripts/consultar_horizons.py](../scripts/consultar_horizons.py).
- **Sitios iniciales de referencia:** Ya cargados 5 sitios reales en [data/sitios_referencia.json](../data/sitios_referencia.json) (*Connecting Ridge*, *Shackleton Rim*, *Malapert Massif*, *Nobile Rim 1 / VIPER* y *Apollo 11* como control ecuatorial).
- **Documentación de APIs:** Disponible en [docs/apis-nasa-y-contexto.md](./apis-nasa-y-contexto.md).

### 📂 Organización y Flujo de Trabajo del Equipo
- **Repositorio oficial:** https://github.com/Luciano-Bonardi/lunaticos-space-apps-2026 (rama principal `main`).
- **Integrantes en GitHub:** `Luciano-Bonardi` (owner) y `sguenio` (`chersaredmi@gmail.com`, invitado con permiso `write` y con fork creado).
- **Dónde va cada cosa:**
  - Propuestas individuales o grupales sin cerrar → [`/ideas`](../ideas/README.md) (usando [PLANTILLA-PROPUESTA.md](../ideas/PLANTILLA-PROPUESTA.md)).
  - Acuerdos y este resumen vivo → [`/docs`](./README.md).
  - Manual completo → [docs/manual-organizacion-repo.md](./manual-organizacion-repo.md).

---

## ⏳ 2. Cosas Charladas pero AÚN NO DEFINIDAS (Para decidir en equipo)

| Área | Pregunta / Decisión pendiente | Opciones sobre la mesa | Estado |
| :--- | :--- | :--- | :--- |
| **1. Alcance del MVP** | ¿Permitimos elegir solo sitios curados del catálogo o cualquier coordenada `(lat, lon)` libre en el mapa? | A) Catálogo curado de 5-10 sitios (más rápido y permite precalcular horizonte LOLA).<br>B) Coordenadas libres + catálogo. | 🔴 **Sin definir** |
| **2. Visualización del Horizonte** | ¿Cómo mostramos el Sol, la Tierra y el terreno LOLA en pantalla? | A) Panorama 2D de 360° (Azimut en eje X, Elevación en eje Y con silueta del terreno).<br>B) Domo / cielo polar 2D + vista 3D.<br>C) Escena 3D interactiva (Three.js / Cesium). | 🔴 **Sin definir** |
| **3. Stack de Frontend** | ¿Con qué tecnología armamos la interfaz web y los gráficos? | React + Vite / Next.js / Vue + Tailwind + librería de gráficos (D3 / Chart.js / Three.js). | 🔴 **Sin definir** |
| **4. Stack de Backend vs Precomputado** | ¿Consultamos JPL Horizons en tiempo real desde un backend o precalculamos datasets? | A) Backend en Python (FastAPI) que consulta Horizons con caché.<br>B) Datasets precalculados en `/data` + llamada directa desde cliente/proxy. | 🔴 **Sin definir** |
| **5. Horizonte Real con LOLA** | ¿Cómo obtenemos el perfil de elevación del terreno (montañas/cráteres) alrededor de cada sitio? | A) Precalcular el perfil de horizonte (0° a 360°) para los sitios de `sitios_referencia.json` usando un DEM de LOLA.<br>B) Modelo simplificado de pendiente/obstáculo. | 🔴 **Sin definir** |
| **6. Experiencia Experto vs Público General** | ¿Hacemos un switch de modo ("Modo Misión / Experto" vs "Modo Explorador / Educativo") o una única vista? | A) Una vista limpia con tooltips educativos.<br>B) Toggle entre vista técnica (métricas detalladas) y vista guiada. | 🔴 **Sin definir** |
| **7. Deploy de la Demo** | ¿Dónde vamos a publicar la app para la entrega del Space Apps? | Vercel / Render / GitHub Pages / Hostinger. | 🔴 **Sin definir** |

---

## 🗓️ 3. Historial de Chats y Sesiones (Bitácora Cronológica)

### 📌 Sesión 1 — 2026-11-14 (Setup, Organización, APIs NASA y Contexto Compartido)
- **Participante:** `@Luciano-Bonardi` + Agente Antigravity
- **Qué se habló y se hizo:**
  1. Se auditaron los MCPs de Antigravity (`stitch` OK, `github` actualizado y funcionando con la cuenta `Luciano-Bonardi`, `hostinger` pendiente de renovar token si se usa).
  2. Se inicializó y publicó el repositorio `lunaticos-space-apps-2026` con la estructura `/docs`, `/data`, `/backend`, `/frontend`, `/notebooks`, `/scripts` y `/ideas`.
  3. Se invitó a `@sguenio` (`chersaredmi@gmail.com`) como colaborador con permisos de escritura (`write`).
  4. Se creó el manual de organización del repo ([docs/manual-organizacion-repo.md](./manual-organizacion-repo.md)) y la plantilla de propuestas ([ideas/PLANTILLA-PROPUESTA.md](../ideas/PLANTILLA-PROPUESTA.md)).
  5. Se probó en vivo la API de **JPL Horizons** para el Polo Sur Lunar y se subieron la guía técnica ([docs/apis-nasa-y-contexto.md](./apis-nasa-y-contexto.md)), el script de consulta ([scripts/consultar_horizons.py](../scripts/consultar_horizons.py)) y los sitios de referencia ([data/sitios_referencia.json](../data/sitios_referencia.json)).
  6. Se estableció esta bitácora (`docs/bitacora-y-pendientes.md`) y una regla automática en `.agents/rules/contexto-equipo.md` para que todos los chats futuros mantengan actualizado este resumen.
- **Qué quedó pendiente de esta sesión:**
  - Que `@sguenio` acepte la invitación de colaborador en https://github.com/Luciano-Bonardi/lunaticos-space-apps-2026/invitations.
  - Que el equipo suba sus primeras ideas en `/ideas` y defina los 7 puntos de la tabla de decisiones abiertas.

---

## ✍️ Plantilla para agregar nuevos resúmenes de chat

*(Copiá este bloque al final de la sección 3 cada vez que cierres una charla o sesión de trabajo):*

```markdown
### 📌 Sesión X — YYYY-MM-DD ([Tema principal del chat])
- **Participante(s):** @[usuario]
- **Qué se charló / avanzó:**
  - ...
- **Decisiones cerradas (pasar también a la sección 1):**
  - ...
- **Dudas o puntos aún no definidos (pasar también a la sección 2):**
  - ...
```
