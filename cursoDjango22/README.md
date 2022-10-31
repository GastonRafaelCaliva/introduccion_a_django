# Finalizando la instalación con los siguientes pasos:
---
-> Creamos un entorno virtual y lo activamos: 
* `python -m venv djenv`
* `djenv\Scripts\activate`
---
-> Instalamos django:
* `pip install django`
---
-> Creamos nuestro proyecto:
* `django-admin startproject myProject .` (notar que es con "." al final)
---
-> Corriendo el servidor de desarrollo:
* `python manage.py runserver 127.0.0.1:8000`
---
-> En el navegador tipeamos y debería mostrarnos lo siguiente:
* `127.0.0.1:8000`
# ¡La instalación funcionó con éxito! ¡Felicidades!
![Upps no se pudo cargar la imagen django_instalacion_exitosa](https://raw.githubusercontent.com/GastonRafaelCaliva/images/main/Django/django_instalacion_exitosa.png)


# Finalizando la creación de una apliación con los siguientes pasos:
---
-> Activamos el entorno virtual: 
* `djenv\Scripts\activate`
---
-> Creamos una apliación: 
* `python manage.py startapp hello` (en este caso la llamaremos "hello")
---
-> Modificaremos algunos archivos para poder instalar la apliacion en nuestro Proyecto: 
* En la carpeta de nuestro proyecto "myProject" en ***settings.py*** agregamos "hello" a la entrada INSTALLED_APPS y en ALLOWED_HOSTS agregamos la IP de prueba "127.0.0.1"
```python
ALLOWED_HOSTS = ["127.0.0.1"]

INSTALLED_APPS = [
    #...
    #...
    "hello",
]
```
* Creamos una vista, para eso vamos a ***views.py*** e incluimos una función que renderice un archivo html (template):
```python
def hello(request):
  return render(request, "hello.html", {})
```
* Creamos un template, primero creamos una carpeta **templates** dentro de la aplicacion. Dentro de la misma creamos un archivo html "hello.html" con lo siguiente:
```html
<h1>Hola a todos! Vamos Django!</h1>
```
* Hacemos accesible la funcionalidad desarollada, para eso vamos a ***urls.py*** del proyecto y agregamos lo siguiente:
```python
urlpatterns = [
    #...
    path("", include("hello.urls")),
]
```
* Creamos un archivo ***urls.py*** dentro de la aplicacion y linkeamos funcionalidad con función en vista:
```python
from django.urls import path
from hello import views

urlpatterns = [
    path("", views.hello, name="hello"),
]

```
-> En el navegador tipeamos y debería mostrarnos lo siguiente:
* `127.0.0.1:8000`
![Upps no se pudo cargar la imagen hello_app_django](https://raw.githubusercontent.com/GastonRafaelCaliva/images/main/Django/hello_app_django.png)
