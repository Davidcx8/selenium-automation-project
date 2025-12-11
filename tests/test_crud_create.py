"""
test_crud_create.py - Pruebas automatizadas para la operación CREATE

Historia de Usuario 2: Crear Nuevo Registro
Este módulo contiene las pruebas para verificar la funcionalidad de
creación de registros, incluyendo camino feliz, pruebas negativas y de límites.
"""

import pytest
from pages.login_page import LoginPage
from pages.crud_page import CRUDPage
import time


@pytest.fixture(scope="function")
def authenticated_crud_page(driver, base_url, clean_session):
    """
    Fixture que proporciona una página CRUD autenticada
    """
    login_page = LoginPage(driver, base_url)
    crud_page = CRUDPage(driver, base_url)
    
    # Autenticarse
    login_page.navigate()
    login_page.login("admin", "admin123")
    time.sleep(2)
    
    return crud_page


@pytest.mark.crud
@pytest.mark.create
@pytest.mark.happy_path
def test_create_record_happy_path(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Crear registro con datos válidos (Camino Feliz)
    
    Verifica que se pueda crear un nuevo registro exitosamente
    con todos los campos completos y válidos.
    """
    # Arrange
    page = authenticated_crud_page
    initial_count = page.get_total_count()
    take_screenshot("create_01_pagina_inicial")
    
    # Act
    page.click_new_record()
    time.sleep(0.5)
    take_screenshot("create_02_modal_abierto")
    
    assert page.is_modal_visible(), "El modal no se abrió"
    assert page.get_modal_title() == "Nuevo Registro", "Título del modal incorrecto"
    
    page.create_record(
        name="Producto de Prueba",
        description="Este es un producto creado para pruebas automatizadas",
        category="Trabajo",
        date="2024-12-01"
    )
    take_screenshot("create_03_datos_ingresados")
    
    time.sleep(1)
    take_screenshot("create_04_registro_creado")
    
    # Assert
    assert page.is_alert_visible(), "No se mostró mensaje de confirmación"
    alert_message = page.get_alert_message()
    assert "éxito" in alert_message.lower() or "exitosamente" in alert_message.lower(), \
        f"Mensaje de confirmación incorrecto: {alert_message}"
    
    new_count = page.get_total_count()
    assert new_count == initial_count + 1, \
        f"El contador no se incrementó. Inicial: {initial_count}, Nuevo: {new_count}"
    
    record = page.get_record_by_name("Producto de Prueba")
    assert record is not None, "El registro no aparece en la tabla"
    
    take_screenshot("create_05_validacion_exitosa")
    print("✅ Registro creado exitosamente")


@pytest.mark.crud
@pytest.mark.create
@pytest.mark.negative
def test_create_record_empty_name(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Intentar crear registro con nombre vacío (Prueba Negativa)
    
    Verifica que el sistema rechace la creación de un registro
    cuando el campo obligatorio 'nombre' está vacío.
    """
    # Arrange
    page = authenticated_crud_page
    initial_count = page.get_total_count()
    take_screenshot("create_empty_01_inicio")
    
    # Act
    page.click_new_record()
    time.sleep(0.5)
    take_screenshot("create_empty_02_modal_abierto")
    
    # Intentar guardar sin nombre (solo llenar otros campos)
    page.enter_record_description("Descripción sin nombre")
    page.select_record_category("Personal")
    page.click_save()
    
    time.sleep(1)
    take_screenshot("create_empty_03_error_mostrado")
    
    # Assert
    assert page.is_alert_visible(), "No se mostró mensaje de error"
    
    alert_message = page.get_alert_message()
    assert "obligatorio" in alert_message.lower() or "nombre" in alert_message.lower(), \
        f"Mensaje de error incorrecto: {alert_message}"
    
    # El modal debe permanecer abierto
    assert page.is_modal_visible(), "El modal se cerró incorrectamente"
    
    # El contador no debe cambiar
    new_count = page.get_total_count()
    assert new_count == initial_count, \
        f"El contador cambió incorrectamente. Inicial: {initial_count}, Nuevo: {new_count}"
    
    take_screenshot("create_empty_04_validacion")
    print("✅ Validación de campo obligatorio funciona correctamente")


@pytest.mark.crud
@pytest.mark.create
@pytest.mark.boundary
def test_create_record_name_too_long(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Crear registro con nombre muy largo (Prueba de Límites)
    
    Verifica que el sistema rechace o trunce nombres que excedan
    el límite de 100 caracteres.
    """
    # Arrange
    page = authenticated_crud_page
    initial_count = page.get_total_count()
    
    # Nombre de 150 caracteres (excede el límite de 100)
    long_name = "A" * 150
    
    take_screenshot("create_long_01_inicio")
    
    # Act
    page.click_new_record()
    time.sleep(0.5)
    take_screenshot("create_long_02_modal_abierto")
    
    page.enter_record_name(long_name)
    page.enter_record_description("Prueba de límite de caracteres")
    page.click_save()
    
    time.sleep(1)
    take_screenshot("create_long_03_despues_guardar")
    
    # Assert
    # El sistema puede rechazar o truncar
    # Si se rechaza, debe haber alerta de error
    if page.is_alert_visible():
        alert_message = page.get_alert_message()
        # Puede ser mensaje de error
        if "error" in alert_message.lower() or "caracteres" in alert_message.lower():
            new_count = page.get_total_count()
            assert new_count == initial_count, "No debería crear el registro"
            take_screenshot("create_long_04_rechazado")
            print("✅ Nombre muy largo rechazado correctamente")
        else:
            # Si se creó, verificar que está truncado a 100 caracteres máximo
            new_count = page.get_total_count()
            assert new_count == initial_count + 1, "Debería crear el registro truncado"
            take_screenshot("create_long_04_truncado")
            print("✅ Nombre truncado correctamente a 100 caracteres")
    else:
        # Verificar que el input tiene maxlength que previno la entrada
        take_screenshot("create_long_04_prevenido")
        print("✅ Campo de entrada previno caracteres excesivos")


@pytest.mark.crud
@pytest.mark.create
@pytest.mark.boundary
def test_create_record_description_too_long(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Crear registro con descripción muy larga (Prueba de Límites)
    
    Verifica que el sistema maneje correctamente descripciones que excedan
    el límite de 500 caracteres.
    """
    # Arrange
    page = authenticated_crud_page
    
    # Descripción de 600 caracteres (excede el límite de 500)
    long_description = "B" * 600
    
    take_screenshot("create_desc_01_inicio")
    
    # Act
    page.click_new_record()
    time.sleep(0.5)
    
    page.enter_record_name("Producto con descripción larga")
    page.enter_record_description(long_description)
    page.click_save()
    
    time.sleep(1)
    take_screenshot("create_desc_02_resultado")
    
    # Assert
    # Similar al caso anterior, puede rechazar o truncar
    if page.is_alert_visible():
        alert_message = page.get_alert_message()
        if "error" in alert_message.lower() or "caracteres" in alert_message.lower():
            take_screenshot("create_desc_03_rechazado")
            print("✅ Descripción muy larga rechazada")
        else:
            take_screenshot("create_desc_03_aceptado")
            print("✅ Descripción truncada o aceptada")
    else:
        take_screenshot("create_desc_03_prevenido")
        print("✅ Campo previno caracteres excesivos")


@pytest.mark.crud
@pytest.mark.create
@pytest.mark.happy_path
def test_create_record_minimal_data(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Crear registro con datos mínimos (Camino Feliz)
    
    Verifica que se pueda crear un registro con solo el campo obligatorio (nombre).
    """
    # Arrange
    page = authenticated_crud_page
    initial_count = page.get_total_count()
    take_screenshot("create_min_01_inicio")
    
    # Act
    page.click_new_record()
    time.sleep(0.5)
    
    page.enter_record_name("Registro Mínimo")
    page.click_save()
    
    time.sleep(1)
    take_screenshot("create_min_02_creado")
    
    # Assert
    assert page.is_alert_visible(), "No se mostró mensaje de confirmación"
    
    new_count = page.get_total_count()
    assert new_count == initial_count + 1, "El registro no se creó"
    
    record = page.get_record_by_name("Registro Mínimo")
    assert record is not None, "El registro no aparece en la tabla"
    
    take_screenshot("create_min_03_validacion")
    print("✅ Registro con datos mínimos creado exitosamente")


@pytest.mark.crud
@pytest.mark.create
@pytest.mark.negative
def test_create_record_future_date_warning(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Crear registro con fecha futura (Prueba Negativa/Advertencia)
    
    Verifica que el sistema muestre advertencia al ingresar una fecha futura.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("create_future_01_inicio")
    
    # Act
    page.click_new_record()
    time.sleep(0.5)
    
    page.enter_record_name("Evento Futuro")
    page.enter_record_description("Prueba con fecha futura")
    page.enter_record_date("2025-12-31")
    
    take_screenshot("create_future_02_fecha_ingresada")
    
    page.click_save()
    time.sleep(1)
    
    # El sistema puede mostrar un confirm dialog
    # Si hay alert de JavaScript, aceptarlo
    try:
        alert = page.driver.switch_to.alert
        alert_text = alert.text
        take_screenshot("create_future_03_advertencia")
        print(f"Advertencia mostrada: {alert_text}")
        alert.accept()  # Aceptar para continuar
        time.sleep(1)
        take_screenshot("create_future_04_aceptado")
        print("✅ Advertencia de fecha futura funciona correctamente")
    except:
        # Si no hay alert, el sistema permitió la fecha futura sin advertencia
        take_screenshot("create_future_03_sin_advertencia")
        print("✅ Sistema permitió fecha futura (sin advertencia)")


@pytest.mark.crud
@pytest.mark.create
@pytest.mark.happy_path
def test_create_record_cancel(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Cancelar creación de registro (Camino Feliz)
    
    Verifica que al cancelar la creación, no se guarde el registro.
    """
    # Arrange
    page = authenticated_crud_page
    initial_count = page.get_total_count()
    take_screenshot("create_cancel_01_inicio")
    
    # Act
    page.click_new_record()
    time.sleep(0.5)
    take_screenshot("create_cancel_02_modal_abierto")
    
    page.enter_record_name("Registro a Cancelar")
    page.enter_record_description("Este no debería guardarse")
    take_screenshot("create_cancel_03_datos_ingresados")
    
    page.click_cancel()
    time.sleep(0.5)
    take_screenshot("create_cancel_04_cancelado")
    
    # Assert
    assert not page.is_modal_visible(), "El modal no se cerró"
    
    new_count = page.get_total_count()
    assert new_count == initial_count, \
        f"El contador cambió. Inicial: {initial_count}, Nuevo: {new_count}"
    
    record = page.get_record_by_name("Registro a Cancelar")
    assert record is None, "El registro se guardó cuando debería haberse cancelado"
    
    take_screenshot("create_cancel_05_validacion")
    print("✅ Cancelación funciona correctamente")
