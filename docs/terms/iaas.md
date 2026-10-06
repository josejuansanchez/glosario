---
title: "IaaS (Infraestructura como Servicio)"
category: "Computación en la nube"
author: "@josejuansanchez"
tags:
    - ciberseguridad
    - iaas
    - cloud
    - seguridad-cloud
summary: "Modelo de computación en la nube que ofrece recursos virtualizados bajo demanda; el cliente gestiona sus sistemas operativos, aplicaciones y datos."
---

# IaaS (Infraestructura como Servicio)

<div class="term-meta-box">
	<div class="term-meta-item">
		<span class="term-meta-label">Categoría</span>
		<span class="term-meta-value">Computación en la nube</span>
	</div>
	<div class="term-meta-item">
		<span class="term-meta-label">Autor / Colaborador</span>
		<span class="term-meta-value"><a href="https://github.com/josejuansanchez" target="_blank">@josejuansanchez</a></span>
	</div>
</div>

## 📖 Definición

**IaaS** (*Infrastructure as a Service*, infraestructura como servicio) es un modelo de computación en la nube en el que un proveedor ofrece recursos informáticos virtualizados, como capacidad de procesamiento, almacenamiento y redes, que el cliente puede aprovisionar bajo demanda. En lugar de comprar y mantener servidores físicos, la organización utiliza esos recursos a través de una plataforma del proveedor.

El proveedor mantiene la infraestructura física y la capa de virtualización. El cliente suele administrar los sistemas operativos invitados, las aplicaciones, los datos, las identidades y buena parte de la configuración de red. La división exacta de responsabilidades depende del servicio contratado.

!!! note "Responsabilidad compartida"
		Usar IaaS no transfiere toda la responsabilidad de seguridad al proveedor. Este protege la infraestructura que opera; el cliente debe configurar y proteger los recursos que despliega sobre ella.

---

## ⚙️ ¿Cómo funciona? / Principios Fundamentales

1. **Aprovisionamiento**: El cliente crea recursos virtuales, como máquinas, discos y redes, mediante una consola, una API o herramientas de infraestructura como código.
2. **Gestión del sistema**: El cliente selecciona y mantiene el sistema operativo, instala aplicaciones y define las reglas de acceso a sus cargas de trabajo.
3. **Operación del proveedor**: El proveedor mantiene los centros de datos, los equipos físicos y la plataforma de virtualización que soporta esos recursos.
4. **Escalado y consumo**: Los recursos pueden ampliarse, reducirse o eliminarse según las necesidades; normalmente, el uso se factura de acuerdo con el servicio y el tiempo consumido.

---

## 🎯 Ejemplo Práctico o Escenario de Demostración

Una organización despliega una máquina virtual para alojar una aplicación web. Si deja el acceso administrativo SSH abierto a cualquier dirección de Internet y no aplica actualizaciones, aumenta la posibilidad de intrusión y explotación de vulnerabilidades.

=== "Configuración insegura"

		La máquina virtual acepta conexiones SSH desde cualquier origen (`0.0.0.0/0`), usa credenciales débiles y conserva el sistema operativo sin parches. Aunque la infraestructura física sea responsabilidad del proveedor, estas decisiones de configuración corresponden al cliente.

=== "Configuración más segura"

		Se limita el acceso administrativo a una VPN o a direcciones autorizadas, se utiliza autenticación robusta y se mantiene el sistema actualizado. La aplicación solo expone los puertos necesarios y los registros relevantes se supervisan.

---

## 🛡️ Medidas de Mitigación y Buenas Prácticas

- **Aplicar el mínimo privilegio**: Conceder a usuarios, servicios y cuentas de máquina únicamente los permisos necesarios; proteger especialmente las cuentas administrativas con MFA.
- **Endurecer y mantener los sistemas**: Deshabilitar servicios innecesarios, instalar actualizaciones de seguridad y usar imágenes base mantenidas.
- **Restringir la exposición de red**: Denegar el tráfico entrante por defecto y permitir solo los puertos, orígenes y destinos requeridos. Evitar interfaces administrativas expuestas directamente a Internet.
- **Proteger los datos**: Clasificarlos, cifrarlos en tránsito y en reposo cuando corresponda, y controlar las copias de seguridad y su restauración.
- **Supervisar la configuración**: Registrar cambios y accesos, revisar alertas y detectar recursos públicos o configuraciones que se desvíen de la política de seguridad.
- **Aclarar responsabilidades**: Consultar el modelo de responsabilidad compartida del proveedor para cada servicio y documentar qué controles debe operar el cliente.

---

## 🔗 Referencias y Enlaces de Interés

- [NIST SP 800-145: The NIST Definition of Cloud Computing](https://csrc.nist.gov/pubs/sp/800/145/final)
- [AWS: Modelo de responsabilidad compartida](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [Microsoft: Responsabilidad compartida en la nube](https://learn.microsoft.com/es-es/azure/security/fundamentals/shared-responsibility)
