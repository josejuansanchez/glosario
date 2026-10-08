---
title: "Cifrado"
category: "Criptografía"
author: "@mgarlop"
tags:
  - ciberseguridad
  - criptografia
  - cifrado-simetrico
  - cifrado-asimetrico
summary: "Proceso que transforma datos legibles en texto cifrado mediante algoritmos y claves, para proteger su confidencialidad."
---

# Cifrado

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Criptografía</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/mgarlop" target="_blank">@mgarlop</a></span>
  </div>
</div>

## 📖 Definición

El **cifrado** es el proceso criptográfico que transforma información legible (texto claro) en información ininteligible (texto cifrado) mediante un algoritmo y una clave. Solo quien disponga de la clave apropiada puede descifrar los datos y recuperar el contenido original.

Se utiliza para proteger la **confidencialidad** de datos almacenados (en reposo) o transmitidos (en tránsito). Por sí solo, el cifrado no garantiza que los datos no hayan sido modificados ni quién los creó; para esas propiedades se emplean mecanismos de autenticación e integridad, como los códigos de autenticación de mensajes o las firmas digitales.

!!! note "Cifrar no es codificar ni hacer hash"
    La codificación, como Base64, solo cambia la representación de los datos y no requiere una clave secreta. Un hash criptográfico es una función unidireccional y no está diseñado para recuperar el contenido original. El cifrado, en cambio, es reversible con la clave correspondiente.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales

1. **Algoritmo y clave**: El algoritmo define las operaciones criptográficas; la clave controla el resultado. La seguridad debe depender de proteger las claves, no de mantener secreto el algoritmo.
2. **Cifrado y descifrado**: El algoritmo combina el texto claro con la clave para producir texto cifrado. El descifrado utiliza la clave correspondiente para recuperar los datos.
3. **Elección del esquema**:
   - **Cifrado simétrico**: utiliza la misma clave secreta para cifrar y descifrar. Es eficiente para grandes volúmenes de datos; ejemplos actuales incluyen AES-GCM y ChaCha20-Poly1305.
   - **Cifrado asimétrico**: utiliza un par de claves relacionadas: una pública y una privada. La clave pública puede cifrar datos que solo la privada correspondiente descifra. Se usa, entre otras cosas, para establecer claves y proteger comunicaciones.
   - **Cifrado autenticado**: además de confidencialidad, permite detectar modificaciones. Para datos de aplicación, se prefieren modos AEAD como AES-GCM o ChaCha20-Poly1305.

---

## 🎯 Ejemplo práctico o escenario de demostración

Base64 no protege un secreto: cualquiera puede decodificarlo. Para información confidencial, utiliza una biblioteca criptográfica mantenida y protege la clave por separado de los datos cifrados.

=== "Escenario incorrecto: Base64"

    ```python
    import base64

    secreto = "credencial-confidencial"
    representacion = base64.b64encode(secreto.encode("utf-8"))

    # Esto es reversible sin ninguna clave y no proporciona confidencialidad.
    print(base64.b64decode(representacion).decode("utf-8"))
    ```

=== "Escenario seguro: cifrado autenticado"

    ```python
    from cryptography.fernet import Fernet

    # En una aplicación real, genera la clave una vez y guárdala
    # en un gestor de secretos, separada de los datos cifrados.
    clave = Fernet.generate_key()
    cifrador = Fernet(clave)

    texto_claro = b"informacion confidencial"
    texto_cifrado = cifrador.encrypt(texto_claro)
    texto_recuperado = cifrador.decrypt(texto_cifrado)
    ```

    Fernet, de la biblioteca `cryptography`, proporciona cifrado simétrico autenticado. Generar una clave nueva cada vez que se ejecuta el programa no es adecuado para datos que deban descifrarse después: la clave debe gestionarse y respaldarse de forma segura.

---

## 🛡️ Medidas de mitigación y buenas prácticas

- [x] **Usar bibliotecas y algoritmos reconocidos**: evitar diseñar algoritmos propios y no utilizar algoritmos obsoletos como DES o modos inseguros.
- [x] **Proteger las claves**: almacenarlas en un gestor de secretos o módulo de seguridad, limitar su acceso y establecer procesos de rotación y recuperación.
- [x] **Preferir cifrado autenticado**: usar modos AEAD para detectar modificaciones; no reutilizar nonces cuando el algoritmo lo prohíba.
- [x] **Proteger los datos en tránsito y en reposo**: configurar protocolos actuales como TLS y cifrar los dispositivos o soportes que contengan información sensible.
- [x] **No confundir cifrado con controles de acceso**: restringir quién puede obtener las claves y registrar su uso; el cifrado no sustituye la autorización.

---

## 🔗 Referencias y enlaces de interés

- [NIST SP 800-57 Part 1 Rev. 5: Key Management](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
- [NIST SP 800-38D: AES-GCM](https://csrc.nist.gov/pubs/sp/800/38/d/final)
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [Documentación de Fernet en `cryptography`](https://cryptography.io/en/latest/fernet/)
