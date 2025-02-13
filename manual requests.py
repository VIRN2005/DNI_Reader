import requests
from bs4 import BeautifulSoup

url = 'https://censo.cne.hn:81/'
payload = {'dni': '0801200011311'}  # Reemplaza con un DNI válido

try:
    response = requests.post(url, data=payload)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    nombre_div = soup.find('div', {'id': 'nombre'})
    if nombre_div:
        print(nombre_div.text.strip())
    else:
        print("No se encontró el nombre")
except requests.RequestException as e:
    print(f"Error en la solicitud HTTP: {e}")
    print(f"Contenido de la respuesta: {response.text}")