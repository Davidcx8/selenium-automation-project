
**Título**: Como usuario, quiero iniciar sesión en el sistema para acceder a las funcionalidades CRUD

**Descripción**:
Como usuario del sistema, necesito poder autenticarme mediante un formulario de login utilizando mi nombre de usuario y contraseña, para poder acceder de forma segura a las funcionalidades de gestión de registros.

**Prioridad**: Alta

**Criterios de Aceptación**:
1. La página de login debe tener campos claramente identificados para usuario y contraseña
2. Al ingresar credenciales válidas (usuario: "admin", contraseña: "admin123"), el usuario es redirigido a la página principal
3. El sistema muestra un mensaje de bienvenida tras login exitoso
4. Los campos tienen validación de entrada (no pueden estar vacíos)
5. El botón de login solo se activa cuando ambos campos tienen datos

**Criterios de Rechazo**:
1. Si el usuario ingresa credenciales inválidas, debe mostrar mensaje de error "Usuario o contraseña incorrectos"
2. Si los campos están vacíos, debe mostrar mensaje "Por favor complete todos los campos"
3. Después de 3 intentos fallidos, debe mostrar mensaje de advertencia
4. No debe permitir acceso a la página principal sin autenticación exitosa
5. Las contraseñas deben ocultarse con asteriscos o puntos

**Casos de Prueba Asociados**:
- `test_login_happy_path()` - Login exitoso
- `test_login_invalid_credentials()` - Credenciales incorrectas  
- `test_login_empty_fields()` - Campos vacíos

---

## Historia 2: Crear Nuevo Registro

**Título**: Como usuario autenticado, quiero crear nuevos registros en el sistema para almacenar información

**Descripción**:
Como usuario autenticado, necesito poder agregar nuevos registros al sistema mediante un formulario, ingresando información como nombre, descripción, categoría y fecha, para mantener un registro organizado de datos.

**Prioridad**: Alta

**Criterios de Aceptación**:
1. El formulario de creación debe tener campos: Nombre (obligatorio), Descripción, Categoría, Fecha
2. Al completar el formulario y hacer clic en "Guardar", el registro se agrega a la tabla
3. El sistema muestra mensaje de confirmación "Registro creado exitosamente"
4. El nuevo registro aparece inmediatamente en la lista
5. El formulario se limpia después de guardar
6. Cada registro debe tener un ID único autogenerado

**Criterios de Rechazo**:
1. No debe permitir crear registros con el campo "Nombre" vacío
2. Debe mostrar error "El nombre es obligatorio" si se intenta guardar sin nombre
3. No debe aceptar nombres con más de 100 caracteres (mostrar error "Nombre muy largo")
4. No debe aceptar descripciones con más de 500 caracteres
5. Fechas futuras deben mostrar advertencia

**Casos de Prueba Asociados**:
- `test_create_record_happy_path()` - Creación exitosa
- `test_create_record_empty_name()` - Campo obligatorio vacío
- `test_create_record_name_too_long()` - Prueba de límite (>100 caracteres)
- `test_create_record_description_too_long()` - Prueba de límite (>500 caracteres)

---

## Historia 3: Consultar y Visualizar Registros

**Título**: Como usuario autenticado, quiero ver la lista de todos los registros para consultar la información almacenada

**Descripción**:
Como usuario autenticado, necesito poder visualizar todos los registros existentes en una tabla organizada, mostrando sus campos principales, para poder consultar y revisar la información almacenada en el sistema.

**Prioridad**: Media

**Criterios de Aceptación**:
1. La página principal debe mostrar una tabla con todos los registros
2. Cada fila debe mostrar: ID, Nombre, Descripción, Categoría, Fecha
3. La tabla debe tener encabezados claros
4. Los registros se ordenan por ID (ascendente) por defecto
5. La tabla es responsiva y se adapta a diferentes tamaños de pantalla
6. Debe mostrar conteo total de registros (ej: "Total: 5 registros")

**Criterios de Rechazo**:
1. Si no hay registros, debe mostrar mensaje "No hay registros disponibles"
2. No debe mostrar campos vacíos como "undefined" o "null"
3. No debe permitir visualizar registros sin estar autenticado
4. La tabla no debe mostrar información truncada o cortada

**Casos de Prueba Asociados**:
- `test_read_records_happy_path()` - Visualización de registros existentes
- `test_read_records_empty_list()` - Lista vacía muestra mensaje apropiado

---

## Historia 4: Actualizar Registro Existente

**Título**: Como usuario autenticado, quiero modificar registros existentes para mantener la información actualizada

**Descripción**:
Como usuario autenticado, necesito poder editar la información de registros existentes mediante un formulario de edición, para corregir errores o actualizar datos que han cambiado.

**Prioridad**: Alta

**Criterios de Aceptación**:
1. Cada registro debe tener un botón "Editar" visible
2. Al hacer clic en "Editar", se abre un formulario con los datos actuales pre-cargados
3. El usuario puede modificar cualquier campo excepto el ID
4. Al hacer clic en "Actualizar", los cambios se guardan
5. El sistema muestra mensaje "Registro actualizado exitosamente"
6. Los cambios se reflejan inmediatamente en la tabla
7. Existe opción para cancelar la edición sin guardar cambios

**Criterios de Rechazo**:
1. No debe permitir actualizar con el campo "Nombre" vacío
2. Debe mostrar error "El nombre es obligatorio" si se intenta guardar sin nombre
3. No debe cambiar el ID del registro
4. No debe aceptar nombres con más de 100 caracteres
5. Al cancelar, no debe guardar ningún cambio

**Casos de Prueba Asociados**:
- `test_update_record_happy_path()` - Actualización exitosa
- `test_update_record_empty_name()` - Campo obligatorio vacío
- `test_update_record_cancel()` - Cancelar no guarda cambios

---

## Historia 5: Eliminar Registro

**Título**: Como usuario autenticado, quiero eliminar registros obsoletos para mantener el sistema limpio

**Descripción**:
Como usuario autenticado, necesito poder eliminar registros que ya no son necesarios, con una confirmación previa, para evitar eliminaciones accidentales y mantener solo información relevante.

**Prioridad**: Media

**Criterios de Aceptación**:
1. Cada registro debe tener un botón "Eliminar" visible
2. Al hacer clic en "Eliminar", se muestra diálogo de confirmación "¿Está seguro que desea eliminar este registro?"
3. Si el usuario confirma, el registro se elimina de la tabla
4. El sistema muestra mensaje "Registro eliminado exitosamente"
5. El registro desaparece inmediatamente de la lista
6. El contador total de registros se actualiza

**Criterios de Rechazo**:
1. Si el usuario cancela en el diálogo, el registro NO debe eliminarse
2. No debe eliminar sin mostrar confirmación
3. No debe permitir eliminar sin estar autenticado
4. Después de eliminar, no debe ser posible recuperar el registro
5. No debe mostrar errores en consola después de eliminar

**Casos de Prueba Asociados**:
- `test_delete_record_happy_path()` - Eliminación exitosa con confirmación
- `test_delete_record_cancel()` - Cancelar mantiene el registro

---



## Instrucciones para Crear en Jira

### Paso a Paso Detallado:

1. **Accede a Jira**
   - Ve a https://www.atlassian.com/software/jira/free
   - Crea tu cuenta o inicia sesión
   - Crea un proyecto tipo **Kanban** llamado "Selenium Automation Tests"

2. **Crea una nueva Historia (Issue)**
   - Haz clic en el botón **Create** (superior central)
   - **Project**: Tu proyecto
   - **Issue Type**: Story (Historia)

3. **Completa los campos**
   - **Summary**: Copia el título de la plantilla (ej: "Como usuario, quiero iniciar sesión...")
   - **Description**: 
     - Pega la descripción completa
     - Pega los **Criterios de Aceptación**
     - Pega los **Criterios de Rechazo**
     - Pega la lista de **Casos de Prueba**
   - **Priority**: High/Medium/Low según corresponda
   - **Assignee**: Asignar a mí (Assign to me)

4. **Guarda la Historia**
   - Haz clic en **Create**

5. **Repite para las 5 historias**
   - Historia 1: Autenticación de Usuario
   - Historia 2: Crear Nuevo Registro
   - Historia 3: Consultar y Visualizar Registros
   - Historia 4: Actualizar Registro Existente
   - Historia 5: Eliminar Registro

---

## Verificación de Completitud

Asegúrate de que CADA historia tenga:

- [x] Título claro en formato "Como [rol], quiero [acción] para [beneficio]"
- [x] Descripción detallada del contexto
- [x] Prioridad asignada
- [x] Mínimo 5 criterios de aceptación específicos y medibles
- [x] Mínimo 3 criterios de rechazo específicos
- [x] Casos de prueba asociados listados

**Total de Historias**: 5 (cumple requisito mínimo)  
**Total de Casos de Prueba Planeados**: 13+ (excede requisito mínimo de 5)
