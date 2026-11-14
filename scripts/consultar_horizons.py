"""
Script de prueba rápida (sin dependencias externas) para consultar la API de
NASA JPL Horizons y obtener el Azimut y Elevación del Sol (10) y la Tierra (399)
vistos desde un sitio en el Polo Sur Lunar.

Uso:
    python scripts/consultar_horizons.py
"""

import json
import urllib.parse
import urllib.request


HORIZONS_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

BODIES = {
    "Sol": "10",
    "Tierra": "399",
}


def fetch_ephemeris(
    body_command: str,
    lon_deg: float = 0.0,
    lat_deg: float = -89.54,
    alt_km: float = 0.0,
    start_time: str = "2026-11-14",
    stop_time: str = "2026-11-15",
    step_size: str = "6 h",
) -> list[dict]:
    """Consulta JPL Horizons y devuelve una lista de mediciones (UTC, azimut, elevación)."""
    params = {
        "format": "json",
        "COMMAND": f"'{body_command}'",
        "OBJ_DATA": "'NO'",
        "MAKE_EPHEM": "'YES'",
        "EPHEM_TYPE": "'OBSERVER'",
        "CENTER": "'coord@301'",  # 301 = Luna
        "COORD_TYPE": "'GEODETIC'",
        "SITE_COORD": f"'{lon_deg},{lat_deg},{alt_km}'",
        "START_TIME": f"'{start_time}'",
        "STOP_TIME": f"'{stop_time}'",
        "STEP_SIZE": f"'{step_size}'",
        "QUANTITIES": "'4'",  # 4 = Azimut y Elevación aparentes
        "CSV_FORMAT": "'YES'",
    }
    url = f"{HORIZONS_URL}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=15) as response:
        payload = json.loads(response.read().decode("utf-8"))

    raw_text = payload.get("result", "")
    in_table = False
    rows = []

    for line in raw_text.splitlines():
        stripped = line.strip()
        if stripped == "$$SOE":
            in_table = True
            continue
        if stripped == "$$EOE":
            break
        if in_table and stripped:
            parts = [p.strip() for p in stripped.split(",")]
            if len(parts) >= 5:
                rows.append(
                    {
                        "utc": parts[0],
                        "azimuth_deg": float(parts[3]),
                        "elevation_deg": float(parts[4]),
                    }
                )
    return rows


if __name__ == "__main__":
    sitio_nombre = "Borde del Cráter Shackleton (Polo Sur Lunar)"
    lon, lat, alt = 0.0, -89.54, 0.0
    print(f"=== Consultando NASA JPL Horizons para: {sitio_nombre} ({lat}°, {lon}°) ===\n")

    for nombre, codigo in BODIES.items():
        print(f"--- Posición aparente de: {nombre} (COMMAND='{codigo}') ---")
        datos = fetch_ephemeris(codigo, lon_deg=lon, lat_deg=lat, alt_km=alt)
        for fila in datos:
            print(
                f"  UTC: {fila['utc']} | Azimut: {fila['azimuth_deg']:7.3f}° | "
                f"Elevación: {fila['elevation_deg']:+7.3f}°"
            )
        print()
