## README para tu proyecto Flask

**¡Bienvenido a tu proyecto Flask!**

Este archivo README te guiará a través de los pasos para crear, ejecutar y desarrollar tu aplicación Flask.

**Requisitos previos:**

- Tener Python instalado en tu sistema.
- Familiaridad básica con Python y la línea de comandos.

**Pasos:**

### 1. Creación de un directorio de proyecto:

Crea un directorio para almacenar los archivos de tu proyecto Flask. Por ejemplo, puedes llamarlo `mi-proyecto-flask`.

### 2. Creación de un entorno virtual:

Es recomendable utilizar un entorno virtual para aislar las dependencias de tu proyecto del entorno global de Python. Crea un entorno virtual utilizando la herramienta adecuada para tu sistema operativo. Por ejemplo, si usas `virtualenv` en macOS o Linux:

```bash
python3 -m venv entorno-venv
```

Activa el entorno virtual:

```bash
source entorno-venv/bin/activate
```

### 3. Instalación de Flask:

Instala el paquete Flask utilizando pip:

```bash
pip install flask
```

### 4. Creación de la aplicación Flask:

Crea un archivo llamado `app.py` dentro del directorio de tu proyecto. Este será el archivo principal de Python para tu aplicación Flask.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

if __name__ == '__main__':
    app.run(debug=True)
```

Este código crea una aplicación Flask básica con una ruta simple (`/`) que devuelve el texto "¡Hola, Mundo!".

### 5. Ejecución de la aplicación Flask:

Ejecuta la aplicación Flask desde el directorio del proyecto utilizando el comando:

```bash
flask run
```

Esto iniciará el servidor de desarrollo de Flask, que escuchará solicitudes en `http://localhost:5000/` por defecto. Abre un navegador web y navega a `http://localhost:5000/` para ver el mensaje "¡Hola, Mundo!".

### 6. Desarrollo de tu aplicación Flask:

Ahora puedes continuar desarrollando tu aplicación Flask agregando más rutas, creando plantillas, utilizando bases de datos e implementando otras funcionalidades. Consulta la documentación de Flask para obtener instrucciones detalladas: [https://palletsprojects.com/p/flask/](https://palletsprojects.com/p/flask/)

**Recuerda:**

- Activa tu entorno virtual (`source entorno-venv/bin/activate`) antes de ejecutar cualquier comando Flask.
- Este es un ejemplo básico de creación de una aplicación Flask. Puedes ampliar la funcionalidad según tus necesidades.
- Para obtener más información y ejemplos, consulta la documentación oficial de Flask y la comunidad de usuarios.

**Licencia:**

Este README se proporciona bajo la licencia MIT. Puedes usarlo y modificarlo libremente para tus proyectos.

**¡Que disfrutes creando tu aplicación Flask!**
