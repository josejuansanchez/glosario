# Normas de Redacción y Formato para Términos de Ciberseguridad

Aplica a todos los archivos creados o editados en la carpeta `terminos/` y a la plantilla `plantilla.md`.

## 1. Reglas Ortográficas de la RAE
- En títulos y subtítulos en español, solo la primera palabra se escribe con mayúscula inicial (salvo nombres propios o siglas). Ejemplo: `## 🎯 Ejemplo práctico o escenario de demostración` (no *Ejemplo Práctico O Escenario De Demostración*).
- Los títulos aislados en su propia línea no llevan punto final.
- Términos comunes como *ciberseguridad*, *glosario*, *firewall*, *cifrado* van en minúsculas.

## 2. Metadatos YAML (Frontmatter)
- Obligatorios: `title`, `category`, `author`, `tags`, `summary`.
- Prohibido: `difficulty`.
- El campo `author` debe contener un usuario real de GitHub con `@` (ej. `@cibercelia`, `@Mole43`) o `"Comunidad"`.
- El campo `summary` debe ser texto plano breve (<200 caracteres) sin formato Markdown ni etiquetas HTML.

## 3. Sintaxis de Material for MkDocs
- Usar siempre avisos de MkDocs con 4 espacios de sangrado: `!!! note "Nota importante"`.
- No usar sintaxis de GitHub alerts (`> [!NOTE]`).
- Usar pestañas comparativas: `=== "Escenario vulnerable / incorrecto"` y `=== "Escenario seguro / remediado"`.

## 4. Estructura de Secciones
Cada término debe contener las 5 secciones estándar:
1. `## 📖 Definición`
2. `## ⚙️ ¿Cómo funciona? / Principios fundamentales`
3. `## 🎯 Ejemplo práctico o escenario de demostración`
4. `## 🛡️ Medidas de mitigación y buenas prácticas`
5. `## 🔗 Referencias y enlaces de interés`
