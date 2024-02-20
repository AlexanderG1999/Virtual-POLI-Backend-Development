# Desarrollo Backend de Virtual-POLI, plataforma web diseñada para complementar la educación académica, generado por estudiantes para estudiantes.

## Descripción
Desarrollar el backend para una plataforma web orientada a la educación virtual caso de aplicación “Virtual-POLI”.

## Instalación
Para el proyecto se utilizó las siguientes tecnologías y sus respectivas versiones.

- Python 3.10.6
- Django 4.1.13
- MongoDB 7.0.3

Luego, para configurar de manera correcta el presente proyecto se siguen los siguientes pasos:

1) Clonar repositorio.
  ```bash
  git clone https://github.com/AlexanderG1999/Virtual-POLI-Backend-Development.git
  ```

2) Instalar Poetry para la gestión de dependencias.
  ```bash
  pip install poetry
  ```

3) Iniciar entorno virtual de Poetry, donde se encuentren los archivos `poetry.lock` y `pyproject.toml`.
  ```bash
  poetry shell
  ```

4) Instalar dependencias
  ```bash
  poetry install
  ```
`Nota:` En el caso de existir un error con Poetry, se puede crear un entorno virtual e instalar las dependencias del proyecto mediante el archivo `requirements.txt`.

  ```bash
  # Crear entorno virtual
  python -m venv env-backend

  # Iniciar entorno virtual
  env-backend/Scripts/activate

  # Instalar dependencias del proyecto
  pip install -r requirements.txt
  ```

5) Las variables definidas dentro del archivo `.env` son las siguientes:
```bash
# Variables de configuración para proyecto en DJANGO
DJANGO_SECRET_KEY=''
DEBUG=
DATABASE_NAME=''

# Variable secreta de creación de JWT
SECRET_KEY_TOKEN=''

# URL Frontend
URL_FRONTEND=''

# URLs para almacenamiento en Bucket S3
URL_IMAGE_COURSE_STORAGE = ''
URL_VIDEO_COURSE_STORAGE = ''
URL_VIDEO_COURSE_CONTENT_STORAGE = ''
URL_IMAGE_INSTRUCTOR_STORAGE = ''

# Variables para uso de SMTP de Gmail
EMAIL_HOST=''
EMAIL_PORT=''
EMAIL_USE_TLS=''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Variables de configuración para el almacenamiento en Bucket S3
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
AWS_STORAGE_BUCKET_NAME = ''
```

6) Realizar migraciones a MongoDB.
```bash
python manage.py migrate
```

7) Ejecutar proyecto.
```bash
python manage.py runserver
```

## Puntos de acceso

## Usuarios

- `http://127.0.0.1:8000/users/`
  - Métodos: `GET`, `PUT`, `DELETE`
  - Descripción: Obtener, actualizar o eliminar información del usuario.
  - Es necesario enviar el `Token de Autenticación` para cada una de estas peticiones.

  ```bash
  # Método GET
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Retorna los cursos a los cuales el usuario esta inscrito.
  Status: 401 -> Acceso no autorizado, verificar token de sesión
  ```

  ```bash
  # Método PUT - Inscribir en un curso
  # Entrada
  {
  "enrolled_courses": [
    {
      "name": "",
      "state": "enrolled"
    }
  ]
  }
  # Salida
  Status: 200 -> Retorna los cursos a los cuales el usuario esta inscrito.
  Status: 401 -> Acceso no autorizado, verificar token de sesión
  ```

  ```bash
  # Método PUT - Actualizar el resto de información del usuario
  # Entrada
  {
  "name": "",
  "lastname": "",
  "role": "",
  "semester": "",
  "approve_teacher": "",
  "approve_teacher_email": "",
  "user_description": "",
  "profile_image_url": ""
  }
  # Salida
  Status: 200 -> Usuario actualizado
  Status: 400 -> Error al actualizar usuario, revisar información enviada dentro de cada campo
  Status: 401 -> Acceso no autorizado, verificar token de sesión.
  ```

  ```bash
  # Método DELETE
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Usuario eliminado
  Status: 400 -> Usuario no encontrado
  ```

- `http://127.0.0.1:8000/users/last-watched-course/`
  - Método: `POST`
  - Descripción: Agregar el último módulo y tema visto del curso.
  - Es necesario enviar el `Token de Autenticación`.

```bash
  # Entrada
{
  "name": "", # Nombre del último curso visto
  "state": "", # enrolled, in-progress, completed
  "last_module_name": "", # Nombre del último módulo del curso visto
  "last_subtopic_name": "" # Nombre del último tema del módulo visto.
}

  # Salida
  Status: 200 -> Último curso visto agregado.
  Status: 401 -> Acceso no autorizado.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/last-watched-course/<str:course_name>/`
  - Método: `GET`
  - Descripción: Obtener el último curso visto.
  - Es necesario enviar el `Token de Autenticación`.

```bash
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Retorna el último curso visto.
  Status: 401 -> Acceso no autorizado.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/is-enrolled-in-course/<str: course_name>/`
  - Método: `GET`
  - Descripción: Verificar si un usuario esta inscrito en un curso.
  - Es necesario enviar el `Token de Autenticación`.

```bash
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> True, usuario inscrito en el curso
  Status: 200 -> False, usuario no inscrito en el curso
  ```

- `http://127.0.0.1:8000/users/sign-up/`
  - Método: `POST`
  - Descripción: Permite el registro de usuarios.

```bash
  # Entrada
{
  "email": "",
  "name": "",
  "lastname": "",
  "password": "",
  "role": "",
  "semester": "",
  "enrolled_courses": [
  ]
}

  # Salida
  Status: 200 -> Usuario registrado.
  Status: 400 -> Correo electrónico inválido.
  Status: 400 -> Error al guardar el usuario.
  Status: 409 -> Usuario ya registrado en BD.
  ```

- `http://127.0.0.1:8000/users/sign-in/`
  - Método: `POST`
  - Descripción: Iniciar sesión.

```bash
  # Entrada
{
  "email": "",
  "password": ""
}

  # Salida
  Status: 200 -> Inicio de sesión correcto y retorna token de sesión.
  Status: 400 -> Correo electrónico inválido.
  Status: 400 -> Correo electrónico y contraseña no ingresados.
  Status: 401 -> Contraseña incorrecta.
  Status: 403 -> Correo electrónico no verificado.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/sign-out/`
  - Método: `PUT`
  - Descripción: Cerrar la sesión actual del usuario.
  - Se debe enviar el `Token de Autenticación`.

```bash
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Sesión cerrada.
  Status: 400 -> Error al cerrar sesión.
  Status: 401 -> Acceso no autorizado
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/change-password/`
  - Método: `PUT`
  - Descripción: Cambiar contraseña.
  - Se debe enviar el `Token de Autenticación`.

```bash
  # Entrada
{
  "password": ""
}

  # Salida
  Status: 200 -> Contraseña actualizada.
  Status: 400 -> Error al actualizar la contraseña.
  Status: 401 -> Acceso no autorizado
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/send-email-to-restore-password/`
  - Método: `PUT`
  - Descripción: Enviar correo para restaurar contraseña.

```bash
  # Entrada
{
  "email": ""
}

  # Salida
  Status: 200 -> Correo electrónico enviado.
  Status: 400 -> Correo electrónico inválido.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/restore-password/`
  - Método: `PUT`
  - Descripción: Restaurar contraseña.

```bash
  # Entrada
{
  "email": "",
  "password": ""
}

  # Salida
  Status: 200 -> Contraseña actualizada.
  Status: 400 -> Correo electrónico inválido.
  Status: 400 -> Error al actualizar la contraseña.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/set-email-verification/`
  - Método: `POST`
  - Descripción: Establecer la verificación del correo electrónico del usuario.

```bash
  # Entrada
{
  "email": ""
}

  # Salida
  Status: 200 -> Correo electrónico verificado.
  Status: 400 -> Correo electrónico inválido.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/contact-with-us/`
  - Método: `POST`
  - Descripción: Enviar mensaje para contacto con equipo de Virtual-POLI

```bash
  # Entrada
{
  "name": "",
  "email": "",
  "message": ""
}

  # Salida
  Status: 200 -> Correo electrónico enviado.
  Status: 400 -> Correo electrónico inválido.
  ```

- `http://127.0.0.1:8000/users/send-email-to-approve-teacher/`
  - Método: `PUT`
  - Descripción: Enviar correo para aprobación de ser un instructor.
  - Se debe enviar el `Token de Autenticación`.

```bash
  # Entrada
{
  "approve_teacher": "",
  "approve_teacher_email": ""
}

  # Salida
  Status: 200 -> Correo electrónico enviado.
  Status: 400 -> Correo electrónico inválido.
  Status: 401 -> Acceso no autorizado.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/be-an-instructor/`
  - Método: `PUT`
  - Descripción: Actualizar el rol del estudiante.

```bash
  # Entrada
{
  "email": ""
}

  # Salida
  Status: 200 -> Rol del estudiante actualizado.
  Status: 400 -> Correo electrónico inválido.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/profile/`
  - Método: `GET`
  - Descripción: Obtener la información del usuario.
  - Se debe enviar el `Token de Autenticación`.

```bash
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Retorna información del usuario.
  Status: 401 -> Acceso no autorizado.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/instructor-profile/<str: name_lastname>/`
  - Método: `GET`
  - Descripción: Obtener la información de un instructor en función de su nombre y apellido (Nombres-Apellidos)

```bash
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Retorna información del instructor.
  Status: 404 -> Usuario no encontrado.
  ```

- `http://127.0.0.1:8000/users/featured-teachers/`
  - Método: `GET`
  - Descripción: Obtener los instructores destacados.

```bash
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Retorna la información de los instructores destacados.
  Status: 404 -> No hay instructores destacados.
  Status: 404 -> No hay instructores disponibles.
  ```

- `http://127.0.0.1:8000/users/instructors-by-key-word/<str:key_word>/`
  - Método: `GET`
  - Descripción: Obtener los instructores si la palabra clave esta en el nombre o apellido.

```bash
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Retorna la información del o los instructores.
  Status: 404 -> No hay instructores disponibles.
  ```

## Cursos

- `http://127.0.0.1:8000/courses/`
  - Método: `POST`
  - Descripción: Crear un curso.

  ```bash
  # Método POST
  # Entrada
  
  "name": "",
  "description": "",
  "category": "",
  "instructor": "",
  "modules": [
    {
      "title": "",
      "description": "",
    }
  # Otros módulos
  ],
  "comments": [],
  "trailer_video_url": "",
  "course_image_url": ""

  # Salida
  Status: 200 -> Curso creado.
  Status: 404 -> Error al guardar el curso.
  ```

- `http://127.0.0.1:8000/courses/<str:id>/`
  - Método: `GET`, `DELETE`
  - Descripción: Obtener un curso o todos y eliminar un curso dado su id.

  ```bash
  # Método GET
  # Entrada -> Ninguna 
  
  # Salida
  Status: 200 -> Obtiene la información de uno o varios cursos en función del id, si el id = 0, se obtiene todos los cursos.
  Status: 404 -> Curso no encontrado.
  ```

  ```bash
  # Método DELETE
  # Entrada -> Ninguna 
  
  # Salida
  Status: 200 -> Curso eliminado.
  Status: 404 -> Curso no encontrado.
  ```

- `http://127.0.0.1:8000/courses/by-category/<str:category>/`
  - Método: `GET`
  - Descripción: Obtener los cursos en función de una categoría.

  ```bash
  # Entrada -> Ninguna 
  
  # Salida
  Status: 200 -> Devuelve los cursos correspondientes a la categoría.
  Status: 404 -> No hay cursos disponibles.
  ```

- `http://127.0.0.1:8000/courses/featured/`
  - Método: `GET`
  - Descripción: Obtener los cursos destacados.

  ```bash
  # Entrada -> Ninguna 
  
  # Salida
  Status: 200 -> Retorna los cursos destacados.
  Status: 404 -> No hay cursos destacados.
  Status: 404 -> No hay cursos disponibles.
  ```

- `http://127.0.0.1:8000/courses/recently-added/`
  - Método: `GET`
  - Descripción: Obtener los 5 cursos recientemente agregados.

  ```bash
  # Entrada -> Ninguna 
  
  # Salida
  Status: 200 -> Retorna los cursos recientemente añadidos.
  Status: 404 -> No hay cursos disponibles.
  ```

- `http://127.0.0.1:8000/courses/by-instructor/<str:instructor_name>/`
  - Método: `GET`
  - Descripción: Obtener los cursos de un instructor.

  ```bash
  # Entrada -> Ninguna 
  
  # Salida
  Status: 200 -> Retorna los cursos del instructor.
  Status: 404 -> No hay cursos disponibles.
  ```

- `http://127.0.0.1:8000/courses/comments/<str:id>/`
  - Método: `PUT`
  - Descripción: Actualizar comentarios de un curso mediante el id de este.
  - Se debe enviar el `Token de Autenticación`.

  ```bash
  # Entrada
  {
  "comments": [
    {
      "name": "", # Nombre de la persona que envía el comentario
      "assessment": , # Puntuación del curso, es número.
      "comment": "", # Comentario del curso
    }
  ]
  }
  
  # Salida
  Status: 200 -> Comentarios agregados.
  Status: 400 -> Error al agregar comentarios.
  Status: 401 -> Acceso no autorizado.
  Status: 404 -> Curso no encontrado.
  ```

- `http://127.0.0.1:8000/courses/by-key-word/<str:key_word>/`
  - Método: `GET`
  - Descripción: Obtener los cursos si la palabra clave esta en el nombre del curso.

```bash
  # Entrada -> Ninguna

  # Salida
  Status: 200 -> Retorna la información del o los cursos.
  Status: 404 -> No hay cursos disponibles.
  ```

## Categorías

- `http://127.0.0.1:8000/categories/`
  - Método: `POST`, `PUT`
  - Descripción: Crear y actualiza una categoría.

  ```bash
  # Método POST
  # Entrada
  {
   "name": "",
   "description": ""
  }
  
  # Salida
  Status: 200 -> Categoria agregada.
  Status: 404 -> Error al guardar la categoria, revisar los campos que se envían.
  ```

  ```bash
  # Método PUT
  # Entrada
  {
    "id": "",
   "name": "",
   "description": ""
  }
  
  # Salida
  Status: 200 -> Categoria actualizada.
  Status: 404 -> Error al actualizar categoria.
  ```

- `http://127.0.0.1:8000/categories/<str:id>/`
  - Método: `GET`, `DELETE`
  - Descripción: Obtiene y elimina una categoría.

  ```bash
  # Método GET
  # Entrada -> Ninguna
  
  # Salida
  Status: 200 -> Devuelve todas las categorías, si el id = 0, retorna todas las categorias, caso contrario retorna la categoria respectiva al id.
  Status: 404 -> Categoría no encontrada.
  ```

  ```bash
  # Método DELETE
  # Entrada -> Ninguna
  
  # Salida
  Status: 200 -> Categoria eliminada.
  Status: 404 -> Categoria no encontrada.
  ```

- `http://127.0.0.1:8000/categories/id/<str:category_name>/`
  - Método: `GET`
  - Descripción: Obtiene el id de la categoría.

  ```bash
  # Método POST
  # Entrada -> Ninguna
  
  # Salida
  Status: 200 -> Retorna el id de la categoría.
  Status: 404 -> Categoría no encontrada.
  ```

## Content

- `http://127.0.0.1:8000/contents/`
  - Método: `POST`
  - Descripción: Crea el contenido de un curso.

  ```bash
  # Método POST
  # Entrada
  {
    "course_name": "", # Nombre del curso.
    "module": "", # Nombre del módulo del curso.
    "title": "", # Título del tema del módulo.
    "video_url": FILE # Video del tema del módulo.
  }
  
  # Salida
  Status: 200 -> Contenido agregado.
  Status: 400 -> Revisar campos y contenido de entrada.
  ```

**Nota:** Esta documentación está sujeta a cambios a medida que evoluciona la API.
