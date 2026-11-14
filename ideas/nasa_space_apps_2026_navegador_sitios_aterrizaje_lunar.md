# NASA Space Apps Challenge 2026
# Navegador de sitios de aterrizaje lunar (Lunar Landing Site Navigator)

**[Unirse al desafío](https://www.spaceappschallenge.org/2026/challenges/lunar-landing-site-navigator//?tab=teams)**

---

## 1. Información general del desafío

- **Evento:** NASA Space Apps Challenge 2026.
- **Dificultad:** Avanzado / Intermedio.
- **Temáticas:**
  - Exploración humana.
  - Luna.
  - Software.
  - Exploración espacial.

### Descripción del desafío

Las misiones destinadas al polo sur de la Luna enfrentan condiciones extremas de iluminación y comunicación. Su planificación requiere una coordinación cuidadosa entre los equipos científicos y de ingeniería.

Existen herramientas para determinar las posiciones del Sol y de la Tierra en posibles sitios de aterrizaje, pero sus interfaces complejas dificultan la evaluación eficiente de información fundamental.

El desafío consiste en desarrollar una herramienta o aplicación intuitiva que permita a los planificadores de misiones, educadores y al público comparar rápidamente diferentes sitios de aterrizaje y fechas.

La solución deberá visualizar las posiciones del Sol y de la Tierra con respecto al horizonte lunar, permitiendo evaluar:

- El potencial de generación de energía solar.
- Las ventanas de comunicación directa con la Tierra.
- Las condiciones de iluminación.
- La viabilidad de diferentes combinaciones de ubicación y fecha de aterrizaje.

---

# 2. Antecedentes (Background)

El programa de Servicios Comerciales de Carga Lunar (CLPS) de la NASA y otras misiones lunares dependen de una selección cuidadosa de los sitios y las fechas de aterrizaje, equilibrando las necesidades de los equipos científicos y de ingeniería.

Uno de los desafíos más importantes de este proceso es comprender las condiciones locales de iluminación y comunicación de un posible sitio de aterrizaje.

La posición del Sol determina:

- La disponibilidad de energía para los paneles solares.
- Las condiciones térmicas de los equipos.
- Las posibilidades de generación de energía durante la misión.

Por su parte, la posición de la Tierra determina si es posible establecer una comunicación directa sin necesidad de utilizar satélites de retransmisión.

Este desafío es especialmente importante en el polo sur lunar, donde se planifican numerosas misiones futuras debido a la presencia de hielo de agua y otros recursos de gran valor científico.

La geometría del polo sur genera variaciones extremas en la iluminación solar y en la visibilidad de la Tierra a lo largo de los días lunares y las distintas estaciones.

Pequeñas modificaciones en la ubicación del aterrizaje o en la fecha seleccionada pueden afectar considerablemente:

- El potencial de generación de energía.
- Las ventanas de comunicación.
- La viabilidad general de la misión.

Por este motivo, resulta fundamental poder evaluar rápidamente diferentes sitios y escenarios.

En la práctica, el desarrollo de una misión no siempre sigue un cronograma fijo. Los problemas durante el desarrollo del hardware, los retrasos en los lanzamientos u otros factores pueden obligar a los planificadores a reconsiderar la fecha o ubicación original del aterrizaje.

Cuando esto sucede, los ingenieros necesitan evaluar rápidamente:

- Sitios alternativos dentro de una misma región.
- Fechas alternativas para un mismo sitio.
- El impacto de estos cambios sobre la viabilidad de la misión.

Una herramienta que permita comparar múltiples escenarios de manera rápida e intuitiva facilitaría la toma de decisiones y ayudaría a identificar alternativas viables cuando cambian las condiciones iniciales.

Actualmente existen herramientas que proporcionan esta información, como:

- NASA QuickMap.
- Moon Trek.
- Sistema JPL Horizons.

Sin embargo, estas plataformas están diseñadas para realizar análisis detallados y pueden resultar difíciles de utilizar para personas que no son especialistas o que necesitan comparar escenarios rápidamente.

Evaluar cada combinación de sitio y fecha requiere navegar por diferentes interfaces e interpretar datos técnicos sin procesar.

Esto genera una brecha entre la información científica disponible y las herramientas accesibles necesarias para una planificación ágil de las misiones.

Una interfaz intuitiva que transforme datos complejos de efemérides y topografía en visualizaciones claras y comparables podría ayudar a resolver este problema.

---

# 3. Objetivos del desafío (Objectives)

El objetivo es desarrollar una herramienta o aplicación que permita evaluar rápidamente diferentes opciones de sitios de aterrizaje lunar.

La solución puede incluir las siguientes funcionalidades:

## 3.1. Selección y comparación interactiva de sitios

Se puede permitir que los usuarios seleccionen sitios de aterrizaje de una lista de ubicaciones relevantes, como:

- Sitios de aterrizaje de misiones Apollo anteriores.
- Objetivos de futuras misiones CLPS.
- Sitios de aterrizaje de otras misiones lunares comerciales.
- Sitios de aterrizaje de programas lunares de otros países.

También se puede ofrecer la posibilidad de introducir coordenadas lunares personalizadas.

La herramienta podría permitir comparar varios sitios de manera simultánea o secuencial para evaluar rápidamente las ventajas y desventajas de cada ubicación.

## 3.2. Flexibilidad de fechas y horarios

Permitir que los usuarios seleccionen fechas y horarios de aterrizaje.

También se pueden incorporar herramientas para explorar cómo cambian las condiciones durante diferentes días lunares o períodos.

Esto permitiría comprender cómo los cambios en el cronograma de una misión afectan su viabilidad.

## 3.3. Visualización de las posiciones del Sol y la Tierra

Mostrar las posiciones del Sol y de la Tierra con respecto al horizonte desde un sitio de aterrizaje seleccionado y en una fecha determinada.

Se puede incluir información sobre:

- Tiempo restante hasta el atardecer lunar.
- Tiempo restante hasta que la Tierra deje de ser visible.
- Posición angular del Sol.
- Posición angular de la Tierra.

Esta información resulta fundamental para comprender los períodos disponibles de generación de energía y comunicación.

## 3.4. Evaluación de energía y comunicación

Destacar indicadores importantes, como:

- **Ángulo de elevación solar:** influye en la eficiencia de generación de energía.
- **Duración de la luz solar:** tiempo durante el cual el sitio recibe iluminación.
- **Ventanas de visibilidad de la Tierra:** períodos durante los cuales es posible establecer comunicación directa.

Estos indicadores ayudarán a los planificadores a determinar rápidamente si una combinación de sitio y fecha es viable.

## 3.5. Diferentes enfoques de visualización

Se pueden explorar diferentes formas de representar la información:

- Mapas 2D.
- Visualizaciones de superficies 3D.
- Representaciones espaciales interactivas.
- Otras formas creativas de visualizar las relaciones entre el sitio de aterrizaje, el Sol y la Tierra.

## 3.6. Dinámica temporal

Se pueden incorporar animaciones o líneas de tiempo que muestren cómo cambian las posiciones del Sol y de la Tierra:

- Durante un día lunar.
- A lo largo de varios días.
- En diferentes fechas de una misión.

Esto permitirá comprender la duración y los horarios de las ventanas operativas.

## 3.7. Accesibilidad para diferentes niveles de conocimiento

La herramienta puede estar destinada a diferentes tipos de usuarios:

- **Planificadores de misiones:** necesitan información técnica detallada para tomar decisiones rápidamente.
- **Educadores:** buscan explicar los desafíos de la exploración lunar.
- **Público general:** tiene curiosidad por conocer las particularidades de la Luna y sus desafíos tecnológicos.

Se recomienda desarrollar una solución creativa y accesible.

Puede tratarse de:

- Una aplicación web.
- Una aplicación móvil.
- Una visualización interactiva.
- Un videojuego educativo.
- Otro formato que permita evaluar los sitios de aterrizaje de manera clara y eficiente.

---

# 4. Consideraciones potenciales (Potential Considerations)

Los siguientes aspectos pueden tenerse en cuenta durante el desarrollo, aunque no son obligatorios.

## 4.1. Enfoque técnico

### Datos de efemérides

Los datos de efemérides permiten conocer las posiciones y movimientos de los cuerpos celestes.

Se pueden calcular utilizando herramientas como el Sistema JPL Horizons o mediante conjuntos de datos previamente calculados.

### Datos topográficos lunares

Los datos de topografía lunar, como los obtenidos por el instrumento Lunar Orbiter Laser Altimeter (LOLA), pueden utilizarse para:

- Crear visualizaciones realistas de la superficie.
- Calcular con precisión el horizonte.
- Analizar las características del terreno.

### Cálculo del horizonte lunar

Se debe considerar cómo calcular la posición del horizonte teniendo en cuenta que la Luna no tiene atmósfera.

A diferencia de la Tierra, no existe refracción atmosférica. Por lo tanto, el horizonte está determinado por:

- La topografía local.
- Las elevaciones del terreno.
- El borde de la esfera lunar observado desde el sitio de aterrizaje.

### Ángulo de elevación solar

El ángulo de elevación solar es un indicador fundamental para evaluar la generación de energía.

Se recomienda calcularlo y mostrarlo de manera destacada en la aplicación.

## 4.2. Experiencia de usuario

La interfaz podría priorizar la comparación rápida de escenarios para que los planificadores puedan evaluar eficientemente múltiples combinaciones de sitios y fechas.

Se recomienda considerar:

- Cómo comunicar claramente el tiempo restante hasta el atardecer o hasta que la Tierra deje de ser visible.
- Cómo mostrar las diferencias extremas entre las condiciones lunares y terrestres.
- Cómo explicar por qué pequeños cambios en la ubicación o fecha pueden tener un impacto importante en la viabilidad de una misión.

## 4.3. Datos y precisión

Se pueden considerar los siguientes aspectos:

### Topografía real de la Luna

Es importante considerar la topografía real, ya que la elevación del terreno puede modificar significativamente:

- La posición del horizonte.
- Las ventanas de visibilidad.
- Las condiciones de iluminación.

### Libración terrestre y variaciones orbitales

Se puede evaluar si la herramienta tendrá en cuenta factores como:

- La libración de la Tierra (movimiento aparente u oscilación).
- Las variaciones de la órbita lunar.

### Complejidad del terreno del polo sur

El terreno del polo sur presenta características particularmente complejas.

Se pueden representar:

- Pendientes pronunciadas.
- Cráteres profundos.
- Regiones con sombras extremas.
- Zonas con iluminación limitada.

## 4.4. Participación e impacto

La solución podría ayudar a los planificadores de misiones a coordinar el trabajo entre los equipos científicos y de ingeniería durante el desarrollo de una misión.

También podría:

- Facilitar respuestas rápidas ante cambios en los cronogramas.
- Ayudar a evaluar alternativas cuando surgen problemas durante el desarrollo del hardware.
- Permitir ajustar las fechas o ubicaciones de aterrizaje.
- Servir como herramienta educativa para estudiantes y público general.
- Explicar los desafíos de la exploración lunar y la complejidad de planificar una misión.

**Importante:** Para consultar los datos y recursos relacionados con este desafío, se debe revisar la pestaña «Recursos» ubicada en la parte superior de la página. Es posible que se agreguen nuevos recursos antes del comienzo del hackathon.

---

# 5. Datos y recursos de la NASA

## 5.1. Aviso sobre el uso de datos

La NASA no respalda a ningún país que no sea Estados Unidos.

Como entidad gubernamental, no es responsable de la información contenida en datos que no provengan de Estados Unidos.

En el caso de los sitios web gubernamentales de otros países, los participantes deberán cumplir con las condiciones y restricciones de uso de datos establecidas por cada sitio web.

## 5.2. Recursos de la NASA

### 5.2.1. QuickMap

**Enlace:** https://quickmap.lroc.asu.edu/

Herramienta de cartografía interactiva desarrollada por la Universidad Estatal de Arizona (ASU).

Proporciona acceso a:

- Imágenes lunares de alta resolución.
- Datos topográficos.
- Diferentes conjuntos de datos del Orbitador de Reconocimiento Lunar (LRO) de la NASA.

QuickMap permite explorar sitios de aterrizaje, visualizar el terreno y comprender en detalle la superficie lunar.

Es especialmente útil para estudiar la compleja topografía de las regiones del polo sur lunar.

### 5.2.2. Moon Trek

**Enlace:** https://trek.nasa.gov/moon/

Herramienta interactiva de visualización 3D desarrollada por la NASA para la exploración lunar.

Moon Trek permite:

- Explorar la superficie lunar.
- Visualizar datos topográficos.
- Analizar el terreno de posibles sitios de aterrizaje.
- Comprender espacialmente las ubicaciones lunares.
- Visualizar cómo el terreno afecta las posiciones del horizonte.

Proporciona una interfaz intuitiva para estudiar las características geográficas de la Luna.

### 5.2.3. Sistema JPL Horizons

**Enlace:** https://ssd.jpl.nasa.gov/horizons/

Potente herramienta de cálculo de efemérides desarrollada por el Laboratorio de Propulsión a Chorro (JPL) de la NASA.

Permite calcular las posiciones y velocidades de diferentes cuerpos celestes, incluidos el Sol y la Tierra, observados desde cualquier ubicación de la Luna.

Puede utilizarse para obtener:

- Posiciones angulares precisas del Sol.
- Posiciones angulares precisas de la Tierra.
- Datos correspondientes a momentos específicos.
- Datos correspondientes a ubicaciones específicas.

Esta información constituye la base para desarrollar las visualizaciones y evaluaciones de energía y comunicación de la aplicación.

---

# 6. Recursos de socios de agencias espaciales

## 6.1. Agencia Espacial Canadiense (CSA)

### Exploración lunar

**Enlace:** https://www.asc-csa.gc.ca/eng/astronomy/moon-exploration/

Portal de exploración lunar de la Agencia Espacial Canadiense.

Permite conocer las misiones lunares pasadas, actuales y futuras.

Incluye información sobre:

- Las contribuciones de Canadá a la exploración lunar.
- Tecnologías desarrolladas.
- Investigaciones científicas.
- Participación canadiense en el programa Artemis.

---

# 7. Componentes de entrega del proyecto (NASA Space Apps Challenge 2026)

Al presentar el proyecto, se deberán completar los siguientes apartados.

## 7.1. Resumen general del proyecto

**Nombre del proyecto**

Proporcionar un resumen general del proyecto de entre **50 y 200 palabras**.

Se deben responder las siguientes preguntas:

- ¿Qué desarrollaron?
- ¿Cómo aborda el proyecto el desafío?
- ¿Por qué es importante?

## 7.2. Enlace a la demostración del proyecto y enlace al proyecto

Se debe proporcionar una demostración breve (*demo*) del proyecto.

**IMPORTANTE: Incluir solamente UN enlace.**

Se puede elegir una de las siguientes alternativas:

### Opción A. Presentación de diapositivas

- Máximo 7 diapositivas.
- Si se incluye una diapositiva de título, también cuenta dentro del límite de 7 diapositivas.

### Opción B. Presentación en video

- Duración de 30 segundos.
- Puede estar en el idioma nativo del equipo.
- Debe incluir subtítulos en inglés.

### Requisitos de publicación y acceso

La demostración y el proyecto deben subirse a un sitio externo, como un servicio de alojamiento en la nube o un repositorio de código.

Algunas opciones son:

- YouTube.
- Google Drive.
- GitHub.
- OneDrive.
- Dropbox.
- Otros servicios similares.

Se deberá proporcionar un enlace de acceso público.

Si se creó un sitio web nuevo, se recomienda solicitar una clasificación de filtro web (*Web Filter Rating*).

Se debe confirmar que el acceso a la demostración:

- No requiere contraseña.
- No requiere permisos especiales.
- No requiere registro.
- Está disponible públicamente.

Se recomienda probar el enlace con usuarios que no hayan iniciado sesión para confirmar que pueden acceder correctamente.

**Restricción de contenido:** No se deben incluir nombres, voces ni imágenes de ninguna persona menor de 18 años.

## 7.3. Detalles del proyecto

Proporcionar información adicional sobre el funcionamiento y desarrollo de la solución.

Algunas preguntas que pueden orientar esta sección son:

- ¿Qué hace exactamente el proyecto?
- ¿Cómo funciona?
- ¿Qué beneficios tiene?
- ¿Qué esperan lograr?
- ¿Qué herramientas utilizaron?
- ¿Qué lenguajes de programación utilizaron?
- ¿Qué hardware o software utilizaron para desarrollar el proyecto?

## 7.4. Uso de IS (Inteligencia Sintética)

Se permite utilizar herramientas que aceleren la innovación y la creatividad durante el desarrollo de la solución.

Entre ellas se incluyen, pero no se limitan a:

- Modelos de Lenguaje de Gran Escala (LLM).
- Chatbots.
- Herramientas de generación de imágenes.
- Herramientas de generación de video.
- Modelos fundacionales.
- Herramientas de generación de código.

### Requisitos

Se deberá seleccionar en el menú desplegable todas las herramientas de Inteligencia Sintética utilizadas.

Sin embargo, el contenido generado no puede utilizar, contener ni modificar ningún elemento de marca o diseño de la NASA, como:

- Logotipos.
- Banderas.
- Identificadores de misiones de la NASA.

Se deberá indicar dónde y cómo se utilizaron estas herramientas dentro del proyecto.

Esta información puede comunicarse mediante:

- Una marca de agua.
- Una descripción del proyecto.

### Importante

Esta pregunta es obligatoria y se utilizará únicamente con fines de recopilación de datos.

Los jueces no verán la respuesta proporcionada en este apartado.

Sin embargo, sí podrán visualizar cualquier indicador de contenido generado mediante Inteligencia Sintética que esté presente en el proyecto, como marcas de agua, textos descriptivos o metadatos.

## 7.5. Datos de la NASA

La NASA proporciona datos sugeridos para cada desafío en la pestaña «Recursos».

**Requisito obligatorio para optar a premios globales:**

Se debe utilizar al menos un recurso de la NASA correspondiente al desafío.

Se deberá responder:

- ¿Qué datos de la NASA utilizaron en el proyecto?
- ¿Qué recursos consultaron?
- ¿Qué enlaces corresponden a los datos utilizados?

Se deben proporcionar los enlaces de todos los recursos de la NASA utilizados.

## 7.6. Datos de agencias espaciales asociadas y otros recursos

En la pestaña «Recursos» también se proporcionan datos espaciales sugeridos para cada desafío.

Se deberá responder:

- ¿Qué datos de las agencias espaciales asociadas al Space Apps Challenge utilizaron?
- ¿Qué otros recursos utilizaron durante el desarrollo?

El uso de datos de agencias espaciales asociadas es opcional, aunque se recomienda.

En este apartado también se pueden incluir todas las demás referencias utilizadas.

### Recursos que deben documentarse

Se deben proporcionar enlaces a todos los datos y recursos utilizados en el proyecto.

Esto incluye:

- Código.
- Textos.
- Imágenes.
- Recursos de código abierto.
- Recursos de acceso libre.
- Otras fuentes utilizadas durante el desarrollo.

---

# 8. Criterios de evaluación

En cada etapa de evaluación, desde los Eventos Locales y Universales hasta la Evaluación Ejecutiva, el proyecto será calificado en una escala del **1 al 5** en cada uno de los siguientes criterios.

## 8.1. Impacto

Evalúa si el proyecto genera un impacto al abordar un problema, ya sea pequeño o significativo.

Se considera la calidad y cantidad de sus efectos generales, así como su capacidad para inspirar o ayudar a otras personas.

El alcance puede variar desde un grupo específico hasta una audiencia amplia.

### Puntuación 5: Impacto sobresaliente

El proyecto demuestra un impacto excepcional al abordar un problema significativo mediante soluciones propuestas.

Su alcance es amplio y tiene la capacidad de inspirar y beneficiar a una gran audiencia o incluso cambiar el mundo.

La calidad y efectividad de la solución superan ampliamente las expectativas y establecen un estándar elevado para otros proyectos.

## 8.2. Creatividad

Evalúa la originalidad y la innovación del proyecto.

Se considera si introduce:

- Un concepto novedoso que no se había intentado anteriormente.
- Una mejora significativa sobre ideas existentes.
- Una perspectiva diferente.
- Una ejecución creativa e inventiva.

### Puntuación 5: Altamente creativo e innovador

El proyecto demuestra una creatividad notable mediante un enfoque revolucionario que nunca antes se había intentado.

Desafía los métodos convencionales y presenta una solución propuesta original e inventiva que se destaca dentro de su campo.

La singularidad de la idea la convierte en una verdadera innovación.

## 8.3. Validez

Evalúa si la solución propuesta está fundamentada en principios científicos y demuestra viabilidad técnica, funcional o lógica.

Se considera si el proyecto:

- Está diseñado para cumplir eficazmente su propósito.
- Tiene potencial para funcionar en aplicaciones reales.
- Presenta un desarrollo completo.
- Es usable y fácil de utilizar.
- Resulta accesible y práctico.

La solución puede estar completamente desarrollada o todavía necesitar mejoras importantes.

### Puntuación 5: Altamente válido y viable

La solución propuesta es científicamente sólida y técnicamente viable.

Demuestra una fuerte alineación con los principios establecidos.

Está completamente desarrollada y preparada para su implementación en el mundo real.

Cumple eficazmente su propósito y presenta una excelente usabilidad, facilitando su aplicación generalizada.

## 8.4. Relevancia

Evalúa si el proyecto aborda de manera directa y completa el desafío para el cual fue presentado.

Se considera especialmente la integración de los datos de la NASA.

Los datos deben formar parte fundamental de la solución propuesta y no ser simplemente un agregado superficial.

Su utilización debe mejorar la credibilidad y efectividad del proyecto.

### Puntuación 5: Altamente relevante y con fuerte integración de datos de la NASA

El proyecto demuestra una relación directa y profunda con los objetivos del desafío.

Los datos de la NASA son fundamentales para el funcionamiento y el éxito de la solución propuesta.

Su utilización está correctamente implementada y proporciona información significativa que impulsa la innovación.

La integración de estos datos mejora tanto la credibilidad como el impacto del proyecto.

## 8.5. Presentación

Evalúa la capacidad del equipo para comunicar eficazmente su proyecto.

Se considera si el equipo logra transmitir claramente:

- El desafío abordado.
- La solución propuesta.
- El funcionamiento del proyecto.
- Su importancia.
- Su impacto potencial.

La narrativa debe ser atractiva y estar bien estructurada para que la audiencia comprenda el propósito y el valor del trabajo realizado.

La claridad, organización y calidad de la presentación son fundamentales.

Los jueces evalúan tanto la demostración como el proyecto completo para determinar esta puntuación.

### Puntuación 5: Comunicación y narrativa excepcionales

El equipo presenta una exposición convincente y bien estructurada.

Comunica claramente el desafío, la solución propuesta y la importancia del proyecto.

La narrativa es atractiva y permite que la audiencia comprenda plenamente la importancia y el impacto potencial del trabajo.

La presentación está bien organizada, es profesional y resulta altamente efectiva para transmitir las ideas.

---

# 9. Recomendaciones para la presentación del proyecto

Aunque muchos equipos del NASA Space Apps Challenge prestan especial atención a los primeros cuatro criterios de evaluación y se destacan desarrollando proyectos con gran potencial, es importante dedicar la misma atención al último criterio: **la presentación**.

Se recomienda dedicar tiempo y recursos a:

- Desarrollar una presentación clara y atractiva.
- Construir una buena historia alrededor del proyecto.
- Explicar el problema que se busca resolver.
- Mostrar cómo funciona la solución.
- Comunicar el valor y el impacto potencial del trabajo.

También se recomienda incorporar integrantes con habilidades diversas, incluyendo experiencia en:

- Narrativa (*storytelling*).
- Diseño.
- Comunicación.
- Documentación.
- Presentación de proyectos.

Estas habilidades ayudarán a documentar el proyecto y comunicar el valor de la solución al mundo.

Para obtener más consejos sobre cómo crear una demostración efectiva, se recomienda consultar la **Guía de Presentación de Proyectos**.

---

# 10. Lista de verificación para la entrega

Esta lista reúne los principales requisitos que se deben completar antes de enviar el proyecto.

## Información general

- [ ] Nombre del proyecto.
- [ ] Resumen de entre 50 y 200 palabras.
- [ ] Explicación del problema y la solución.
- [ ] Explicación de la importancia del proyecto.

## Demostración y publicación

- [ ] Preparar una presentación de máximo 7 diapositivas o un video de 30 segundos.
- [ ] Elegir solamente un enlace para la demostración.
- [ ] Publicar el proyecto en una plataforma externa.
- [ ] Configurar el acceso como público.
- [ ] Verificar que no se requiera contraseña, permiso ni registro.
- [ ] Probar el acceso sin iniciar sesión.
- [ ] No incluir nombres, voces ni imágenes de menores de 18 años.

## Detalles técnicos

- [ ] Explicar qué hace el proyecto.
- [ ] Describir cómo funciona.
- [ ] Explicar sus beneficios.
- [ ] Indicar qué se espera lograr.
- [ ] Detallar herramientas y tecnologías utilizadas.
- [ ] Indicar lenguajes de programación.
- [ ] Identificar hardware y software utilizados, si corresponde.

## Inteligencia Sintética

- [ ] Seleccionar todas las herramientas de IS utilizadas.
- [ ] Explicar dónde y cómo se utilizaron.
- [ ] Incluir los indicadores correspondientes, si corresponde.
- [ ] Verificar que el contenido generado no utilice ni modifique elementos de marca o diseño de la NASA.

## Datos y recursos

- [ ] Utilizar al menos un recurso de la NASA correspondiente al desafío.
- [ ] Documentar todos los datos de la NASA utilizados.
- [ ] Incorporar los enlaces de los recursos.
- [ ] Documentar los datos de agencias espaciales asociadas, si se utilizaron.
- [ ] Incorporar todas las referencias adicionales.
- [ ] Documentar código, textos, imágenes y otros materiales utilizados.

## Preparación de la evaluación

- [ ] Revisar el impacto del proyecto.
- [ ] Revisar su creatividad e innovación.
- [ ] Comprobar su validez científica y técnica.
- [ ] Verificar su relevancia respecto del desafío.
- [ ] Preparar una presentación clara y convincente.
- [ ] Construir una narrativa que explique el problema, la solución y su importancia.

---

# 11. Resumen de los aspectos más importantes

| Aspecto | Requisito |
|---|---|
| Desafío | Lunar Landing Site Navigator |
| Evento | NASA Space Apps Challenge 2026 |
| Objetivo | Comparar sitios y fechas de aterrizaje lunar |
| Elementos principales | Sol, Tierra, horizonte, iluminación y comunicación |
| Demo | Máximo 7 diapositivas o video de 30 segundos |
| Enlace de demo | Solamente uno |
| Resumen | Entre 50 y 200 palabras |
| Datos NASA | Al menos un recurso del desafío para optar a premios globales |
| Uso de IS | Declaración obligatoria |
| Recursos | Documentar todos los datos y materiales utilizados |
| Evaluación | 5 criterios, cada uno con puntuación de 1 a 5 |

**Los cinco criterios de evaluación son:**

1. Impacto.
2. Creatividad.
3. Validez.
4. Relevancia.
5. Presentación.

**Prioridad fundamental:** desarrollar una solución funcional, científicamente válida, directamente relacionada con el desafío y que integre datos reales de la NASA. Además, comunicarla mediante una demostración clara y una narrativa convincente.
