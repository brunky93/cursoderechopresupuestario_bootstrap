import subprocess
# Llamada al comando pip para instalar la librería beautifulsoup4
subprocess.check_call(['pip', 'install', 'beautifulsoup4'])
# Llamada al comando pip para instalar la librería pyperclip
subprocess.check_call(['pip', 'install', 'pyperclip'])

import os
from bs4 import BeautifulSoup
import pyperclip

# Directorio donde se encuentran los archivos HTML
# Directorio actual donde se encuentra el script
directorio_script = os.path.dirname(os.path.abspath(__file__))

# Solicitar la URL nueva desde el portapapeles
url_nueva = pyperclip.paste()

# Función para actualizar los enlaces en un archivo HTML
def actualizar_enlace_en_html(html_file, url_nueva):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Encuentra todos los enlaces que necesitas actualizar
    enlaces = soup.find_all('a', href=lambda href: href and 'couponCode' in href)

    for enlace in enlaces:
        enlace['href'] = url_nueva

    with open(html_file, 'w') as f:
        f.write(str(soup))

# Recorre los archivos HTML en el directorio y actualiza los enlaces
for root, dirs, files in os.walk(directorio_script):
    for archivo in files:
        if archivo.endswith('.html'):
            archivo_html = os.path.join(root, archivo)
            actualizar_enlace_en_html(archivo_html, url_nueva)

print("Enlaces actualizados en todos los archivos HTML con la URL nueva del portapapeles.")