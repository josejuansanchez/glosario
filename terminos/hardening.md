---
title: "Hardening (bastionado de sistemas)"
category: "Seguridad de sistemas"
author: "@cromsal"
tags:
  - hardening
  - bastionado
  - configuracion-segura
  - reduccion-superficie-ataque
  - cis-benchmarks
summary: "Práctica de seguridad que reduce la superficie de ataque de sistemas mediante la eliminación de componentes innecesarios y la aplicación y verificación de configuraciones seguras."
---

# Hardening (bastionado de sistemas)

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Seguridad de sistemas / Bastionado</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Marcos de referencia</span>
    <span class="term-meta-value">CIS Benchmarks | NIST SP 800-70</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor</span>
    <span class="term-meta-value"><a href="https://github.com/cromsal" target="_blank">@cromsal</a></span>
  </div>
</div>

## 📖 Definición

El **hardening**, también llamado **bastionado**, es el proceso de reducir la superficie de ataque de un sistema mediante la eliminación o limitación de componentes, servicios, cuentas y permisos innecesarios, y la aplicación de configuraciones seguras. Se aplica a sistemas operativos, servidores, dispositivos de red, aplicaciones, contenedores y servicios en la nube.

El bastionado no consiste en aplicar una configuración universal: las medidas deben ajustarse a la función del activo, sus riesgos y sus requisitos operativos. Las guías como **CIS Benchmarks** ofrecen recomendaciones técnicas que pueden seleccionarse y adaptarse a cada entorno.

!!! note "Importante"
    El hardening es un proceso continuo. Las configuraciones deben probarse, documentarse y revisarse cuando cambien las amenazas, el software o las necesidades del servicio. Una regla demasiado restrictiva también puede interrumpir operaciones legítimas.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales

1. **Inventariar y definir el propósito**: identificar los activos, sus responsables, los servicios necesarios y el nivel de riesgo aceptable.
2. **Reducir la superficie de ataque**: desinstalar o deshabilitar componentes no requeridos, cerrar puertos innecesarios y retirar cuentas o permisos que no se utilicen.
3. **Aplicar una configuración segura**: establecer controles de acceso, autenticación, cifrado, registro y actualización de acuerdo con una línea base reconocida y las necesidades del entorno.
4. **Validar y mantener**: comprobar técnicamente los cambios, vigilar desviaciones respecto de la línea base y revisar la configuración de forma periódica.

---

## 🎯 Ejemplo práctico o escenario de demostración

Un servidor Linux administrado por SSH no debería permitir el acceso remoto directo como `root` ni depender de contraseñas débiles. El siguiente ejemplo muestra una configuración mínima orientativa para `/etc/ssh/sshd_config`; debe adaptarse a las políticas y a la versión de OpenSSH del sistema.

=== "Escenario vulnerable / incorrecto"

    ```text
    PermitRootLogin yes
    PasswordAuthentication yes
    ```

=== "Escenario seguro / remediado"

    ```text
    PermitRootLogin no
    PubkeyAuthentication yes
    PasswordAuthentication no
    MaxAuthTries 3
    X11Forwarding no
    ```

Antes de recargar SSH, valida la sintaxis con `sshd -t` y confirma la configuración efectiva con `sshd -T`. Comprueba que el acceso con clave pública funciona en una sesión independiente y conserva una vía de recuperación para evitar perder el acceso al servidor.

---

## 🛡️ Medidas de mitigación y buenas prácticas

- [x] **Usar líneas base reconocidas**: seleccionar las recomendaciones CIS u otra guía aplicable al sistema y documentar las excepciones justificadas.
- [x] **Deshabilitar lo innecesario**: retirar servicios, paquetes, puertos, cuentas y permisos que no sean necesarios para la función del activo.
- [x] **Mantener sistemas actualizados**: aplicar parches de seguridad mediante un proceso controlado, con pruebas y seguimiento de las actualizaciones pendientes.
- [x] **Limitar y proteger el acceso**: aplicar mínimo privilegio, autenticación robusta, gestión segura de claves y separación de cuentas administrativas.
- [x] **Registrar y verificar cambios**: habilitar registros relevantes, revisar desviaciones de configuración y volver a evaluar el bastionado tras cambios importantes.

---

## 🔗 Referencias y enlaces de interés

- [CIS Benchmarks: guías de configuración segura](https://www.cisecurity.org/cis-benchmarks)
- [NIST SP 800-70 Rev. 4: Security Configuration Checklists Program](https://csrc.nist.gov/pubs/sp/800/70/r4/final)
- [NIST SP 800-123: Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final)
- [OpenSSH: documentación de sshd_config](https://man.openbsd.org/sshd_config)