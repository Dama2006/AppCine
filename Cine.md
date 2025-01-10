# AppCine

## Introducción
Propósito:
La aplicación AppCine es una solución innovadora diseñada para optimizar y modernizar la experiencia de los usuarios en el ámbito cinematográfico. Su objetivo principal es proporcionar una plataforma intuitiva y eficiente para consultar carteleras, gestionar boletos y acceder a servicios complementarios como la dulcería, todo desde una interfaz atractiva y funcional.

## Objetivos:

* Facilitar el acceso rápido y sencillo a la información de películas en estreno y horarios.
* Ofrecer una experiencia personalizada mediante colores personalizados y un diseño amigable.
* Incorporar funcionalidades adicionales que mejoren la experiencia del usuario, como la gestión de pedidos de dulcería.
* Proveer una estructura bien organizada que permita la escalabilidad y el mantenimiento del sistema.

## Contexto del Problema
En la actualidad, la gestión y consulta de información sobre películas y servicios en los cines carece de una integración eficaz. Muchas aplicaciones existentes tienen interfaces complicadas, tiempos de carga prolongados o carecen de funcionalidades clave, como la personalización de la experiencia del usuario.
Ejemplo: Según un estudio reciente, el 65% de los usuarios abandonan una aplicación móvil de cine debido a una mala experiencia de usuario. Además, la falta de accesibilidad para consultar dulcerías y otros servicios desde la misma plataforma genera molestias y disminuye la fidelización de los clientes.

## Justificación:
La creación de AppCine responde a la necesidad de consolidar todos los servicios asociados a los cines en una única aplicación fácil de usar. Con un diseño centrado en el usuario, esta herramienta busca solucionar los puntos débiles de las aplicaciones actuales y mejorar la satisfacción general de los clientes.

## Análisis de Requerimientos
* Requerimientos Funcionales
Estos requerimientos definen las características y funcionalidades principales que la aplicación debe ofrecer:

## Gestión de cartelera:
* Los usuarios deben poder consultar horarios, géneros y sinopsis de películas.
* La cartelera debe estar organizada de forma intuitiva, permitiendo filtrar por fecha, género o clasificación.
* Las actualizaciones en los horarios deben reflejarse automáticamente en la aplicación.
## Compra de boletos:
* Selección de asientos interactiva en un mapa visual de la sala.
* Proceso de compra sencillo y seguro, con opciones de pago integradas (tarjetas de crédito, débito, y billeteras digitales).
* Confirmación de la compra mediante un correo electrónico con el resumen del boleto y un código QR para el ingreso.
## Personalización:
* Permitir a los usuarios cambiar los colores de la interfaz según sus preferencias.
* Guardar configuraciones de personalización en el perfil del usuario para mantener la experiencia consistente.
## Servicios de dulcería:
* Mostrar el menú de productos de la dulcería con imágenes y precios.
* Permitir la compra anticipada de productos para recogida en el cine o entrega directa en la sala.
* Integrar promociones y descuentos especiales para usuarios registrados.
## Soporte para multimedia:
* Mostrar imágenes promocionales, posters y trailers de las películas.
* Optimizar el tiempo de carga de multimedia para garantizar una experiencia fluida.

## Requerimientos No Funcionales
Estos requerimientos aseguran la calidad del sistema y la experiencia del usuario.

## Interfaz de usuario:
* Diseñada para ser intuitiva y atractiva, con un enfoque en la facilidad de uso tanto para usuarios nuevos como recurrentes.
* Diseño responsivo para adaptarse a dispositivos móviles, tabletas y navegadores de escritorio.
## Tiempo de respuesta:
* Todas las páginas y acciones principales deben cargar en menos de 2 segundos en condiciones de red normales.
* Optimización de consultas a la base de datos y uso de caché para mejorar el rendimiento.
## Escalabilidad:
* El sistema debe ser capaz de manejar un crecimiento en la base de usuarios sin comprometer el rendimiento.
* Preparado para integrarse con nuevas funcionalidades, como eventos especiales o reservas de salas privadas.
## Seguridad:
* Implementar protocolos de encriptación SSL para proteger datos sensibles, como información personal y de pago.
* Autenticación segura de usuarios, incluyendo opciones como autenticación de dos factores (2FA) en futuras versiones.

## Clasificación de Requerimientos
####  Esenciales:
* Gestión de cartelera: Actualización y consulta de horarios y detalles de películas.
* Compra de boletos: Selección de asientos y procesamiento de pagos.
#### Deseables:
* Personalización de colores y estilos para una experiencia más atractiva.
* Integración de servicios de dulcería con pedidos anticipados.
#### Opcionales:
* Soporte para múltiples idiomas, adaptándose a audiencias internacionales.
* Opciones avanzadas de personalización, como temas oscuros o claros.
## Modelo
![Modelo Django](https://github.com/user-attachments/assets/cb19e7de-4371-4487-a710-e55b3315b35e)

## Desarrollo de proyecto
