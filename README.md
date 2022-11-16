# Instrucciones para ejecutar este proyecto en local

- Abrir Git Bash para `Windows` o una terminal para `Linux/Unix`.

- Crear directorio de trabajo para el proyecto de curso 
```bash
cd
mkdir -p Documents/coder_projects
cd Documents/coder_projects
ls 
```

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/profecoder/django-coderhouse-project.git

cd django-coderhouse-project

git checkout master
```

Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

- Para generar una SECRET_KEY:
```bash
python manage.py shell
```
```bash
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```

- Crear variables de entorno (GitBash/Linux terminal)
```bash
export SECRET_KEY='5jlof$oxhsgbhlamhh+6@f9@8nb#=85h92bih+_hfegr2t6a'
export DEBUG='True'
export ALLOWED_HOSTS='*,'
```

o crear el archivo `my_blog/.env` con el siguente contenido
```text
SECRET_KEY=5jlof$oxhsgbhlamhh+6@f9@8nb#=85h92bih+_hfegr2t6a
DEBUG=True
ALLOWED_HOSTS=*,
```

- Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

- Crear base de datos a partir de las migraciones
```bash
python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```
Ingrese `Username`, `Email address` y `Password` 


- Crear estáticos
```bash
python manage.py collectstatic
```

- Ejecutar proyecto, el servidor de Django expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```

# Instrucciones para desplegar en projecto en Heroku (utilizar GitBash)

Crear cuenta en [Heroku](https://signup.heroku.com/dc)

Instalar Heroku. [Windows](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

- Logearse (GitBash)
```bash
heroku login
```

## En la rama master del projecto ejecutar los siguiente comandos (GitBash):
- Crear el app `my-blog-coderhouse-live` en Heroku
```bash
heroku create my-blog-coderhouse-live
```

- Configurar la variables de entorno en Heroku, ejecutar linea a linea
```bash
heroku config:set DEBUG_COLLECTSTATIC=1
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set ALLOWED_HOSTS='.herokuapp.com',
heroku config:set DEBUG=1
heroku config:set SECRET_KEY='5jlof$oxhsgbhlamhh+6@f9@^8nb#=85h92bih+_hfegr2^t6a'
```

- Revisar las configurariones de Heroku que acabamos de ingresar
```bash
heroku config
```

- Desplegar el proyecto en Heroku
```bash
git push heroku master
```

- Configurar la base de datos del projecto Django en Heroku
```bash
heroku run bash
```

- En la bash de heroku ejecutar
```bash
python manage.py migrate
python manage.py createsuperuser
```
ir a https://my-blog-coderhouse-live.herokuapp.com/ para ver el projecto desplegado.

# Comandos útiles para Django

## Crear proyecto
```bash
django-admin startproject <nombre del proyecto>
cd <nombre del proyecto>
```
## Crear una aplicación en un proyecto
```bash
python manage.py startapp <nombre del app>
```
## Actualizar la base de datos del proyecto con cambios en nuestros modelos
Se realiza en dos pasos la creación de las migraciones, una por aplicación, y luego se realiza la creación de las tablas en la base de datos.
```bash
python manage.py makemigrations
python manage.py migrate
```
# Comandos básicos para Git

## Git clone
Git clone es un comando para descargarte el código fuente existente desde un repositorio remoto (como Github, por ejemplo). Descarga la última versión de tu proyecto en un repositorio y la guarda en tu ordenador
```bash
git clone <https://link-con-nombre-del-repositorio>
```

## Git branch
- Creando una nueva rama:
```bash
git branch <nombre-de-la-rama>

```
- Visualización de ramas:
```bash
git branch
git branch --list
```
- Borrar una rama:
```bash
git branch -d <nombre-de-la-rama>
```

## Git checkout
- Para cambiarte a una rama existente
```bash
git checkout <nombre-de-la-rama>
```
- Para crear y cambiarte a esa rama al mismo tiempo
```bash
git checkout -b <nombre-de-tu-rama>

```

## Git status
El comando de git status nos da toda la información necesaria sobre la rama actual:
- Si la rama actual está actualizada
- Si hay algo para confirmar, enviar o recibir (pull).
- Si hay archivos en preparación (staged), sin preparación(unstaged) o que no están recibiendo seguimiento (untracked)
- Si hay archivos creados, modificados o eliminadosstatus
```bash
git status
```

## Git add
- Añadir un único archivo:
```bash
git add <archivo>
```

- Añadir todo de una vez:
```bash
git add -A
git add .
```
***Importante: El comando ``git add`` almacena en el ``stage`` los cambios de los archivos sin embargo aún no quedan registrados en el repositorio hasta que se utilice el comando de confirmación ``git commit`` para registrar un punto de control de los cambios.***

## Git commit
Git commit establece un punto de control al cual puedes volver más tarde si es necesario.
Resulta muy aconsejable escribir un mensaje corto para explicar qué hemos desarrollado o modificado en el código fuente.

```bash
git commit -m "mensaje de confirmación"
```

## Git push
Después de haber confirmado tus cambios, el siguiente paso que quieres dar es enviar tus cambios al servidor remoto. Git push envía tus commits al repositorio remoto.
```bash
git push <nombre-remoto> <nombre-de-tu-rama>
git push origin <nombre-de-tu-rama>
```
***Importante: Git push solamente carga los cambios que han sido confirmados con un ``git commit``.***

## Git pull
El comando git pull se utiliza para recibir actualizaciones del repositorio remoto.
```bash
git pull <nombre-remoto> <nombre-de-tu-rama>
git pull origin master
```
## Git remote
Sirve para cambiar la dirección url del repositorio que tenemos por origin.
```bash
git remote set-url origin <url_de_tu_repositorio_en_GitHub>
git remote set-url origin https://github.com/coder-live-class/django-coderhouse-project.git
```
