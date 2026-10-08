---
title: "Nombre del término o concepto"
category: "Vulnerabilidades Web"  # Ej: Criptografía, Redes, Identidad y Acceso, Malware, OWASP Top 10, DevSecOps, etc.
author: "@tu-usuario-github"      # Tu usuario de GitHub para atribuirte la autoría
tags:
  - ciberseguridad
  - ejemplo-tag
  - web
summary: "Breve resumen explicativo del término en una o dos frases (máximo 200 caracteres)."
---

# Nombre del término o concepto

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Vulnerabilidades Web</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/tu-usuario-github" target="_blank">@tu-usuario-github</a></span>
  </div>
</div>

## 📖 Definición
Explicación detallada y rigurosa del concepto. ¿Qué es exactamente? ¿Cuál es su origen o contexto histórico/técnico?

!!! note "Nota importante"
    Utiliza notas o avisos destacados para resaltar aspectos clave o advertencias importantes sobre este concepto.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales
Explica la arquitectura, los mecanismos subyacentes o el flujo de ejecución:

1. **Paso o componente 1**: Descripción técnica.
2. **Paso o componente 2**: Descripción técnica.
3. **Paso o componente 3**: Descripción técnica.

---

## 🎯 Ejemplo práctico o escenario de demostración
Presenta un ejemplo claro. Si aplica, incluye bloques de código o diagramas.

=== "Escenario vulnerable / incorrecto"

    ```python
    # Ejemplo de código vulnerable o configuración insegura
    def query_insegura(user_input):
        return f"SELECT * FROM users WHERE username = '{user_input}'"
    ```

=== "Escenario seguro / remediado"

    ```python
    # Ejemplo de código seguro con consultas parametrizadas
    def query_segura(user_input, cursor):
        cursor.execute("SELECT * FROM users WHERE username = %s", (user_input,))
        return cursor.fetchall()
    ```

---

## 🛡️ Medidas de mitigación y buenas prácticas
Lista las recomendaciones oficiales (OWASP, NIST, CIS, etc.) para prevenir o aplicar este concepto:

- [x] **Recomendación 1**: Descripción de la contramedida.
- [x] **Recomendación 2**: Descripción de la contramedida.
- [x] **Recomendación 3**: Descripción de la contramedida.

---

## 🔗 Referencias y enlaces de interés
- [Estándar o Guía Oficial (e.g., OWASP / NIST)](https://owasp.org)
- [Documentación técnica complementaria](https://cve.mitre.org)
- [MITRE ATT&CK Technique / CWE](https://attack.mitre.org)
