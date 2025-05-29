# sendAPI.py


import requests
import os
from download_csv import ruta_documentos
from datetime import datetime
from config import USERNAME, PASSWORDWISER, UNIT_ID, BASE_URLWISER, CSV_FILENAME, CSV_HEADERS_JSON
import logging


AUTH_URL = f"{BASE_URLWISER}/api/auth/security/signin"
UPLOAD_URL = f"{BASE_URLWISER}/cargues-propia/cargues/compromisos-genericos"

# Nombre del archivo
nombre_archivo = CSV_FILENAME

# Ruta de destino donde se guardará el archivo
ruta_archivo = os.path.join(ruta_documentos, nombre_archivo)

def obtener_token():
    auth_payload = {
        "username": USERNAME,
        "password": PASSWORDWISER,
        "unitId": UNIT_ID
    }

    try:
        response = requests.post(AUTH_URL, json=auth_payload, verify=False)
        response.raise_for_status()
        token = response.json().get("token")
        token = response.json().get("token")
        if not token:
            print("❌ No se encontró el token en la respuesta.")
            return None
        print("✅ Token obtenido correctamente.")
        return token
    except Exception as e:
        print(f"❌ Error durante autenticación: {e}")
        return None


# Configura el logger (haz esto una sola vez en tu módulo)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('upload.log', encoding='utf-8')
handler.setFormatter(logging.Formatter(
    '%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))
logger.addHandler(handler)

def enviar_csv(token):
    """
    Envía un CSV vía POST y hace logging de todo el proceso:
    - upload.log: información general y trazas de error
    - upload_success.txt: respuestas exitosas
    - upload_errors.txt: detalles de los errores
    """
    # Aviso de inicio
    logger.info(f"Iniciando subida del archivo: {ruta_archivo}")
    print("🔄 Subiendo archivo...")

    headers = {"Authorization": f"Bearer {token}"}
    form_data = {
        "unidad_id": UNIT_ID,
        "headers": CSV_HEADERS_JSON,
        "delimitador": ","
    }

    try:
        with open(ruta_archivo, "rb") as f:
            print("URL direccionada: " + UPLOAD_URL)
            files = {"datos": f}
            response = requests.post(
                UPLOAD_URL,
                headers=headers,
                data=form_data,
                files=files,
                verify=False,
            )
            response.raise_for_status()

        # Éxito
        success_msg = "✅ Archivo enviado exitosamente."
        print(success_msg)
        print("📄 Respuesta del servidor:")
        print(response.text)

        logger.info(success_msg)
        logger.info(f"Respuesta del servidor: {response.text}")

        with open('upload_success.txt', 'a', encoding='utf-8') as out:
            out.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} SUCCESS:\n")
            out.write(response.text + "\n\n")

    except FileNotFoundError:
        err_msg = f"❌ El archivo '{ruta_archivo}' no fue encontrado."
        print(err_msg)
        logger.error(err_msg)

        with open('upload_errors.txt', 'a', encoding='utf-8') as errf:
            errf.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} ERROR: archivo no encontrado: {ruta_archivo}\n\n")

    except Exception as e:
        err_msg = f"❌ Error al enviar archivo: {e}"
        print(err_msg)
        logger.error(err_msg, exc_info=True)

        with open('upload_errors.txt', 'a', encoding='utf-8') as errf:
            errf.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} ERROR al enviar archivo:\n{e}\n\n")
def enviar_archivo_api():
    print("\n🔐 Autenticando y enviando archivo por API...")
    token = obtener_token()
    if token:
        enviar_csv(token)
