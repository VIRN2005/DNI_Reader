import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

# Cargar el archivo Excel con los DNIs
archivo_entrada = r'C:\Users\Victo\OneDrive\Víctor\Papi\DNI_Reader\DNI_Entrada.xlsx'
archivo_salida = r'C:\Users\Victo\OneDrive\Víctor\Papi\DNI_Reader\DNI_Resultado.xlsx'

try:
    df = pd.read_excel(archivo_entrada, usecols=['DNI'], dtype={'DNI': str})
except Exception as e:
    print(f"[Error] No se pudo leer el archivo: {e}")
    exit()

# Configuración de headers para evitar bloqueos
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://censo.cne.hn:81/'
}

# Función para consultar el nombre por DNI
def consultar_nombre(dni):
    url = 'https://censo.cne.hn:81/'  # URL de la consulta
    payload = {'dni': dni}

    for intento in range(3):  # Intentar hasta 3 veces
        try:
            response = requests.post(url, data=payload, headers=headers, timeout=30)  # Aumentar el tiempo de espera
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Ajustar al elemento correcto del HTML
            nombre_div = soup.find('div', class_='nombre-clase')  # Ajustar según la estructura real
            if nombre_div:
                return nombre_div.text.strip()
            else:
                print(f"[Aviso] No se encontró el nombre para el DNI {dni}")
                return None
        except requests.RequestException as e:
            print(f"[Error] Intento {intento+1}/3 - Problema con DNI {dni}: {e}")
            print(f"Contenido de la respuesta: {response.text}")
            time.sleep(10)  # Esperar antes de reintentar
    return None

# Consultar nombres con barra de progreso
nombres_completos = []
for dni in tqdm(df['DNI'], desc="Consultando nombres"):
    nombre = consultar_nombre(dni)
    nombres_completos.append(nombre)
    time.sleep(10)  # Esperar 10 segundos entre cada solicitud

df['Nombre Completo'] = nombres_completos

# Guardar los resultados en un nuevo archivo Excel
try:
    df.to_excel(archivo_salida, index=False)
    print(f"Archivo guardado en: {archivo_salida}")
except Exception as e:
    print(f"[Error] No se pudo guardar el archivo: {e}")