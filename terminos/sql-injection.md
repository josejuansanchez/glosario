---
title: "Inyección SQL (SQL injection - SQLi)"
category: "Vulnerabilidades Web / OWASP"
author: "@cibercelia"
tags:
  - owasp-top-10
  - sqli
  - web-security
  - bases-de-datos
  - cwe-89
summary: "Vulnerabilidad de seguridad web que permite a un atacante interferir en las consultas que una aplicación realiza a su base de datos relacional."
---

# Inyección SQL (SQL injection - SQLi)

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Vulnerabilidades Web / OWASP</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Identificadores</span>
    <span class="term-meta-value">CWE-89 | OWASP A03:2021</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor</span>
    <span class="term-meta-value"><a href="https://github.com/cibercelia" target="_blank">@cibercelia</a></span>
  </div>
</div>

## 📖 Definición

La **Inyección SQL (SQLi)** es una vulnerabilidad de inyección de código en la capa de persistencia donde datos no confiables introducidos por el usuario son concatenados directamente en una sentencia SQL sin sanitización ni parametrización previa. Esto permite al atacante manipular la estructura lógica de la consulta original, logrando leer, modificar o eliminar datos confidenciales, eludir mecanismos de autenticación e incluso ejecutar comandos en el sistema operativo subyacente.

!!! danger "Advertencia crítica"
    SQLi se mantiene de manera recurrente entre las vulnerabilidades más críticas del **OWASP Top 10** debido a su severo impacto en la confidencialidad, integridad y disponibilidad del negocio.

---

## 🧭 Tipos principales de SQLi

| Tipo | Denominación | Descripción |
| :--- | :--- | :--- |
| **In-band (Clásica)** | Error-based / UNION-based | El atacante utiliza el mismo canal de comunicación para lanzar el ataque y recopilar los resultados. |
| **Inferential (Ciega / Blind)** | Boolean-based / Time-based | La aplicación no devuelve datos directos, pero el atacante deduce la información observando diferencias en respuestas HTTP o retardos de tiempo (`SLEEP()`). |
| **Out-of-band (OOB)** | DNS / HTTP requests | Se fuerza al motor de base de datos a realizar conexiones externas (p. ej., peticiones DNS) hacia un servidor controlado por el atacante. |

---

## 🎯 Ejemplo práctico: autenticación vulnerable vs. segura

Supongamos un formulario de inicio de sesión vulnerable donde el atacante introduce como usuario: `' OR 1=1 --`.

=== "❌ Código inseguro (concatenación)"

    ```python linenums="1"
    import sqlite3

    def login_inseguro(username, password):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        # ⚠️ VULNERABILIDAD: Concatenación directa de entradas de usuario
        query = f"SELECT * FROM users WHERE user = '{username}' AND pass = '{password}'"
        print(f"[DEBUG] Ejecutando: {query}")
        
        cursor.execute(query)
        return cursor.fetchone()
    ```

=== "✅ Código seguro (consultas parametrizadas)"

    ```python linenums="1"
    import sqlite3

    def login_seguro(username, password):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        # 🛡️ PROTECCIÓN: Parámetros tipados gestionados por el driver
        query = "SELECT * FROM users WHERE user = ? AND pass = ?"
        
        cursor.execute(query, (username, password))
        return cursor.fetchone()
    ```

---

## 🛡️ Medidas de mitigación

1. **Sentencias Preparadas (Prepared Statements / Parameterized Queries)**: Es la defensa primaria e imprescindible. Separa el código SQL de los datos.
2. **Uso de ORMs Modernos**: Frameworks como SQLAlchemy, Hibernate o Entity Framework utilizan consultas parametrizadas de forma nativa por defecto.
3. **Principio de Mínimo Privilegio**: La cuenta de base de datos usada por la aplicación web no debe tener privilegios de superadministrador (`sa`, `root`, `dba`).
4. **Validación y listas blancas de entrada**: Validar formato de datos, tipos y longitud antes de procesarlos.
5. **Web Application Firewall (WAF)**: Capa secundaria de defensa en profundidad para detectar patrones maliciosos en tránsito.

---

## 🔗 Referencias

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [PortSwigger Web Security Academy - SQL Injection](https://portswigger.net/web-security/sql-injection)
- [MITRE CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)
