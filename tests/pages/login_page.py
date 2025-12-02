"""
login_page.py - Page Object para la página de login
"""

from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object para la página de autenticación
    """
    
    # Localizadores
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "btn-login")
    ALERT_CONTAINER = (By.ID, "alert-container")
    ALERT_MESSAGE = (By.ID, "alert-message")
    
    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url
        self.url = f"{base_url}/login.html"
    
    def navigate(self):
        """
        Navega a la página de login
        """
        self.driver.get(self.url)
        return self
    
    def enter_username(self, username):
        """
        Ingresa el nombre de usuario
        
        Args:
            username: Nombre de usuario a ingresar
        """
        self.send_keys(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password):
        """
        Ingresa la contraseña
        
        Args:
            password: Contraseña a ingresar
        """
        self.send_keys(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self):
        """
        Hace clic en el botón de login
        """
        self.click_element(self.LOGIN_BUTTON)
        return self
    
    def login(self, username, password):
        """
        Realiza el proceso completo de login
        
        Args:
            username: Nombre de usuario
            password: Contraseña
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self
    
    def is_alert_visible(self):
        """
        Verifica si la alerta es visible
        
        Returns:
            True si la alerta es visible, False en caso contrario
        """
        return self.is_element_visible(self.ALERT_CONTAINER, timeout=3)
    
    def get_alert_message(self):
        """
        Obtiene el mensaje de alerta
        
        Returns:
            Texto del mensaje de alerta
        """
        if self.is_alert_visible():
            return self.get_text(self.ALERT_MESSAGE)
        return ""
    
    def is_alert_error(self):
        """
        Verifica si la alerta es de error
        
        Returns:
            True si es alerta de error, False en caso contrario
        """
        element = self.find_element(self.ALERT_CONTAINER, timeout=3)
        return "alert-error" in element.get_attribute("class")
    
    def is_alert_success(self):
        """
        Verifica si la alerta es de éxito
        
        Returns:
            True si es alerta de éxito, False en caso contrario
        """
        element = self.find_element(self.ALERT_CONTAINER, timeout=3)
        return "alert-success" in element.get_attribute("class")
    
    def clear_credentials(self):
        """
        Limpia los campos de credenciales
        """
        self.send_keys(self.USERNAME_INPUT, "", clear_first=True)
        self.send_keys(self.PASSWORD_INPUT, "", clear_first=True)
        return self
    
    def is_on_login_page(self):
        """
        Verifica si estamos en la página de login
        
        Returns:
            True si estamos en la página de login
        """
        current_url = self.get_current_url()
        return "login.html" in current_url
    
    def wait_for_redirect_to_index(self, timeout=10):
        """
        Espera a que se redirija a index.html
        
        Args:
            timeout: Tiempo máximo de espera
            
        Returns:
            True si se redirigió, False en caso contrario
        """
        return self.wait_for_url_contains("index.html", timeout)
