"""
test_crud_update.py - Pruebas automatizadas para la operación UPDATE

Historia de Usuario 4: Actualizar Registro Existente
Este módulo contiene las pruebas para verificar la funcionalidad de
actualización de registros existentes.
"""

import pytest
from tests.pages.login_page import LoginPage
from tests.pages.crud_page import CRUDPage
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
@pytest.mark.update
@pytest.mark.happy_path
def test_update_record_happy_path(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Actualizar registro exitosamente (Camino Feliz)
    
    Verifica que se pueda actualizar un registro existente correctamente.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("update_01_inicio")
    
    # Crear registro inicial
    page.create_record("Producto Original", "Descripción original", "Trabajo", "2024-01-01")
    time.sleep(1)
    take_screenshot("update_02_registro_creado")
    
    # Act - Editar el registro
    assert page.click_edit_button_by_name("Producto Original"), "No se encontró el botón editar"
    time.sleep(0.5)
    take_screenshot("update_03_modal_editar_abierto")
    
    assert page.is_modal_visible(), "El modal no se abrió"
    assert page.get_modal_title() == "Editar Registro", "Título del modal incorrecto"
    
    # Actualizar campos
    page.enter_record_name("Producto Actualizado")
    page.enter_record_description("Descripción actualizada con nuevos datos")
    page.select_record_category("Personal")
    page.enter_record_date("2024-12-25")
    take_screenshot("update_04_nuevos_datos")
    
    page.click_save()
    time.sleep(1)
    take_screenshot("update_05_guardado")
    
    # Assert
    assert page.is_alert_visible(), "No se mostró mensaje de confirmación"
    alert_message = page.get_alert_message()
    assert "actualizado" in alert_message.lower() or "éxito" in alert_message.lower(), \
        f"Mensaje incorrecto: {alert_message}"
    
    # Verificar que el nombre viejo no existe y el nuevo sí
    assert page.get_record_by_name("Producto Original") is None, \
        "El registro viejo todavía existe"
    
    assert page.get_record_by_name("Producto Actualizado") is not None, \
        "El registro actualizado no aparece"
    
    take_screenshot("update_06_validacion")
    print("✅ Registro actualizado exitosamente")


@pytest.mark.crud
@pytest.mark.update
@pytest.mark.negative
def test_update_record_empty_name(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Intentar actualizar con nombre vacío (Prueba Negativa)
    
    Verifica que no se pueda actualizar un registro dejando el nombre vacío.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("update_empty_01_inicio")
    
    # Crear registro
    page.create_record("Producto a Editar", "Descripción test")
    time.sleep(1)
    take_screenshot("update_empty_02_creado")
    
    # Act - Intentar actualizar con nombre vacío
    page.click_edit_button_by_name("Producto a Editar")
    time.sleep(0.5)
    take_screenshot("update_empty_03_modal_abierto")
    
    page.send_keys(page.RECORD_NAME_INPUT, "", clear_first=True)  # Limpiar nombre
    page.click_save()
    time.sleep(1)
    take_screenshot("update_empty_04_error")
    
    # Assert
    assert page.is_alert_visible(), "No se mostró mensaje de error"
    
    alert_message = page.get_alert_message()
    assert "obligatorio" in alert_message.lower() or "nombre" in alert_message.lower(), \
        f"Mensaje de error incorrecto: {alert_message}"
    
    # El modal debe permanecer abierto
    assert page.is_modal_visible(), "El modal se cerró incorrectamente"
    
    # El registro original debe seguir existiendo
    page.click_cancel()
    time.sleep(0.5)
    
    assert page.get_record_by_name("Producto a Editar") is not None, \
        "El registro original desapareció"
    
    take_screenshot("update_empty_05_validacion")
    print("✅ Validación de nombre vacío funciona correctamente")


@pytest.mark.crud
@pytest.mark.update
@pytest.mark.happy_path
def test_update_record_partial(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Actualizar solo algunos campos (Camino Feliz)
    
    Verifica que se puedan actualizar solo algunos campos manteniendo otros.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("update_partial_01_inicio")
    
    # Crear registro completo
    page.create_record("Producto Parcial", "Descripción inicial", "Trabajo", "2024-05-10")
    time.sleep(1)
    take_screenshot("update_partial_02_creado")
    
    # Act - Actualizar solo la descripción
    page.click_edit_button_by_name("Producto Parcial")
    time.sleep(0.5)
    
    page.enter_record_description("Descripción modificada")
    take_screenshot("update_partial_03_solo_descripcion_cambiada")
    
    page.click_save()
    time.sleep(1)
    take_screenshot("update_partial_04_guardado")
    
    # Assert
    record = page.get_record_by_name("Producto Parcial")
    assert record is not None, "El registro no existe"
    
    # El nombre debe seguir igual
    cells = record.find_elements("tag name", "td")
    assert cells[1].text == "Producto Parcial", "El nombre cambió incorrectamente"
    assert "modificada" in cells[2].text, "La descripción no se actualizó"
    
    take_screenshot("update_partial_05_validacion")
    print("✅ Actualización parcial exitosa")


@pytest.mark.crud
@pytest.mark.update
@pytest.mark.negative
def test_update_record_cancel(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Cancelar actualización (Prueba Negativa)
    
    Verifica que al cancelar la edición no se guarden cambios.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("update_cancel_01_inicio")
    
    page.create_record("Producto Sin Cambios", "Descripción original", "Estudio")
    time.sleep(1)
    take_screenshot("update_cancel_02_creado")
    
    # Act - Abrir edición y hacer cambios pero cancelar
    page.click_edit_button_by_name("Producto Sin Cambios")
    time.sleep(0.5)
    take_screenshot("update_cancel_03_modal_abierto")
    
    page.enter_record_name("Nombre que no debería guardarse")
    page.enter_record_description("Descripción que no debería guardarse")
    take_screenshot("update_cancel_04_cambios_realizados")
    
    page.click_cancel()
    time.sleep(0.5)
    take_screenshot("update_cancel_05_cancelado")
    
    # Assert
    assert not page.is_modal_visible(), "El modal no se cerró"
    
    # Verificar que el registro original sigue igual
    record = page.get_record_by_name("Producto Sin Cambios")
    assert record is not None, "El registro original debe existir"
    
    # El nombre nuevo no debe existir
    assert page.get_record_by_name("Nombre que no debería guardarse") is None, \
        "Los cambios se guardaron cuando deberían haberse cancelado"
    
    take_screenshot("update_cancel_06_validacion")
    print("✅ Cancelación funciona correctamente")
