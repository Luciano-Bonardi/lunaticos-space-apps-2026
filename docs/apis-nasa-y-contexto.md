# 🛰️ APIs de la NASA y Contexto Técnico — Lunáticos 2026

Este documento reúne los endpoints, parámetros exactos y ejemplos probados de las APIs de la NASA para que cualquier integrante del equipo pueda consultar posiciones del **Sol**, la **Tierra** y **topografía lunar (LOLA)** desde el primer minuto.

> 💡 **¿Necesito una API Key paga o privada?**
> **No.** La API principal de nuestro desafío (**JPL Horizons**) es **100% pública y no requiere API Key**. Para los servicios generales de `api.nasa.gov` dejamos configurada `NASA_API_KEY=DEMO_KEY` por defecto en `.env.example` (y cualquiera puede generar una key gratuita en 30 segundos en https://api.nasa.gov/ si necesita mayor límite de consultas).

---

## 1. API Principal: JPL Horizons (Posición de Sol y Tierra desde la Luna)

- **Endpoint REST (GET):** `https://ssd.jpl.nasa.gov/api/horizons.api`
- **Documentación oficial:** https://ssd-api.jpl.nasa.gov/doc/horizons.html
- **Autenticación:** **Ninguna** (acceso libre).

### Parámetros clave para nuestro Challenge

Cuando un observador está parado sobre la superficie de la Luna mirando al cielo:
- **Observador (`CENTER`):** `'coord@301'` (`301` es el código NAIF de la Luna; `coord@301` indica una coordenada topocéntrica en la superficie lunar).
- **Coordenadas del sitio (`SITE_COORD`):** `'longitud_este,latitud,altitud_km'` en formato `GEODETIC`.
  - Ejemplo borde del cráter Shackleton (Polo Sur): `'0.0,-89.54,0'`
- **Objetivo a observar (`COMMAND`):**
  - `'10'` → **El Sol** (para calcular generación de energía solar y elevación solar).
  - `'399'` → **La Tierra** (para calcular ventanas de comunicación directa y libración aparente).
- **Magnitudes a devolver (`QUANTITIES`):**
  - `'4'` → Devuelve **Azimut (`Azi_(a-app)`)** y **Elevación (`Elev_(a-app)`)** aparentes en grados respecto del horizonte matemático local (sin refracción atmosférica, ya que la Luna no tiene atmósfera).
- **Formato fácil de parsear (`CSV_FORMAT`):** `'YES'` (devuelve filas separadas por comas entre las marcas `$$SOE` y `$$EOE`).

### Ejemplo real probado (URL directa en navegador o `curl`)

Posición del **Sol (`COMMAND='10'`)** vista desde el Polo Sur Lunar (`0° E, -89.54° S`) cada 6 horas:

```text
https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='10'&OBJ_DATA='NO'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&CENTER='coord@301'&COORD_TYPE='GEODETIC'&SITE_COORD='0,-89.54,0'&START_TIME='2026-11-14'&STOP_TIME='2026-11-15'&STEP_SIZE='6%20h'&QUANTITIES='4'&CSV_FORMAT='YES'
```

**Respuesta real obtenida (bloque entre `$$SOE` y `$$EOE`):**
```csv
Date__(UT)__HR:MN, , ,Azi_(a-app), Elev_(a-app),
$$SOE
 2026-Nov-14 00:00,*, , 126.626621,     1.282199,
 2026-Nov-14 06:00,*, , 123.579976,     1.302246,
 2026-Nov-14 12:00,*, , 120.533651,     1.322942,
 2026-Nov-14 18:00,*, , 117.487654,     1.344231,
 2026-Nov-15 00:00,*, , 114.441995,     1.366057,
$$EOE
```
- **Columna 1:** Fecha y hora UTC.
- **Columna 4 (`Azi`):** Azimut en grados (`0°` = Norte, `90°` = Este, `180°` = Sur, `270°` = Oeste).
- **Columna 5 (`Elev`):** Elevación en grados sobre el horizonte plano (`> 0°` arriba del horizonte plano; luego se compara contra el ángulo de elevación del terreno real LOLA en ese mismo azimut).

> 🧪 **Script listo para probar:** Ejecutá `python scripts/consultar_horizons.py` en la terminal para ver en vivo la posición del Sol y la Tierra sin instalar dependencias externas.

---

## 2. Topografía Lunar LOLA y Mapas (Moon Trek / LROC QuickMap)

Para saber si una montaña o el borde de un cráter tapa al Sol o a la Tierra, comparamos `Elev_(a-app)` de Horizons contra el perfil de elevación del terreno (**LOLA — Lunar Orbiter Laser Altimeter**):

1. **NASA Moon Trek (WMTS / Tiles cartográficos 2D y 3D):**
   - Portal: https://trek.nasa.gov/moon/
   - Documentación de API de Tiles (WMTS/WMS): https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=moon
   - Permite superponer capas de pendiente (*Slope*), elevación (*LOLA DEM*) e iluminación en visores web (Leaflet, OpenLayers, CesiumJS, Three.js).
2. **LROC QuickMap:**
   - Portal interactivo: https://quickmap.lroc.asu.edu/
   - Ideal para validar visualmente perfiles de elevación, cráteres con sombra permanente (PSR) y sitios Artemis/CLPS.
3. **Archivos DEM LOLA del Polo Sur (PDS Geosciences Node):**
   - Catálogo oficial de modelos de elevación digital (GeoTIFF / IMG) del polo sur lunar (80°S a 90°S, resoluciones de 5 m/px a 100 m/px):
   - https://imbrium.mit.edu/DATA/LOLA_GDR/POLAR/JP2/ y https://pds-geosciences.wustl.edu/missions/lro/lola.htm

---

## 3. NASA Open APIs (`api.nasa.gov`)

Si el frontend o backend necesita recursos complementarios del portal general de APIs de la NASA:
- **URL Base:** `https://api.nasa.gov/`
- **API Key por defecto (incluida en `.env.example`):** `DEMO_KEY` (permite 30 requests/hora por IP y 50/día sin registro).
- **API Key gratuita personal (1.000 requests/hora):** Solicitar con cualquier email en https://api.nasa.gov/ y pegarla en `.env` como `NASA_API_KEY=...`.

---

## 4. Sitios de Alunizaje Pre-cargados en `/data`

Ya dejamos en [data/sitios_referencia.json](../data/sitios_referencia.json) un catálogo inicial con coordenadas reales de regiones candidatas **Artemis III**, misiones **CLPS** e históricas **Apollo** para que tanto `/backend` como `/frontend` tengan datos reales desde el inicio.
