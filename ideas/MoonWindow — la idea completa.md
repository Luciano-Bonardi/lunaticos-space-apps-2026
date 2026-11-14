# MoonWindow — la idea completa

Nov 14, 2026 · @Lucas

## La idea en una página

MoonWindow no muestra dónde está el Sol: muestra **cuánto margen tiene una misión** antes de quedarse sin energía o sin contacto con la Tierra.

| Campo | Contenido |
| --- | --- |
| Nombre | MoonWindow |
| Frase | Si tu alunizaje en el polo sur se atrasa, MoonWindow te dice en segundos qué sitios y fechas siguen siendo viables y con cuánto margen. |
| Usuario principal | Ingeniero de planificación de una misión CLPS cuyo lanzamiento se atrasó. |
| Otros usuarios | Docentes y público general, con textos en lenguaje llano en inglés y español. |
| Problema | Reevaluar un sitio y una fecha exige cruzar Quickmap, Moon Trek y Horizons e interpretar datos crudos. En el polo sur, pocos días o pocos kilómetros cambian todo. |
| Desafío | Lunar Landing Site Navigator, NASA Space Apps 2026, sede Santiago del Estero. |

### El concepto que nos distingue: tres márgenes

Los demás equipos muestran posiciones. MoonWindow responde tres preguntas de decisión con el mismo cálculo.

| Margen | Pregunta | Función |
| --- | --- | --- |
| En días | ¿Cuánto puedo atrasarme sin perder la misión? | Tolerancia al retraso |
| En metros | ¿Cuánto Sol gano si elevo el panel? | Control de altura del mástil |
| En kilómetros | ¿Y si aterrizo un poco más allá? | Vecindario del sitio |

## Las funciones elegidas

Son 10 funciones: 5 de núcleo, 4 que nos distinguen y 1 para el relato. Se construyen en este orden y se recortan de abajo hacia arriba.

| Orden | Función | Tipo | Qué hace | Costo |
| --- | --- | --- | --- | --- |
| 1 | Panorama del horizonte | Núcleo | Silueta real del terreno en 360° con el recorrido del Sol y de la Tierra. | Alto |
| 2 | Cuatro métricas | Núcleo | % de tiempo con Sol, noche más larga, % con la Tierra a la vista, corte de comunicación más largo. | Medio |
| 3 | Comparación lado a lado | Núcleo | Dos sitios o dos fechas con las cuatro métricas. | Bajo |
| 4 | Mapa de calor sitio × fecha | Núcleo | Verde si es viable según umbrales que el usuario ajusta. | Medio |
| 5 | Cuenta regresiva | Núcleo | Tiempo hasta la próxima puesta de Sol y de Tierra. | Bajo |
| 6 | Margen en días | Distintiva | Días consecutivos que la fecha puede correrse sin perder viabilidad, más las 3 mejores alternativas. | Bajo |
| 7 | Veredicto de supervivencia | Distintiva | Compara la noche más larga con la autonomía de batería que carga el usuario. | Muy bajo |
| 8 | Margen en metros | Distintiva | Control que sube el panel de 2 a 10 m y muestra cuánto Sol se gana. | Bajo |
| 9 | Margen en kilómetros | Distintiva | Grilla de 5 × 5 puntos alrededor del sitio, coloreada por viabilidad. | Medio |
| 10 | Comparación con Santiago del Estero | Relato | El recorrido del Sol en nuestra ciudad contra el del polo lunar. Va en el video y el pitch. | Bajo |

La tabla de validación y la lista de límites no son funciones opcionales: forman parte del núcleo y aparecen en la web.

### Lo que no hacemos

- Globo 3D de toda la Luna.
- Chatbot de IA.
- Modelo térmico o de batería completo.
- Satélite de retransmisión.
- Cuentas de usuario, servidor en vivo o aplicación móvil.
- Coordenadas libres fuera de los sitios precalculados.

## Cobertura del texto oficial

La idea cubre los 7 objetivos del desafío salvo las coordenadas personalizadas, que quedan parciales; la revisión contra el texto oficial dejó 5 ajustes chicos, marcados como "Agregar".

| Objetivo del desafío | Cómo lo cubrimos | Ajuste |
| --- | --- | --- |
| Selección y comparación de sitios: Apolo, CLPS, otras misiones comerciales, otros países | Lista curada y comparación lado a lado. | Agregar: que los 4 sitios representen esas categorías: 1 de Apolo, 1 de CLPS, 1 de otro país y 1 o 2 candidatos polares. |
| Coordenadas personalizadas | Fuera del alcance: los sitios están precalculados. | Opcional: el vecindario permite elegir cualquiera de sus 25 puntos. Declararlo como límite. |
| Flexibilidad de fecha y hora, días lunares y estaciones | Selector de fecha y hora sobre 24 meses de datos. | Ninguno. |
| Sol y Tierra respecto del horizonte; tiempo hasta la puesta | Panorama y cuenta regresiva. | Ninguno. |
| Evaluación de energía y comunicación; ángulo de elevación solar destacado | Cuatro métricas y veredicto. | Agregar: la elevación solar actual, en grados, como dato grande en las tarjetas. |
| Varias visualizaciones: mapas 2D, 3D u otras | Panorama, mapa de calor y grilla del vecindario. | Ninguno. No hacemos 3D. |
| Dinámica temporal: animaciones o líneas de tiempo | Deslizador de hora. | Agregar: un botón de reproducir que anima un día lunar completo en el panorama. |
| Accesible para planificadores, docentes y público | Interfaz simple en dos idiomas. | Agregar: una frase en lenguaje llano por sitio y fecha, generada con plantillas a partir de los números. |

### Consideraciones del texto oficial

| Consideración | Estado |
| --- | --- |
| Sin refracción; horizonte definido por el terreno y el borde de la esfera lunar | Cubierto: terreno de LOLA más corrección por curvatura. |
| Libración y variaciones orbitales | Cubierto: ya vienen en los ángulos de Horizons. Decirlo en la web. |
| Pendientes y cráteres con sombras extremas | Cubierto por el horizonte del terreno y el vecindario. |
| Por qué cambios pequeños de lugar o fecha tienen gran impacto | Cubierto: es el concepto de los tres márgenes. |
| Diferencia entre condiciones lunares y terrestres | Cubierto: comparación con Santiago del Estero y con un sitio de Apolo. |
| Coordinación entre equipos de ciencia e ingeniería | Agregar: enlace compartible que guarda sitio, fecha y umbrales. |
| Condiciones térmicas | No se modelan. Declarado como límite. |

Los sitios fuera del modelo de elevación polar (Apolo y, según su latitud, el de otro país) usan horizonte plano, y la web lo indica.

## Las pantallas

La web tiene una sola página con cinco zonas. El usuario entra, toca "Ver ejemplo" y ya tiene cargado el caso del retraso.

| Zona | Qué ve el usuario | Qué puede tocar |
| --- | --- | --- |
| Barra superior | Sitio, fecha de alunizaje, duración de la misión e idioma. | Selectores y el botón "Ver ejemplo". |
| Panorama | Eje horizontal de 0° a 360° de azimut, eje vertical de −5° a +10°. Silueta del terreno rellena, línea del Sol, línea de la Tierra y cuenta regresiva. | Deslizador de hora y de altura del mástil. |
| Tarjetas | Las cuatro métricas y el veredicto: sobrevive, al límite o no sobrevive. | Autonomía de batería y corte de comunicación máximo. |
| Márgenes | Mapa de calor sitio × fecha, margen en días con las 3 mejores alternativas y la grilla del vecindario. | Clic en una celda para cargar ese escenario. |
| Confianza | Tabla de validación contra NASA, límites declarados y créditos de datos. | Enlaces a las fuentes. |

La comparación lado a lado duplica las zonas de panorama y tarjetas para un segundo sitio o una segunda fecha.

## Cómo se calcula

Todo se precalcula en Python y la web solo lee archivos JSON, así que la demo no depende de un servidor ni de internet.

1. **Efemérides.** Se pide a la API de JPL Horizons el azimut y la elevación del Sol y de la Tierra, cada hora, para un observador en cada sitio. Se guarda en CSV.
2. **Horizonte.** Con el modelo de elevación de LOLA se calcula, para 360 direcciones y hasta 150 km, el ángulo más alto del terreno, corrigiendo por la curvatura lunar (radio 1737,4 km).
3. **Visibilidad.** Hora por hora: fracción del disco solar por encima del horizonte y si la Tierra supera el horizonte en su dirección.
4. **Métricas.** Para cada sitio y cada fecha de inicio se calculan las cuatro métricas sobre la duración de la misión.
5. **Márgenes.** Se repiten los pasos 2 a 4 con alturas de 2 a 10 m (margen en metros) y en 25 puntos alrededor del sitio (margen en kilómetros). El margen en días se calcula en el navegador.

La fórmula del paso 2, con *h* la diferencia de altura, *d* la distancia y *R* el radio lunar:

```latex
\theta(d) = \arctan\left(\frac{h}{d} - \frac{d}{2R}\right)
```

### Datos

| Dato | Para qué | Fuente |
| --- | --- | --- |
| JPL Horizons | Posición del Sol y la Tierra | [ssd.jpl.nasa.gov/horizons](https://ssd.jpl.nasa.gov/horizons/) |
| Topografía LOLA | Horizonte del terreno | Pendiente: URL exacta del producto descargado |
| LROC Quickmap | Validación | [quickmap.lroc.asu.edu](https://quickmap.lroc.asu.edu/) |
| NASA Moon Trek | Mapa base, si se usa | [trek.nasa.gov/moon](https://trek.nasa.gov/moon/) |

### Validación

| Qué se valida | Contra qué | Cómo se muestra |
| --- | --- | --- |
| Ángulos del Sol y la Tierra | 10 instantes al azar en la web de Horizons | Diferencia en grados |
| Cordura física | En el polo, el Sol no supera unos 1,5° y la Tierra oscila con un ciclo de unos 27 días | Un gráfico |
| Silueta del horizonte | Perfil de elevación de Quickmap en 4 direcciones por sitio | Tabla con la diferencia |
| % de iluminación | Capa de iluminación polar de Quickmap | Diferencia en puntos porcentuales |

Los números de validación se escriben recién cuando estén medidos. Si un valor no existe el domingo, se quita la frase; no se inventa.

## Por qué gana

Responde la pregunta de decisión que plantea el desafío, con datos de NASA como motor y con evidencia en pantalla, en un espacio que la competencia revisada no ocupa.

| Criterio | Qué ve el juez | Puntaje realista |
| --- | --- | --- |
| Impacto | Un retraso de 9 días resuelto en segundos, con la mejor alternativa. Tres públicos, dos idiomas. | 4 |
| Creatividad | Los tres márgenes: días, metros y kilómetros. Una pregunta nueva sobre datos que ya existían. | 4 a 5 |
| Validez | Tabla de validación contra Horizons y Quickmap, límites escritos y demo en línea que no se cae. | 4 a 5 |
| Relevancia | Cubre comparar sitios, comparar fechas, Sol y Tierra contra el terreno real, y métricas de energía y comunicación. | 5 |
| Presentación | Una sola historia: "se atrasó 9 días, ¿sobrevive?". Página completa en inglés y video con subtítulos. | 4 a 5 |

Los puntajes son una estimación propia, suponiendo una ejecución buena y no perfecta.

### Frente a la competencia

Según el relevamiento del 14 de noviembre que nos pasaron, hay al menos 6 repositorios públicos de este desafío con globo 3D, horizonte LOLA y asistente de IA. Ninguno de los leídos mide la tolerancia al retraso. Ese relevamiento no fue verificado desde este documento.

| Qué hacen | Quién | Nuestro lugar |
| --- | --- | --- |
| Globo 3D con marcadores | Casi todos | No lo hacemos |
| Sol y Tierra con horizonte plano | La mayoría | Usamos el terreno real |
| Chatbot que explica el sitio | Muchos | No lo hacemos; la aplicación no usa IA |
| Horizonte de terreno desde LOLA | Varios en el mundo | Lo igualamos y lo validamos |
| Margen en días, metros y kilómetros | No visto | Es nuestro diferencial |

Premio global al que apuntamos: Best Use of Data. Mensaje: "Horizons y LOLA ya existían; MoonWindow los convierte en una respuesta de 10 segundos."

## Plan de construcción

El código se congela el domingo a las 15:00 y la entrega se envía a las 21:30. Si un bloque arranca tarde, se corre, pero esas dos horas no se mueven.

| Persona | Responsabilidad |
| --- | --- |
| P1 | Horizons, métricas, JSON, mapa de calor y margen en días. |
| P2 | Modelo de elevación, horizonte del terreno, margen en metros y en kilómetros, validación. |
| P3 | Web estática, publicación, panorama, comparación y pruebas en celular y proyector. |
| C | Formulario, historia, página en inglés, videos, enlaces de recursos y ensayo del pitch. |

### Bloques

| Cuándo | Qué | Listo cuando | Si no sale |
| --- | --- | --- | --- |
| Sábado, primeras 2 horas | Prueba de Horizons, modelo de elevación abierto, repositorio y web publicada, campos del formulario copiados. | Un sitio de punta a punta: gráfico del Sol contra la silueta. | Si Horizons falla, revisar el texto del error antes de seguir. |
| Sábado hasta las 17:00 | Horizonte de 4 sitios y efemérides de 24 meses. | CSV y horizontes guardados. | Bajar al modelo de 80 m o a 3 sitios. No eliminar el terreno. |
| Sábado hasta las 20:00 | Métricas, panorama y comparación con datos reales. | Una demo fea pero completa de un flujo. | Se posterga todo lo distintivo hasta tener esto. |
| Sábado a la noche | Mapa de calor, margen en días y veredicto de supervivencia. | Mapa en pantalla con umbrales que se mueven. | Queda una tabla de fechas en lugar del mapa. |
| Domingo 9:00 a 12:00 | Margen en metros, margen en kilómetros y validación. | Tabla de validación con diferencias medidas. | Primero cae el margen en kilómetros, después el de metros. La validación no cae. |
| Domingo 12:00 a 15:00 | Pulido, dos idiomas, estados de error y ensayo cronometrado. | Demo sin tropiezos desde otro dispositivo. | Se quita el segundo idioma de la interfaz. |
| Domingo 15:00 | Se congela el código. | Solo arreglos de errores. | — |
| Domingo 15:00 a 18:00 | Video de 30 segundos, video de 2 minutos y README. | Videos subidos y enlaces probados en modo incógnito. | Si el formato lo permite, 7 diapositivas en lugar del video. |
| Domingo 18:00 a 20:00 | Página del proyecto completa y prueba de la demo desde otra red. | Todos los campos cargados. | Nada nuevo entra después de las 20:00. |
| Domingo 21:30 | Envío y captura de la confirmación. | Enviado. | Margen hasta las 23:59 para fallas de conexión. |

Nunca se recorta: horizonte del terreno, comparación, validación, demo en línea y página en inglés.

## El relato

Todo el material cuenta un solo caso: el alunizaje se atrasó 9 días. Los valores entre corchetes se reemplazan por números medidos.

### Video global de 30 segundos

| Segundos | Pantalla | Texto en inglés |
| --- | --- | --- |
| 0 a 5 | Portada con el caso | "Your Moon landing just slipped 9 days. Do you still have sunlight and a link to Earth?" |
| 5 a 13 | Panorama y cambio de fecha | "This is the real skyline from NASA's LOLA data. Nine days later, Earth is behind the ridge." |
| 13 a 23 | Los tres márgenes | "MoonWindow shows your margin: \[N\] days of delay, \[N\] meters of mast, \[N\] kilometers of ground." |
| 23 a 30 | Cierre con créditos | "MoonWindow: from three expert tools to one answer in ten seconds." |

El video debe entenderse sin sonido y llevar subtítulos en inglés.

### Video local de 2 minutos

1. El caso: el módulo iba a alunizar cerca del polo sur y el cohete se atrasó 9 días.
2. El panorama en la fecha original: la silueta real del terreno y el Sol rozando las montañas.
3. La fecha corrida 9 días: la Tierra queda detrás de la cresta y el módulo no sobrevive la noche.
4. Margen en días: el mapa de calor y el sitio vecino que sí tolera el retraso.
5. Margen en metros y en kilómetros: subir el panel y moverse en la grilla.
6. Santiago del Estero contra el polo lunar: por qué allá todo depende de un grado.
7. Validación y límites: la tabla contra NASA y lo que no modelamos.
8. Cierre: "de tres herramientas expertas a una respuesta en diez segundos".

### Los cinco mensajes que el jurado debe llevarse

1. Responde la pregunta del desafío sobre retrasos; no solo muestra datos.
2. El horizonte es el terreno real de LOLA y los ángulos son de Horizons.
3. Mide márgenes de decisión en días, metros y kilómetros.
4. Los números están validados y los límites están declarados.
5. Funciona en el navegador, en dos idiomas, sin instalar nada.

## Límites, riesgos y probabilidades

Ganar a nivel global es muy improbable para cualquier equipo; este plan apunta a la nominación desde la sede y a pelear por ser finalistas.

### Límites que declaramos

- "Viable" es geometría: luz y línea de vista. No hay modelo térmico, de energía detallado ni de antena.
- El veredicto de supervivencia compara dos números; no simula la batería.
- Los sitios están precalculados; fuera de ellos no hay respuesta.
- El paso es de 1 hora: los eventos tienen una precisión de ±30 minutos.
- El modelo de elevación tiene resolución finita; un bloque no resuelto puede tapar el Sol.
- No es una herramienta oficial de NASA.

### Riesgos

| Riesgo | Cómo se evita | Plan B |
| --- | --- | --- |
| La demo falla o el enlace no carga | Web estática precalculada; probar desde otra red. | Video de respaldo. |
| Error de convención: longitud, azimut o proyección polar | Prueba con un sitio conocido antes de procesar todos. | Mostrar solo los casos validados. |
| No sale el horizonte del terreno | Punto de corte del sábado a las 17:00. | Modelo de 80 m y 3 sitios. |
| Falta tiempo para la página y el video | C trabaja en eso desde el sábado; código congelado a las 15:00. | 7 diapositivas, si el formato lo permite. |
| Demasiadas funciones a medias | Orden de recorte fijado: kilómetros, metros, segundo idioma. | Quedarse con el margen en días. |
| Recursos sin citar o IA sin declarar | Lista de enlaces viva desde el primer día. | Revisión cruzada el domingo a las 18:00. |

### Probabilidades

| Resultado | Escenario base | Confianza |
| --- | --- | --- |
| Nominación global desde la sede | 25 a 40 % | Media-baja |
| Finalista global, si nos nominan | 4 a 8 % | Baja |
| Ganador global | 0,2 a 0,6 % | Baja |

Los rangos vienen del relevamiento del 14 de noviembre, que usa las cifras de 2025: unos 11.500 proyectos, 1.290 nominados, 45 finalistas y 10 ganadores. Son un juicio aplicado sobre esas tasas, no un cálculo exacto.

### Pendiente de confirmar

- [ ] ¿El organizador permite usar el modelo de elevación de LOLA descargado de NASA?
- [ ] ¿Cuántos nominados tiene la sede y cómo se reparten?
- [ ] ¿El video local de 2 minutos se sube al mismo formulario?
- [ ] Coordenadas de los 4 sitios, cada una con su fuente.
- [ ] ¿Algún otro equipo ya usa el nombre MoonWindow?
