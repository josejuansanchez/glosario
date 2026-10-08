---
title: "Principio de Menor Privilegio"
category: "Identidad y Acceso"
author: "@radasir"
tags:
  - ciberseguridad
  - control-de-acceso
  - autorizacion
  - hardening
  - seguridad-web
summary: "Principio de seguridad que limita los permisos de usuarios y procesos al mínimo necesario para realizar una tarea autorizada."
---

# Principio de Menor Privilegio


<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Identidad y Acceso</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/radasir" target="_blank">@radasir</a></span>
  </div>
</div>


## 📖 Definición

El **principio de menor privilegio** establece que un usuario, proceso, cuenta de servicio o componente de un sistema debe recibir únicamente los permisos, recursos y autorizaciones mínimos necesarios para completar una tarea legítima.

NIST define este principio como una arquitectura de seguridad en la que cada entidad recibe los recursos del sistema y las autorizaciones mínimas que necesita para desempeñar su función. No se aplica solo a personas: también debe aplicarse a procesos, aplicaciones, servicios, cuentas técnicas y componentes de infraestructura.

Este principio forma parte de los principios clásicos de diseño seguro descritos por Jerome H. Saltzer y Michael D. Schroeder. Los autores indican que cada programa y usuario debe operar con el conjunto mínimo de privilegios requerido para terminar su trabajo. Su propósito principal es limitar el daño que puede producir un error, accidente, mala configuración o compromiso de una cuenta.

!!! note "Nota Importante"
    El menor privilegio no significa impedir que los usuarios trabajen. Significa conceder permisos basados en una necesidad concreta, documentada y revisable, evitando privilegios amplios, permanentes o heredados sin justificación.


---


## ⚙️ ¿Cómo funciona? / Principios Fundamentales

El principio se implementa definiendo qué entidad necesita acceder a qué recurso, para qué acción y bajo qué condiciones.

1. **Identificar entidades y recursos**: Se inventarían usuarios, administradores, aplicaciones, cuentas de servicio, API, bases de datos, sistemas, archivos y funciones administrativas.

2. **Definir acciones necesarias**: Para cada rol se determina qué operaciones necesita realizar sobre cada recurso, por ejemplo: leer, crear, modificar, eliminar, ejecutar o administrar.

3. **Asignar permisos mínimos**: Se concede solamente la autorización necesaria. Por ejemplo, una aplicación que solo consulta datos no debe recibir permisos de escritura o administración sobre la base de datos.

4. **Separar cuentas privilegiadas y no privilegiadas**: Un administrador debe utilizar una cuenta estándar para actividades cotidianas, como navegar o consultar el correo, y una cuenta administrativa separada para tareas de administración.

5. **Denegar por defecto**: Cuando no existe una regla explícita que permita una operación, el acceso debe ser rechazado. Este enfoque reduce la exposición causada por configuraciones incompletas o nuevas funcionalidades.

6. **Validar las autorizaciones en cada solicitud**: En aplicaciones web y API, el servidor debe verificar permisos sobre cada recurso y operación solicitada. Ocultar botones en la interfaz no sustituye la autorización del lado del servidor.

7. **Revisar y retirar privilegios**: Los permisos deben revisarse periódicamente para detectar *privilege creep* o acumulación de privilegios. Si ya no existe una necesidad de negocio, el permiso debe modificarse o eliminarse.

8. **Registrar acciones privilegiadas**: El uso de funciones administrativas debe quedar registrado para facilitar la detección de abuso, la investigación de incidentes y las auditorías.


---


## 🎯 Ejemplo Práctico o Escenario de Demostración

Una API de gestión de usuarios dispone de una operación para eliminar cuentas. Un usuario normal autenticado no debe poder ejecutar esa operación aunque conozca o modifique directamente la URL del endpoint.

=== "Escenario Vulnerable / Incorrecto"

    ```java
    @DeleteMapping("/api/users/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteById(id);
        return ResponseEntity.noContent().build();
    }
    ```

    En este caso, cualquier usuario que llegue al endpoint podría eliminar una cuenta si no existe una comprobación de autorización en el servidor. Ocultar el botón "Eliminar" en el frontend no evita que un atacante envíe manualmente una petición `DELETE`.

=== "Escenario Seguro / Remediado"

    ```java
    @DeleteMapping("/api/users/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteById(id);
        return ResponseEntity.noContent().build();
    }
    ```

    En este ejemplo, solo un usuario que tenga el rol `ADMIN` puede acceder a la operación. La comprobación se realiza en el servidor mediante Spring Security.

    Para reforzar el menor privilegio, el rol `ADMIN` no debe asignarse a usuarios que únicamente necesiten consultar o modificar su propio perfil.

### Matriz mínima de autorización

| Recurso / acción | Usuario estándar | Soporte | Administrador |
|---|---:|---:|---:|
| Consultar su propio perfil | Permitido | Permitido | Permitido |
| Modificar su propio perfil | Permitido | No permitido | Permitido |
| Consultar usuarios | No permitido | Permitido | Permitido |
| Eliminar usuarios | No permitido | No permitido | Permitido |
| Cambiar roles o permisos | No permitido | No permitido | Permitido |

La matriz debe convertirse en pruebas automatizadas para verificar que los roles no puedan realizar acciones no autorizadas, incluidos casos de escalada horizontal y vertical de privilegios.


---


## 🛡️ Medidas de Mitigación y Buenas Prácticas

- [x] **Aplicar denegación por defecto**: Permitir el acceso solamente cuando una política, rol o regla lo autorice explícitamente.

- [x] **Crear una matriz de autorización**: Documentar la relación entre actor, recurso y acción antes de desarrollar o desplegar una aplicación.

- [x] **Aplicar autorización del lado del servidor**: Comprobar los permisos en cada solicitud y para el objeto específico solicitado, no solo en la interfaz gráfica.

- [x] **Separar cuentas administrativas**: Usar una cuenta estándar para el trabajo diario y una cuenta privilegiada independiente para tareas administrativas.

- [x] **Restringir cuentas privilegiadas**: Limitar cuentas de administrador, superusuario, `root`, `Domain Admins` o equivalentes al personal y roles que realmente las necesiten.

- [x] **Evitar permisos excesivos en cuentas de servicio**: Una cuenta de servicio debe disponer solo de los permisos necesarios sobre los recursos que usa. No debe recibir privilegios globales por comodidad.

- [x] **Revisar privilegios periódicamente**: Validar que los permisos actuales siguen siendo necesarios y retirar accesos de empleados que cambian de puesto, proveedores, cuentas inactivas o proyectos finalizados.

- [x] **Registrar funciones privilegiadas**: Registrar operaciones administrativas, cambios de permisos, creación de cuentas y accesos a información sensible.

- [x] **Automatizar pruebas de autorización**: Incorporar pruebas de permisos en CI/CD para detectar regresiones cuando se añadan endpoints, funciones o roles.

- [x] **Aplicar separación de funciones**: Para acciones críticas, evitar que una sola identidad pueda iniciar, aprobar y ejecutar todo el proceso.


---


## 🔗 Referencias y Enlaces de Interés

- [NIST CSRC Glossary: Least Privilege](https://csrc.nist.gov/glossary/term/least_privilege)
- [NIST SP 800-53 Rev. 5 — Control AC-6: Least Privilege](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP Authorization Testing Automation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Testing_Automation_Cheat_Sheet.html)
- [OWASP Authorization Regression Testing Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Regression_Testing_Cheat_Sheet.html)
- [Saltzer y Schroeder: The Protection of Information in Computer Systems — University of Virginia](https://www.cs.virginia.edu/~evans/cs551/saltzer/)
- [Saltzer y Schroeder: documento alojado por Princeton University](https://www.princeton.edu/~rblee/ELE572Papers/Fall04Readings/ProtectionInfo_Saltzer.pdf)