"""
crud_page.py - Page Object para la página principal del CRUD
"""

from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
import time


class CRUDPage(BasePage):
    """
    Page Object para la página de gestión CRUD
    """
    
    # Localizadores - Navbar
    CURRENT_USER = (By.ID, "current-user")
    LOGOUT_BUTTON = (By.ID, "btn-logout")
    
    # Localizadores - Botones principales
    NEW_RECORD_BUTTON = (By.ID, "btn-new-record")
    
    # Localizadores - Alerta
    ALERT_CONTAINER = (By.ID, "alert-container")
    ALERT_MESSAGE = (By.ID, "alert-message")
    
    # Localizadores - Tabla
    TABLE_BODY = (By.ID, "table-body")
    EMPTY_STATE = (By.ID, "empty-state")
    TOTAL_COUNT = (By.ID, "total-count")
    
    # Localizadores - Modal Crear/Editar
    RECORD_MODAL = (By.ID, "record-modal")
    MODAL_TITLE = (By.ID, "modal-title")
    RECORD_NAME_INPUT = (By.ID, "record-name")
    RECORD_DESCRIPTION_INPUT = (By.ID, "record-description")
    RECORD_CATEGORY_INPUT = (By.ID, "record-category")
    RECORD_DATE_INPUT = (By.ID, "record-date")
    SAVE_BUTTON = (By.ID, "btn-save")
    CANCEL_BUTTON = (By.ID, "btn-cancel")
    
    # Localizadores - Modal Eliminar
    DELETE_MODAL = (By.ID, "delete-modal")
    CONFIRM_DELETE_BUTTON = (By.ID, "btn-confirm-delete")
    CANCEL_DELETE_BUTTON = (By.ID, "btn-cancel-delete")
    
    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url
        self.url = f"{base_url}/index.html"
    
    def navigate(self):
        """
        Navega a la página principal del CRUD
        """
        self.driver.get(self.url)
        return self
    
    # ===== Métodos de Autenticación =====
    
    def is_authenticated(self):
        """
        Verifica si el usuario está autenticado
        
        Returns:
            True si está autenticado, False en caso contrario
        """
        return self.is_element_present(self.CURRENT_USER, timeout=3)
    
    def get_current_user(self):
        """
        Obtiene el nombre del usuario actual
        
        Returns:
            Nombre del usuario
        """
        return self.get_text(self.CURRENT_USER)
    
    def logout(self):
        """
        Cierra sesión
        """
        self.click_element(self.LOGOUT_BUTTON)
        return self
    
    # ===== Métodos de Alertas =====
    
    def is_alert_visible(self):
        """
        Verifica si la alerta es visible
        
        Returns:
            True si la alerta es visible
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
    
    # ===== Métodos de Tabla =====
    
    def get_total_count(self):
        """
        Obtiene el total de registros
        
        Returns:
            Total de registros como entero
        """
        count_text = self.get_text(self.TOTAL_COUNT)
        return int(count_text)
    
    def is_empty_state_visible(self):
        """
        Verifica si el estado vacío es visible
        
        Returns:
            True si no hay registros
        """
        return self.is_element_visible(self.EMPTY_STATE, timeout=3)
    
    def get_table_rows(self):
        """
        Obtiene todas las filas de la tabla
        
        Returns:
            Lista de elementos de fila
        """
        rows = self.find_elements((By.CSS_SELECTOR, "#table-body tr"))
        return rows
    
    def get_table_row_count(self):
        """
        Obtiene el número de filas en la tabla
        
        Returns:
            Número de filas
        """
        rows = self.get_table_rows()
        return len(rows)
    
    def get_record_by_name(self, name):
        """
        Busca un registro por nombre
        
        Args:
            name: Nombre del registro a buscar
            
        Returns:
            Elemento de fila si se encuentra, None en caso contrario
        """
        rows = self.get_table_rows()
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 1 and cells[1].text == name:
                return row
        return None
    
    # ===== Métodos del Modal Crear/Editar =====
    
    def click_new_record(self):
        """
        Hace clic en el botón de nuevo registro
        """
        # Scroll al botón y esperar a que sea clickeable
        button = self.find_element(self.NEW_RECORD_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.3)
        self.click_element(self.NEW_RECORD_BUTTON)
        time.sleep(0.8)  # Esperar animación del modal
        return self
    
    def is_modal_visible(self):
        """
        Verifica si el modal está visible
        
        Returns:
            True si el modal es visible
        """
        return self.is_element_visible(self.RECORD_MODAL, timeout=3)
    
    def get_modal_title(self):
        """
        Obtiene el título del modal
        
        Returns:
            Título del modal
        """
        return self.get_text(self.MODAL_TITLE)
    
    def enter_record_name(self, name):
        """
        Ingresa el nombre del registro
        
        Args:
            name: Nombre a ingresar
        """
        self.send_keys(self.RECORD_NAME_INPUT, name)
        return self
    
    def enter_record_description(self, description):
        """
        Ingresa la descripción del registro
        
        Args:
            description: Descripción a ingresar
        """
        self.send_keys(self.RECORD_DESCRIPTION_INPUT, description)
        return self
    
    def select_record_category(self, category):
        """
        Selecciona la categoría del registro
        
        Args:
            category: Categoría a seleccionar
        """
        element = self.find_element(self.RECORD_CATEGORY_INPUT)
        from selenium.webdriver.support.ui import Select
        select = Select(element)
        select.select_by_visible_text(category)
        return self
    
    def enter_record_date(self, date):
        """
        Ingresa la fecha del registro
        
        Args:
            date: Fecha en formato YYYY-MM-DD
        """
        self.send_keys(self.RECORD_DATE_INPUT, date)
        return self
    
    def click_save(self):
        """
        Hace clic en el botón de guardar
        """
        self.click_element(self.SAVE_BUTTON)
        time.sleep(0.5)  # Esperar que se guarde
        return self
    
    def click_cancel(self):
        """
        Hace clic en el botón de cancelar
        """
        self.click_element(self.CANCEL_BUTTON)
        time.sleep(0.5)  # Esperar animación
        return self
    
    def create_record(self, name, description="", category="", date=""):
        """
        Crea un nuevo registro completo
        
        Args:
            name: Nombre del registro (obligatorio)
            description: Descripción del registro
            category: Categoría del registro
            date: Fecha del registro
        """
        self.click_new_record()
        time.sleep(0.5)  # Esperar a que modal abra completamente
        self.enter_record_name(name)
        
        if description:
            self.enter_record_description(description)
        
        if category:
            self.select_record_category(category)
        
        if date:
            self.enter_record_date(date)
        
        self.click_save()
        
        # Manejar alert de fecha futura si aparece
        try:
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            WebDriverWait(self.driver, 2).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()  # Aceptar el alert
            time.sleep(0.3)
        except:
            pass  # No hay alert, continuar normalmente
        
        time.sleep(0.5)  # Esperar confirmación
        return self
    
    # ===== Métodos para Editar =====
    
    def click_edit_button_by_name(self, name):
        """
        Hace clic en el botón de editar de un registro específico
        
        Args:
            name: Nombre del registro a editar
        """
        row = self.get_record_by_name(name)
        if row:
            edit_button = row.find_element(By.CLASS_NAME, "btn-edit")
            edit_button.click()
            time.sleep(0.5)  # Esperar animación del modal
            return True
        return False
    
    def update_record_name(self, old_name, new_name):
        """
        Actualiza el nombre de un registro
        
        Args:
            old_name: Nombre actual del registro
            new_name: Nuevo nombre del registro
            
        Returns:
            True si se actualizó correctamente
        """
        if self.click_edit_button_by_name(old_name):
            self.enter_record_name(new_name)
            self.click_save()
            time.sleep(0.5)
            return True
        return False
    
    # ===== Métodos para Eliminar =====
    
    def click_delete_button_by_name(self, name):
        """
        Hace clic en el botón de eliminar de un registro específico
        
        Args:
            name: Nombre del registro a eliminar
        """
        row = self.get_record_by_name(name)
        if row:
            delete_button = row.find_element(By.CLASS_NAME, "btn-delete")
            delete_button.click()
            time.sleep(0.5)  # Esperar animación del modal
            return True
        return False
    
    def is_delete_modal_visible(self):
        """
        Verifica si el modal de confirmación de eliminación es visible
        
        Returns:
            True si es visible
        """
        return self.is_element_visible(self.DELETE_MODAL, timeout=3)
    
    def confirm_delete(self):
        """
        Confirma la eliminación
        """
        self.click_element(self.CONFIRM_DELETE_BUTTON)
        time.sleep(0.5)  # Esperar que se elimine
        return self
    
    def cancel_delete(self):
        """
        Cancela la eliminación
        """
        self.click_element(self.CANCEL_DELETE_BUTTON)
        time.sleep(0.5)  # Esperar animación
        return self
    
    def delete_record_by_name(self, name, confirm=True):
        """
        Elimina un registro por nombre
        
        Args:
            name: Nombre del registro a eliminar
            confirm: Si debe confirmar la eliminación
            
        Returns:
            True si se eliminó correctamente
        """
        if self.click_delete_button_by_name(name):
            if confirm:
                self.confirm_delete()
            else:
                self.cancel_delete()
            return True
        return False
    
    def wait_for_redirect_to_index(self, timeout=10):
        """
        Espera a que se redirija a index.html
        
        Args:
            timeout: Tiempo máximo de espera
            
        Returns:
            True si se redirigió, False en caso contrario
        """
        return self.wait_for_url_contains("index.html", timeout)
