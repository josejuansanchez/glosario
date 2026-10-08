---
title: "Sistema de prevención de intrusiones (IPS)"
category: "Redes / Seguridad de Red"
author: "@Mole43"
tags:
  - ciberseguridad
  - redes
  - seguridad-de-red
  - firewall
  - deteccion
summary: "Sistema de seguridad de red que monitoriza el tráfico en tiempo real y bloquea actividad maliciosa para prevenir intrusiones y ataques."
---

# Sistema de prevención de intrusiones (IPS)

<div class="term-meta-box">
  <div class="term-meta-item">
    <span class="term-meta-label">Categoría</span>
    <span class="term-meta-value">Redes / Seguridad de Red</span>
  </div>
  <div class="term-meta-item">
    <span class="term-meta-label">Autor / Colaborador</span>
    <span class="term-meta-value"><a href="https://github.com/Mole43" target="_blank">@Mole43</a></span>
  </div>
</div>

## 📖 Definición

Un **Sistema de Prevención de Intrusiones (IPS, Intrusion Prevention System)** es una solución de seguridad de red que inspecciona el tráfico en tiempo real para detectar actividades sospechosas, patrones maliciosos o comportamientos anómalos, y responde de manera automática para bloquear, filtrar o mitigar la amenaza antes de que esta perjudique los sistemas o los datos de la organización.

El IPS suele desplegarse en un punto estratégico de la red, como entre el perímetro de Internet y la infraestructura interna, o en segmentos críticos de la organización. A diferencia de un simple monitor de tráfico, su valor principal reside en su capacidad de actuar de forma proactiva: no solo identifica una amenaza, sino que intenta detenerla en el mismo instante en que aparece.

!!! note "Diferencia con IDS"
    Un **IDS (Intrusion Detection System)** se centra en detectar y alertar. Un **IPS** va un paso más allá y puede bloquear la conexión, descartar paquetes o aplicar reglas de mitigación automáticamente.

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales

El funcionamiento de un IPS se basa en la combinación de inspección del tráfico, análisis de contenido y respuesta automatizada:

1. **Captura del tráfico**: El IPS recibe una copia o se sitúa en línea con el flujo de red para observar paquetes, conexiones y sesiones entrantes y salientes.
2. **Inspección profunda**: Analiza protocolos, cabeceras, payloads y patrones de comportamiento para detectar firmas, anomalías o actividades conocidas de malware, escaneos, acceso no autorizado o exfiltración.
3. **Motor de detección**: Emplea distintas técnicas, como:
   - **Firmas**: comparan tráfico con patrones de ataque conocidos.
   - **Detección por anomalías**: identifica comportamientos fuera de la norma.
   - **Reputación / listas negras**: bloquea origen o destinos considerados maliciosos.
   - **Inspección de protocolos**: valida que la comunicación respete el comportamiento esperado.
4. **Respuesta automática**: Cuando se activa una regla, el IPS puede descartar paquetes, cerrar conexiones, bloquear direcciones IP, enviar alertas o ejecutar acciones definidas por la política de seguridad.
5. **Registro y análisis forense**: Guarda eventos y alertas para estudio posterior, identificación de amenazas y mejora de las reglas de prevención.

En otras palabras, un IPS actúa como una capa activa de defensa en profundidad: detecta amenazas en tránsito y toma medidas inmediatas para evitar que entren o se propaguen dentro de la infraestructura.

---

## 🎯 Ejemplo práctico o escenario de demostración

Supongamos que un atacante intenta escanear puertos de un servidor interno o lanzar un ataque de fuerza bruta contra un servicio web. El IPS puede detectar patrones típicos del comportamiento malicioso.

=== "Escenario de ataque"

    ```text
    2026-10-06 12:14:22 ALERT: TCP scan detected from 203.0.113.45
    2026-10-06 12:15:30 ALERT: Multiple failed login attempts to SSH on 10.0.0.12
    2026-10-06 12:16:10 ACTION: Blocked source IP 203.0.113.45 for 600 seconds
    ```

=== "Respuesta del IPS"

    ```text
    Regla activada: "Brute Force Login Attempt"
    Acción: bloquear origen, cerrar socket y registrar evento
    Resultado: el atacante queda aislado antes de poder continuar con el intento de acceso
    ```

Este tipo de respuesta es típica en entornos empresariales donde la reducción de tiempo de exposición es clave para evitar compromisos graves.

---

## 🛡️ Medidas de mitigación y buenas prácticas

- [x] **Actualizar firmas y reglas**: Mantener el IPS actualizado con la última base de conocimientos de amenazas.
- [x] **Segmentación de red**: Ubicar el IPS en puntos críticos para controlar tráfico entre zonas internas, DMZ y accesos externos.
- [x] **Políticas de bloqueo basadas en contexto**: Configurar reglas que bloqueen únicamente tráfico realmente sospechoso, evitando perturbaciones innecesarias.
- [x] **Supervisión de eventos y alertas**: Revisar registros para validar que las reglas no generan falsos positivos ni bloqueos indebidos.
- [x] **Combinar con otras capas de defensa**: Integrar IPS con firewalls, EDR, SIEM y control de acceso para reforzar la respuesta ante incidentes.
- [x] **Hardening y administración segura**: Restringir accesos a la consola del IPS, aplicar autenticación fuerte y revisar cambios en configuración.

---

## 🔗 Referencias y enlaces de interés

- [NIST SP 800-94: Guide to Intrusion Detection and Prevention Systems](https://csrc.nist.gov/publications/detail/sp/800-94/final)
- [CIS Controls v8](https://www.cisecurity.org/controls)
- [Cisco - Intrusion Prevention Systems](https://www.cisco.com/c/en/us/products/security/ips/index.html)
- [Microsoft Learn - Azure Firewall / IPS concepts](https://learn.microsoft.com/)
