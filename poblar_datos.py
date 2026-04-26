from core.models import Autor,Libro,Resena

# Crear autores
autor1 = Autor.objects.create(nombre="Gabriel Garcia Marquez", nacionalidad="Colombiano")
autor2 = Autor.objects.create(nombre="Mario Mendoza", nacionalidad="Colombiano")
autor3 = Autor.objects.create(nombre="Ana Frank", nacionalidad="Alemana")

# Crear libros
libro1 = Libro.objects.create(
    titulo="Cien años de soledad",
    autor=autor1,
    fecha_publicacion="1967-06-05",
    resumen="Narra la historia de siete generaciones de la familia Buendía en el pueblo ficticio de Macondo. Fundado por José Arcadio Buendía y Úrsula Iguarán, el pueblo evoluciona desde la utopía aislada hasta su destrucción, marcado por guerras civiles, incesto, soledad y hechos fantásticos tratados como cotidianos."
    )

libro2 = Libro.objects.create(
    titulo="El coronel no tiene quien le escriba",
    autor=autor1,
    fecha_publicacion="1961-08-12",
    resumen="Es la historia de la triste espera de un coronel retirado en una aldea de mala muerte. Junto a su mujer asmática, malvive con la doble esperanza de recibir su pensión como veterano de guerra, y de hacer crecer a un gallo de pelea lo suficiente como para poder sacar ganancias en las apuestas."
    )

libro3 = Libro.objects.create(
    titulo="Apocalipsis",
    autor=autor2,
    fecha_publicacion="2024-06-15",
    resumen="Tras el suicidio de su padre, Marcos ve su vida desmoronarse mientras investiga, junto a sus amigos, una misteriosa secta que utiliza una poción ancestral (psima) para alterar la percepción y el deseo, desatando el caos."
    )

libro4 = Libro.objects.create(
    titulo="Akelarre",
    autor=autor2,
    fecha_publicacion="2019-10-08",
    resumen="Novela de suspenso policial ambientada en Bogotá, centrada en el detective privado Frank Molina, un hombre alcohólico y paciente psiquiátrico, quien investiga una serie de brutales asesinatos de prostitutas en el barrio Santa Fe cometidos por un imitador de Jack el Destripador."
    )

libro5 = Libro.objects.create(
    titulo="El diario de Ana Frank",
    autor=autor3,
    fecha_publicacion="1947-06-25",
    resumen="El Diario de Ana Frank es el testimonio real de una niña judía de 13 años que se esconde de los nazis en Ámsterdam durante la Segunda Guerra Mundial (1942-1944). Narra la convivencia forzada en un anexo secreto, el miedo constante, la maduración de Ana, sus conflictos familiares y su esperanza en la humanidad."
    )

#Crear reseñas
resena1 = Resena.objects.create(
    libro=libro1,
    texto="Es un libro que exige atención pero que recompensa con una de las experiencias más profundas que la literatura puede ofrecer. No es solo lectura; es un lugar en el que te quedas a vivir hasta que pasas la última página.",
    calificacion=4,
    fecha="2026-04-25"
    )

resena2 = Resena.objects.create(
    libro=libro2,
    texto="Es una novela corta, casi una nouvelle, que se lee en una tarde pero se queda grabada para siempre. Es la prueba de que no se necesitan 500 páginas ni elementos fantásticos para crear una tragedia universal.",
    calificacion=4,
    fecha="2026-04-25"
    )

resena3 = Resena.objects.create(
    libro=libro3,
    texto="	Apocalipsis es una lectura fascinante pero perturbadora. Es un libro que te obliga a mirar hacia donde normalmente cierras los ojos. Es ideal para quienes buscan una literatura que cuestione el sistema y explore los límites de la cordura.",
    calificacion=3,
    fecha="2026-04-25"
    )

resena4 = Resena.objects.create(
    libro=libro4,
    texto="Akelarre es una novela sucia, rápida y profundamente cínica. Es el cierre perfecto para el personaje de Frank Molina y una fotografía movida, pero real, de la desesperanza urbana. Mendoza ya no solo narra historias; aquí parece estar lanzando una advertencia final.",
    calificacion=3,
    fecha="2026-04-25"
    )

resena5 = Resena.objects.create(
    libro=libro5,
    texto="Leer el diario es un ejercicio de empatía necesario. Es un recordatorio de lo que sucede cuando el odio se institucionaliza, pero también un monumento a la resiliencia del espíritu humano.",
    calificacion=4,
    fecha="2026-04-25"
    )

