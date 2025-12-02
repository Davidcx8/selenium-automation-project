"""
test_login.py - Pruebas automatizadas para el módulo de autenticación

Historia de Usuario 1: Autenticación de Usuario
Este módulo contiene las pruebas para verificar el correcto funcionamiento
del sistema de login, incluyendo camino feliz y pruebas negativas.
"""

import pytest
from tests.pages.login_page import LoginPage
from tests.pages.crud_page import CRUDPage
import time


@pytest.mark.login
@pytest.mark.happy_path
def test_login_happy_path(driver, base_url, clean_session, take_screenshot):
    """
    PRUEBA: Login exitoso con credenciales válidas (Camino Feliz)
    
    Verifica que un usuario pueda iniciar sesión exitosamente
    con credenciales válidas y sea redirigido a la página principal.
    """
    # Arrange
    login_page = LoginPage(driver, base_url)
    crud_page = CRUDPage(driver, base_url)
    
    # Act
    login_page.navigate()
    take_screenshot("login_01_pagina_inicial")
    
    login_page.login("admin", "admin123")
    take_screenshot("login_02_credenciales_ingresadas")
    
    # Esperar redirección
    time.sleep(2)
    take_screenshot("login_03_redireccion_exitosa")
    
    # Assert
    assert crud_page.wait_for_redirect_to_index(timeout=10), \
        "No se redirigió a la página principal"
    
    assert crud_page.is_authenticated(), \
        "El usuario no está autenticado"
    
    current_user = crud_page.get_current_user()
    assert current_user == "admin", \
        f"Usuario incorrecto. Esperado: 'admin', Obtenido: '{current_user}'"
    
    take_screenshot("login_04_validacion_exitosa")
    print("✅ Login exitoso - Usuario autenticado correctamente")


@pytest.mark.login
@pytest.mark.negative
def test_login_invalid_credentials(driver, base_url, clean_session, take_screenshot):
    """
    PRUEBA: Login con credenciales incorrectas (Prueba Negativa)
    
    Verifica que el sistema rechace credenciales inválidas
    y muestre un mensaje de error apropiado.
    """
    # Arrange
    login_page = LoginPage(driver, base_url)
    
    # Act
    login_page.navigate()
    take_screenshot("login_invalid_01_pagina_inicial")
    
    login_page.login("usuario_incorrecto", "password_incorrecta")
    take_screenshot("login_invalid_02_credenciales_incorrectas")
    
    # Esperar que aparezca el mensaje de error
    time.sleep(1)
    take_screenshot("login_invalid_03_mensaje_error")
    
    # Assert
    assert login_page.is_alert_visible(), \
        "No se mostró mensaje de error"
    
    assert login_page.is_alert_error(), \
        "La alerta no es de tipo error"
    
    alert_message = login_page.get_alert_message()
    assert "Usuario o contraseña incorrectos" in alert_message, \
        f"Mensaje de error incorrecto. Obtenido: '{alert_message}'"
    
    assert login_page.is_on_login_page(), \
        "No debería haber redirigido de la página de login"
    
    take_screenshot("login_invalid_04_validacion_error")
    print("✅ Prueba negativa exitosa - Credenciales inválidas rechazadas correctamente")


@pytest.mark.login
@pytest.mark.negative
def test_login_empty_fields(driver, base_url, clean_session, take_screenshot):
    """
    PRUEBA: Login con campos vacíos (Prueba Negativa)
    
    Verifica que el sistema no permita login con campos vacíos
    y muestre un mensaje de error apropiado.
    """
    # Arrange
    login_page = LoginPage(driver, base_url)
    
    # Act
    login_page.navigate()
    take_screenshot("login_empty_01_pagina_inicial")
    
    # Intentar login sin ingresar datos
    login_page.click_login()
    time.sleep(1)
    take_screenshot("login_empty_02_campos_vacios")
    
    # Assert
    assert login_page.is_alert_visible(), \
        "No se mostró mensaje de error para campos vacíos"
    
    alert_message = login_page.get_alert_message()
    assert "complete todos los campos" in alert_message.lower(), \
        f"Mensaje de error incorrecto. Obtenido: '{alert_message}'"
    
    assert login_page.is_on_login_page(), \
        "No debería haber redirigido de la página de login"
    
    take_screenshot("login_empty_03_validacion_error")
    print("✅ Prueba negativa exitosa - Campos vacíos validados correctamente")


@pytest.mark.login
@pytest.mark.negative
def test_login_empty_username(driver, base_url, clean_session, take_screenshot):
    """
    PRUEBA: Login con usuario vacío (Prueba Negativa)
    
    Verifica que el sistema no permita login con solo la contraseña.
    """
    # Arrange
    login_page = LoginPage(driver, base_url)
    
    # Act
    login_page.navigate()
    take_screenshot("login_empty_user_01_pagina")
    
    login_page.enter_password("admin123")
    login_page.click_login()
    time.sleep(1)
    take_screenshot("login_empty_user_02_error")
    
    # Assert
    assert login_page.is_alert_visible(), \
        "No se mostró mensaje de error"
    
    assert login_page.is_on_login_page(), \
        "No debería haber redirigido"
    
    take_screenshot("login_empty_user_03_validacion")
    print("✅ Usuario vacío rechazado correctamente")


@pytest.mark.login
@pytest.mark.negative
def test_login_empty_password(driver, base_url, clean_session, take_screenshot):
    """
    PRUEBA: Login con contraseña vacía (Prueba Negativa)
    
    Verifica que el sistema no permita login con solo el usuario.
    """
    # Arrange
    login_page = LoginPage(driver, base_url)
    
    # Act
    login_page.navigate()
    take_screenshot("login_empty_pass_01_pagina")
    
    login_page.enter_username("admin")
    login_page.click_login()
    time.sleep(1)
    take_screenshot("login_empty_pass_02_error")
    
    # Assert
    assert login_page.is_alert_visible(), \
        "No se mostró mensaje de error"
    
    assert login_page.is_on_login_page(), \
        "No debería haber redirigido"
    
    take_screenshot("login_empty_pass_03_validacion")
    print("✅ Contraseña vacía rechazada correctamente")


@pytest.mark.login
@pytest.mark.negative
def test_login_multiple_failed_attempts(driver, base_url, clean_session, take_screenshot):
    """
    PRUEBA: Múltiples intentos fallidos de login (Prueba Negativa)
    
    Verifica que el sistema muestre advertencia después de 3 intentos fallidos.
    """
    # Arrange
    login_page = LoginPage(driver, base_url)
    login_page.navigate()
    take_screenshot("login_multiple_01_inicio")
    
    # Act - Realizar 3 intentos fallidos
    for i in range(3):
        login_page.clear_credentials()
        login_page.login("admin", f"wrongpass{i}")
        time.sleep(1)
        take_screenshot(f"login_multiple_02_intento_{i+1}")
    
    # Assert
    assert login_page.is_alert_visible(), \
        "No se mostró mensaje después de múltiples intentos"
    
    alert_message = login_page.get_alert_message()
    assert "excedido" in alert_message.lower() or "máximo" in alert_message.lower(), \
        "No se mostró advertencia de intentos máximos"
    
    take_screenshot("login_multiple_03_advertencia_final")
    print("✅ Advertencia de múltiples intentos mostrada correctamente")
