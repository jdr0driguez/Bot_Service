# download_csv.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pywinauto import Desktop
import time


def download_csv_selenium(driver):
    try:
        wait = WebDriverWait(driver, 20)

        # Ir al sitio directamente
        driver.get("https://app.servicebots.ai/analytics")
        time.sleep(6)


        # Cambiar al iframe adecuado (ajustá el índice si hay más de uno)
        wait = WebDriverWait(driver, 15)
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(iframe)

        driver.execute_script("document.querySelector('span[title=\"Reporte Unicos\"]').click();")

        time.sleep(5)

        driver.execute_script("document.getElementById('sheet_control_panel_header').click();")

        time.sleep(5)

        # Lista de valores a seleccionar Company
        valores_a_seleccionar = [
            "Banco Falabella",
            "ENTIDAD FALABELLA",
            "ENTIDAD Falabella",
            "Entidad FALABELLA",
            "FALABELLA",
            "Prueba Falabella"
        ]

        # Lista de valores a seleccionar Resultado Gestion
        valor_a_seleccionar = [
            "contestada efectiva"
        ]

        # Lista de valores a seleccionar Estado Objetivo
        valor_a_seleccionar1 = [
            "si"
        ]

        # 1. FILTRO COMPAÑIA
        dropdown_company = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-automation-id="sheet_control_value"][data-automation-context="Company"]')
        ))
        dropdown_company.click()
        time.sleep(0.5)

        # Buscar y desmarcar "Select all" si está seleccionado
        try:
            select_all_checkbox = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-automation-id="dropdown_select_all_search_result_entry"] input[type="checkbox"]')
            ))

            is_checked = driver.execute_script("return arguments[0].checked;", select_all_checkbox)
            if is_checked:
                driver.execute_script("arguments[0].click();", select_all_checkbox)
                time.sleep(0.5)
        except Exception as e:
            print(f"No se pudo desmarcar 'Select all': {e}")


        # Buscar "fala" en el input de búsqueda
        search_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'input[aria-label="Search value"]')
        ))
        search_input.clear()
        search_input.send_keys("fala")
        time.sleep(1)

        # Esperar opciones
        opciones = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-automation-id="param_value_as_entry"]')
        ))

        # Clic en cada opción deseada
        for valor in valores_a_seleccionar:
            try:
                # Re-obtener todas las opciones activas en el DOM actual
                opciones = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="param_value_as_entry"]')

                for opcion in opciones:
                    label = opcion.text.strip()
                    if label == valor:
                        checkbox = opcion.find_element(By.CSS_SELECTOR, '[data-automation-id="multi-select-control"] input[type="checkbox"]')
                        driver.execute_script("arguments[0].click();", checkbox)
                        time.sleep(0.2)
                        break  # ya lo encontramos, salimos del inner loop
            except Exception as e:
                print(f"Error seleccionando '{valor}': {e}")

        # Cerrar dropdown con ESC
        search_input.send_keys(Keys.ESCAPE)





        # 2. FILTRO RESULTADO GESTION
        dropdown_company = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-automation-id="sheet_control_value"][data-automation-context="Resultado Gestion"]')
        ))
        dropdown_company.click()
        time.sleep(0.5)

        # Buscar y desmarcar "Select all" si está seleccionado
        try:
            select_all_checkbox = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-automation-id="dropdown_select_all_search_result_entry"] input[type="checkbox"]')
            ))

            is_checked = driver.execute_script("return arguments[0].checked;", select_all_checkbox)
            if is_checked:
                driver.execute_script("arguments[0].click();", select_all_checkbox)
                time.sleep(0.5)
        except Exception as e:
            print(f"No se pudo desmarcar 'Select all': {e}")

        # Buscar "contestada efectiva" en el input de búsqueda
        search_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'input[aria-label="Search value"]')
        ))
        search_input.clear()
        search_input.send_keys("contestada efectiva")
        time.sleep(1)

        # Esperar opciones
        opciones = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-automation-id="param_value_as_entry"]')
        ))

        # Clic en cada opción deseada
        for valor in valor_a_seleccionar:
            try:
                # Re-obtener todas las opciones activas en el DOM actual
                opciones = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="param_value_as_entry"]')

                for opcion in opciones:
                    label = opcion.text.strip()
                    if label == valor:
                        checkbox = opcion.find_element(By.CSS_SELECTOR, '[data-automation-id="multi-select-control"] input[type="checkbox"]')
                        driver.execute_script("arguments[0].click();", checkbox)
                        time.sleep(0.2)
                        break  # ya lo encontramos, salimos del inner loop
            except Exception as e:
                print(f"Error seleccionando '{valor}': {e}")

        # Cerrar dropdown con ESC
        search_input.send_keys(Keys.ESCAPE)





        # 3. FILTRO ESTADO OBJETIVO
        dropdown_company = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-automation-id="sheet_control_value"][data-automation-context="Estado Objetivo"]')
        ))
        dropdown_company.click()
        time.sleep(0.5)

        # Buscar y desmarcar "Select all" si está seleccionado
        try:
            select_all_checkbox = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-automation-id="dropdown_select_all_search_result_entry"] input[type="checkbox"]')
            ))

            is_checked = driver.execute_script("return arguments[0].checked;", select_all_checkbox)
            if is_checked:
                driver.execute_script("arguments[0].click();", select_all_checkbox)
                time.sleep(0.5)
        except Exception as e:
            print(f"No se pudo desmarcar 'Select all': {e}")

        # Buscar "contestada efectiva" en el input de búsqueda
        search_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'input[aria-label="Search value"]')
        ))
        search_input.clear()
        search_input.send_keys("si")
        time.sleep(1)

        # Esperar opciones
        opciones = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-automation-id="param_value_as_entry"]')
        ))

        # Clic en cada opción deseada
        for valor in valor_a_seleccionar1:
            try:
                # Re-obtener todas las opciones activas en el DOM actual
                opciones = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="param_value_as_entry"]')

                for opcion in opciones:
                    label = opcion.text.strip()
                    if label == valor:
                        checkbox = opcion.find_element(By.CSS_SELECTOR, '[data-automation-id="multi-select-control"] input[type="checkbox"]')
                        driver.execute_script("arguments[0].click();", checkbox)
                        time.sleep(0.2)
                        break  # ya lo encontramos, salimos del inner loop
            except Exception as e:
                print(f"Error seleccionando '{valor}': {e}")


        # Cerrar dropdown con ESC
        search_input.send_keys(Keys.ESCAPE)



        # PROCESO DE DESCARGA

        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        # Encontrar el contenedor de la tabla
        tabla = wait.until(EC.presence_of_element_located(
            (By.ID, 'block-e0f7648e-bf39-4d90-8a1a-042933ba4471_ffe0b6d9-3fa0-46da-af01-b9b50ed55d9f')
        ))

        # Hover para que aparezca el menú
        actions.move_to_element(tabla).perform()
        time.sleep(1)

        # Buscar el botón del menú SOLO dentro de esa tabla
        boton_menu = tabla.find_element(
            By.CSS_SELECTOR, 'button[data-automation-id="analysis_visual_dropdown_menu_button"]'
        )
        driver.execute_script("arguments[0].click();", boton_menu)
        time.sleep(0.5)

        # Clic en la opción "Export to CSV"
        export_csv = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-automation-id="dashboard_visual_dropdown_export"]')
        ))
        driver.execute_script("arguments[0].click();", export_csv)

        

        # Ruta de destino donde se guardará el archivo
        ruta_archivo = r"C:\Users\Desarrollo\Documents\archivo_descargado.csv"

        # Esperar unos segundos para dar tiempo a que aparezca la ventana (ajustable)
        time.sleep(3)

        # Usar backend win32 (uia no detecta la ventana correctamente)
        desktop = Desktop(backend="win32")

        # Buscar la ventana de Guardar como / Save As
        ventanas = desktop.windows(class_name="#32770")
        ventana_guardar = None

        for v in ventanas:
            titulo = v.window_text().lower()
            if "guardar como" in titulo or "save as" in titulo:
                ventana_guardar = v
                break

        if ventana_guardar:
            print("✅ Ventana detectada:", ventana_guardar.window_text())
            ventana_guardar.set_focus()

            # Escribir la ruta en el campo Edit (buscar todos)
            try:
                edits = ventana_guardar.descendants(class_name="Edit")
                for idx, edit in enumerate(edits):
                    try:
                        edit.set_edit_text(ruta_archivo)
                        print(f"✍️ Ruta escrita en Edit #{idx+1}")
                        break
                    except Exception as e:
                        print(f"❌ No se pudo escribir en Edit #{idx+1}: {e}")
            except Exception as e:
                print("❌ No se encontraron campos Edit:", e)

            # Hacer clic en el botón Guardar / Save
            try:
                botones = ventana_guardar.descendants(class_name="Button")
                guardado = False
                for btn in botones:
                    if "guardar" in btn.window_text().lower() or "save" in btn.window_text().lower():
                        btn.double_click_input()
                        print("✅ Botón 'Guardar/Save' presionado")
                        guardado = True
                        break
                if not guardado:
                    print("❌ No se encontró botón Guardar/Save")
            except Exception as e:
                print("❌ No se pudo hacer clic en Guardar:", e)

            # Esperar posible ventana de confirmación de sobrescritura
            time.sleep(1)

            ventanas_conf = desktop.windows(class_name="#32770")
            for v in ventanas_conf:
                titulo = v.window_text().lower()
                if "confirmar" in titulo or "confirm save as" in titulo:
                    try:
                        v.set_focus()
                        botones_conf = v.descendants(class_name="Button")
                        for btn in botones_conf:
                            if "sí" in btn.window_text().lower() or "yes" in btn.window_text().lower():
                                btn.click()
                                print("🟢 Confirmación de sobrescritura aceptada")
                                break
                    except Exception as e:
                        print("❌ No se pudo confirmar sobrescritura:", e)

        else:
            print("❌ No se encontró la ventana 'Guardar como' / 'Save As'")

    except Exception as e:
        print(f"❌ Error durante la automatización: {e}")

