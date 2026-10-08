---
name: redactar-termino
description: >-
  Crea, redacta, formatea, audita o actualiza términos técnicos para el Glosario
  Colaborativo de Ciberseguridad siguiendo estrictamente la plantilla oficial,
  las normas ortográficas de la RAE y la sintaxis de Material for MkDocs.
---

# Redacción y Validación de Términos del Glosario

Esta guía operacional instruye al agente sobre cómo crear o modificar términos técnicos de ciberseguridad en el repositorio, garantizando el cumplimiento de todos los estándares de diseño, metadatos y calidad editorial.

---

## 1. Verificación Inicial y Nomenclatura

1. **Evitar duplicados**: Comprueba en la carpeta `terminos/` si el término ya existe antes de redactar uno nuevo.
2. **Nombre del archivo**: Debe estar en minúsculas y formato **kebab-case**, con extensión `.md` dentro de `terminos/` (ejemplo: `terminos/ataque-man-in-the-middle.md`).
3. **Plantilla base**: Utiliza siempre como referencia estructural el archivo `plantilla.md` de la raíz.

---

## 2. Bloque Frontmatter YAML

El archivo debe comenzar en la línea 1 con delimitadores `---`:

```yaml
---
title: "Título del término con mayúscula solo inicial"
category: "Categoría temática estandarizada"
author: "@usuario-github-real"
tags:
  - ciberseguridad
  - tag-en-kebab-case
summary: "Resumen técnico de 1 o 2 líneas explicativas (máximo 200 caracteres)."
---
```

### Reglas críticas de metadatos:
- **`title`**: Seguir la regla RAE (mayúscula solo en la primera palabra y siglas/nombres propios).
- **`category`**: Escoger una de las categorías del glosario (`Vulnerabilidades Web`, `Redes / Seguridad de Red`, `Criptografía`, `Identidad y Acceso`, `Operaciones de Seguridad (SOC)`, `Gobernanza y Cumplimiento`, `Seguridad en Sistemas`, `Forense y Respuesta a Incidentes`, etc.).
- **`author`**: Debe ser un handle válido de GitHub con `@` (ej. `@cibercelia`, `@Mole43`).
- **`tags`**: De 2 a 5 etiquetas en minúsculas (sin mayúsculas ni caracteres especiales raros).
- **`summary`**: Texto explicativo sin HTML ni sintaxis markdown enriquecida.
- ⛔ **NO incluir `difficulty`** bajo ninguna circunstancia.

---

## 3. Bloque de Encabezado y Metadatos Visuales

Inmediatamente después del YAML:

```markdown
# Nombre del término o concepto

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Categoría Exacta</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/usuario-github" target="_blank">@usuario-github</a></span>
  </div>
</div>
```

---

## 4. Estructura Obligatoria de Secciones

Todo término debe contener las siguientes secciones con sus respectivos emojis y nombres normalizados:

### Sección 1: `## 📖 Definición`
- Explicación conceptual clara, rigurosa y didáctica.
- Origen, contexto o estándar de referencia.
- Si se añaden notas destacadas, usar exclusivamente la sintaxis de MkDocs:
  ```markdown
  !!! note "Nota importante"
      Texto explicativo destacado.
  ```

### Sección 2: `## ⚙️ ¿Cómo funciona? / Principios fundamentales`
- Explicar el ciclo de vida, mecanismo técnico, arquitectura o fases de ataque/defensa.
- Usar listas ordenadas, diagramas conceptuales o explicaciones por capas.

### Sección 3: `## 🎯 Ejemplo práctico o escenario de demostración`
- Incluir un ejemplo práctico tangible.
- Emplear pestañas de contenido (*Content Tabs*) de MkDocs contrastando el caso inseguro vs. el caso seguro/remediado:
  ```markdown
  === "Escenario vulnerable / incorrecto"

      ```python
      # Código o configuración con vulnerabilidad
      ```

  === "Escenario seguro / remediado"

      ```python
      # Código o configuración corregida y segura
      ```
  ```

### Sección 4: `## 🛡️ Medidas de mitigación y buenas prácticas`
- Lista de acciones preventivas, reactivas o de hardening.
- Referenciar marcos reconocidos (OWASP Top 10, NIST SP 800, CIS Benchmarks, MITRE ATT&CK, RFCs).
- Utilizar formato de checklist o listas con viñetas:
  ```markdown
  - [x] **Sanitización y validación de entradas**: Descripción...
  - [x] **Principio de mínimo privilegio**: Descripción...
  ```

### Sección 5: `## 🔗 Referencias y enlaces de interés`
- Mínimo 2-3 enlaces fiables a documentación oficial o estándares de la industria (ej. owasp.org, nist.gov, cve.org, mitre.org, rfc-editor.org).

---

## 5. Lista de Comprobación y Validación (Checklist)

Antes de finalizar la tarea, verifica:
- [ ] El archivo está en `terminos/<slug-en-kebab-case>.md`.
- [ ] No se usa estilo *Title Case* anglosajón en ningún encabezado.
- [ ] No hay ningún campo `difficulty` en el YAML.
- [ ] Los bloques `!!!` y `===` tienen exactamente 4 espacios de sangrado en su contenido.
- [ ] La prueba del generador de índice funciona: `python3 .mkdocs/hooks/generate_glossary_index.py`.
