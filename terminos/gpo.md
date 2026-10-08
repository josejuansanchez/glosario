---
title: "GPO (Objetos de directiva de grupo)"
category: "Identidad y Administración de Sistemas"
author: "@AndriySym"
tags:
  - gpo
  - active-directory
  - windows
  - hardening
  - gestión-de-configuración
summary: "Conjunto centralizado de directivas que permite administrar la configuración y seguridad de usuarios y equipos Windows en un dominio o de forma local."
---

# GPO (Objetos de directiva de grupo)

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Identidad y Administración de Sistemas</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Tecnología</span>
    <span class="term-meta-value">Microsoft Windows / Active Directory</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/AndriySym" target="_blank">@AndriySym</a></span>
  </div>
</div>

## 📖 Definición

Un **Objeto de Política de Grupo** (*Group Policy Object*, **GPO**) es un conjunto de configuraciones que permite administrar de forma centralizada usuarios y equipos Windows. En un entorno de **Active Directory Domain Services (AD DS)**, las GPO se vinculan a sitios, dominios u unidades organizativas (OU) para aplicar configuraciones como requisitos de contraseña, reglas del firewall, instalación de software, scripts de inicio o restricciones del sistema.

Una GPO de dominio se compone de información almacenada en Active Directory y de archivos de configuración ubicados en **SYSVOL**; ambos componentes deben estar disponibles y replicados para que los clientes procesen la directiva. Windows también permite definir directivas locales en equipos que no pertenecen a un dominio.

!!! warning "Importante"
    Una GPO puede afectar a muchos equipos o usuarios. Un vínculo demasiado amplio, una delegación incorrecta o una configuración de seguridad débil puede introducir cambios no autorizados o interrumpir servicios. Valida los cambios en una OU de prueba antes de desplegarlos.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales

1. **Creación y almacenamiento**: Un administrador crea o edita la GPO con herramientas como Group Policy Management Console (GPMC). Sus atributos se almacenan en Active Directory y su plantilla de directiva en SYSVOL.
2. **Vinculación y alcance**: La GPO se vincula a un sitio, dominio u OU. El filtrado de seguridad determina qué usuarios o equipos pueden aplicarla; el filtrado WMI puede restringirla según las características del equipo.
3. **Procesamiento y precedencia**: En general, las directivas se procesan en el orden **Local, Sitio, Dominio y OU (LSDOU)**. Si varias directivas configuran el mismo ajuste, la configuración aplicada más tarde suele prevalecer, salvo opciones como **Forzar** (*Enforced*) o **Bloquear herencia**, que alteran la precedencia.
4. **Aplicación y actualización**: El cliente descarga y aplica las directivas durante el inicio o el inicio de sesión, y después en las actualizaciones periódicas. `gpupdate` permite solicitar una actualización; ciertos ajustes requieren cerrar sesión o reiniciar.

---

## 🎯 Ejemplo práctico o escenario de demostración

Un equipo de seguridad necesita exigir el bloqueo automático de sesión en los equipos de administración. Aplicar el ajuste a todo el dominio puede afectar a usuarios y equipos que no forman parte del alcance previsto.

=== "Asignación incorrecta"

    Se vincula la GPO a la raíz del dominio y se deja que se aplique a todos los equipos autenticados. Esto amplía innecesariamente el alcance y hace más difícil anticipar el impacto del cambio.

    ```text
    Vínculo: raíz del dominio
    Filtrado: todos los equipos autenticados
    Configuración: tiempo de inactividad antes del bloqueo
    ```

=== "Asignación recomendada"

    Se crea una OU de prueba y después una OU de equipos de administración. Se vincula allí la GPO y se limita su aplicación al grupo de equipos previsto, comprobando antes el resultado efectivo.

    ```powershell
    # Genera un informe de las directivas aplicadas al equipo actual
    gpresult /h "$env:TEMP\resultado-gpo.html"
    ```

    Revisa el informe para confirmar la GPO ganadora y el ámbito aplicado. Despliega el cambio primero en el grupo piloto y amplía el alcance solo después de validar el comportamiento.

---

## 🛡️ Medidas de mitigación y buenas prácticas

- [x] **Aplicar mínimo privilegio**: Restringir quién puede crear, editar, vincular o delegar GPO; revisar periódicamente permisos y delegaciones.
- [x] **Limitar el alcance**: Vincular cada directiva a la OU adecuada y usar filtrado de seguridad explícito. Evitar filtros WMI complejos si una estructura de OUs clara resuelve el caso.
- [x] **Probar antes del despliegue**: Usar una OU o grupo piloto, revisar el modelado de directivas en GPMC y generar informes con `gpresult` o `Get-GPOReport`.
- [x] **Auditar cambios**: Registrar modificaciones, mantener copias de seguridad de las GPO y revisar cambios inesperados en Active Directory y SYSVOL.
- [x] **Separar funciones**: Evitar que las cuentas administrativas de uso diario tengan permisos para modificar directivas de dominio.
- [x] **Mantener consistencia**: Verificar replicación de Active Directory y SYSVOL, y documentar excepciones como GPO forzadas o bloqueo de herencia.

---

## 🔗 Referencias y enlaces de interés

- [Microsoft Learn: Group Policy overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)
- [Microsoft Learn: Group Policy processing and precedence](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing)
- [Microsoft Learn: Group Policy Management Console (GPMC)](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-management-console)
