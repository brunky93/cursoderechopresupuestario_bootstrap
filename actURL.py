import os
import argparse
from bs4 import BeautifulSoup
from git import Repo  # Importa la biblioteca GitPython

# Directorio donde se encuentran los archivos HTML
# Directorio actual donde se encuentra el script
directorio_script = os.path.dirname(os.path.abspath(__file__))

def actualizar_enlace_en_html(html_file, url_nueva):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    enlaces = soup.find_all('a', href=lambda href: href and 'couponCode' in href)

    for enlace in enlaces:
        enlace['href'] = url_nueva

    with open(html_file, 'w') as f:
        f.write(str(soup))

def main():
    parser = argparse.ArgumentParser(description='Actualizar enlaces en archivos HTML con una URL nueva.')
    parser.add_argument('url_nueva', type=str, help='La nueva URL a utilizar para actualizar los enlaces.')

    args = parser.parse_args()
    url_nueva = args.url_nueva

    # Actualiza los enlaces en los archivos HTML
    for root, dirs, files in os.walk(directorio_script):
        for archivo in files:
            if archivo.endswith('.html'):
                archivo_html = os.path.join(root, archivo)
                actualizar_enlace_en_html(archivo_html, url_nueva)

    # Inicializa el repositorio Git
    repo = Repo.init(directorio_script)

    # Agrega todos los cambios al índice
    repo.git.add(all=True)

    # Realiza un commit con un mensaje
    commit_message = f"Actualización de enlaces con la URL: {url_nueva}"
    repo.index.commit(commit_message)

    # Realiza un push de los cambios a la rama Script-externo
    origin = repo.remote('origin')
    origin.push('main:Script-externo')

    print("Enlaces actualizados en todos los archivos HTML con la URL nueva proporcionada y los cambios se han sincronizado en la rama Script-externo.")

if __name__ == '__main__':
    main()
