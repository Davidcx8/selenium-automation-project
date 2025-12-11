"""
conftest.py - Configuración simplificada de pytest
"""

import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pathlib import Path

# Configuración de rutas
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / "app"
REPORTS_DIR = BASE_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"

# Crear directorios
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="function")
def driver():
    """Fixture del driver de Chrome"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Intentar encontrar Chrome
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            options.binary_location = path
            break
    
    # Crear driver
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    # Cleanup
    try:
        driver.quit()
    except:
        pass


@pytest.fixture(scope="function")
def base_url():
    """URL base de la aplicación"""
    return f"file:///{str(APP_DIR).replace(os.sep, '/')}"


@pytest.fixture(scope="function")
def clean_session(driver):
    """Limpiar sessionStorage antes y después de cada prueba"""
    # No limpiar al inicio - el test navegará primero
    yield
    # Limpiar al final si la página está cargada
    try:
        driver.execute_script("sessionStorage.clear();")
        driver.execute_script("localStorage.clear();")
    except:
        pass  # Ignorar si no hay página cargada

@pytest.fixture(scope="function")
def take_screenshot(driver, request):
    """Fixture para tomar capturas de pantalla"""
    def _screenshot(name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = SCREENSHOTS_DIR / screenshot_name
        driver.save_screenshot(str(screenshot_path))
        return str(screenshot_path)
    
    return _screenshot
