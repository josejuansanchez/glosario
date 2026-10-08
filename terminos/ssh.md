---
title: "SSH (Secure Shell)"
category: "Redes"
author: "@lizank176"
tags:
  - ciberseguridad
  - redes
  - ssh
  - cifrado
  - administracion-remota
  - bastionado
summary: "Protocolo de red cifrado para administrar sistemas de forma remota, transferir archivos y crear túneles seguros, sustituto seguro de Telnet y rlogin."
---

# SSH (Secure Shell)

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Redes</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/lizank176" target="_blank">@lizank176</a></span>
  </div>
</div>

## 📖 Definición
**SSH** (*Secure Shell*) es un protocolo de red criptográfico que permite acceder y administrar equipos remotos a través de una red no confiable, garantizando **confidencialidad**, **integridad** y **autenticación**. Por defecto escucha en el puerto **22/TCP**.

Fue creado en 1995 por Tatu Ylönen tras un ataque de captura de contraseñas en la red de su universidad, con el fin de sustituir protocolos que enviaban credenciales en texto claro, como **Telnet**, **rlogin** o **FTP**. La versión actual, **SSH-2**, está estandarizada en las RFC 4251 a 4254, y la implementación más extendida es **OpenSSH**.

Además del acceso a una terminal remota, SSH permite transferir archivos (**SFTP**, **SCP**), crear túneles y reenviar puertos (*port forwarding*), y autenticar operaciones automatizadas (Git, Ansible, copias de seguridad).

!!! note "Nota importante"
    SSH cifra el canal, pero no vuelve seguro un servidor mal configurado. Un servicio SSH expuesto a Internet con contraseñas débiles es uno de los vectores de ataque más comunes (fuerza bruta, *credential stuffing*). Además, **cambiar el puerto 22 no es una medida de seguridad real**, solo reduce el ruido en los registros.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales
Una conexión SSH sigue una arquitectura cliente-servidor y se establece en varias fases:

1. **Negociación de versión y algoritmos**: cliente y servidor acuerdan la versión del protocolo y los algoritmos de intercambio de claves, cifrado, MAC y firma.
2. **Intercambio de claves y autenticación del servidor**: se genera una clave de sesión compartida (por ejemplo, con Diffie-Hellman de curva elíptica). El servidor se identifica con su **clave de host**, que el cliente verifica contra el archivo `known_hosts` para detectar suplantaciones (ataques *man-in-the-middle*).
3. **Autenticación del usuario**: el cliente demuestra su identidad mediante contraseña, **clave pública/privada** (recomendado), certificados SSH o autenticación multifactor.
4. **Canal cifrado y multiplexado**: una vez autenticado, se abre una sesión interactiva, una transferencia de archivos o un túnel, todo dentro del canal cifrado.

**Métodos de autenticación habituales:**

| Método | Seguridad | Observaciones |
|---|---|---|
| Contraseña | Baja | Vulnerable a fuerza bruta y reutilización de credenciales |
| Clave pública | Alta | Requiere proteger la clave privada con *passphrase* |
| Certificados SSH | Alta | Escalable en entornos grandes, con caducidad y revocación |
| Clave pública + MFA | Muy alta | Recomendado para accesos privilegiados |

---

## 🎯 Ejemplo práctico o escenario de demostración
Configuración del servidor OpenSSH (`/etc/ssh/sshd_config`) en un servidor expuesto a Internet.

=== "Escenario vulnerable / incorrecto"

    Acceso de root con contraseña, sin límite de intentos y con funciones innecesarias activas:

    ```bash
    # /etc/ssh/sshd_config  (configuración insegura)
    PermitRootLogin yes
    PasswordAuthentication yes
    PermitEmptyPasswords yes
    MaxAuthTries 20
    X11Forwarding yes
    # Sin restricción de usuarios ni de origen
    ```

    Un atacante puede lanzar fuerza bruta contra `root` desde cualquier lugar y, si acierta, obtiene control total del sistema.

=== "Escenario seguro / remediado"

    Solo claves públicas, sin acceso directo de root y con superficie reducida:

    ```bash
    # /etc/ssh/sshd_config  (configuración bastionada)
    PermitRootLogin no
    PasswordAuthentication no
    PermitEmptyPasswords no
    PubkeyAuthentication yes
    KbdInteractiveAuthentication no
    MaxAuthTries 3
    LoginGraceTime 30
    AllowUsers admin deploy
    X11Forwarding no
    AllowTcpForwarding no
    ClientAliveInterval 300
    ClientAliveCountMax 2
    LogLevel VERBOSE
    ```

    Generación de una clave moderna en el cliente y verificación de la configuración antes de recargar:

    ```bash
    ssh-keygen -t ed25519 -a 100 -C "usuario@equipo"
    ssh-copy-id -i ~/.ssh/id_ed25519.pub admin@servidor

    sudo sshd -t && sudo systemctl reload sshd
    ```

    !!! warning "Antes de desactivar contraseñas"
        Comprueba en **otra sesión abierta** que el acceso con clave funciona, o podrías bloquearte el acceso al servidor.

---

## 🛡️ Medidas de mitigación y buenas prácticas

- [x] **Autenticación por clave pública**: desactivar las contraseñas y proteger las claves privadas con *passphrase*.
- [x] **Deshabilitar el acceso directo de root**: entrar con un usuario sin privilegios y elevar con `sudo`.
- [x] **Restringir usuarios y orígenes**: usar `AllowUsers`/`AllowGroups` y limitar el acceso por IP con cortafuegos.
- [x] **MFA**: añadir un segundo factor (TOTP, llaves FIDO2) en accesos privilegiados.
- [x] **Protección frente a fuerza bruta**: limitar intentos (`MaxAuthTries`) y usar herramientas como Fail2ban o reglas de limitación de conexiones.
- [x] **No exponer SSH a Internet**: acceder mediante VPN, un **bastión (jump host)** o soluciones de acceso Zero Trust.
- [x] **Algoritmos modernos**: desactivar cifrados y MAC obsoletos, y mantener OpenSSH actualizado.
- [x] **Reducir funciones innecesarias**: desactivar `X11Forwarding` y `AllowTcpForwarding` si no se usan.
- [x] **Gestión de claves**: rotar y revocar claves, auditar `authorized_keys` y evitar claves compartidas.
- [x] **Registro y monitorización**: centralizar logs (`LogLevel VERBOSE`) en un SIEM y alertar sobre intentos fallidos masivos o accesos inusuales.
- [x] **Verificar claves de host**: confirmar la huella en la primera conexión para evitar suplantaciones.

---

## 🔗 Referencias y enlaces de interés
- [OpenSSH: documentación oficial](https://www.openssh.com/manual.html)
- [RFC 4251: The Secure Shell (SSH) Protocol Architecture](https://www.rfc-editor.org/rfc/rfc4251)
- [NIST IR 7966: Security of Interactive and Automated Access Management Using SSH](https://csrc.nist.gov/pubs/ir/7966/final)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [MITRE ATT&CK T1021.004: Remote Services: SSH](https://attack.mitre.org/techniques/T1021/004/)
- [CWE-307: Improper Restriction of Excessive Authentication Attempts](https://cwe.mitre.org/data/definitions/307.html)