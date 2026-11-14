# Guía de Contribución — Lunáticos 2026

¡Bienvenido/a al repositorio del equipo **Lunáticos 2026** para el NASA Space Apps Challenge 2026! Para trabajar de forma ordenada y sin conflictos durante el hackathon, seguimos este flujo simple:

## 1. Ramas por funcionalidad (`feat/<nombre>`)
- Nunca hagas commits directos sobre `main`.
- Creá siempre una rama nueva desde `main` actualizado usando el prefijo `feat/<nombre>`:
  ```bash
  git checkout main
  git pull origin main
  git checkout -b feat/comparador-sitios
  ```

## 2. Commits cortos en español
- Escribí mensajes de commit breves, claros y en español (podés usar prefijos convencionales como `feat:`, `fix:`, `docs:`, `chore:`, `data:`):
  - `feat: agrega cálculo de elevación solar`
  - `docs: documenta sitios CLPS en data`
  - `fix: corrige horizonte con libración`

## 3. Pull Request (PR) a `main` y revisión
- Subí tu rama al remoto:
  ```bash
  git push -u origin feat/<nombre>
  ```
- Abrí un **Pull Request (PR)** apuntando a la rama `main`.
- **Requisito para mergear:** Al menos **1 aprobación** de otro integrante del equipo antes de hacer merge a `main`.

## 4. Cuidado con archivos pesados y secretos
- No subas credenciales ni archivos `.env` (usá `.env.example` como plantilla).
- Guardá los datasets crudos pesados (como recortes grandes de LOLA o descargas masivas de Horizons) dentro de `data/raw/`, que ya está excluido en `.gitignore`.
