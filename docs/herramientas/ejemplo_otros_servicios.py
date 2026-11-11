# -*- coding: utf-8 -*-
"""Servicio otros-servicios (ES y EN). Pagina paraguas de servicios complementarios.

Frontera con sus vecinos, que es el problema real de esta pagina:
  - outsourcing  = gestion del personal de limpieza (reclutar, capacitar,
    supervisar, reemplazar). El argumento "un contrato, un proveedor, menos
    administracion" que traia la pagina anterior ERA el de outsourcing; se
    retira de aqui para no canibalizar.
  - handyman-empresas = reparaciones menores con personal asignado. Ya es una
    pagina larga del cliente; aqui solo se enlaza.
  - fumigacion = control de plagas, incluido el de jardines.
  - limpieza-industrial / puertos = residuos peligrosos y sustancias controladas.
otros-servicios = los servicios adyacentes a la limpieza que tienen logistica
diaria propia: areas verdes, recepcion, residuos comunes y mensajeria.

Se retira del texto original, por no tener respaldo: "manejo integral de
residuos y reciclaje" (sin un solo detalle de alcance) y el bloque "Por que Go
Services" con el pitch de consolidacion de proveedores. Quedan 3 TODOs.
"""

WA = "https://wa.me/50769823165?text="

PAGES = [
    dict(
        file="es/otros-servicios.html", lang="es", img="recursos.webp",
        url="https://www.go-cleaning.com/es/otros-servicios",
        list_id="complementarios",
        list_name="Servicios complementarios de facilities",
        service_type="Servicios complementarios de facilities",
        h1="Otros servicios de facilities",
        alt="Servicios complementarios",
        lead="Lo que rodea a la limpieza y también hay que operar todos los días.",
        meta="Servicios complementarios en Panamá: jardinería, conserjería y recepción, manejo de residuos y mensajería interna, coordinados con el programa de limpieza.",
        svc_desc="Servicios complementarios de facilities en Panamá: jardinería y áreas verdes, conserjería y recepción, manejo de residuos y reciclaje, y mensajería interna.",
        cta_h2="Cuéntanos qué servicios necesitas sumar",
        cta_p="Dinos qué instalación es, qué servicios te faltan y con qué frecuencia, y preparamos una propuesta.",
        cta_href=WA + "Hola%2C%20quiero%20cotizar%20servicios%20complementarios%20de%20facilities",
        cta_btn="Solicitar una propuesta",
        blocks=[
            ("p20", "Una instalación no se mantiene solo con limpieza. Las áreas verdes crecen, la correspondencia llega, los residuos salen y alguien tiene que estar en la recepción cuando se abre la puerta. Vistas de una en una son tareas pequeñas; sumadas son una carga real que casi siempre termina repartida entre quien tenga tiempo."),
            ("p20", "Go Services las atiende como servicios complementarios al contrato de limpieza. No son tareas que se le añaden al turno de limpieza: cada una tiene su horario, su personal y su supervisión, y por eso se definen por separado aunque las ejecute el mismo proveedor."),

            ("h2", "¿Qué servicios complementarios cubre Go Services?"),
            ("p", "Son cuatro frentes distintos, y cada uno se contrata por el volumen de trabajo real de la instalación, no como un extra genérico."),
            ("p", "Lo que tienen en común es que ninguno se resuelve con una visita puntual: todos piden presencia con una frecuencia definida."),
            ("h3", "Jardinería y mantenimiento de áreas verdes"),
            ("p", 'Corte, limpieza de jardineras y retiro de material vegetal en entradas, estacionamientos y patios. En el clima de Panamá la temporada de lluvias cambia el ritmo: lo que en verano se atiende cada quince días, en lluvia pide más frecuencia. El control de plagas en jardines se contrata aparte, en <a href="fumigacion">fumigación</a>.'),
            ("todo", "confirmar con el cliente el alcance de jardineria: si incluye poda en altura, riego y fertilizacion, y si los equipos los pone Go Services o el cliente."),
            ("h3", "Conserjería y recepción"),
            ("p", 'Personal en el acceso para recibir visitantes, registrar entradas y manejar la correspondencia que llega durante la jornada. En un edificio con varios inquilinos es el puesto que define la primera impresión, y su día a día se parece al de <a href="edificios">edificios y áreas comunes</a>.'),
            ("h3", "Manejo de residuos y reciclaje"),
            ("p", "Recolección interna, separación en el punto donde se genera el residuo y traslado al área de acopio para que salga el día que pasa la recolección. Lo que decide si funciona no es el servicio en sí, sino que los puntos de separación estén donde la gente realmente bota."),
            ("h3", "Mensajería interna y soporte operativo"),
            ("p", "Movimiento de documentos y materiales entre pisos o entre sedes, y las tareas de apoyo que aparecen durante la jornada y no tienen dueño fijo."),
            ("todo", "confirmar con el cliente si la mensajeria es solo interna o tambien externa (tramites, bancos, entregas a clientes)."),

            ("h2", "¿Cómo se coordinan estos servicios con la operación diaria?"),
            ("p", "Cada uno tiene una ventana horaria distinta, y ahí está la mitad del trabajo."),
            ("p", "La jardinería se hace temprano o en fin de semana, porque hace ruido y levanta polvo. La recepción cubre exactamente la jornada del edificio, ni más ni menos. Los residuos se mueven contra el calendario de recolección de la zona, que no es el calendario de la empresa. La mensajería se acumula y sale en rondas, no cada vez que alguien lo pide."),
            ("p20", "Por eso el programa se arma por horarios antes que por lista de tareas: dos servicios bien hechos a la hora equivocada estorban igual que uno mal hecho."),

            ("h2", "¿Qué cambia cuando el mismo equipo cubre limpieza y servicios complementarios?"),
            ("p", "Cambia la supervisión, que es donde se cae la mayoría de estos servicios."),
            ("p", "Con equipos fijos por instalación, el mismo supervisor que revisa el checklist de limpieza revisa también las áreas verdes y el área de acopio, y todo entra en el mismo reporte por turno. No hay que perseguir a tres empresas para saber por qué el jardín quedó a medias."),
            ("p", 'El personal es del mismo tipo: en planilla formal, con verificación de antecedentes y protocolos de confidencialidad. En conserjería y mensajería eso pesa más que en limpieza, porque son puestos con acceso a la correspondencia y trato directo con los visitantes. La gestión del personal en sí se describe en <a href="outsourcing">outsourcing de personal</a>.'),

            ("h2", "¿Qué residuos entran en el manejo de residuos y cuáles no?"),
            ("p", "El manejo de residuos de una oficina o un edificio cubre lo común: papel, cartón, plástico, vidrio, orgánicos del comedor y el residuo general del día."),
            ("p", 'Los residuos peligrosos, los químicos y las sustancias controladas no entran ahí. Tienen su propia cadena, a cargo del generador o de un gestor autorizado, y eso aplica igual en una planta que en una terminal: ver <a href="limpieza-industrial">limpieza industrial</a> y <a href="puertos">puertos y zonas logísticas</a>.'),
            ("p", "Conviene dejar por escrito, antes de arrancar, qué retira el servicio y qué queda con el cliente. Es el punto donde más seguido se descubre, a mitad de contrato, que nadie se hizo cargo."),
            ("todo", "confirmar con el cliente el alcance real del manejo de residuos: que categorias retira Go Services, si hay convenio con un gestor autorizado y si el reciclaje se entrega a un tercero. La pagina anterior decia \"manejo integral de residuos y reciclaje\" sin ningun detalle."),

            ("h2", "¿Qué no cubre este servicio?"),
            ("p", "Hay cuatro cosas que suelen buscarse aquí y que tienen su propia página, porque se contratan distinto."),
            ("p", 'Las reparaciones menores, una puerta que no cierra o una luminaria quemada, son <a href="handyman-empresas">servicio de handyman</a>, con personal asignado a la instalación. El control de plagas es <a href="fumigacion">fumigación</a>. La limpieza después de una obra o una remodelación es <a href="limpieza-post-construccion">limpieza post-construcción</a>. Y si lo que necesitas es personal de limpieza fijo bajo tu techo, eso es <a href="outsourcing">outsourcing de personal</a>.'),
            ("p20", 'Si no tienes claro dónde cae lo que necesitas, el catálogo completo está en <a href="servicios">servicios</a>.'),
        ],
    ),
    dict(
        file="en/otros-servicios.html", lang="en", img="recursos.webp",
        url="https://www.go-cleaning.com/en/otros-servicios",
        list_id="complementarios",
        list_name="Complementary facility services",
        service_type="Complementary facility services",
        h1="Additional facility services",
        alt="Complementary services",
        lead="The work that surrounds cleaning and also has to run every day.",
        meta="Complementary services in Panama: grounds care, concierge and reception, waste management and internal courier, coordinated with the cleaning program.",
        svc_desc="Complementary facility services in Panama: grounds and green-area care, concierge and reception, waste management and recycling, and internal courier.",
        cta_h2="Tell us which services you need to add",
        cta_p="Tell us what the facility is, which services you are missing and how often, and we will prepare a proposal.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20quote%20for%20complementary%20facility%20services",
        cta_btn="Request a proposal",
        blocks=[
            ("p20", "A facility is not kept up by cleaning alone. The grounds keep growing, the mail keeps arriving, the trash has to go out, and someone has to be at the front desk when the doors open. Taken one at a time these are small jobs; added up they are a real load that usually ends up split among whoever has a free moment."),
            ("p20", "Go Services handles them as complementary services alongside the cleaning contract. They are not tasks bolted onto the cleaning shift: each one has its own schedule, its own staff and its own supervision, which is why they are defined separately even when the same provider carries them out."),

            ("h2", "Which complementary services does Go Services cover?"),
            ("p", "There are four distinct areas, and each is contracted against the facility's real workload, not as a generic add-on."),
            ("p", "What they have in common is that none of them is solved by a one-off visit: they all call for presence at a defined frequency."),
            ("h3", "Grounds and green-area care"),
            ("p", 'Mowing, clearing planters and removing yard waste at entrances, parking areas and courtyards. In Panama\'s climate the rainy season changes the rhythm: what is handled every two weeks in the dry season calls for more frequency in the rain. Pest control in gardens is contracted separately, under <a href="fumigacion">fumigation</a>.'),
            ("todo", "confirm with the client the scope of grounds care: whether it includes high pruning, irrigation and fertilizing, and whether Go Services or the client supplies the equipment."),
            ("h3", "Concierge and reception"),
            ("p", 'Staff at the entrance to receive visitors, log arrivals and handle the mail that comes in during the day. In a building with several tenants this is the post that sets the first impression, and its day looks a lot like the one described under <a href="edificios">buildings and common areas</a>.'),
            ("h3", "Waste management and recycling"),
            ("p", "Internal collection, separation at the point where the waste is generated, and transfer to the holding area so it goes out on collection day. What decides whether it works is not the service itself, but whether the separation points are where people actually throw things away."),
            ("h3", "Internal courier and operational support"),
            ("p", "Moving documents and materials between floors or between sites, plus the support tasks that come up during the day and have no fixed owner."),
            ("todo", "confirm with the client whether the courier service is internal only or also external (errands, banks, deliveries to clients)."),

            ("h2", "How are these services coordinated with daily operations?"),
            ("p", "Each one has a different time window, and that is half the work."),
            ("p", "Grounds care is done early or on weekends, because it is noisy and kicks up dust. Reception covers exactly the building's hours, no more and no less. Waste moves against the area's collection calendar, which is not the company's calendar. Courier runs pile up and go out in rounds, not every time someone asks."),
            ("p20", "That is why the program is built around schedules before it is built around a task list: two services done well at the wrong hour get in the way just as much as one done badly."),

            ("h2", "What changes when the same team covers cleaning and complementary services?"),
            ("p", "Supervision changes, and supervision is where most of these services fall apart."),
            ("p", "With fixed teams for each facility, the same supervisor who goes through the cleaning checklist also goes through the grounds and the holding area, and it all lands in the same report for the shift. There is no chasing three companies to find out why the garden was left half done."),
            ("p", 'The staff are the same kind of staff: on the formal payroll, with background checks and confidentiality protocols. In concierge and courier work that matters more than it does in cleaning, because those posts have access to the mail and deal directly with visitors. Staff management itself is described under <a href="outsourcing">staffing outsourcing</a>.'),

            ("h2", "Which waste is included in waste management and which is not?"),
            ("p", "Waste management for an office or a building covers the ordinary stream: paper, cardboard, plastic, glass, organics from the break room and the general waste of the day."),
            ("p", 'Hazardous waste, chemicals and controlled substances are not part of it. They have their own chain, in the hands of the generator or an authorized waste manager, and that holds as much in a plant as in a terminal: see <a href="limpieza-industrial">industrial cleaning</a> and <a href="puertos">ports and logistics zones</a>.'),
            ("p", "It is worth setting out in writing, before starting, what the service removes and what stays with the client. This is the point where it most often turns out, halfway through a contract, that nobody took ownership."),
            ("todo", "confirm with the client the real scope of waste management: which categories Go Services removes, whether there is an agreement with an authorized waste manager, and whether recycling is handed to a third party. The previous page said \"end-to-end waste management and recycling\" without a single detail."),

            ("h2", "What does this service not cover?"),
            ("p", "There are four things people tend to look for here that have their own page, because they are contracted differently."),
            ("p", 'Minor repairs, a door that will not close or a burned-out light, are <a href="handyman-empresas">handyman service</a>, with staff assigned to the facility. Pest control is <a href="fumigacion">fumigation</a>. Cleaning after construction or a remodel is <a href="limpieza-post-construccion">post-construction cleaning</a>. And if what you need is permanent cleaning staff under your own roof, that is <a href="outsourcing">staffing outsourcing</a>.'),
            ("p20", 'If you are not sure where what you need belongs, the full catalog is under <a href="servicios">services</a>.'),
        ],
    ),
]
