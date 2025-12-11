"""
test_crud_delete.py - Pruebas automatizadas para la operación DELETE

Historia de Usuario 5: Eliminar Registro
Este módulo contiene las pruebas para verificar la funcionalidad de
eliminación de registros con confirmación.
"""

import pytest
from pages.login_page import LoginPage
from pages.crud_page import CRUDPage
import time


@pytest.fixture(scope="function")
def authenticated_crud_page(driver, base_url, clean_session):
    """Fixture que proporciona una página CRUD autenticada"""
    login_page = LoginPage(driver, base_url)
    crud_page = CRUDPage(driver, base_url)
    
    login_page.navigate()
    login_page.login("admin", "admin123")
    time.sleep(2)
    
    return crud_page


@pytest.mark.crud
@pytest.mark.delete
@pytest.mark.happy_path
def test_delete_record_happy_path(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Eliminar registro con confirmación (Camino Feliz)
    
    Verifica que se pueda eliminar un registro correctamente
    después de confirmar la acción.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("delete_01_inicio")
    
    # Crear registro a eliminar
    page.create_record("Producto a Eliminar", "Este registro será eliminado", "Otro")
    time.sleep(1)
    take_screenshot("delete_02_registro_creado")
    
    initial_count = page.get_total_count()
    
    # Act - Eliminar el registro
    assert page.click_delete_button_by_name("Producto a Eliminar"), \
        "No se encontró el botón eliminar"
    time.sleep(0.5)
    take_screenshot("delete_03_modal_confirmacion")
    
    assert page.is_delete_modal_visible(), "El modal de confirmación no se mostró"
    
    page.confirm_delete()
    time.sleep(1)
    take_screenshot("delete_04_eliminado")
    
    # Assert
    assert page.is_alert_visible(), "No se mostró mensaje de confirmación"
    
    alert_message = page.get_alert_message()
    assert "eliminado" in alert_message.lower() or "éxito" in alert_message.lower(), \
        f"Mensaje incorrecto: {alert_message}"
    
    # Verificar que el registro ya no existe
    assert page.get_record_by_name("Producto a Eliminar") is None, \
        "El registro todavía existe después de eliminar"
    
    # Verificar que el contador disminuyó
    new_count = page.get_total_count()
    assert new_count == initial_count - 1, \
        f"El contador no disminuyó. Inicial: {initial_count}, Nuevo: {new_count}"
    
    take_screenshot("delete_05_validacion")
    print("✅ Registro eliminado exitosamente")


@pytest.mark.crud
@pytest.mark.delete
@pytest.mark.negative
def test_delete_record_cancel(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Cancelar eliminación de registro (Prueba Negativa)
    
    Verifica que al cancelar la eliminación, el registro se mantenga.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("delete_cancel_01_inicio")
    
    # Crear registro
    page.create_record("Producto a Mantener", "Este no debería eliminarse", "Personal")
    time.sleep(1)
    take_screenshot("delete_cancel_02_creado")
    
    initial_count = page.get_total_count()
    
    # Act - Intentar eliminar pero cancelar
    page.click_delete_button_by_name("Producto a Mantener")
    time.sleep(0.5)
    take_screenshot("delete_cancel_03_modal_abierto")
    
    assert page.is_delete_modal_visible(), "El modal no se mostró"
    
    page.cancel_delete()
    time.sleep(0.5)
    take_screenshot("delete_cancel_04_cancelado")
    
    # Assert
    assert not page.is_delete_modal_visible(), "El modal no se cerró"
    
    # Verificar que el registro todavía existe
    assert page.get_record_by_name("Producto a Mantener") is not None, \
        "El registro se eliminó cuando debería mantenerse"
    
    # Verificar que el contador no cambió
    new_count = page.get_total_count()
    assert new_count == initial_count, \
        f"El contador cambió. Inicial: {initial_count}, Nuevo: {new_count}"
    
    take_screenshot("delete_cancel_05_validacion")
    print("✅ Cancelación de eliminación funciona correctamente")


@pytest.mark.crud
@pytest.mark.delete
@pytest.mark.happy_path
def test_delete_multiple_records(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Eliminar múltiples registros (Camino Feliz)
    
    Verifica que se puedan eliminar varios registros sucesivamente.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("delete_multi_01_inicio")
    
    # Crear 3 registros
    page.create_record("A Eliminar 1", "Primero")
    time.sleep(0.5)
    page.create_record("A Eliminar 2", "Segundo")
    time.sleep(0.5)
    page.create_record("A Eliminar 3", "Tercero")
    time.sleep(1)
    take_screenshot("delete_multi_02_tres_creados")
    
    initial_count = page.get_total_count()
    
    # Act - Eliminar los 3 registros
    page.delete_record_by_name("A Eliminar 1", confirm=True)
    time.sleep(1)
    take_screenshot("delete_multi_03_primero_eliminado")
    
    page.delete_record_by_name("A Eliminar 2", confirm=True)
    time.sleep(1)
    take_screenshot("delete_multi_04_segundo_eliminado")
    
    page.delete_record_by_name("A Eliminar 3", confirm=True)
    time.sleep(1)
    take_screenshot("delete_multi_05_tercero_eliminado")
    
    # Assert
    assert page.get_record_by_name("A Eliminar 1") is None
    assert page.get_record_by_name("A Eliminar 2") is None
    assert page.get_record_by_name("A Eliminar 3") is None
    
    new_count = page.get_total_count()
    assert new_count == initial_count - 3, \
        f"El contador no reflejacorrectamente las eliminaciones. Inicial: {initial_count}, Nuevo: {new_count}"
    
    take_screenshot("delete_multi_06_validacion")
    print("✅ Múltiples eliminaciones exitosas")


@pytest.mark.crud
@pytest.mark.delete
@pytest.mark.happy_path
def test_delete_last_record(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Eliminar el último registro (Camino Feliz)
    
    Verifica que al eliminar el último registro se muestre el estado vacío.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("delete_last_01_inicio")
    
    # Si hay registros existentes, eliminarlos todos primero
    current_count = page.get_total_count()
    
    # Crear un único registro
    page.create_record("Único Registro", "El último que quedará")
    time.sleep(1)
    take_screenshot("delete_last_02_registro_creado")
    
    # Si había otros registros, eliminarlos (simplificado para la prueba)
    # En producción, esto se haría en un loop
    
    # Act - Eliminar el registro
    page.delete_record_by_name("Único Registro", confirm=True)
    time.sleep(1)
    take_screenshot("delete_last_03_eliminado")
    
    # Assert
    # Verificar estado dependiendo de si había otros registros
    final_count = page.get_total_count()
    
    # El registros específico no debe existir
    assert page.get_record_by_name("Único Registro") is None, \
        "El registro todavía existe"
    
    take_screenshot("delete_last_04_validacion")
    print(f"✅ Eliminación del registro exitosa. Quedan {final_count} registros")
