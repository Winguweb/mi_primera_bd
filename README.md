# ONG-Management

Ejecutar `source bin/activate` para crear el entorno virtual

Ejecutar `pip install -r requirements.txt` para instalar los paquetes necesarios

Ejecutar `python manage.py makemigrations` para crear archivos de la BDD (asegurarse que PostgreSQL funcione, ver especificaciones en `miprimerabdd/miprimerabdd/settings.py` -> **DATABASES**)

Ejecutar `python manage.py createsuperuser` para crear un administrador

Ejecutar `python manage.py migrate` para ejecutar archivos en BDD

Ejecutar `python manage.py runserver` para correr en `localhost:8000`
