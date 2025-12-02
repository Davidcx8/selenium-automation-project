"""
conftest.py - Configuración de pytest y fixtures para las pruebas
"""

import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path


# Configuración de rutas
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / "app"
REPORTS_DIR = BASE_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
HTML_REPORTS_DIR = REPORTS_DIR / "html"

# Crear directorios si no existen
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
HTML_REPORTS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="function")
def driver():
    """
    Fixture que proporciona una instancia de ChromeDriver para cada prueba.
    Se cierra automáticamente después de cada prueba.
    """
    # Configurar opciones de Chrome
    chrome_options = Options()
    
    # Opciones recomendadas para pruebas
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    
    # Descomentar para ejecutar en modo headless (sin interfaz gráfica)
    # chrome_options.add_argument("--headless")
    
    # Inicializar el driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Configurar timeouts implícitos
    driver.implicitly_wait(10)
    
    yield driver
    
    # Cerrar el navegador después de la prueba
    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    """
    Fixture que proporciona la URL base de la aplicación.
    """
    # Usar file:// para archivos HTML locales
    return f"file:///{str(APP_DIR).replace(os.sep, '/')}"


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Hook de pytest para capturar el resultado de cada prueba.
#     Permite tomar capturas de pantalla en caso de fallos.
#     """
#     # Ejecutar todas las demás hooks para obtener el resultado
#     outcome = yield
#     rep = outcome.get_result()
#     
#     # Determinar qué fase de la prueba estamos
#     setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    """
    Fixture que toma captura de pantalla automáticamente si una prueba falla.
    Versión simplificada para máxima compatibilidad.
    """
    yield
    
    # Intentar tomar captura si hay indicio de fallo (o siempre al final para debug)
    # Nota: Sin el hook makereport, no podemos saber con certeza si falló en teardown.
    # Pero podemos intentar capturar si la excepción está en request.node
    
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = request.node.name
            screenshot_name = f"FAIL_{test_name}_{timestamp}.png"
            screenshot_path = SCREENSHOTS_DIR / screenshot_name
            driver.save_screenshot(str(screenshot_path))
            print(f"\n📸 Captura guardada: {screenshot_path}")
        except:
            pass


# COMENTADO POR COMPATIBILIDAD CON PYTEST-HTML 4.x
# def pytest_html_report_title(report):
#     report.title = "Reporte de Pruebas Automatizadas - Selenium"

# def pytest_configure(config):
#     config._metadata = {
#         'Proyecto': 'Sistema de Gestión CRUD',
#         'Tester': 'Automatización Selenium',
#         'Framework': 'Selenium + pytest',
#         'Navegador': 'Google Chrome',
#         'Ambiente': 'Local'
#     }

# def pytest_html_results_table_header(cells):
#     cells.insert(2, '<th>Descripción</th>')
#     cells.insert(1, '<th>Tiempo</th>')

# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, f'<td>{report.description}</td>')
#     cells.insert(1, f'<td>{report.duration:.2f}s</td>')

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_protocol(item, nextitem):
#     item.description = item.function.__doc__ or ""
#     yield


@pytest.fixture(scope="function")
def take_screenshot(driver):
    """
    Fixture que proporciona una función para tomar capturas de pantalla manualmente.
    Uso: take_screenshot("nombre_descriptivo")
    """
    def _take_screenshot(name: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = SCREENSHOTS_DIR / screenshot_name
        driver.save_screenshot(str(screenshot_path))
        print(f"\n📸 Captura guardada: {screenshot_path}")
        return str(screenshot_path)
    
    return _take_screenshot


@pytest.fixture(scope="function")
def clean_session(driver, base_url):
    """
    Fixture que limpia la sesión antes de cada prueba.
    Elimina cookies, sessionStorage y localStorage.
    """
    try:
        driver.get(f"{base_url}/login.html")
        driver.delete_all_cookies()
        
        # Limpiar sessionStorage y localStorage
        driver.execute_script("sessionStorage.clear(); localStorage.clear();")
    except:
        pass
    
    yield
    
    # Limpiar después de la prueba también
    try:
        driver.execute_script("sessionStorage.clear(); localStorage.clear();")
    except:
        pass
