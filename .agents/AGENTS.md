# 🛡️ Reglas y Directrices para el Glosario de Ciberseguridad

Este documento define los estándares obligatorios de redacción, formato, ortografía y arquitectura que todo agente debe seguir al crear, modificar o validar términos en este repositorio.

---

## 1. Arquitectura y Ubicación de Archivos

- **Directorio de términos**: Todos los términos deben crearse exclusivamente en la carpeta `terminos/` con nombres en formato **kebab-case** en minúsculas (ejemplo: `terminos/cross-site-scripting.md`, `terminos/zero-trust.md`).
- **Limpieza de la raíz**: La raíz del repositorio debe contener únicamente:
  - `terminos/` (carpeta con los artículos).
  - `plantilla.md` (plantilla oficial para nuevos términos).
  - `README.md` (guía de contribución para el alumnado).
  - `.agents/` (configuración y directrices para agentes).
  - Archivos de configuración de Git/GitHub (`.gitignore`, `.github/`).
- **Infraestructura**: Toda la configuración de MkDocs, Docker, hooks de Python y estilos reside en `.mkdocs/`. **Nunca** agregues archivos de configuración de MkDocs en la raíz.

---

## 2. Reglas de Ortografía y Estilo (RAE)

- **Mayúsculas en encabezados y títulos**: En español, los títulos y encabezados llevan mayúscula **únicamente en la primera palabra** y en nombres propios o siglas técnicas (ej. `"Inyección SQL (SQL injection)"`, `"Sistema de prevención de intrusiones (IPS)"`). **Nunca** utilices el estilo anglosajón *Title Case* (poner mayúscula en cada palabra).
- **Punto final en encabezados**: Los encabezados que aparecen aislados en su propia línea **no llevan punto final**.
- **Tono y registro**: Redacción técnica, rigurosa, clara y didáctica, en tercera persona o impersonal.
- **Nombres comunes**: Palabras como *ciberseguridad*, *glosario*, *repositorio*, *firewall*, *encriptación/cifrado* son nombres comunes y se escriben en minúscula.

---

## 3. Metadatos Obligatorios (Frontmatter YAML)

Todo archivo de término en `terminos/*.md` debe iniciar obligatoriamente con el bloque YAML:

```yaml
---
title: "Nombre del término o concepto"
category: "Vulnerabilidades Web"
author: "@usuario-github-real"
tags:
  - ciberseguridad
  - tag-en-kebab-case
summary: "Resumen técnico y conciso de 1 o 2 líneas explicativas (máximo 200 caracteres)."
---
```

### Reglas para los campos:
1. **`title`**: Nombre del término en español con mayúscula inicial según la RAE. Se pueden incluir siglas o nombres en inglés entre paréntesis.
2. **`category`**: Debe asignarse a una categoría técnica clara (ejemplos: `Vulnerabilidades Web`, `Redes / Seguridad de Red`, `Criptografía`, `Identidad y Acceso`, `Operaciones de Seguridad (SOC)`, `Gobernanza y Cumplimiento`, `Seguridad en Sistemas`, `Forense y Respuesta a Incidentes`).
3. **`author`**: Debe ser un identificador de usuario **real** de GitHub precedido por `@` (ejemplo: `"@cibercelia"`). Si no se conoce, utilizar `"Comunidad"`.
4. **`tags`**: Lista de 2 a 5 etiquetas descriptivas en minúsculas y sin espacios.
5. **`summary`**: Texto plano sin etiquetas HTML ni enlaces Markdown, de 1 o 2 frases.
6. ⛔ **PROHIBIDO**: No incluir el campo `difficulty` (fue eliminado del diseño).

---

## 4. Bloque Visual de Metadatos (HTML)

Inmediatamente después del encabezado `# Título`, se debe incluir el bloque de metadatos visual:

```html
<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Vulnerabilidades Web</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/usuario-github" target="_blank">@usuario-github</a></span>
  </div>
</div>
```

---

## 5. Estructura y Secciones del Término

Cada término debe desarrollar de forma clara y exhaustiva las siguientes 5 secciones:

1. `## 📖 Definición`: Explicación conceptual, contexto técnico y origen.
2. `## ⚙️ ¿Cómo funciona? / Principios fundamentales`: Mecanismos, flujo de ejecución, vectores de ataque o componentes.
3. `## 🎯 Ejemplo práctico o escenario de demostración`: Escenario real con código o configuración en pestañas comparativas.
4. `## 🛡️ Medidas de mitigación y buenas prácticas`: Lista de verificación basada en marcos estándar (OWASP, NIST, CIS, etc.).
5. `## 🔗 Referencias y enlaces de interés`: Enlaces a fuentes técnicas primarias y oficiales.

---

## 6. Sintaxis Específica de Material for MkDocs

- **Avisos destacados (Admonitions)**: Utiliza siempre la sintaxis de MkDocs con 4 espacios de sangrado:
  ```markdown
  !!! note "Nota importante"
      Texto explicativo...

  !!! warning "Advertencia de seguridad"
      Texto de advertencia...
  ```
  *(Nunca uses la sintaxis de GitHub `> [!NOTE]` o `> [!WARNING]`)*.

- **Pestañas de contenido (Content Tabs)**:
  ```markdown
  === "Escenario vulnerable / incorrecto"

      ```python
      # Código vulnerable
      ```

  === "Escenario seguro / remediado"

      ```python
      # Código mitigado
      ```
  ```

---

## 7. Verificación y Calidad

Antes de dar por finalizado un término o cambio:
- Comprueba que el YAML sea válido y no contenga tabulaciones (`\t`).
- Verifica que los enlaces Markdown relativos no generen errores 404.
- Ejecuta la prueba local del hook si realizas cambios en scripts: `python3 .mkdocs/hooks/generate_glossary_index.py`.
