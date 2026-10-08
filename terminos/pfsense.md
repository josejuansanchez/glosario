---
title: "pfSense"
category: "Redes y Seguridad Perimetral"
author: "@aperfer126"
tags:
  - pfsense
  - firewall
  - router
  - redes
  - seguridad-perimetral
summary: "Distribución basada en FreeBSD que proporciona funciones de firewall, router y servicios de red mediante una interfaz de administración web."
---

# pfSense

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Redes y Seguridad Perimetral</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Tipo</span>
    <span class="term-meta-value">Firewall y router de código abierto</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor</span>
    <span class="term-meta-value"><a href="https://github.com/aperfer126" target="_blank">@aperfer126</a></span>
  </div>
</div>

## 📖 Definición

**pfSense** es una distribución de software basada en **FreeBSD** que convierte un equipo físico o virtual en un firewall y router. Se administra principalmente desde una interfaz web y puede ofrecer servicios como traducción de direcciones de red (NAT), DHCP, DNS, VPN y redes VLAN. Está disponible en ediciones mantenidas por Netgate, entre ellas pfSense Community Edition (CE) y pfSense Plus.

pfSense permite definir políticas de tráfico entre interfaces y mantener el estado de las conexiones. No sustituye el diseño seguro de la red: una regla permisiva o una interfaz de administración expuesta puede anular buena parte de la protección que proporciona.

!!! warning "Administración segura"
    La interfaz web de administración no debe exponerse directamente a Internet. Limita su acceso a una red de gestión confiable o a una VPN y mantén el sistema actualizado.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales

1. **Interfaces y zonas de red**: Se asignan interfaces a redes como WAN (exterior) y LAN (interior). También pueden crearse VLAN para separar, por ejemplo, equipos de usuarios, servidores e IoT.
2. **Reglas de firewall**: Las reglas se aplican normalmente en la interfaz por la que entra el tráfico. Evalúan datos como dirección, protocolo, puertos y destino para permitir o bloquear conexiones. En general, el tráfico entrante que no coincide con una regla de permiso se bloquea.
3. **Seguimiento de estado**: El firewall mantiene una tabla de estados para asociar los paquetes con conexiones existentes. Así puede permitir el tráfico de respuesta de una conexión autorizada sin abrir indiscriminadamente el sentido contrario.
4. **NAT y enrutamiento**: El enrutamiento determina por dónde se envían los paquetes entre redes; NAT puede traducir direcciones, por ejemplo, para que varios equipos de una LAN compartan una dirección IPv4 pública.
5. **Servicios y extensiones**: La instalación puede habilitar servicios de red o paquetes adicionales. Cada servicio y paquete amplía la superficie que debe configurarse, actualizarse y supervisarse.

---

## 🎯 Ejemplo práctico o escenario de demostración

En una red doméstica o de laboratorio, pfSense puede separar la red interna de Internet. Un conjunto inicial de políticas podría ser:

| Interfaz | Política de ejemplo | Objetivo |
| :--- | :--- | :--- |
| WAN | Bloquear conexiones entrantes no solicitadas | Evitar que servicios internos queden accesibles desde Internet. |
| LAN | Permitir a los clientes acceder a servicios necesarios | Proporcionar conectividad sin abrir puertos entrantes en WAN. |
| Gestión | Permitir HTTPS a la consola solo desde equipos administradores | Reducir quién puede cambiar la configuración del firewall. |

=== "Configuración arriesgada"

    Una regla amplia en WAN que permita cualquier origen y cualquier destino puede publicar servicios internos y dejar accesible la propia administración. También es arriesgado habilitar acceso remoto a la consola sin restringir su origen.

=== "Configuración más segura"

    Mantén bloqueadas las conexiones entrantes de WAN salvo excepciones justificadas. Si un servicio debe ser público, crea una regla específica para su destino, protocolo y puerto; administra pfSense desde una VLAN de gestión o por VPN, y permite el acceso únicamente a los equipos autorizados.

---

## 🛡️ Medidas de mitigación y buenas prácticas

- [x] **Restringir la administración**: No publiques la GUI ni SSH en WAN. Limita su acceso a una red de gestión o VPN y a direcciones de origen autorizadas.
- [x] **Aplicar mínimo privilegio a las reglas**: Evita reglas amplias como «cualquier origen a cualquier destino»; documenta las excepciones y elimina las que ya no sean necesarias.
- [x] **Mantener el sistema actualizado**: Instala versiones y parches compatibles desde los canales oficiales y revisa las notas de publicación antes de actualizar.
- [x] **Revisar servicios y paquetes**: Desactiva lo que no se utilice y evalúa la procedencia, mantenimiento y permisos de los paquetes instalados.
- [x] **Proteger credenciales y acceso**: Usa contraseñas únicas y robustas, habilita el segundo factor cuando esté disponible y evita compartir cuentas administrativas.
- [x] **Respaldar y supervisar**: Conserva copias de seguridad de la configuración en un lugar protegido y revisa los registros, estados y cambios de reglas con regularidad.

---

## 🔗 Referencias y enlaces de interés

- [Documentación oficial de pfSense](https://docs.netgate.com/pfsense/en/latest/)
- [Documentación oficial: reglas de firewall](https://docs.netgate.com/pfsense/en/latest/firewall/)
- [Documentación oficial: copias de seguridad y restauración](https://docs.netgate.com/pfsense/en/latest/backup/index.html)
- [Netgate: avisos de seguridad](https://www.netgate.com/resources/security)