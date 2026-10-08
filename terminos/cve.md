---
title: "CVE (Common Vulnerabilities and Exposures)"
category: "Gestión de Vulnerabilidades"
author: "@francisjrmoreno"
tags:
  - ciberseguridad
  - cve
  - vulnerabilidades
  - nvd
  - mitre
  - gestion-de-vulnerabilidades
summary: "Sistema estándar de identificación pública de vulnerabilidades que asigna un ID único (CVE-AAAA-NNNN) a cada fallo, facilitando su seguimiento e intercambio entre herramientas y organizaciones."
---

# CVE (Common Vulnerabilities and Exposures)

<div class="term-meta-box">
<div class="term-meta-item">
<span class="term-meta-label">Categoría</span>
<span class="term-meta-value">Gestión de Vulnerabilidades</span>
</div>
<div class="term-meta-item">
<span class="term-meta-label">Autor / Colaborador</span>
<span class="term-meta-value"><a href="https://github.com/francisjrmoreno" target="_blank">@francisjrmoreno</a>, <a href="https://github.com/LuzSerranoDiaz" target="_blank">@LuzSerranoDiaz</a></span>
</div>
</div>

## 📖 Definición
**CVE** (*Common Vulnerabilities and Exposures*) es un programa y un catálogo público que asigna un **identificador único y estandarizado** a vulnerabilidades y exposiciones de seguridad conocidas en software, firmware y hardware. Cada identificador sigue el formato `CVE-AAAA-NNNN`, donde `AAAA` es el año de asignación o publicación y `NNNN` es un número secuencial de cuatro o más dígitos (por ejemplo, `CVE-2021-44228`).

El programa fue lanzado en **1999** por la corporación **MITRE**, con financiación del gobierno de EE. UU. (actualmente a través de **CISA**), para resolver un problema muy concreto: cada fabricante y cada herramienta de seguridad nombraba la misma vulnerabilidad de forma distinta, lo que hacía casi imposible correlacionar alertas, parches e informes. CVE proporciona un "idioma común" para referirse a un mismo fallo.

Conviene distinguir dos conceptos que CVE recoge:

- **Vulnerabilidad**: un fallo en la lógica, el diseño o la implementación que puede ser aprovechado para comprometer la confidencialidad, integridad o disponibilidad de un sistema.
- **Exposición**: una configuración incorrecta o un error que facilita el acceso indebido a datos o capacidades del sistema, sin ser necesariamente un fallo de código.

!!! note "Nota importante"
    CVE **solo identifica y describe** la vulnerabilidad. No indica su gravedad ni cómo explotarla. La puntuación de riesgo (**CVSS**), la clasificación del tipo de debilidad (**CWE**) y la lista de productos afectados (**CPE**) son estándares complementarios que suelen añadirse sobre el identificador CVE, por ejemplo en la **NVD** (*National Vulnerability Database*, del NIST).

---

## ⚙️ ¿Cómo funciona? / Principios fundamentales
El ciclo de vida de un CVE involucra a varios actores: investigadores, fabricantes, **CNAs** (*CVE Numbering Authorities*, organizaciones autorizadas a asignar IDs), el programa CVE y bases de datos que enriquecen el registro.

1. **Descubrimiento y reporte**: un investigador, un cliente o el propio fabricante identifica una vulnerabilidad y la comunica de forma responsable (*coordinated disclosure*) al fabricante o a una CNA.
2. **Asignación del ID**: una CNA (fabricantes como Microsoft, Red Hat o Google, CERTs, o MITRE como CNA de último recurso) **reserva** un identificador `CVE-AAAA-NNNN` para el fallo.
3. **Preparación de la corrección**: mientras el CVE está en estado *reservado*, el fabricante desarrolla y prueba el parche. Los detalles aún no son públicos.
4. **Publicación del registro CVE**: se publica el *CVE Record* con una descripción, los productos y versiones afectados y al menos una referencia pública (aviso del fabricante, *advisory*, parche, etc.). Actualmente el formato de datos es JSON (*CVE JSON 5*).
5. **Enriquecimiento**: bases de datos como la **NVD** añaden puntuación **CVSS**, la debilidad asociada (**CWE**) y los productos afectados en formato **CPE**. CISA puede añadir el CVE al catálogo **KEV** (*Known Exploited Vulnerabilities*) si existe explotación activa.
6. **Consumo por herramientas**: escáneres de vulnerabilidades, SCA, SIEM y gestores de parches usan el ID como clave común para detectar, priorizar y remediar.

!!! warning "CVE no es lo mismo que CVSS ni que CWE"
    - **CVE** → *¿Qué vulnerabilidad concreta es?* (instancia individual).
    - **CWE** → *¿Qué tipo de debilidad es?* (categoría, p. ej. CWE-89: SQL Injection).
    - **CVSS** → *¿Qué gravedad tiene?* (puntuación de 0.0 a 10.0).

---

## 🎯 Ejemplo práctico o escenario de demostración
Un caso paradigmático es **Log4Shell** (`CVE-2021-44228`), una vulnerabilidad de ejecución remota de código en la biblioteca Java **Apache Log4j 2** con puntuación CVSS **10.0**. Una organización que no gestiona CVEs sigue usando la versión afectada sin saberlo; otra que sí lo hace detecta el ID en su inventario de dependencias y actualiza.

=== "Escenario vulnerable / incorrecto"

    ```xml
    <!-- pom.xml: dependencia fijada a una versión afectada por CVE-2021-44228 -->
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
        <version>2.14.1</version>
    </dependency>
    ```

    Sin inventario de componentes ni escaneo de dependencias, nadie en la organización sabe que este servicio es vulnerable hasta que es explotado.

=== "Escenario seguro / remediado"

    ```xml
    <!-- pom.xml: versión corregida tras consultar el CVE y el aviso del fabricante -->
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
        <version>2.17.1</version>
    </dependency>
    ```

    ```bash
    # Detección automática de CVEs en el proyecto (ejemplos con herramientas SCA)
    trivy fs --scanners vuln .
    osv-scanner --lockfile=pom.xml
    ```

---

## 🛡️ Medidas de mitigación y buenas prácticas
Recomendaciones para gestionar correctamente las vulnerabilidades identificadas mediante CVE (alineadas con OWASP A06:2021 *Vulnerable and Outdated Components*, NIST SP 800-40 y los controles CIS):

- [x] **Mantener un inventario de activos y software (SBOM)**: no se puede parchear lo que no se sabe que existe. Generar SBOM en formato CycloneDX o SPDX.
- [x] **Automatizar el escaneo continuo**: integrar herramientas SCA y de escaneo (OWASP Dependency-Check, Trivy, Grype, Dependabot, OSV-Scanner) en el pipeline CI/CD.
- [x] **Priorizar por riesgo real, no solo por CVSS**: combinar CVSS con **EPSS** (probabilidad de explotación), la presencia en el catálogo **CISA KEV** y la criticidad del activo afectado.
- [x] **Definir SLAs de remediación**: plazos de parcheo según severidad (por ejemplo, críticas en 48-72 h, altas en 7-15 días).
- [x] **Suscribirse a fuentes de avisos**: avisos de fabricantes, CERTs nacionales (INCIBE-CERT, CCN-CERT), feeds de la NVD y de CISA.
- [x] **Aplicar mitigaciones temporales cuando no haya parche**: segmentación de red, reglas de WAF/IPS (*virtual patching*), desactivación de funcionalidades vulnerables.
- [x] **Verificar tras el parcheo**: reescanear para confirmar que el CVE ya no aparece y documentar la excepción si se acepta el riesgo.

---

## 🔗 Referencias y enlaces de interés
- [CVE Program (sitio oficial)](https://www.cve.org)
- [NVD - National Vulnerability Database (NIST)](https://nvd.nist.gov)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [CVSS - Common Vulnerability Scoring System (FIRST)](https://www.first.org/cvss/)
- [EPSS - Exploit Prediction Scoring System (FIRST)](https://www.first.org/epss/)
- [MITRE CWE - Common Weakness Enumeration](https://cwe.mitre.org)
- [OWASP Top 10 A06:2021 - Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)
- [NIST SP 800-40 Rev. 4 - Guide to Enterprise Patch Management Planning](https://csrc.nist.gov/pubs/sp/800/40/r4/final)