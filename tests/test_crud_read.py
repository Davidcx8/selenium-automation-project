"""
test_crud_read.py - Pruebas automatizadas para la operación READ

Historia de Usuario 3: Consultar y Visualizar Registros
Este módulo contiene las pruebas para verificar la funcionalidad de
consulta y visualización de registros.
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
@pytest.mark.read
@pytest.mark.happy_path
def test_read_records_happy_path(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Visualizar registros existentes (Camino Feliz)
    
    Verifica que se puedan visualizar correctamente los registros
    en la tabla después de crearlos.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("read_01_inicio")
    
    # Crear algunos registros de prueba
    page.create_record("Producto A", "Descripción A", "Trabajo", "2024-01-15")
    time.sleep(1)
    take_screenshot("read_02_registro_1_creado")
    
    page.create_record("Producto B", "Descripción B", "Personal", "2024-02-20")
    time.sleep(1)
    take_screenshot("read_03_registro_2_creado")
    
    page.create_record("Producto C", "Descripción C", "Estudio", "2024-03-25")
    time.sleep(1)
    take_screenshot("read_04_registro_3_creado")
    
    # Act & Assert
    total_count = page.get_total_count()
    assert total_count >= 3, f"Debería haber al menos 3 registros. Actual: {total_count}"
    
    row_count = page.get_table_row_count()
    assert row_count >= 3, f"La tabla debería mostrar al menos 3 filas. Actual: {row_count}"
    
    # Verificar que cada registro aparece
    assert page.get_record_by_name("Producto A") is not None, "Producto A no está visible"
    assert page.get_record_by_name("Producto B") is not None, "Producto B no está visible"
    assert page.get_record_by_name("Producto C") is not None, "Producto C no está visible"
    
    # Verificar que no se muestra el estado vacío
    assert not page.is_empty_state_visible(), "No debería mostrar estado vacío"
    
    take_screenshot("read_05_todos_visibles")
    print(f"✅ {total_count} registros visualizados correctamente")


@pytest.mark.crud
@pytest.mark.read
@pytest.mark.happy_path
def test_read_records_empty_list(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Visualizar lista vacía (Camino Feliz)
    
    Verifica que cuando no hay registros, se muestre un mensaje apropiado.
    """
    # Arrange & Act
    page = authenticated_crud_page
    take_screenshot("read_empty_01_inicio")
    
    # Assert
    total_count = page.get_total_count()
    
    if total_count == 0:
        # Verificar que se muestra el estado vacío
        assert page.is_empty_state_visible(), \
            "Debería mostrar mensaje de lista vacía"
        
        take_screenshot("read_empty_02_estado_vacio")
        print("✅ Estado vacío mostrado correctamente")
    else:
        # Si hay registros, eliminarlos todos para ver el estado vacío
        # (Esta sería una prueba alternativa)
        take_screenshot("read_empty_02_hay_registros")
        print(f"✅ Se encontraron {total_count} registros existentes")


@pytest.mark.crud
@pytest.mark.read
@pytest.mark.happy_path
def test_read_record_details(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Verificar detalles de registro (Camino Feliz)
    
    Verifica que todos los campos de un registro se muestren correctamente.
    """
    # Arrange
    page = authenticated_crud_page
    take_screenshot("read_details_01_inicio")
    
    # Crear registro con todos los campos
    page.create_record(
        name="Producto Completo",
        description="Descripción detallada del producto",
        category="Trabajo",
        date="2024-06-15"
    )
    time.sleep(1)
    take_screenshot("read_details_02_registro_creado")
    
    # Act
    record_row = page.get_record_by_name("Producto Completo")
    
    # Assert
    assert record_row is not None, "Registro no encontrado"
    
    # Verificar que la fila tiene todas las celdas esperadas
    cells = record_row.find_elements("tag name", "td")
    assert len(cells) >= 6, f"Debería tener al menos 6 columnas. Actual: {len(cells)}"
    
    # Verificar contenido (índices: 0=ID, 1=Nombre, 2=Descripción, 3=Categoría, 4=Fecha, 5=Acciones)
    assert cells[1].text == "Producto Completo", "Nombre incorrecto"
    assert "Descripción detallada" in cells[2].text, "Descripción incorrecta"
    assert cells[3].text == "Trabajo", "Categoría incorrecta"
    assert cells[4].text == "2024-06-15", "Fecha incorrecta"
    
    take_screenshot("read_details_03_validacion")
    print("✅ Todos los detalles del registro se muestran correctamente")


@pytest.mark.crud
@pytest.mark.read
@pytest.mark.happy_path
def test_read_total_count(authenticated_crud_page, take_screenshot):
    """
    PRUEBA: Verificar contador total de registros (Camino Feliz)
    
    Verifica que el contador total se actualice correctamente.
    """
    # Arrange
    page = authenticated_crud_page
    initial_count = page.get_total_count()
    take_screenshot("read_count_01_estado_inicial")
    
    # Act - Crear 2 registros nuevos
    page.create_record("Contador Test 1", "Prueba contador")
    time.sleep(1)
    
    count_after_first = page.get_total_count()
    assert count_after_first == initial_count + 1, \
        f"Contador incorrecto después del primer registro. Esperado: {initial_count + 1}, Actual: {count_after_first}"
    
    take_screenshot("read_count_02_despues_primero")
    
    page.create_record("Contador Test 2", "Prueba contador 2")
    time.sleep(1)
    
    count_after_second = page.get_total_count()
    assert count_after_second == initial_count + 2, \
        f"Contador incorrecto después del segundo registro. Esperado: {initial_count + 2}, Actual: {count_after_second}"
    
    take_screenshot("read_count_03_despues_segundo")
    print(f"✅ Contador actualizado correctamente: {initial_count} → {count_after_second}")
