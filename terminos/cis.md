---
title: "CIS (Center for Internet Security)"
category: "Seguridad de sistemas"
author: "@Honestdwarf9573"
tags:
  - ciberseguridad
  - cis
  - cis-controls
  - cis-benchmarks
summary: "Organización sin ánimo de lucro que desarrolla controles y guías de configuración para ayudar a las organizaciones a reducir sus riesgos de ciberseguridad."
---

# CIS (Center for Internet Security)

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Seguridad de sistemas</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Denominación</span>
    <span class="term-meta-value">Center for Internet Security (CIS)</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor</span>
    <span class="term-meta-value">Comunidad</span>
  </div>
</div>

## 📖 Definición

El **Center for Internet Security (CIS)** es una organización independiente y sin ánimo de lucro que desarrolla recursos para ayudar a las organizaciones a proteger sus sistemas y datos frente a amenazas de ciberseguridad. Entre sus iniciativas más conocidas están los **CIS Controls**, un conjunto priorizado de salvaguardas de seguridad, y los **CIS Benchmarks**, guías técnicas para configurar de forma segura productos y plataformas concretos.

El término **CIS** puede referirse a la organización o, de manera informal, a sus recomendaciones. Conviene especificar el recurso concreto: los Controls orientan qué prácticas de seguridad implantar, mientras que los Benchmarks describen cómo configurar tecnologías específicas. Ambos pueden servir como referencia para un programa de bastionado, pero no sustituyen la evaluación de riesgos ni las obligaciones legales de cada organización.

!!! note "CIS no es una certificación"
    Aplicar un CIS Benchmark o utilizar los CIS Controls no significa, por sí solo, que una organización esté certificada ni que sus sistemas sean invulnerables. Las recomendaciones deben seleccionarse, probarse y adaptarse al contexto operativo.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales

CIS publica recursos que permiten abordar la seguridad desde dos perspectivas complementarias:

1. **Priorizar salvaguardas con CIS Controls**: los controles agrupan acciones para reducir riesgos comunes, como gestionar activos, proteger cuentas, mantener software actualizado y recopilar registros. Sus grupos de implementación ayudan a adaptar el alcance a los recursos y al nivel de riesgo de cada organización.
2. **Aplicar configuraciones con CIS Benchmarks**: cada Benchmark recoge recomendaciones técnicas para una plataforma o producto, como un sistema operativo, una base de datos o un servicio en la nube. Algunas guías ofrecen niveles de recomendación con distintos requisitos de seguridad y compatibilidad.
3. **Evaluar el entorno real**: se compara la configuración existente con las salvaguardas o recomendaciones seleccionadas. Herramientas como CIS-CAT pueden ayudar a evaluar determinados sistemas frente a los Benchmarks compatibles.
4. **Planificar e implantar cambios**: se priorizan las desviaciones, se prueban las medidas en un entorno controlado y se documentan los cambios y las excepciones justificadas.
5. **Verificar y mantener**: se comprueba que los cambios no interrumpen los servicios, se supervisan las desviaciones y se repite la evaluación cuando cambian los sistemas o las guías.

---

## 🎯 Ejemplo práctico o escenario de demostración

Una organización quiere bastionar sus servidores Ubuntu y utilizar las recomendaciones CIS como línea base. No debería aplicar indiscriminadamente todas las opciones sin revisar su impacto: primero identifica qué servicios ofrece cada servidor, selecciona el Benchmark y el nivel apropiados, y prueba los cambios antes de extenderlos.

=== "Aplicación deficiente"

    - Se ejecuta una herramienta de evaluación sin confirmar que el Benchmark corresponde a la versión del sistema.
    - Se aplican todas las recomendaciones de forma automática, incluidas las que pueden deshabilitar servicios necesarios.
    - No se documentan las excepciones ni se verifica el funcionamiento de las aplicaciones.

=== "Aplicación controlada"

    1. Se inventarían los servidores y se confirma la versión y el propósito de cada uno.
    2. Se consulta el CIS Benchmark correspondiente y se selecciona un nivel compatible con los requisitos del entorno.
    3. Se evalúa una muestra y se revisan los resultados para distinguir desviaciones relevantes de recomendaciones no aplicables.
    4. Se prueban los cambios en un entorno de preproducción, se documentan las excepciones y se prepara una vía de reversión.
    5. Se despliegan los cambios por etapas y se vuelve a evaluar la configuración para comprobar el resultado.

---

## 🛡️ Medidas de mitigación y buenas prácticas

- [x] **Elegir el recurso adecuado**: usar CIS Controls para priorizar salvaguardas organizativas y CIS Benchmarks para revisar configuraciones técnicas.
- [x] **Ajustar las recomendaciones al contexto**: considerar el riesgo, la función del activo, las dependencias, los requisitos legales y la disponibilidad del servicio.
- [x] **Validar versión y alcance**: comprobar que la guía corresponde al producto y versión desplegados, y revisar qué recomendaciones son aplicables.
- [x] **Probar antes de desplegar**: aplicar cambios primero en un entorno de pruebas o a un grupo reducido de sistemas y verificar el funcionamiento de las aplicaciones.
- [x] **Documentar excepciones**: registrar el motivo, los activos afectados, los controles compensatorios y la fecha de revisión de cada excepción.
- [x] **Medir y revisar periódicamente**: reevaluar la configuración, gestionar las desviaciones y actualizar la línea base cuando cambie el entorno o se publique una guía revisada.

---

## 🔗 Referencias y enlaces de interés

- [Center for Internet Security: sitio oficial](https://www.cisecurity.org/about-us)
- [CIS Critical Security Controls](https://www.cisecurity.org/controls)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [CIS-CAT Pro Assessor](https://www.cisecurity.org/cis-cat-pro)