from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_selenium(driver, email, password, base_url):
    driver.get(base_url)

    wait = WebDriverWait(driver, 15)

    try:
        # Esperar que cargue el campo de email
        wait.until(EC.presence_of_element_located((By.ID, "user_email")))

        # Ingresar credenciales
        driver.find_element(By.ID, "user_email").send_keys(email)
        driver.find_element(By.ID, "user_password").send_keys(password)

        # Hacer clic en el botón de login
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Esperar el menú de GEMELO_DIGITAL como confirmación
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'GEMELO_DIGITAL')]")))
        print("Login exitoso: menu GEMELO_DIGITAL detectado")

    except Exception as e:
        raise Exception(f"❌ Login fallido: {e}")
