1. El ORM de Django y la Estructura de Datos

En este proyecto se utilizó el ORM (Object-Relational Mapping) de Django para definir la base de datos mediante clases de Python. La estructura se basa en tres entidades principales: Autor, Libro y Reseña, las cuales mantienen una relación de jerarquía mediante el uso de ForeignKey.

•	Relación Autor-Libro: Se definió una relación de uno a muchos, donde un autor puede estar vinculado a múltiples libros.
•	Relación Libro-Reseña: Se estableció un vínculo donde cada reseña pertenece a un libro específico.

2. Representación de Objetos (_str_)

Se sobrescribió el método _str_() en todos los modelos para mejorar la legibilidad en el panel de administración.
Sin este método, Django mostraría etiquetas genéricas como <Libro: Libro object (1)>. Al implementarlo, logramos que la interfaz sea intuitiva, mostrando el nombre del autor, el título del libro o un resumen de la calificación directamente en las listas.

3. Validadores Personalizados

Para garantizar la integridad de la base de datos y cumplir con el reto propuesto, se implementaron funciones de validación antes de guardar los datos:

•	Autor: Se asegura que el nombre no contenga únicamente espacios en blanco o esté vacío.
•	Libro: Se restringió el campo resumen para que cumpla con una longitud mínima de caracteres (50).
•	Reseña: Se validó que la calificación sea un número entero dentro del rango permitido (1 a 5).

4. Personalización del Panel Admin

Se utilizó la clase ModelAdmin para transformar la visualización de los datos:

•	list_display: Permite visualizar múltiples columnas de información de un solo vistazo.
•	Búsqueda Relacional: Se configuró search_fields usando la sintaxis autor__nombre. Esto es necesario porque autor es una ForeignKey y para buscar por texto debemos acceder al campo específico del modelo relacionado.
•	Filtros: Se implementó list_filter para facilitar la navegación por categorías como el autor.

5. Carga de Datos Automatizada

Se incluyó un script poblar_datos.py que utiliza la shell de Django para insertar registros iniciales de forma masiva. Esto facilita el despliegue del proyecto en nuevos entornos y asegura que la aplicación cuente con datos de prueba consistentes para su evaluación.