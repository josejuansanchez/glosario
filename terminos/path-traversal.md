---
title: "Path Traversal (Traversal de rutas)"
category: "Vulnerabilidades Web"  # Ej: Criptografía, Redes, Identidad y Acceso, Malware, OWASP Top 10, DevSecOps, etc.
author: "@Zero-RTC"      # (Pablo Quintana)
tags:
  - ciberseguridad
  - hacking
  - explotación web
summary: "Vulnerabilidad que permite manipular rutas para acceder a archivos fuera del directorio autorizado mediante entradas no validadas."
---

# Path Traversal (Traversal de rutas)

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Vulnerabilidades Web</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/Zero-RTC" target="_blank">@Zero-RTC</a></span>
  </div>
</div>

## 📖 Definición
Path Traversal, también llamado **directory traversal**, es una vulnerabilidad que aparece cuando una aplicación usa datos controlados por el usuario para construir una ruta de archivo sin comprobar que el resultado permanezca dentro del directorio autorizado. Un atacante puede manipular esa ruta para leer archivos fuera de dicho directorio y, si la aplicación permite escrituras, modificarlos.

La secuencia `../` representa el directorio padre en sistemas tipo Unix. Las variantes codificadas, las barras invertidas en Windows y las diferencias de normalización pueden ayudar a evadir filtros simples. La debilidad se relaciona con **CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')**.

!!! warning "Impacto"
    El impacto depende de los permisos del proceso y de las operaciones disponibles: puede ir desde la divulgación de archivos de configuración o credenciales hasta la modificación de archivos.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales

1. **Entrada controlada**: La aplicación recibe un nombre de archivo o una ruta desde una petición, por ejemplo, un parámetro de descarga.
2. **Construcción insegura**: Concatena esa entrada con un directorio base sin normalizarla ni validar el destino final.
3. **Acceso fuera del límite**: Componentes como `../` hacen que la ruta resuelta apunte fuera del directorio previsto, y la aplicación accede al archivo con los permisos de su proceso.

---

## 🎯 Ejemplo práctico: descarga de archivos

Una aplicación que descarga informes a partir de un nombre proporcionado por el usuario no debe confiar en que ese nombre señale un archivo dentro de `documentos/`.

=== "Código vulnerable"

    ```python
  from pathlib import Path

  BASE_DIR = Path("documentos")

  def leer_informe(nombre):
    ruta = BASE_DIR / nombre
    return ruta.read_text(encoding="utf-8")
    ```

  Una entrada como `../../etc/passwd` puede escapar del directorio `documentos` en sistemas tipo Unix.

=== "Código con comprobación del directorio"

    ```python
  from pathlib import Path

  BASE_DIR = Path("documentos").resolve()

  def leer_informe(nombre):
    ruta = (BASE_DIR / nombre).resolve()
    try:
      ruta.relative_to(BASE_DIR)
    except ValueError:
      raise ValueError("Ruta no permitida")

    return ruta.read_text(encoding="utf-8")
    ```

  `resolve()` normaliza la ruta y resuelve enlaces simbólicos; `relative_to()` comprueba que el destino siga dentro del directorio permitido. En aplicaciones reales, es preferible aceptar identificadores de archivo y buscar la ruta correspondiente en el servidor, en vez de aceptar rutas arbitrarias.

---

## 🛡️ Medidas de mitigación y buenas prácticas

- **Evitar rutas arbitrarias**: Usar identificadores o una lista permitida de nombres y resolverlos en el servidor.
- **Validar el destino final**: Normalizar y resolver la ruta, incluidos los enlaces simbólicos, y verificar que permanezca dentro del directorio base.
- **No confiar en filtros de cadenas**: Bloquear únicamente `../` es insuficiente por las codificaciones y diferencias entre sistemas operativos.
- **Aplicar mínimo privilegio**: Ejecutar el servicio con permisos limitados y restringir el acceso del proceso a los archivos que necesita.
- **Proteger también las escrituras**: Aplicar las mismas comprobaciones a cargas, extracciones de archivos comprimidos y cualquier operación que cree o modifique rutas.

---

## 🔗 Referencias
- [OWASP: Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [MITRE CWE-22: Path Traversal](https://cwe.mitre.org/data/definitions/22.html)
- [PortSwigger Web Security Academy: Path Traversal](https://portswigger.net/web-security/file-path-traversal)
