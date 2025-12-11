# Script para Video Demostrativo
## Sistema de Gestión de Registros con Pruebas Automatizadas

**Duración estimada**: 5-8 minutos  
**Objetivo**: Demostrar las funcionalidades del primer release del sistema

---

## SECCIÓN 1: INTRODUCCIÓN (30 segundos)

### Elementos a mostrar:
- Título del proyecto en pantalla
- Información básica (Estudiante, Matrícula)

### Narración sugerida:
> "Este es el proyecto Sistema de Gestión de Registros con Pruebas Automatizadas, desarrollado como proyecto final de Programación III en ITLA. El sistema implementa operaciones CRUD completas con autenticación y una suite de 26 pruebas automatizadas, siguiendo metodología Scrum."

---

## SECCIÓN 2: DEMOSTRACIÓN DE LA APLICACIÓN WEB (3 minutos)

### 2.1 Login - Camino Feliz (40 segundos)
**Acciones**:
1. Abrir `login.html` en el navegador
2. Mostrar la interfaz de login
3. Ingresar credenciales válidas (admin/admin123)
4. Click en "Iniciar Sesión"
5. Verificar redirección a página principal

**Puntos clave a mencionar**:
- Sistema de autenticación funcional
- Validación de credenciales
- Gestión de sesión con sessionStorage

### 2.2 Crear Registros (60 segundos)
**Acciones**:
1. Click en "Nuevo Registro"
2. Llenar formulario completo:
   - Nombre: "Proyecto Final Programación III"
   - Descripción: "Implementación de sistema CRUD con automatización"
   - Categoría: "Estudio"
   - Fecha: Fecha actual
3. Click en "Guardar"
4. Verificar que aparece en la lista

**Puntos clave**:
- Validación de campos
- Almacenamiento en localStorage
- Actualización inmediata de la UI

### 2.3 Visualizar Registros (20 segundos)
**Acciones**:
1. Mostrar tabla con registros
2. Señalar contador total
3. Mostrar diferentes columnas de datos

**Puntos clave**:
- Lista completa de registros
- Contador funcional

### 2.4 Actualizar Registro (40 segundos)
**Acciones**:
1. Click en botón "Editar" de un registro
2. Modificar algún campo
3. Click en "Guardar"
4. Verificar cambios en la lista

**Puntos clave**:
- Pre-carga de datos
- Actualización correcta

### 2.5 Eliminar Registro (40 segundos)
**Acciones**:
1. Click en botón "Eliminar"
2. Mostrar modal de confirmación
3. Click en "Eliminar" (confirmar)
4. Verificar eliminación de la lista

**Puntos clave**:
- Confirmación antes de eliminar
- Eliminación correcta

---

## SECCIÓN 3: PRUEBAS AUTOMATIZADAS (2 minutos)

### 3.1 Mostrar Estructura del Proyecto (20 segundos)
**Acciones**:
1. Abrir explorador de archivos
2. Mostrar estructura de carpetas:
   - `/app` - Aplicación web
   - `/tests` - Pruebas automatizadas
   - `/tests/pages` - Page Object Model
   - `/reports` - Reportes generados

**Puntos clave**:
- Organización del proyecto
- Uso de Page Object Model

### 3.2 Ejecutar Pruebas (40 segundos)
**Acciones**:
1. Abrir terminal
2. Ejecutar comando: `pytest tests/ --html=reports/html/report.html --self-contained-html -v`
3. Mostrar pruebas ejecutándose (puede ser acelerado)
4. Mostrar resumen final

**Puntos clave**:
- 26 casos de prueba
- Ejecución automatizada
- Resultados en tiempo real

### 3.3 Visualizar Reporte HTML (60 segundos)
**Acciones**:
1. Abrir `reports/html/report.html`
2. Mostrar resumen ejecutivo:
   - Total de pruebas
   - Passed/Failed
   - Duración
3. Expandir algunos casos de prueba para mostrar detalles
4. Mostrar capturas de pantalla integradas

**Puntos clave**:
- Reporte profesional
- Evidencias visuales
- Información detallada

---

## SECCIÓN 4: DOCUMENTACIÓN Y JIRA (1.5 minutos)

### 4.1 Documentación (40 segundos)
**Acciones**:
1. Abrir carpeta `/docs`
2. Mostrar archivos de documentación:
   - Secciones del proyecto
   - Historias de usuario
   - Plantillas
3. Abrir uno de los archivos para mostrar contenido

**Puntos clave**:
- Documentación completa
- Organización por secciones
- Historias de usuario detalladas

### 4.2 Tablero Jira (50 segundos)
**Acciones**:
1. Abrir navegador en Jira
2. Mostrar backlog con las 10 historias de usuario
3. Abrir una historia para mostrar:
   - Descripción
   - Criterios de aceptación
   - Puntos de historia
   - Estado
4. Mostrar organización en épicas (si está configurado)

**Puntos clave**:
- 10 historias de usuario completas
- Criterios de aceptación
- Metodología Scrum aplicada

---

## SECCIÓN 5: REPOSITORIO GITHUB (40 segundos)

**Acciones**:
1. Abrir repositorio en GitHub
2. Mostrar README.md
3. Scroll por las secciones principales
4. Mostrar commits recientes

**Puntos clave**:
- Código versionado
- README profesional
- Repositorio público

---

## SECCIÓN 6: CIERRE (20 segundos)

### Narración final sugerida:
> "Este proyecto demuestra la implementación completa de un sistema CRUD con autenticación, incluyendo 26 pruebas automatizadas con Selenium y pytest, siguiendo la metodología Scrum con 10 historias de usuario definidas. El proyecto incluye documentación completa, tablero Jira configurado y repositorio Git funcional."

### Mostrar en pantalla:
- Nombre del proyecto
- Estudiante: Jose David Castillo
- Matrícula: 20241546
- Enlaces principales (GitHub, Jira)

---

## NOTAS TÉCNICAS

### Preparación antes de grabar:
- [ ] Cerrar pestañas innecesarias del navegador
- [ ] Limpiar historial de navegación
- [ ] Reiniciar el localStorage (datos frescos)
- [ ] Tener terminal abierta en directorio del proyecto
- [ ] Tener Jira abierto y logueado
- [ ] Verificar resolución de pantalla (1920x1080 recomendado)
- [ ] Cerrar notificaciones y distracciones

### Software necesario para grabar:
- OBS Studio (gratuito) - Recomendado
- O Captura de pantalla de Windows (Win + G)
- O ScreenToGif para GIFs animados

### Configuración de grabación:
- Resolución: 1920x1080 o 1280x720
- FPS: 30
- Formato: MP4
- Audio: Opcional (puedes agregar narración o música de fondo)

### Post-producción (opcional):
- Agregar títulos/subtítulos
- Acelerar sección de ejecución de pruebas
- Agregar música de fondo
- Agregar intro/outro

---

## TIMELINE DETALLADO

| Tiempo | Sección | Contenido |
|--------|---------|-----------|
| 0:00-0:30 | Intro | Presentación del proyecto |
| 0:30-3:30 | App Web | Demostración completa CRUD |
| 3:30-5:30 | Pruebas | Ejecución y reporte |
| 5:30-7:00 | Docs/Jira | Documentación y gestión |
| 7:00-7:40 | GitHub | Repositorio |
| 7:40-8:00 | Cierre | Resumen y créditos |

**Duración total**: ~8 minutos
