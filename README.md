# Biblioteca

Este proyecto es una aplicación web desarrollada en Django para la gestión de una biblioteca, permitiendo administrar autores, libros y reseñas a través de un panel administrativo personalizado.

---

## Requisitos previos

- Python 3.8+  
- pip  
- Virtualenv (recomendado)  
- Git  

---

## Instalación y puesta en marcha

1. **Clona o haz fork** de este repositorio en tu cuenta de GitHub:  
   ```bash
   git clone https://github.com/ClaudyPedroza/ejercicio-django-biblioteca.git
   cd biblioteca
   ```

2. **Crea un entorno virtual** (opcional pero recomendado):  
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```
3. **Instala las dependencias**:  
   ```bash
   pip install -r requirements.txt
   ```
4. **Realiza las migraciones**:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Crea un superusuario (para acceder al admin)** para iniciar sesión.  
   python manage.py createsuperuser

6. **Cargar datos iniciales (script de poblacion)**:  
   ```bash
   python manage.py shell
   exec(open('poblar_datos.py', encoding='utf-8').read())
   exit()
   ```

7. **Ejecutar el servidor**:  
   ```bash
   python manage.py runserver
   Accede a http://127.0.0.1:8000/admin/ e inicia sesión con las credenciales creadas
   ```