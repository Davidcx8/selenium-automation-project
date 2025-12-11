# Historias de Usuario - Sistema de Gestión de Registros con Pruebas Automatizadas

## Épicas del Proyecto

### Épica 1: Autenticación y Seguridad
Gestión de acceso y seguridad del sistema

### Épica 2: Gestión de Registros (CRUD)
Operaciones completas para crear, leer, actualizar y eliminar registros

### Épica 3: Automatización de Pruebas
Suite completa de pruebas automatizadas para validar el sistema

---

## Historia de Usuario 1: Login de Usuario

**ID**: HU-001  
**Épica**: Autenticación y Seguridad  
**Puntos**: 3  
**Prioridad**: Alta

**Como** usuario del sistema  
**Quiero** poder autenticarme con mis credenciales  
**Para** acceder de forma segura a la funcionalidad de gestión de registros

### Criterios de Aceptación

- El sistema debe mostrar una página de login con campos de usuario y contraseña
- El usuario puede ingresar credenciales válidas (admin/admin123) y acceder al sistema
- Si las credenciales son incorrectas, debe mostrarse un mensaje de error claro
- Los campos vacíos deben ser validados antes de intentar login
- Después de login exitoso, el usuario debe ser redirigido a la página principal
- El sistema debe mantener la sesión del usuario mediante sessionStorage
- Debe existir un botón de "Cerrar Sesión" visible después del login

---

## Historia de Usuario 2: Crear Nuevo Registro

**ID**: HU-002  
**Épica**: Gestión de Registros  
**Puntos**: 5  
**Prioridad**: Alta

**Como** usuario autenticado  
**Quiero** poder crear nuevos registros con información relevante  
**Para** almacenar y organizar mis datos de forma estructurada

### Criterios de Aceptación

- Debe existir un botón visible "Nuevo Registro" en la interfaz principal
- Al hacer clic, debe abrirse un modal/formulario con los siguientes campos:
  - Nombre (requerido, máximo 100 caracteres)
  - Descripción (opcional, máximo 500 caracteres)
  - Categoría (opcional, selección de opciones predefinidas)
  - Fecha (opcional, tipo date)
- El campo "Nombre" es obligatorio y debe validarse
- El sistema debe asignar automáticamente un ID único a cada registro
- Debe mostrarse un mensaje de confirmación tras crear exitosamente
- El nuevo registro debe aparecer inmediatamente en la lista
- Los botones "Guardar" y "Cancelar" deben funcionar correctamente
- El formulario debe limpiarse después de guardar exitosamente

---

## Historia de Usuario 3: Visualizar Lista de Registros

**ID**: HU-003  
**Épica**: Gestión de Registros  
**Puntos**: 3  
**Prioridad**: Alta

**Como** usuario autenticado  
**Quiero** ver todos mis registros en una lista ordenada  
**Para** consultar rápidamente la información almacenada

### Criterios de Aceptación

- La lista debe mostrarse en formato de tabla con las columnas: ID, Nombre, Descripción, Categoría, Fecha, Acciones
- Todos los registros deben cargarse automáticamente al acceder a la página
- Si no hay registros, debe mostrarse un mensaje "No hay registros disponibles"
- Debe mostrarse un contador con el total de registros
- Los datos deben persistirse en localStorage
- La interfaz debe ser responsive y clara
- Cada registro debe tener botones de acción visibles (Editar, Eliminar)

---

## Historia de Usuario 4: Actualizar Registro Existente

**ID**: HU-004  
**Épica**: Gestión de Registros  
**Puntos**: 5  
**Prioridad**: Alta

**Como** usuario autenticado  
**Quiero** poder modificar la información de registros existentes  
**Para** mantener mis datos actualizados y corregir errores

### Criterios de Aceptación

- Cada registro debe tener un botón "Editar" claramente visible
- Al hacer clic en "Editar", debe abrirse el mismo formulario usado para crear
- El formulario debe pre-llenarse con los datos actuales del registro
- El título del modal debe cambiar a "Editar Registro"
- El usuario puede modificar cualquier campo excepto el ID
- Las mismas validaciones de creación deben aplicarse
- Al guardar, los cambios deben reflejarse inmediatamente en la lista
- Debe mostrarse mensaje de confirmación tras actualizar exitosamente
- El botón "Cancelar" debe cerrar el modal sin guardar cambios

---

## Historia de Usuario 5: Eliminar Registro

**ID**: HU-005  
**Épica**: Gestión de Registros  
**Puntos**: 3  
**Prioridad**: Alta

**Como** usuario autenticado  
**Quiero** poder eliminar registros que ya no necesito  
**Para** mantener mi lista de datos limpia y organizada

### Criterios de Aceptación

- Cada registro debe tener un botón "Eliminar" claramente visible
- Al hacer clic en "Eliminar", debe mostrarse un modal de confirmación
- El modal debe advertir que la acción no se puede deshacer
- El usuario puede confirmar o cancelar la eliminación
- Si se confirma, el registro debe eliminarse de la lista inmediatamente
- Debe mostrarse mensaje de confirmación tras eliminar exitosamente
- El contador total de registros debe actualizarse
- Si se elimina el último registro, debe mostrarse el estado vacío

---

## Historia de Usuario 6: Validación de Campos en Formularios

**ID**: HU-006  
**Épica**: Gestión de Registros  
**Puntos**: 2  
**Prioridad**: Media

**Como** usuario del sistema  
**Quiero** que se validen mis datos antes de guardarlos  
**Para** asegurar la integridad y calidad de la información

### Criterios de Aceptación

- El campo "Nombre" no puede estar vacío
- El campo "Nombre" tiene límite de 100 caracteres
- El campo "Descripción" tiene límite de 500 caracteres
- El límite de caracteres debe visualizarse al usuario
- Debe mostrarse mensaje de error claro si la validación falla
- El botón "Guardar" solo debe funcionar con datos válidos
- Las fechas futuras deben permitirse pero mostrar advertencia opcional

---

## Historia de Usuario 7: Persistencia de Datos

**ID**: HU-007  
**Épica**: Gestión de Registros  
**Puntos**: 2  
**Prioridad**: Alta

**Como** usuario del sistema  
**Quiero** que mis datos se guarden localmente  
**Para** no perder información al cerrar o recargar la página

### Criterios de Aceptación

- Los registros deben guardarse en localStorage del navegador
- Los datos deben cargarse automáticamente al abrir la aplicación
- La sesión de usuario debe guardarse en sessionStorage
- Al cerrar sesión, solo se debe limpiar sessionStorage (no los registros)
- Los datos deben persistir entre recargas de página
- El formato de almacenamiento debe ser JSON válido

---

## Historia de Usuario 8: Gestión de Sesión

**ID**: HU-008  
**Épica**: Autenticación y Seguridad  
**Puntos**: 3  
**Prioridad**: Alta

**Como** usuario del sistema  
**Quiero** que el sistema mantenga mi sesión activa  
**Para** no tener que autenticarme en cada interacción

### Criterios de Aceptación

- El sistema debe verificar si hay sesión activa al cargar index.html
- Si no hay sesión, debe redirigir automáticamente a login.html
- La información del usuario debe mostrarse en la barra de navegación
- El botón "Cerrar Sesión" debe limpiar la sesión y redirigir a login
- No debe ser posible acceder a index.html sin autenticarse
- La sesión debe limpiarse completamente al cerrar sesión

---

## Historia de Usuario 9: Pruebas Automatizadas de Login

**ID**: HU-009  
**Épica**: Automatización de Pruebas  
**Puntos**: 5  
**Prioridad**: Alta

**Como** desarrollador/tester  
**Quiero** automatizar las pruebas de autenticación  
**Para** validar que el login funciona correctamente en diferentes escenarios

### Criterios de Aceptación

- Prueba de login exitoso con credenciales válidas
- Prueba de login fallido con credenciales incorrectas
- Prueba de validación de campos vacíos
- Prueba de validación de solo usuario sin contraseña
- Prueba de validación de solo contraseña sin usuario
- Prueba de múltiples intentos fallidos
- Todas las pruebas deben generar capturas de pantalla automáticas
- Las pruebas deben reportarse en formato HTML

---

## Historia de Usuario 10: Pruebas Automatizadas CRUD Completas

**ID**: HU-010  
**Épica**: Automatización de Pruebas  
**Puntos**: 8  
**Prioridad**: Alta

**Como** desarrollador/tester  
**Quiero** automatizar todas las operaciones CRUD  
**Para** asegurar que el sistema funciona correctamente en todos los escenarios

### Criterios de Aceptación

- **CREATE**: Mínimo 8 casos de prueba
  - Camino feliz con todos los campos
  - Solo campo requerido
  - Validación de campos vacíos
  - Validación de límites de caracteres
  - Prueba con fecha futura
  - Cancelación de creación
  
- **READ**: Mínimo 4 casos de prueba
  - Visualización de registros existentes
  - Lista vacía
  - Verificación de detalles completos
  - Contador de registros
  
- **UPDATE**: Mínimo 4 casos de prueba
  - Actualización exitosa
  - Actualización parcial de campos
  - Validación al actualizar
  - Cancelación de actualización
  
- **DELETE**: Mínimo 4 casos de prueba
  - Eliminación con confirmación
  - Cancelación de eliminación
  - Eliminación múltiple
  - Eliminación del último registro

- Todas las pruebas deben usar Page Object Model (POM)
- Generación automática de reportes HTML
- Capturas de pantalla en fallos
- Mínimo 26 casos de prueba totales funcionando

---

## Resumen de Puntos por Épica

| Épica | Historias | Puntos Totales |
|-------|-----------|----------------|
| Autenticación y Seguridad | 2 | 6 |
| Gestión de Registros | 5 | 20 |
| Automatización de Pruebas | 2 | 13 |
| **TOTAL** | **10** | **39** |

---

## Sprint Planning (Sugerido)

### Sprint 1 (Semana 1-2)
- HU-001: Login de Usuario
- HU-007: Persistencia de Datos
- HU-008: Gestión de Sesión

### Sprint 2 (Semana 3-4)
- HU-002: Crear Nuevo Registro
- HU-003: Visualizar Lista de Registros
- HU-006: Validación de Campos

### Sprint 3 (Semana 5-6)
- HU-004: Actualizar Registro
- HU-005: Eliminar Registro

### Sprint 4 (Semana 7-8)
- HU-009: Pruebas Automatizadas de Login
- HU-010: Pruebas Automatizadas CRUD Completas
