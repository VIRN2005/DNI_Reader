# DNI Reader

DNI Reader es una herramienta automatizada para consultar nombres completos asociados a DNIs (Documentos Nacionales de Identidad) a partir de un archivo Excel. Utiliza la biblioteca `pandas` para manejar los archivos Excel, `requests` para realizar las solicitudes HTTP, `BeautifulSoup` para analizar el HTML de las respuestas, y `tqdm` para mostrar una barra de progreso durante las consultas.

## Características

- **Carga de DNIs desde un archivo Excel**: Lee un archivo Excel que contiene una lista de DNIs.
- **Consulta automatizada**: Realiza consultas a un sitio web para obtener los nombres completos asociados a los DNIs.
- **Manejo de errores y reintentos**: Incluye manejo de errores y reintentos para asegurar la robustez del proceso de consulta.
- **Barra de progreso**: Muestra una barra de progreso durante las consultas para indicar el avance.
- **Guardado de resultados**: Guarda los resultados en un nuevo archivo Excel.

## Requisitos

- Python 3.x
- Bibliotecas de Python:
  - `pandas`
  - `requests`
  - `beautifulsoup4`
  - `tqdm`
  
Puedes instalar las bibliotecas necesarias utilizando `pip`:

```bash
pip install pandas requests beautifulsoup4 tqdm
```

## Uso
Preparar el archivo de entrada: Asegúrate de tener un archivo Excel ```(DNI_Entrada.xlsx)``` con una columna llamada DNI que contenga los DNIs a consultar.

Configurar el script: Asegúrate de que las rutas de los archivos de entrada y salida en el script ```(DNI_Reader.py)``` sean correctas.

Ejecutar el script: Ejecuta el script para iniciar el proceso de consulta.

```bash
python DNI_Reader.py
```

## Notas
Asegúrate de ajustar la URL y los selectores de HTML (nombre-clase) según la estructura real del sitio web de consulta.
El script incluye un tiempo de espera de 10 segundos entre cada solicitud para evitar bloqueos por parte del sitio web.

## Estructura del proyecto
```bash
DNI_Reader/
│
├── DNI_Reader.py          # Script principal para leer y consultar DNIs
├── DNI_Entrada.xlsx       # Archivo de entrada con los DNIs a consultar
└── DNI_Resultado.xlsx     # Archivo de salida con los resultados de las consultas
```

## Contribuciones
Las contribuciones son bienvenidas. Si tienes alguna mejora o corrección, por favor abre un issue o un pull request.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
