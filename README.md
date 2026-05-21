# 🚀 Sistema de Gestión de Registros con Pruebas Automatizadas

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15-green.svg)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-7.4-orange.svg)](https://pytest.org/)

## 📋 Descripción del Proyecto

> [!NOTE]
> **Este proyecto es de practicas**
>
> Sistema completo de gestión de registros (CRUD) con autenticación y suite de pruebas automatizadas desarrollado siguiendo metodología Scrum. Incluye documentación formal completa, tablero Jira con 10 historias de usuario, y 26 casos de prueba automatizados.
>
> 📄 **Documentación Formal**: Ver carpeta `/docs` para documento PDF completo  
> 📊 **Jira**: [Ver Tablero](https://josedavid.atlassian.net/jira/software/projects/SAT/boards/2/backlog)  
> 🎥 **Video Demostrativo**:

Este proyecto implementa un sistema completo de pruebas automatizadas usando **Selenium WebDriver** con Python para una aplicación web CRUD (Crear, Leer, Actualizar, Eliminar). El sistema incluye autenticación de usuarios y gestión de registros, desarrollado siguiendo la metodología ágil **Scrum**.

### Características Principales

✅ **5 Historias de Usuario** completamente implementadas  
✅ **26 Casos de Prueba** automatizados  
✅ **Pruebas de Camino Feliz, Negativas y de Límites**  
✅ **Reportes HTML** con capturas de pantalla automáticas  
✅ **Page Object Model** para código mantenible  
✅ **Aplicación Web Funcional** incluida

---

## 🏗️ Estructura del Proyecto

```
selenium-automation-project/
├── app/                                    # Aplicación web base
│   ├── index.html                         # Página principal CRUD
│   ├── login.html                         # Página de autenticación
│   ├── css/
│   │   └── styles.css                     # Estilos modernos
│   └── js/
│       ├── app.js                         # Lógica del CRUD
│       └── login.js                       # Lógica de autenticación
│
├── docs/                                   # 📄 Documentación del Proyecto Final
│   ├── Proyecto_Final_Documentacion.md    # Portada e índice
│   ├── seccion_1_planificacion.md         # Estrategia de trabajo
│   ├── seccion_2_scrum.md                 # Metodología Scrum
│   ├── seccion_3_plan_pruebas.md          # Plan de pruebas
│   ├── seccion_4_conclusiones_bibliografia.md
│   ├── historias_usuario.md               # 10 Historias de Usuario detalladas
│   ├── COMO_GENERAR_PDF.md                # Guía para crear PDF
│   ├── templates/                         # Plantillas de Scrum
│   └── imagenes/                          # Capturas y diagramas
│
├── tests/                                  # Pruebas automatizadas
│   ├── __init__.py
│   ├── conftest.py                        # Configuración de pytest
│   ├── test_login.py                      # Pruebas de login (6 casos)
│   ├── test_crud_create.py                # Pruebas CREATE (8 casos)
│   ├── test_crud_read.py                  # Pruebas READ (4 casos)
│   ├── test_crud_update.py                # Pruebas UPDATE (4 casos)
│   ├── test_crud_delete.py                # Pruebas DELETE (4 casos)
│   └── pages/                             # Page Object Model
│       ├── __init__.py
│       ├── base_page.py                   # Clase base
│       ├── login_page.py                  # PO del login
│       └── crud_page.py                   # PO del CRUD
│
├── reports/                                # Reportes generados
│   ├── html/
│   │   └── report.html                    # Reporte HTML
│   └── screenshots/                       # Capturas automáticas
│
├── utils/                                  # Utilidades
│   └── __init__.py
│
├── requirements.txt                        # Dependencias Python
├── pytest.ini                             # Configuración pytest
├── .gitignore                             # Exclusiones Git
└── README.md                              # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.8+ | Lenguaje base |
| **Selenium WebDriver** | 4.15.2 | Automatización web |
| **pytest** | 7.4.3 | Framework de testing |
| **pytest-html** | 4.1.1 | Generación de reportes |
| **webdriver-manager** | 4.0.1 | Gestión de ChromeDriver |
| **Google Chrome** | Latest | Navegador de pruebas |

---

## ⚙️ Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- Google Chrome instalado
- Git (opcional, para clonar)

### Paso 1: Clonar o Descargar el Proyecto

```bash
git clone https://github.com/Davidcx8/selenium-automation-project.git
cd selenium-automation-project
```

### Paso 2: Crear Entorno Virtual (Recomendado)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecutar las Pruebas

### Ejecutar Todas las Pruebas

```bash
pytest tests/ --html=reports/html/report.html --self-contained-html -v
```

### Ejecutar Pruebas Específicas

```bash
# Solo pruebas de login
pytest tests/test_login.py -v

# Solo pruebas de CREATE
pytest tests/test_crud_create.py -v

# Solo camino feliz
pytest tests/ -m happy_path -v

# Solo pruebas negativas
pytest tests/ -m negative -v
```

### Ver el Reporte HTML

Después de ejecutar las pruebas, abre:

```
reports/html/report.html
```

O en Windows:
```powershell
start reports/html/report.html
```

---

## 📊 Historias de Usuario y Casos de Prueba

### Historia 1: Autenticación de Usuario 🔐

**Casos de Prueba:**
1. Login exitoso con credenciales válidas (Camino feliz)
2. Login con credenciales incorrectas (Negativo)
3. Login con campos vacíos (Negativo)
4. Login con solo usuario (Negativo)
5. Login con solo contraseña (Negativo)
6. Múltiples intentos fallidos (Negativo)

**Credenciales de Prueba:**
- Usuario: `admin`
- Contraseña: `admin123`

---

### Historia 2: Crear Nuevo Registro ➕

**Casos de Prueba:**
1. Crear registro con datos válidos completos (Camino feliz)
2. Crear registro solo con nombre (Camino feliz)
3. Crear registro con nombre vacío (Negativo)
4. Crear registro con nombre muy largo >100 caracteres (Límites)
5. Crear registro con descripción muy larga >500 caracteres (Límites)
6. Crear registro con fecha futura (Negativo/Advertencia)
7. Cancelar creación de registro (Negativo)

---

### Historia 3: Consultar y Visualizar Registros 👁️

**Casos de Prueba:**
1. Visualizar registros existentes (Camino feliz)
2. Visualizar lista vacía (Camino feliz)
3. Verificar detalles completos de registro (Camino feliz)
4. Verificar contador total de registros (Camino feliz)

---

### Historia 4: Actualizar Registro Existente ✏️

**Casos de Prueba:**
1. Actualizar registro exitosamente (Camino feliz)
2. Actualizar solo algunos campos (Camino feliz)
3. Intentar actualizar con nombre vacío (Negativo)
4. Cancelar actualización (Negativo)

---

### Historia 5: Eliminar Registro 🗑️

**Casos de Prueba:**
1. Eliminar registro con confirmación (Camino feliz)
2. Cancelar eliminación (Negativo)
3. Eliminar múltiples registros (Camino feliz)
4. Eliminar el último registro (Camino feliz)

---

## 📸 Capturas de Pantalla

Las capturas se generan automáticamente en:
- ✅ Cada paso importante de la prueba
- ✅ Cuando una prueba falla
- ✅ Al completar validaciones

Ubicación: `reports/screenshots/`

---

## 🎯 Características del Framework

### Page Object Model (POM)

Implementamos el patrón Page Object Model para:
- ✅ Código reutilizable y mantenible
- ✅ Separación de lógica de prueba y elementos UI
- ✅ Fácil actualización ante cambios en la UI

### Capturas Automáticas

```python
# En conftest.py
@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    # Toma captura automática si la prueba falla
```

### Reportes HTML Detallados

Los reportes incluyen:
- ✅ Resumen ejecutivo
- ✅ Resultados por prueba
- ✅ Capturas de pantalla integradas
- ✅ Tiempos de ejecución
- ✅ Logs detallados

---

## 📚 Documentación del Proyecto Final

### Documento Formal (PDF)

Toda la documentación formal del proyecto está en la carpeta `/docs` con las siguiente secciones:

1. **Portada e Índice**: Información general del proyecto
2. **Estrategia de Trabajo**: Planificación, tecnologías, objetivos, alcance, cronograma, primer release
3. **Metodología Scrum**: Equipo, herramientas, épicas, ceremonias, 10 historias de usuario
4. **Plan de Pruebas**: Requerimientos, criterios, herramientas, cronograma, automatización
5 **Conclusiones y Bibliografía**: Logros, aprendizajes, mejoras futuras, referencias

**📄 Para generar el PDF final**, consulta: `docs/COMO_GENERAR_PDF.md`

### Historias de Usuario

Las 10 historias de usuario están documentadas en:
- **Detalle completo**: `docs/historias_usuario.md`
- **Tablero Jira**: https://josedavid.atlassian.net/jira/software/projects/SAT/boards/2/backlog

### Templates

Plantillas estándar disponibles en `docs/templates/`:
- `plantilla_historia_usuario.md` - Formato para historias de usuario
- `plantilla_caso_prueba.md` - Formato para casos de prueba

### README Técnico

Este README se enfoca en la información técnica para ejecutar y desarrollar el proyecto.

---

## 🔗 Enlaces del Proyecto

### Entregables

- **Repositorio GitHub**: https://github.com/Davidcx8/selenium-automation-project
- **Tablero Jira**: https://josedavid.atlassian.net/jira/software/projects/SAT/boards/2/backlog
- **Videos Demostrativos YouTube**:
  - Parte 1 (Instalación y configuración): https://youtu.be/_7KEweSvsAA
  - Parte 2 (Ejecución de pruebas): https://youtu.be/N-PWXoN5bT0
  - Parte 3 (Reporte y resultados): https://youtu.be/kIWkV8BJs-Y

### Permisos Otorgados

✅ Libre Uso Practico
---

## 📝 Notas Importantes

### Cumplimiento de Requisitos

| Requisito | Estado | Detalle |
|-----------|--------|---------|
| Mínimo 5 historias de usuario | ✅ | 5 historias implementadas |
| Mínimo 1 caso por historia | ✅ | 26 casos totales |
| Pruebas de login | ✅ | 6 casos |
| Pruebas CRUD | ✅ | 20 casos |
| Camino feliz | ✅ | Implementado |
| Pruebas negativas | ✅ | Implementado |
| Pruebas de límites | ✅ | Implementado |
| Reporte HTML | ✅ | Auto-generado |
| Capturas automáticas | ✅ | Implementadas |
| Documentación en Jira | ✅ | Plantillas provistas |
| **NO usar Selenium IDE** | ✅ | **Código puro Selenium** |

---

## 🚫 Advertencias

⚠️ **NO se usó Selenium IDE** - Todo el código es Selenium WebDriver puro con Python  
⚠️ **Proyecto único** - No compartido con otros estudiantes  
⚠️ **Repositorio público** - Accesible para evaluación  

---

## 🐛 Solución de Problemas

### Error: "PowerShell no puede ejecutar scripts"

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error: "ChromeDriver no encontrado"

```bash
pip install --upgrade webdriver-manager
```

### Las pruebas fallan porque la aplicación no carga

Asegúrate de que las rutas en `conftest.py` apuntan correctamente a la carpeta `app/`.

---

## 👨‍💻 Autor

**Jose David Castillo**  
**Desarrollador Software**

---

## 📄 Licencia

Este proyecto es para fines prácticos

---

## ⭐ Agradecimientos

- ITLA - Instituto Tecnológico de Las Américas

---

**Última actualización**: Diciembre 2025
