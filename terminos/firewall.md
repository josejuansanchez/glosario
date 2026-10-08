---
title: "Firewall (cortafuegos)"
category: "Redes y Seguridad Perimetral"
author: "@empoleon00"
tags:
  - firewall
  - redes
  - filtrado-de-trafico
  - seguridad-perimetral
summary: "Sistema que controla el tráfico de red entrante y saliente mediante reglas para permitir o bloquear conexiones según una política de seguridad."
---

# Firewall (cortafuegos)

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Redes y Seguridad Perimetral</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/empoleon00" target="_blank">@empoleon00</a></span>
  </div>
</div>

## 📖 Definición

Un **firewall** o **cortafuegos** es un sistema de hardware, software o ambos que supervisa y controla el tráfico de red que entra y sale de un dispositivo o una red. Aplica reglas definidas por una política de seguridad para permitir, rechazar o registrar las comunicaciones.

Puede proteger un equipo individual (firewall de host) o una red completa (firewall de red). Según su tecnología, puede filtrar paquetes por direcciones y puertos, mantener el estado de las conexiones o inspeccionar protocolos y contenido de aplicación. Los firewalls de nueva generación (NGFW) pueden añadir funciones como prevención de intrusiones y reconocimiento de aplicaciones.

!!! warning "Importante"
    Un firewall reduce la superficie de exposición, pero no reemplaza las actualizaciones, la autenticación segura ni la protección de los servicios permitidos. Una regla demasiado amplia puede dejar accesibles sistemas que deberían estar restringidos.

---

## ⚙️ ¿Cómo funciona?

1. **Observa el tráfico**: examina datos como las direcciones IP de origen y destino, el protocolo, los puertos y, según el tipo de firewall, el estado de la conexión o información de la capa de aplicación.
2. **Compara con las reglas**: evalúa las reglas en el orden y con la prioridad definidos por el producto. La política debe especificar qué tráfico se permite, cuál se bloquea y qué eventos se registran.
3. **Aplica la decisión**: acepta, descarta o rechaza la comunicación y, cuando corresponde, genera registros para auditoría y detección de incidentes.

En un firewall con seguimiento de estado (*stateful*), las respuestas a conexiones iniciadas desde dentro suelen reconocerse como parte de una sesión válida. Un filtro sin estado evalúa cada paquete de forma independiente.

---

## 🎯 Ejemplo práctico: reglas con UFW

En un servidor Linux, una política de mínimo privilegio puede bloquear por defecto las conexiones entrantes y abrir únicamente los servicios necesarios. El siguiente ejemplo permite SSH solo desde una subred administrativa, además de tráfico web público:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 192.0.2.0/24 to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status numbered
```

La red `192.0.2.0/24` es un rango reservado para documentación; debe sustituirse por la subred administrativa real antes de aplicar la regla. Conviene confirmar el acceso SSH permitido antes de activar UFW para evitar bloquear la administración remota.

Una configuración como `sudo ufw allow 1:65535/tcp` expondría prácticamente todos los puertos TCP. Es preferible abrir solo los puertos requeridos y limitar por dirección de origen aquellos que no deban ser públicos.

---

## 🛡️ Buenas prácticas

- Aplicar el principio de **denegación por defecto** y permitir solo los flujos necesarios.
- Restringir las reglas por origen, destino, protocolo y puerto siempre que sea posible.
- Revisar y eliminar reglas obsoletas; documentar el motivo y el responsable de cada excepción.
- Registrar los eventos relevantes y revisar los registros para detectar intentos de acceso anómalos.
- Mantener actualizado el firewall y probar los cambios para evitar interrupciones o aperturas accidentales.
- Usar firewalls de host y de red como capas complementarias, sin asumir que uno sustituye al otro.

---

## 🔗 Referencias

- [NIST SP 800-41 Rev. 1: Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final)
- [Documentación de UFW](https://help.ubuntu.com/community/UFW)
- [Documentación de nftables](https://www.netfilter.org/projects/nftables/)
