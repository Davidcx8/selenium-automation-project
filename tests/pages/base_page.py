"""
base_page.py - Clase base para Page Object Model
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
from pathlib import Path


class BasePage:
    """
    Clase base que contiene métodos comunes para todos los Page Objects
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.screenshots_dir = Path(__file__).resolve().parent.parent.parent / "reports" / "screenshots"
        self.screenshots_dir.mkdir(parents=True, exist_ok=True)
    
    def find_element(self, locator, timeout=10):
        """
        Encuentra un elemento con espera explícita
        
        Args:
            locator: Tupla (By.ID, "id_value")
            timeout: Tiempo máximo de espera en segundos
            
        Returns:
            WebElement encontrado
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"No se pudo encontrar el elemento: {locator}")
    
    def find_elements(self, locator, timeout=10):
        """
        Encuentra múltiples elementos con espera explícita
        
        Args:
            locator: Tupla (By.CLASS_NAME, "class_value")
            timeout: Tiempo máximo de espera en segundos
            
        Returns:
            Lista de WebElements encontrados
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []
    
    def click_element(self, locator, timeout=10):
        """
        Hace clic en un elemento después de esperar a que sea clickeable
        
        Args:
            locator: Tupla (By.ID, "id_value")
            timeout: Tiempo máximo de espera en segundos
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise TimeoutException(f"El elemento no es clickeable: {locator}")
    
    def send_keys(self, locator, text, clear_first=True, timeout=10):
        """
        Envía texto a un campo de entrada
        
        Args:
            locator: Tupla (By.ID, "id_value")
            text: Texto a enviar
            clear_first: Si debe limpiar el campo primero
            timeout: Tiempo máximo de espera
        """
        element = self.find_element(locator, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def get_text(self, locator, timeout=10):
        """
        Obtiene el texto de un elemento
        
        Args:
            locator: Tupla (By.ID, "id_value")
            timeout: Tiempo máximo de espera
            
        Returns:
            Texto del elemento
        """
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_element_visible(self, locator, timeout=5):
        """
        Verifica si un elemento es visible
        
        Args:
            locator: Tupla (By.ID, "id_value")
            timeout: Tiempo máximo de espera
            
        Returns:
            True si el elemento es visible, False en caso contrario
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=5):
        """
        Verifica si un elemento está presente en el DOM
        
        Args:
            locator: Tupla (By.ID, "id_value")
            timeout: Tiempo máximo de espera
            
        Returns:
            True si el elemento está presente, False en caso contrario
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_url_to_be(self, url, timeout=10):
        """
        Espera a que la URL sea la especificada
        
        Args:
            url: URL esperada
            timeout: Tiempo máximo de espera
            
        Returns:
            True si la URL coincide, False en caso contrario
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False
    
    def wait_for_url_contains(self, url_part, timeout=10):
        """
        Espera a que la URL contenga el texto especificado
        
        Args:
            url_part: Parte de la URL esperada
            timeout: Tiempo máximo de espera
            
        Returns:
            True si la URL contiene el texto, False en caso contrario
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.url_contains(url_part))
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """
        Obtiene la URL actual
        
        Returns:
            URL actual como string
        """
        return self.driver.current_url
    
    def take_screenshot(self, name):
        """
        Toma una captura de pantalla
        
        Args:
            name: Nombre descriptivo para la captura
            
        Returns:
            Ruta del archivo de captura
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = self.screenshots_dir / screenshot_name
        self.driver.save_screenshot(str(screenshot_path))
        return str(screenshot_path)
    
    def execute_script(self, script, *args):
        """
        Ejecuta JavaScript en el navegador
        
        Args:
            script: Script de JavaScript a ejecutar
            *args: Argumentos para el script
            
        Returns:
            Resultado de la ejecución del script
        """
        return self.driver.execute_script(script, *args)
    
    def clear_session_storage(self):
        """
        Limpia el sessionStorage del navegador
        """
        self.execute_script("sessionStorage.clear();")
    
    def clear_local_storage(self):
        """
        Limpia el localStorage del navegador
        """
        self.execute_script("localStorage.clear();")
    
    def refresh_page(self):
        """
        Recarga la página actual
        """
        self.driver.refresh()
    
    def get_alert_text(self):
        """
        Obtiene el texto de una alerta
        
        Returns:
            Texto de la alerta
        """
        alert = self.driver.switch_to.alert
        return alert.text
    
    def accept_alert(self):
        """
        Acepta una alerta
        """
        alert = self.driver.switch_to.alert
        alert.accept()
    
    def dismiss_alert(self):
        """
        Rechaza una alerta
        """
        alert = self.driver.switch_to.alert
        alert.dismiss()
