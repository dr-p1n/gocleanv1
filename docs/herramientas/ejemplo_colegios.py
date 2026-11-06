# -*- coding: utf-8 -*-
"""Par limpieza-centros-educativos (servicio) / colegios (industria), ES y EN.

SERVICIO  -> que se limpia en cada zona del colegio, con que productos y cuando.
INDUSTRIA -> que necesita quien administra el centro: tipo de centro, que exigir,
             conserjes propios vs proveedor, arranque, como comunicarlo a familias.
Sin cifras, tarifas, SLA, clientes ni normas citadas. Se retira "certificados"
de los productos biofriendly (el hecho publicado es protocolo 100% biofriendly).
"""

WA = "https://wa.me/50769823165?text="

PAGES = [
    # ------------------------------------------------------------ ES servicio
    dict(
        file="es/limpieza-centros-educativos.html", lang="es", img="colegios-moderna.webp",
        url="https://www.go-cleaning.com/es/limpieza-centros-educativos",
        list_id="zonas", list_name="Limpieza de un centro educativo por zona",
        service_type="Limpieza para Centros Educativos",
        h1="Limpieza para colegios y centros educativos", alt="Limpieza para centros educativos",
        lead="El protocolo de limpieza de un centro educativo, zona por zona: qué se hace, con qué productos y cuándo.",
        meta="Limpieza de colegios por zona: aulas, baños, comedores y áreas deportivas, con productos biofriendly de baja toxicidad y horarios fuera de clases. Panamá.",
        svc_desc="Limpieza para colegios y centros educativos por zona, con productos biofriendly de baja toxicidad y cronogramas fuera del horario de clases. ISO 9001, ISSA, GBAC.",
        cta_h2="Solicita una evaluación de tu centro",
        cta_p="El protocolo correcto se define recorriendo el recinto. Cuéntanos qué zonas tiene tu centro y en qué horarios opera, y evaluamos cómo organizar el servicio.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20para%20mi%20centro%20educativo",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "La limpieza de un colegio no puede usar los mismos químicos que una bodega industrial. Los productos deben ser de baja toxicidad, sin olores fuertes y seguros para el contacto indirecto con menores, y el trabajo tiene que terminar antes de que lleguen los estudiantes. Esta página explica cómo se organiza ese trabajo."),
            ("p20", 'Go Services aplica un protocolo biofriendly como estándar incluido, con cronogramas fuera del horario de clases. Si administras un colegio, una escuela o una universidad y lo que necesitas es decidir cómo contratar la limpieza, esa guía está en <a href="colegios">limpieza de colegios y escuelas</a>.'),

            ("h2", "¿Qué incluye la limpieza de un centro educativo en cada zona?"),
            ("p", "Cada zona de un colegio tiene un uso, un riesgo y una frecuencia distintos. Estas son las cuatro que más cambian el protocolo."),
            ("h3", "Aulas y pasillos"),
            ("p", "Son las superficies de más tránsito: pupitres, manijas, interruptores, barandas y pasamanos. Se limpian a diario, con desinfección de los puntos de contacto frecuente, y el piso se trabaja al final para no volver a ensuciar lo ya limpio."),
            ("h3", "Baños"),
            ("p", "Son el punto de mayor riesgo higiénico del colegio. Piden desinfección diaria de sanitarios, lavamanos, grifería y pisos, con utensilios exclusivos de esta zona que no se usan en aulas ni comedores."),
            ("h3", "Comedores, cocinas escolares y fuentes de agua"),
            ("p", "Aquí se limpia pensando en los alimentos y en el agua. El criterio es separar la limpieza de las superficies que tocan alimentos de la del resto, usar productos aptos para estas zonas y no dejar residuos ni olores."),
            ("h3", "Áreas deportivas y vestidores"),
            ("p", "Canchas techadas, gimnasios y vestidores combinan sudor, humedad y calzado de exterior. Piden limpieza según el material del piso y desinfección de bancas, casilleros y duchas, con ventilación para que la humedad no favorezca el moho."),
            ("todo", "confirmar con el cliente los procedimientos exactos por zona (utensilios exclusivos, separacion en cocinas, frecuencias) antes de afirmarlos como protocolo propio; hoy se describen como criterio general."),

            ("h2", "¿Por qué importa que los productos sean de baja toxicidad en un colegio?"),
            ("p", "Los niños pasan el día en contacto con pupitres, pisos y manijas, y respiran en espacios cerrados, así que los productos fuertes tienen un costo que en una bodega no existe. Un protocolo biofriendly usa productos de baja toxicidad y sin olores fuertes, que desinfectan sin dejar residuos químicos activos cuando los estudiantes regresan."),
            ("p", "Eso no reemplaza el criterio de uso: la ficha técnica de cada producto define la dilución, el tiempo de contacto y dónde puede aplicarse, y esas indicaciones se respetan en cada zona."),

            ("h2", "¿Qué se limpia a diario y qué se hace en profundidad?"),
            ("p", "La limpieza diaria mantiene el colegio funcional entre clases. La sanitización profunda interviene las zonas de más riesgo con una frecuencia pactada, y los recesos permiten el trabajo que no se puede hacer con estudiantes presentes:"),
            ("ul", [
                "<strong>A diario.</strong> Aulas, pasillos, baños y puntos de contacto frecuente.",
                "<strong>Con frecuencia pactada.</strong> Comedores, cocinas escolares, fuentes de agua, áreas deportivas y vestidores.",
                "<strong>En recesos.</strong> Intervenciones que necesitan espacios vacíos, como el tratamiento de pisos o la limpieza de vidrios.",
            ]),
            ("p20", 'Para esas intervenciones, el detalle está en <a href="cuidado-pisos">cuidado de pisos</a> y <a href="vidrios-fachadas">vidrios y fachadas</a>.'),

            ("h2", "¿Cómo se organizan los horarios para no interrumpir las clases?"),
            ("p", "La regla es que el colegio esté limpio antes de que lleguen los estudiantes y que el trabajo no coincida con las clases. Para eso el servicio se programa en horario vespertino o de fin de semana, según cómo opere el centro, y se coordina con la administración para que cada zona quede lista a tiempo."),

            ("h2", "¿Cómo se verifica el trabajo?"),
            ("p", "Cada zona tiene su checklist y el equipo entrega un reporte por turno, de modo que la administración puede comprobar qué se limpió y cuándo sin tener que supervisarlo en persona."),
        ],
    ),

    # ------------------------------------------------------------ ES industria
    dict(
        file="es/colegios.html", lang="es", img="colegios.webp",
        url="https://www.go-cleaning.com/es/colegios",
        list_id="tipos-de-centro", list_name="Tipos de centro educativo que atendemos",
        service_type="Limpieza de colegios y centros educativos",
        h1="Limpieza de colegios y escuelas", alt="Centro educativo",
        lead="Ambientes seguros y saludables para estudiantes y personal docente.",
        meta="Qué debe pedir un colegio, escuela o universidad a su proveedor de limpieza: tipo de centro, personal, tercerización y puesta en marcha. Panamá.",
        svc_desc="Limpieza para colegios, escuelas y universidades en Panamá: qué exigir al proveedor, cómo contratar y cómo se inicia el servicio.",
        cta_h2="Solicita una evaluación para tu colegio",
        cta_p="Cuéntanos cuántas zonas tiene tu colegio y cómo es su calendario, y te decimos cómo organizaríamos el servicio.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20para%20mi%20colegio",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "En un centro educativo, la bioseguridad protege a la población más vulnerable y da tranquilidad a las familias. Los ambientes limpios y sanitizados ayudan a contener los contagios y a sostener la continuidad del año escolar. Un colegio con protocolos de limpieza visibles no solo cumple: se diferencia ante las familias que evalúan dónde matricular."),
            ("p20", 'Si diriges un colegio, una escuela o una universidad, aquí está lo que conviene saber antes de contratar la limpieza. Qué se limpia en cada zona, con qué productos y en qué horarios se explica en <a href="limpieza-centros-educativos">limpieza para colegios y centros educativos</a>.'),

            ("h2", "¿Qué cambia según el tipo de centro educativo?"),
            ("p", "Un preescolar y una universidad no se limpian igual, y lo que se contrata cambia con la edad de los estudiantes y el tamaño del campus."),
            ("h3", "Preescolares y guarderías"),
            ("p", "Niños pequeños que gatean, comen en el piso y se llevan objetos a la boca. Piden más desinfección de pisos y juguetes, productos de muy baja toxicidad y atención especial a los baños y las áreas de cambio."),
            ("h3", "Escuelas primarias y secundarias"),
            ("p", "Es el grueso de la demanda: aulas, comedor, baños y áreas deportivas con mucho tránsito y horarios muy marcados. Lo que más pesa es terminar antes del inicio de clases y acordar en el contrato cómo se mantienen los baños durante la jornada."),
            ("h3", "Universidades e institutos"),
            ("p", "Campus con varios edificios, laboratorios, bibliotecas y áreas comunes, y horarios que varían por facultad y por turno. Aquí cuenta la coordinación de cronogramas por edificio y la capacidad de cubrir varios turnos."),
            ("h3", "Centros de formación y academias"),
            ("p", "Salas de capacitación y talleres con clases de tarde y de noche. Necesitan un servicio que se adapte a cuándo hay clases, más que a un calendario escolar fijo."),

            ("h2", "¿Qué debe pedir un colegio a su proveedor de limpieza?"),
            ("p", "Con menores en el recinto, algunos criterios pesan más que el precio:"),
            ("ul", [
                "Verificación de antecedentes de todo el personal que entra al recinto, y personal en planilla formal",
                "Productos de baja toxicidad con ficha técnica disponible",
                "Horarios de trabajo fuera de la jornada de clases, definidos por escrito",
                "Un equipo fijo asignado al centro, para que el personal sea siempre el mismo",
                "Checklists por zona y reporte por turno que la administración pueda revisar",
                "Una forma clara de cubrir las ausencias antes del inicio de clases",
            ]),
            ("p20", 'En Go Services el personal está en planilla formal y pasa por verificación de antecedentes, el protocolo biofriendly es estándar incluido y cada centro cuenta con su equipo fijo y checklists auditables. Para llevar estos criterios a la comparación entre propuestas, hay una guía completa de <a href="como-elegir-empresa-limpieza">cómo elegir una empresa de limpieza</a>.'),

            ("h2", "¿Conviene tercerizar la limpieza de un colegio o tener conserjes propios?"),
            ("p", "Un colegio puede tener conserjes propios para el día a día, y eso funciona para el mantenimiento durante la jornada. Lo que suele exigir más de un equipo pequeño son las intervenciones profundas, la cobertura de ausencias y la limpieza de los recesos, cuando hay que mover más personas durante pocos días."),
            ("p20", 'Un modelo mixto es posible: conserjes propios para la jornada y un proveedor para la limpieza profunda y los recesos. Más sobre este modelo en <a href="outsourcing">outsourcing de personal</a>.'),

            ("h2", "¿Cómo se inicia el servicio en un colegio?"),
            ("p", "El mejor momento suele ser el receso anterior al inicio de clases, porque permite una limpieza profunda inicial sin estudiantes. La secuencia es:"),
            ("ul", [
                "Recorrido del recinto y mapa de las zonas: aulas, baños, comedor y áreas deportivas",
                "Definición de checklists, productos y horarios junto con la administración",
                "Limpieza profunda inicial en un receso, cuando sea posible",
                "Asignación del equipo fijo e inicio con reporte por turno",
            ]),
            ("todo", "confirmar con el cliente que esta secuencia de arranque refleja su proceso real; esta redactada como secuencia general."),

            ("h2", "¿Cómo se comunica el protocolo de limpieza a las familias?"),
            ("p", "Un protocolo de limpieza solo diferencia al colegio si las familias lo conocen. Los checklists y los reportes por turno dan a la administración información concreta para compartir con los padres, en lugar de promesas generales."),
        ],
    ),

    # ------------------------------------------------------------ EN servicio
    dict(
        file="en/limpieza-centros-educativos.html", lang="en", img="colegios-moderna.webp",
        url="https://www.go-cleaning.com/en/limpieza-centros-educativos",
        list_id="zonas", list_name="Educational facility cleaning by zone",
        service_type="Cleaning for Educational Centers",
        h1="Cleaning for schools and educational centers", alt="Cleaning for educational centers",
        lead="The cleaning protocol for an educational facility, zone by zone: what is done, with which products and when.",
        meta="School cleaning by zone: classrooms, restrooms, cafeterias and sports areas, with low-toxicity biofriendly products and off-hours schedules. Panama.",
        svc_desc="Cleaning for schools and educational centers by zone, with low-toxicity biofriendly products and schedules outside class hours. ISO 9001, ISSA, GBAC.",
        cta_h2="Request an assessment of your facility",
        cta_p="The right protocol is defined by walking the grounds. Tell us which zones your facility has and when it operates, and we will assess how to organize the service.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20cleaning%20assessment%20for%20my%20school",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "Cleaning a school cannot use the same chemicals as an industrial warehouse. Products must be low-toxicity, free of strong odors and safe for indirect contact with minors, and the work has to finish before students arrive. This page explains how that work is organized."),
            ("p20", 'Go Services applies a biofriendly protocol as an included standard, on schedules outside class hours. If you run a school, a college or a university and need to decide how to contract cleaning, that guide is at <a href="colegios">school and campus cleaning</a>.'),

            ("h2", "What does cleaning an educational facility include in each zone?"),
            ("p", "Each zone of a school has a different use, risk and frequency. These are the four that change the protocol most."),
            ("h3", "Classrooms and hallways"),
            ("p", "These are the highest-traffic surfaces: desks, door handles, switches, railings and handrails. They are cleaned daily, with disinfection of the high-touch points, and the floor is done last so that nothing already clean gets dirty again."),
            ("h3", "Restrooms"),
            ("p", "They are the school's highest hygiene risk. They call for daily disinfection of toilets, sinks, fixtures and floors, with tools dedicated to this zone that are never used in classrooms or cafeterias."),
            ("h3", "Cafeterias, school kitchens and water fountains"),
            ("p", "Here the cleaning is designed around food and water. The working rule is to keep food-contact surfaces separate from everything else, to use products suited to these zones and to leave no residue or odor."),
            ("h3", "Sports areas and locker rooms"),
            ("p", "Covered courts, gyms and locker rooms combine sweat, humidity and street footwear. They call for cleaning suited to the floor material and disinfection of benches, lockers and showers, with ventilation so humidity does not encourage mold."),
            ("todo", "confirm with the client the exact procedures per zone (dedicated tools, separation in kitchens, frequencies) before stating them as the company's own protocol; for now they are described as general practice."),

            ("h2", "Why do low-toxicity products matter in a school?"),
            ("p", "Children spend the day in contact with desks, floors and handles, and breathe in enclosed spaces, so strong products carry a cost that a warehouse does not have. A biofriendly protocol uses low-toxicity products without strong odors, which disinfect without leaving active chemical residue when students return."),
            ("p", "That does not replace sound use: each product's technical data sheet sets the dilution, the contact time and where it can be applied, and those instructions are followed in every zone."),

            ("h2", "What is cleaned daily and what is done in depth?"),
            ("p", "Daily cleaning keeps the school running between classes. Deep sanitizing covers the highest-risk zones at an agreed frequency, and school breaks allow the work that cannot be done with students present:"),
            ("ul", [
                "<strong>Daily.</strong> Classrooms, hallways, restrooms and high-touch points.",
                "<strong>At an agreed frequency.</strong> Cafeterias, school kitchens, water fountains, sports areas and locker rooms.",
                "<strong>During breaks.</strong> Work that needs empty spaces, such as floor treatment or window cleaning.",
            ]),
            ("p20", 'For that work, the detail is under <a href="cuidado-pisos">floor care</a> and <a href="vidrios-fachadas">windows and facades</a>.'),

            ("h2", "How are schedules organized so classes are not interrupted?"),
            ("p", "The rule is that the school is clean before students arrive and that the work never overlaps with classes. So the service is scheduled for the evening or the weekend, depending on how the facility operates, and coordinated with administration so that each zone is ready on time."),

            ("h2", "How is the work verified?"),
            ("p", "Each zone has its checklist and the team hands in a report for each shift, so administration can confirm what was cleaned and when without having to supervise in person."),
        ],
    ),

    # ------------------------------------------------------------ EN industria
    dict(
        file="en/colegios.html", lang="en", img="colegios.webp",
        url="https://www.go-cleaning.com/en/colegios",
        list_id="tipos-de-centro", list_name="Types of educational facility we serve",
        service_type="School and educational facility cleaning",
        h1="School and campus cleaning", alt="Educational center",
        lead="Safe, healthy environments for students and teaching staff.",
        meta="What a school, college or university should ask of its cleaning provider: facility type, staffing, outsourcing and start-up. Panama.",
        svc_desc="Cleaning for schools, colleges and universities in Panama: what to require from a provider, how to contract and how the service starts.",
        cta_h2="Request an assessment for your school",
        cta_p="Tell us how many zones your school has and what its calendar looks like, and we will tell you how we would organize the service.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20cleaning%20assessment%20for%20my%20school",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "In an educational facility, biosafety protects the most vulnerable population and reassures families. Clean, sanitized environments help contain contagion and keep the school year running. A school with visible cleaning protocols does not just comply: it stands out to the families deciding where to enroll."),
            ("p20", 'If you run a school, a college or a university, this is what is worth knowing before you contract cleaning. What is cleaned in each zone, with which products and on what schedule is explained at <a href="limpieza-centros-educativos">cleaning for schools and educational centers</a>.'),

            ("h2", "How does the type of educational facility change what you need?"),
            ("p", "A preschool and a university are not cleaned the same way, and what you contract changes with the age of the students and the size of the campus."),
            ("h3", "Preschools and daycare centers"),
            ("p", "Small children who crawl, eat on the floor and put objects in their mouths. They call for more floor and toy disinfection, very low-toxicity products and special attention to restrooms and changing areas."),
            ("h3", "Elementary and secondary schools"),
            ("p", "This is the bulk of the demand: classrooms, cafeteria, restrooms and sports areas with heavy traffic and tight schedules. What weighs most is finishing before classes begin and agreeing in the contract how restrooms are kept up during the school day."),
            ("h3", "Universities and institutes"),
            ("p", "Campuses with several buildings, laboratories, libraries and common areas, and schedules that vary by faculty and by shift. Here what counts is coordinating schedules building by building and being able to cover several shifts."),
            ("h3", "Training centers and academies"),
            ("p", "Training rooms and workshops with afternoon and evening classes. They need a service that adapts to when classes are held, rather than to a fixed school calendar."),

            ("h2", "What should a school ask of its cleaning provider?"),
            ("p", "With minors on the premises, some criteria weigh more than price:"),
            ("ul", [
                "Background checks for every staff member who enters the grounds, and staff on the formal payroll",
                "Low-toxicity products with a technical data sheet available",
                "Working hours outside the school day, defined in writing",
                "A fixed team assigned to the facility, so the staff are always the same people",
                "Checklists by zone and a report for each shift that administration can review",
                "A clear way to cover absences before classes begin",
            ]),
            ("p20", 'At Go Services staff are on the formal payroll and go through background checks, the biofriendly protocol is an included standard, and each facility has its own fixed team and auditable checklists. To carry these criteria into a comparison of proposals, there is a full guide to <a href="como-elegir-empresa-limpieza">how to choose a cleaning company</a>.'),

            ("h2", "Should a school outsource its cleaning or keep its own custodians?"),
            ("p", "A school can keep its own custodians for the day-to-day, and that works for upkeep during the school day. What tends to stretch a small team is deep cleaning, absence cover and cleaning during breaks, when more people are needed for a few days."),
            ("p20", 'A mixed model is possible: in-house custodians for the school day and a provider for deep cleaning and breaks. More on this model under <a href="outsourcing">staff outsourcing</a>.'),

            ("h2", "How does the service start in a school?"),
            ("p", "The best time is usually the break before classes begin, because it allows an initial deep clean without students on site. The sequence is:"),
            ("ul", [
                "A walk-through of the grounds and a map of the zones: classrooms, restrooms, cafeteria and sports areas",
                "Checklists, products and schedules defined together with administration",
                "An initial deep clean during a break, where possible",
                "Assignment of the fixed team and a start with a report for each shift",
            ]),
            ("todo", "confirm with the client that this start-up sequence reflects their real process; it is written as a general sequence."),

            ("h2", "How is the cleaning protocol communicated to families?"),
            ("p", "A cleaning protocol only sets a school apart if families know about it. Checklists and shift reports give administration concrete information to share with parents, instead of general promises."),
        ],
    ),
]
