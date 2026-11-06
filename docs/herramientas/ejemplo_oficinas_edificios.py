# -*- coding: utf-8 -*-
"""Industrias oficinas / edificios (ES y EN), con limpieza-corporativa como hermana.

FRONTERA DE LAS TRES PAGINAS
  limpieza-corporativa (servicio, NO se toca el cuerpo): el programa diario,
      zonas, frecuencias, reporteria. Ya tiene FAQ.
  oficinas  (industria): lo propio de la oficina como espacio ocupado: tipo y
      tamano, jornada vs fuera de horario, equipos y documentos en los puestos,
      insumos, limpieza profunda.
  edificios (industria): lo propio del edificio con varios inquilinos: zonas
      comunes, quien limpia que, coordinacion con la administracion, horarios
      sin molestar, altura.

A diferencia de colegios/hospitales, estas dos paginas NO reusan las preguntas
"que debe pedir / tercerizar / como se inicia": cada industria lleva preguntas
propias para que la plantilla no se repita en las siete.

Se retira de oficinas la frase "la oficina promedio tiene mas bacterias por
centimetro cuadrado en el escritorio que en el bano": es una estadistica sin
fuente y el contexto prohibe inventarlas.
"""

WA = "https://wa.me/50769823165?text="

PAGES = [
    # ------------------------------------------------------------ ES oficinas
    dict(
        file="es/oficinas.html", lang="es", img="oficina-corporativa.webp",
        url="https://www.go-cleaning.com/es/oficinas",
        list_id="tipos-de-oficina", list_name="Tipos de oficina que atendemos",
        service_type="Limpieza de oficinas",
        h1="Limpieza de oficinas", alt="Oficina corporativa",
        lead="Un espacio de trabajo limpio no es un beneficio: es infraestructura de productividad.",
        meta="Limpieza de oficinas en Panamá según el tipo de oficina: horarios, puestos de trabajo, insumos y limpieza profunda. Programas diarios con personal fijo.",
        svc_desc="Limpieza de oficinas en Panamá según el tipo de oficina: horarios, puestos de trabajo, insumos sanitarios y limpieza profunda.",
        cta_h2="Solicita una evaluación para tu oficina",
        cta_p="Dinos el tamaño de la oficina y su horario de uso, y armamos una propuesta a la medida.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20para%20mi%20oficina",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "Cuando la limpieza de una oficina falla, el equipo lo nota: quejas internas, baños y cocinas que nadie quiere usar, y esa sensación general de descuido que erosiona la moral. Para las empresas que compiten por talento, el estado físico de la oficina es parte de la propuesta de valor al empleado."),
            ("p20", 'Esta página trata de lo que es propio de una oficina: su tamaño, sus horarios, sus equipos y sus documentos. El programa diario, con zonas, frecuencias y reportería, está en <a href="limpieza-corporativa">limpieza corporativa</a>. Si administras el edificio donde está la oficina, mira <a href="edificios">limpieza de edificios corporativos</a>.'),

            ("h2", "¿Qué cambia según el tipo de oficina?"),
            ("p", "El tamaño y el uso de la oficina definen cuánta limpieza hace falta y cuándo."),
            ("h3", "Oficinas pequeñas"),
            ("p", "Un solo espacio con pocos puestos, una cocineta y un baño. Importa más una frecuencia pactada y un horario que no estorbe que una estructura de varios turnos."),
            ("h3", "Oficinas corporativas de una o varias plantas"),
            ("p", "Recepción, muchos puestos de trabajo, salas de reunión, cocina o comedor y baños con tránsito constante. Aquí el espacio se divide en zonas, cada una con su frecuencia y su responsable."),
            ("h3", "Coworking y espacios flexibles"),
            ("p", "Gente distinta cada día, salas que se reservan por horas y áreas compartidas de uso intensivo. Piden más atención a los puntos de contacto frecuente y a la limpieza entre un uso y otro de las salas."),
            ("h3", "Oficinas con atención al público"),
            ("p", "Bancos, aseguradoras, notarías o centros de servicio donde entran visitantes todo el día. La recepción y la sala de espera pesan tanto como los puestos de trabajo, porque son lo primero que ve el cliente."),

            ("h2", "¿Se limpia durante la jornada o fuera de ella?"),
            ("p", "Depende de la zona. Los baños, la cocina y las áreas de alto tránsito necesitan atención varias veces al día, mientras que los puestos de trabajo y las salas se limpian mejor cuando están vacíos, antes o después del horario."),
            ("p", "Limpiar fuera de horario implica entrar a la oficina sin que haya nadie: llaves, alarma y áreas restringidas. Por eso conviene definir por escrito quién entra, a qué zonas y con qué registro. El personal de Go Services pasa verificación de antecedentes y opera bajo protocolos de confidencialidad."),

            ("h2", "¿Cómo se limpian los puestos de trabajo sin dañar equipos ni documentos?"),
            ("p", "Un escritorio de oficina tiene monitores, teclados, teléfonos y papeles, y no se limpia como un piso. El criterio es no mover documentos, no rociar producto directamente sobre los equipos y limpiar las superficies despejadas con paños apenas húmedos, tratando aparte los puntos de contacto como teclados y teléfonos."),
            ("p", "Conviene acordar con el responsable de la oficina qué hacer con los escritorios que tienen papeles o equipos encima, para que el personal de limpieza no tenga que decidirlo cada noche."),
            ("todo", "confirmar con el cliente los procedimientos exactos para puestos de trabajo (paños, productos, tratamiento de teclados) antes de afirmarlos como protocolo propio; hoy se describen como criterio general."),

            ("h2", "¿Qué incluye la reposición de insumos sanitarios?"),
            ("p", "La reposición continua de insumos sanitarios, como jabón, papel y desinfectante, forma parte del programa de limpieza. Lo que conviene dejar por escrito es qué se repone, con qué frecuencia, qué incluye la cotización y qué se factura aparte."),
            ("p", 'El desglose de lo que mueve una cotización está en <a href="cuanto-cuesta-limpieza-oficinas">cuánto cuesta la limpieza de oficinas en Panamá</a>.'),
            ("todo", "confirmar con el cliente si los consumibles (jabon, papel) los suministra Go Services o el cliente, y si se facturan aparte."),

            ("h2", "¿Cada cuánto conviene una limpieza profunda?"),
            ("p", "La limpieza profunda se programa aparte de la diaria, de forma mensual o trimestral según el uso de la oficina. Cubre lo que el servicio diario no alcanza: alfombras y tapicería, vidrios, rincones y el polvo acumulado en lugares de difícil acceso."),
            ("p20", 'Para esas tareas, el detalle está en <a href="alfombras-muebles">alfombras y muebles</a> y en <a href="cuidado-pisos">cuidado de pisos</a>. Sobre el polvo en la oficina y su efecto en el ambiente de trabajo, ver <a href="polvo-en-oficinas">polvo en oficinas</a>.'),
        ],
    ),

    # ------------------------------------------------------------ ES edificios
    dict(
        file="es/edificios.html", lang="es", img="edificios.webp",
        url="https://www.go-cleaning.com/es/edificios",
        list_id="zonas", list_name="Zonas de un edificio corporativo",
        service_type="Limpieza de edificios corporativos",
        h1="Limpieza de edificios corporativos", alt="Edificio corporativo",
        lead="La imagen del edificio es la primera impresión de cada empresa que lo ocupa.",
        meta="Limpieza de edificios corporativos en Panamá: áreas comunes, coordinación con la administración, horarios sin afectar a inquilinos y fachadas en altura.",
        svc_desc="Limpieza de edificios corporativos y torres en Panamá: áreas comunes, coordinación con la administración, horarios sin afectar a inquilinos y fachadas en altura.",
        cta_h2="Solicita una evaluación para tu edificio",
        cta_p="Cuéntanos cuántas plantas tiene, qué áreas comunes administras y cómo funciona el acceso, y evaluamos cómo organizar el servicio.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20para%20mi%20edificio",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "Un edificio corporativo con lobbies opacos, baños descuidados o pisos manchados comunica negligencia antes de que el visitante llegue al piso del inquilino. Para los administradores de propiedad, la limpieza es retención de inquilinos: cada queja sin resolver es un argumento para no renovar contrato."),
            ("p20", 'Aquí se trata de las áreas comunes y de cómo se coordina un edificio con varios inquilinos. Si tu empresa ocupa una oficina dentro del edificio, mira <a href="oficinas">limpieza de oficinas</a>; el programa diario, con zonas y reportería, está en <a href="limpieza-corporativa">limpieza corporativa</a>.'),

            ("h2", "¿Qué zonas de un edificio corporativo exigen más atención?"),
            ("p", "Un edificio reúne espacios muy distintos entre sí, y cada uno se limpia con otro criterio."),
            ("h3", "Lobby y recepción"),
            ("p", "Es la primera impresión del edificio. Piso, vidrios, mostrador y mobiliario tienen que estar impecables desde la apertura, y se revisan durante el día porque el tránsito los ensucia constantemente."),
            ("h3", "Ascensores y escaleras"),
            ("p", "Son los puntos de contacto más usados del edificio: botoneras, pasamanos, paredes y piso de cabina. Piden desinfección frecuente de lo que se toca y atención al piso, donde se acumula la suciedad que entra de la calle."),
            ("h3", "Baños comunes de cada planta"),
            ("p", "Son de uso constante y de las quejas más frecuentes de los inquilinos. Se atienden varias veces durante el día, con reposición de insumos, y no se dejan para el cierre."),
            ("h3", "Estacionamientos y azoteas"),
            ("p", "Son áreas de servicio con otro tipo de suciedad: polvo, aceite, hojas y residuos. Se programan con su propia frecuencia, más espaciada que la de las áreas interiores."),

            ("h2", "¿Quién limpia qué: las áreas comunes o los pisos de los inquilinos?"),
            ("p", "En un edificio con varios inquilinos conviven dos responsabilidades. La administración contrata las áreas comunes, como lobby, ascensores, baños comunes y estacionamientos, y cada empresa contrata la limpieza de su propia planta."),
            ("p20", 'Los problemas aparecen en la frontera: la puerta de la planta, el pasillo del piso o el baño que usan dos inquilinos. Conviene definir por escrito dónde termina un contrato y dónde empieza el otro, para que ninguna zona quede sin responsable. Una empresa que ocupa pisos completos puede resolverlos con su propio <a href="limpieza-corporativa">programa de limpieza corporativa</a>.'),

            ("h2", "¿Cómo se coordina la limpieza con la administración del edificio?"),
            ("p", "Con una coordinación directa con la administración y con un reporte por turno que deja constancia de lo ejecutado. Go Services asigna equipos permanentes por edificio, de modo que quien limpia conoce las áreas y los horarios del sitio."),
            ("p", "Ese reporte sirve para una auditoría y para responder a un inquilino que reclama, porque muestra qué se hizo, en qué zona y cuándo."),

            ("h2", "¿Cómo se limpia sin molestar a inquilinos y visitantes?"),
            ("p", "El edificio nunca está vacío: hay inquilinos que llegan temprano, visitantes durante el día y empresas que salen tarde. Por eso las áreas de más exposición, como el lobby y los ascensores, se limpian antes de la apertura y se revisan durante el día, y la limpieza de pisos por planta sigue un cronograma adaptado a los horarios de oficina."),
            ("p", "Cuando hay piso mojado o una intervención en un ascensor de servicio, la zona se señaliza y se usa el acceso que defina la administración, para que nadie tenga que esquivar el trabajo."),
            ("todo", "confirmar con el cliente los horarios tipicos (apertura, lobby durante el dia) y el procedimiento de senalizacion antes de afirmarlos como protocolo propio; hoy se describen como criterio general."),

            ("h2", "¿Qué implica la limpieza de fachadas y cristales en altura?"),
            ("p", 'Es un trabajo distinto de la limpieza diaria. El trabajo en altura exige equipo y procedimientos propios, depende del clima y se programa como una intervención con su propio calendario, no como parte del servicio diario. El detalle está en <a href="vidrios-fachadas">vidrios y fachadas</a>.'),
            ("todo", "confirmar con el cliente el alcance real del trabajo en altura (equipos, alturas maximas, procedimientos de seguridad) antes de describirlos."),
        ],
    ),

    # ------------------------------------------------------------ EN oficinas
    dict(
        file="en/oficinas.html", lang="en", img="oficina-corporativa.webp",
        url="https://www.go-cleaning.com/en/oficinas",
        list_id="tipos-de-oficina", list_name="Types of office we serve",
        service_type="Office cleaning",
        h1="Office cleaning", alt="Corporate office",
        lead="A clean workspace isn't a perk: it's productivity infrastructure.",
        meta="Office cleaning in Panama by type of office: schedules, workstations, supplies and deep cleaning. Daily programs with fixed staff.",
        svc_desc="Office cleaning in Panama by type of office: schedules, workstations, sanitary supplies and deep cleaning.",
        cta_h2="Request an assessment for your office",
        cta_p="Tell us the size of the office and when it is in use, and we will put together a proposal to fit.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20cleaning%20assessment%20for%20my%20office",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "When office cleaning fails, the team notices: internal complaints, restrooms and kitchens nobody wants to use, and that general sense of neglect that erodes morale. For companies competing for talent, the physical state of the office is part of the employee value proposition."),
            ("p20", 'This page is about what is specific to an office: its size, its hours, its equipment and its documents. The daily program, with zones, frequencies and reporting, is at <a href="limpieza-corporativa">corporate cleaning</a>. If you manage the building the office is in, see <a href="edificios">corporate building cleaning</a>.'),

            ("h2", "How does the type of office change what you need?"),
            ("p", "The size and use of the office decide how much cleaning it needs and when."),
            ("h3", "Small offices"),
            ("p", "A single space with a few desks, a kitchenette and a restroom. An agreed frequency and a schedule that stays out of the way matter more than a multi-shift structure."),
            ("h3", "Corporate offices on one or several floors"),
            ("p", "Reception, many workstations, meeting rooms, a kitchen or dining area and restrooms with constant traffic. Here the space is divided into zones, each with its own frequency and its own person responsible."),
            ("h3", "Coworking and flexible spaces"),
            ("p", "Different people every day, rooms booked by the hour and heavily used shared areas. They call for more attention to high-touch points and to cleaning rooms between one use and the next."),
            ("h3", "Offices that receive the public"),
            ("p", "Banks, insurers, notary offices or service centers where visitors come in all day. The reception and waiting area weigh as much as the workstations, because they are the first thing the client sees."),

            ("h2", "Is the office cleaned during the working day or outside it?"),
            ("p", "It depends on the zone. Restrooms, the kitchen and high-traffic areas need attention several times a day, while workstations and meeting rooms are best cleaned when empty, before or after hours."),
            ("p", "Cleaning after hours means entering the office with nobody there: keys, alarm and restricted areas. That is why it is worth setting out in writing who enters, which zones and with what record. Go Services staff go through background checks and work under confidentiality protocols."),

            ("h2", "How are workstations cleaned without damaging equipment or documents?"),
            ("p", "An office desk has monitors, keyboards, phones and papers, and it is not cleaned like a floor. The working rule is not to move documents, not to spray product directly onto equipment, and to wipe the clear surfaces with barely damp cloths, treating high-touch items such as keyboards and phones separately."),
            ("p", "It is worth agreeing with whoever is responsible for the office what to do with desks that have papers or equipment on them, so cleaning staff do not have to decide it every night."),
            ("todo", "confirm with the client the exact procedures for workstations (cloths, products, keyboard treatment) before stating them as the company's own protocol; for now they are described as general practice."),

            ("h2", "What does replenishing sanitary supplies include?"),
            ("p", "Continuous replenishment of sanitary supplies, such as soap, paper and disinfectant, is part of the cleaning program. What is worth setting out in writing is what is replenished, how often, what the quote includes and what is billed separately."),
            ("p", 'A breakdown of what moves a quote is in <a href="cuanto-cuesta-limpieza-oficinas">how much office cleaning costs in Panama</a>.'),
            ("todo", "confirm with the client whether consumables (soap, paper) are supplied by Go Services or by the client, and whether they are billed separately."),

            ("h2", "How often is deep cleaning worthwhile?"),
            ("p", "Deep cleaning is scheduled separately from the daily service, monthly or quarterly depending on how the office is used. It covers what the daily service does not reach: carpets and upholstery, glass, corners and dust that builds up in hard-to-reach places."),
            ("p20", 'For those tasks, the detail is under <a href="alfombras-muebles">carpets and furniture</a> and <a href="cuidado-pisos">floor care</a>. For dust in the office and its effect on the working environment, see <a href="polvo-en-oficinas">dust in offices</a>.'),
        ],
    ),

    # ------------------------------------------------------------ EN edificios
    dict(
        file="en/edificios.html", lang="en", img="edificios.webp",
        url="https://www.go-cleaning.com/en/edificios",
        list_id="zonas", list_name="Zones of a corporate building",
        service_type="Corporate building cleaning",
        h1="Corporate building cleaning", alt="Corporate building",
        lead="The building's image is the first impression of every company inside it.",
        meta="Corporate building cleaning in Panama: common areas, coordination with building management, schedules that do not disturb tenants and facades at height.",
        svc_desc="Cleaning for corporate buildings and towers in Panama: common areas, coordination with building management, schedules that do not disturb tenants and facades at height.",
        cta_h2="Request an assessment for your building",
        cta_p="Tell us how many floors it has, which common areas you manage and how access works, and we will assess how to organize the service.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20cleaning%20assessment%20for%20my%20building",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "A corporate building with dull lobbies, neglected restrooms or stained floors communicates negligence before the visitor even reaches the tenant's floor. For property managers, cleaning is tenant retention: every unresolved complaint is an argument not to renew."),
            ("p20", 'This page is about common areas and how a building with several tenants is coordinated. If your company occupies an office inside the building, see <a href="oficinas">office cleaning</a>; the daily program, with zones and reporting, is at <a href="limpieza-corporativa">corporate cleaning</a>.'),

            ("h2", "Which zones of a corporate building need the most attention?"),
            ("p", "A building brings together very different spaces, and each is cleaned by its own criteria."),
            ("h3", "Lobby and reception"),
            ("p", "This is the building's first impression. Floor, glass, front desk and furniture have to be spotless from opening time, and they are checked through the day because foot traffic keeps dirtying them."),
            ("h3", "Elevators and stairwells"),
            ("p", "These are the most-touched points in the building: buttons, handrails, walls and the cab floor. They call for frequent disinfection of what gets touched and attention to the floor, where the dirt that comes in from the street builds up."),
            ("h3", "Common restrooms on each floor"),
            ("p", "They are in constant use and the source of some of tenants' most frequent complaints. They are attended several times through the day, with supplies replenished, and are not left for closing time."),
            ("h3", "Parking and rooftops"),
            ("p", "These are service areas with a different kind of dirt: dust, oil, leaves and debris. They are scheduled on their own frequency, more spread out than indoor areas."),

            ("h2", "Who cleans what: the common areas or the tenants' floors?"),
            ("p", "In a building with several tenants, two responsibilities coexist. Building management contracts the common areas, such as the lobby, elevators, common restrooms and parking, and each company contracts the cleaning of its own floor."),
            ("p20", 'Problems arise at the boundary: the floor door, the corridor on the floor or the restroom two tenants share. It is worth setting out in writing where one contract ends and the other begins, so that no zone is left without someone responsible. A company that occupies whole floors can handle them with its own <a href="limpieza-corporativa">corporate cleaning program</a>.'),

            ("h2", "How is cleaning coordinated with building management?"),
            ("p", "Through direct coordination with building management and a report for each shift that records what was carried out. Go Services assigns permanent teams to each building, so the people cleaning know the areas and the schedules of the site."),
            ("p", "That report serves an audit, and it serves when a tenant complains, because it shows what was done, in which zone and when."),

            ("h2", "How is the building cleaned without disturbing tenants and visitors?"),
            ("p", "The building is never empty: some tenants arrive early, visitors come through the day and some companies leave late. So the most exposed areas, such as the lobby and elevators, are cleaned before opening and checked during the day, and floor-by-floor cleaning follows a schedule adapted to office hours."),
            ("p", "When a floor is wet or a service elevator is being worked on, the zone is marked off and the access that building management defines is used, so nobody has to step around the work."),
            ("todo", "confirm with the client the typical schedules (opening, lobby during the day) and the signage procedure before stating them as the company's own protocol; for now they are described as general practice."),

            ("h2", "What does cleaning facades and exterior glass at height involve?"),
            ("p", 'It is different work from daily cleaning. Work at height calls for its own equipment and procedures, depends on the weather and is scheduled as an intervention with its own calendar, not as part of the daily service. The detail is under <a href="vidrios-fachadas">windows and facades</a>.'),
            ("todo", "confirm with the client the real scope of work at height (equipment, maximum heights, safety procedures) before describing it."),
        ],
    ),
]
