# -*- coding: utf-8 -*-
"""Industrias embajadas y call-centers (ES y EN).

Cada una lleva preguntas propias del sector (no la plantilla de colegios/hospitales).

embajadas: tipos de espacio, acceso con la seguridad de la sede, verificacion y
confidencialidad (hechos publicados: verificacion de antecedentes, protocolos de
confidencialidad, planilla formal, Ley 81 de 2019), que se toca y que no, eventos.
Se retira "cero riesgo operativo y cero incidentes" (promesa absoluta), y el
"manejo ... de documentacion sensible" se reformula como regla de NO tocarla.

call-centers: tipos de operacion continua, sin interrumpir llamadas, headsets y
perifericos, turnos rotativos, fines de semana/feriados/ausencias. El "24/7" ya
esta publicado en el title y el menu; queda un TODO para confirmar la capacidad.
"""

WA = "https://wa.me/50769823165?text="

PAGES = [
    # ------------------------------------------------------------ ES embajadas
    dict(
        file="es/embajadas.html", lang="es", img="embajadas.webp",
        url="https://www.go-cleaning.com/es/embajadas",
        list_id="espacios", list_name="Espacios de una sede diplomática",
        service_type="Limpieza de embajadas y sedes diplomáticas",
        h1="Limpieza de embajadas y sedes diplomáticas", alt="Sede diplomática",
        lead="Servicio discreto para entornos donde la confianza es requisito de acceso.",
        meta="Limpieza para embajadas y sedes diplomáticas en Panamá: acceso coordinado con la seguridad, verificación de antecedentes, confidencialidad y salones protocolares.",
        svc_desc="Limpieza para embajadas y sedes diplomáticas en Panamá: acceso coordinado con la seguridad, verificación de antecedentes, confidencialidad y salones protocolares.",
        cta_h2="Solicita una evaluación para tu sede",
        cta_p="Cuéntanos qué espacios tiene la sede y cómo funciona su acceso, y proponemos un esquema coordinado con la seguridad de tu recinto.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20para%20una%20sede%20diplomatica",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "Una embajada o sede diplomática no contrata limpieza: contrata personas que van a estar dentro de sus instalaciones. El criterio de elección no es el precio, sino la confianza: quién entra, bajo qué reglas y con qué registro. Y el trabajo debe hacerse sin alterar la rutina de un entorno de alta sensibilidad."),
            ("p20", 'Esta página trata de lo propio de una sede diplomática. El programa diario de limpieza de oficinas, con zonas y reportería, está en <a href="limpieza-corporativa">limpieza corporativa</a>.'),

            ("h2", "¿Qué tipos de espacio tiene una sede diplomática y cómo cambia la limpieza?"),
            ("p", "Una sede diplomática reúne espacios con usos y niveles de reserva muy distintos, y cada uno se limpia con su propio criterio."),
            ("h3", "Cancillería y oficinas"),
            ("p", "Es donde se trabaja a diario, con escritorios, equipos y documentos. Se limpia con el criterio de no mover ni abrir nada, y en los horarios que defina la seguridad interna de la sede."),
            ("h3", "Salones protocolares y de recepciones"),
            ("p", "Son espacios de representación, donde la presentación es parte del trabajo diplomático. Piden atención al detalle en pisos, vidrios y mobiliario, y una limpieza programada alrededor del calendario de eventos."),
            ("h3", "Residencias oficiales"),
            ("p", "Combinan áreas de representación con áreas de vida privada. El trabajo se acuerda por zonas y horarios con quien administra la residencia, y se respeta la privacidad de quienes viven allí."),
            ("h3", "Áreas restringidas y de seguridad"),
            ("p", "Son zonas a las que no entra cualquiera, ni siquiera dentro de la sede. Se limpian solo cuando y como lo autorice la seguridad, con el acompañamiento de personal de la sede si así se define."),

            ("h2", "¿Cómo se coordina el acceso del personal con la seguridad de la sede?"),
            ("p", "Antes de empezar, la seguridad de la sede define quién puede entrar, por dónde, en qué horario y con qué registro. Lo habitual es trabajar con una lista previa de personal autorizado y con horarios coordinados con la seguridad interna del recinto."),
            ("p", "Con equipos fijos por instalación, esa lista no cambia cada semana. Conviene acordar que cualquier sustitución se avise por adelantado, para que la seguridad la autorice antes de que la persona llegue."),

            ("h2", "¿Qué verificación y qué compromiso de confidencialidad tiene el personal?"),
            ("p", "El personal de Go Services pasa verificación de antecedentes y opera bajo protocolos de confidencialidad. Está en planilla formal, lo que permite que cada persona esté identificada y responda ante un empleador."),
            ("p", "Conviene que el contrato formalice esos compromisos por escrito. Los datos del cliente se tratan conforme a la Ley 81 de 2019 de Protección de Datos Personales de Panamá."),

            ("h2", "¿Qué se hace con los documentos y los equipos que están a la vista?"),
            ("p", "La regla es no tocar lo que no es de limpieza. No se abren cajones ni carpetas, no se mueven documentos y no se manipulan equipos, y las superficies con papeles o dispositivos se limpian alrededor o se dejan para que las despeje su responsable."),
            ("p", "Las áreas donde hay material reservado se acuerdan caso por caso con la seguridad de la sede: si se limpian, cuándo y con quién presente."),
            ("todo", 'confirmar con el cliente el protocolo real. La pagina anterior decia "manejo discreto de areas restringidas y documentacion sensible" y "personal capacitado en entornos de alta seguridad"; hoy se describe solo como criterio general de no tocar.'),

            ("h2", "¿Cómo se prepara la limpieza antes de una recepción o un evento?"),
            ("p", "Los eventos concentran la exigencia: el salón tiene que estar impecable a una hora exacta, y después hay que devolver el espacio a su estado normal. La limpieza profunda se programa alrededor del calendario de eventos de la sede y se coordina con el equipo de protocolo."),
            ("p20", 'Los pisos y la tapicería de los salones suelen pedir tratamientos específicos según el material. Para eso, ver <a href="cuidado-pisos">cuidado de pisos</a> y <a href="alfombras-muebles">alfombras y muebles</a>.'),
        ],
    ),

    # ------------------------------------------------------------ ES call-centers
    dict(
        file="es/call-centers.html", lang="es", img="call-center.webp",
        url="https://www.go-cleaning.com/es/call-centers",
        list_id="operaciones", list_name="Tipos de operación continua que atendemos",
        service_type="Limpieza de call centers y operaciones continuas",
        h1="Limpieza de call centers y operaciones 24/7", alt="Call center",
        lead="Limpieza continua que no interrumpe la operación ni la concentración.",
        meta="Limpieza para call centers y operaciones continuas en Panamá: turnos que no interrumpen llamadas, headsets y periféricos, relevo entre turnos y salas técnicas.",
        svc_desc="Limpieza para call centers y operaciones continuas en Panamá: turnos que no interrumpen llamadas, headsets y periféricos compartidos, relevo entre turnos y salas técnicas.",
        cta_h2="Solicita una evaluación para tu operación",
        cta_p="Cuéntanos cómo son tus turnos y cuántas estaciones o salas tiene el piso, y diseñamos un esquema de limpieza que no interrumpa.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20para%20mi%20call%20center",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "Un call center opera en turnos rotativos, con personal en estaciones fijas durante horas. El ambiente se degrada rápido: auriculares compartidos, escritorios en uso constante, áreas de descanso con alta rotación. La limpieza tiene que ocurrir en paralelo a la operación, sin ruido excesivo, sin químicos de olor fuerte y sin interrumpir llamadas activas."),
            ("p20", 'Esta página trata de lo propio de las operaciones continuas. El programa diario de oficinas, con zonas, frecuencias y reportería, está en <a href="limpieza-corporativa">limpieza corporativa</a>.'),

            ("h2", "¿Cómo cambia la limpieza según el tipo de operación continua?"),
            ("p", "Una operación que nunca cierra no se limpia igual en todas sus áreas."),
            ("h3", "Piso de producción del call center"),
            ("p", "Filas de estaciones ocupadas durante horas, con equipos, auriculares y mucho contacto con las superficies. Se limpia por bloques cortos, sin retirar a nadie de su puesto, y con productos de olor suave."),
            ("h3", "Centros de datos y salas NOC"),
            ("p", "Son salas técnicas con acceso limitado y equipos sensibles. Qué zonas se tocan, con qué productos y con quién presente se define con el cliente antes de empezar, y no se usan líquidos cerca de los equipos."),
            ("h3", "Back office y centros de servicios compartidos"),
            ("p", "Operaciones administrativas con turnos más estables, donde la limpieza se parece a la de una oficina grande y se puede programar por zonas y horarios."),
            ("h3", "Áreas de descanso, cocinas y baños de alta rotación"),
            ("p", "Son los puntos donde se concentra el desgaste: en una operación de turnos rotativos nunca hay un momento sin uso. Se atienden con mayor frecuencia y por rondas."),

            ("h2", "¿Cómo se limpia sin interrumpir llamadas ni la concentración?"),
            ("p", "Con bajo ruido, productos sin olor fuerte y trabajo por bloques cortos, de modo que ninguna zona se interviene durante mucho tiempo. La ronda se coordina con los supervisores del piso para evitar los picos de llamadas."),
            ("p", "Si el cliente lo pide, la limpieza de las estaciones se hace entre turnos, cuando la estación queda libre unos minutos, en lugar de con el agente presente."),

            ("h2", "¿Cómo se sanitizan los headsets y los periféricos compartidos?"),
            ("p", "Las estaciones compartidas, con auriculares, teclados, ratones y teléfonos, son el punto de más contacto del piso. El criterio es sanitizar entre un turno y el siguiente, con productos compatibles con equipos electrónicos y sin rociar sobre ellos, usando paños apenas húmedos."),
            ("p", "Las almohadillas y otros accesorios de uso personal dependen de la política de cada operación, y conviene definir por escrito qué se sanitiza en sitio y qué se reemplaza."),
            ("todo", "confirmar con el cliente los procedimientos exactos para headsets y perifericos (productos, paños, momento de la sanitizacion) antes de afirmarlos como protocolo propio; hoy se describen como criterio general."),

            ("h2", "¿Cómo se coordina la limpieza con los turnos rotativos del cliente?"),
            ("p", "La limpieza se organiza alrededor de los turnos del cliente: cada equipo de limpieza conoce el horario de relevo de la operación y evita intervenir justo en el cambio. Con equipos fijos por instalación, el personal conoce el piso, los horarios y los puntos críticos."),
            ("p", "Cada turno deja un reporte de lo ejecutado, de modo que el supervisor del cliente puede ver qué se hizo en su turno sin tener que acompañar al equipo."),

            ("h2", "¿Cómo se cubren los fines de semana, los feriados y las ausencias?"),
            ("p", "Una operación continua no cierra en feriados, así que el calendario de limpieza se acuerda para todos los días del año. Las ausencias y los reemplazos se gestionan desde <a href=\"outsourcing\">outsourcing de personal</a>, para que el turno no quede sin cubrir."),
            ("todo", "confirmar con el cliente la capacidad real de cobertura 24/7 y feriados; el title y el menu ya la prometen, y la frase del cierre anterior (capacidad operativa para cubrir turnos 24/7) se retiro hasta confirmarla."),
        ],
    ),

    # ------------------------------------------------------------ EN embajadas
    dict(
        file="en/embajadas.html", lang="en", img="embajadas.webp",
        url="https://www.go-cleaning.com/en/embajadas",
        list_id="espacios", list_name="Spaces in a diplomatic mission",
        service_type="Embassy and diplomatic mission cleaning",
        h1="Embassy and diplomatic mission cleaning", alt="Diplomatic building",
        lead="Discreet service for environments where trust is a condition of access.",
        meta="Cleaning for embassies and diplomatic missions in Panama: access coordinated with security, background checks, confidentiality and protocol halls.",
        svc_desc="Cleaning for embassies and diplomatic missions in Panama: access coordinated with security, background checks, confidentiality and protocol halls.",
        cta_h2="Request an assessment for your mission",
        cta_p="Tell us which spaces the mission has and how access works, and we will propose an arrangement coordinated with your premises' security.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20cleaning%20assessment%20for%20a%20diplomatic%20mission",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "An embassy or diplomatic mission does not hire cleaning: it hires the people who will be inside its premises. The choice is not about price but about trust: who comes in, under what rules and with what record. And the work has to be done without disturbing the routine of a high-sensitivity environment."),
            ("p20", 'This page is about what is specific to a diplomatic mission. The daily office cleaning program, with zones and reporting, is at <a href="limpieza-corporativa">corporate cleaning</a>.'),

            ("h2", "What types of space does a diplomatic mission have, and how does cleaning change?"),
            ("p", "A diplomatic mission brings together spaces with very different uses and levels of confidentiality, and each is cleaned by its own criteria."),
            ("h3", "Chancery and offices"),
            ("p", "This is where daily work happens, with desks, equipment and documents. It is cleaned on the principle of moving or opening nothing, and during the hours set by the mission's internal security."),
            ("h3", "Protocol halls and reception rooms"),
            ("p", "These are representation spaces, where presentation is part of diplomatic work. They call for attention to detail in floors, glass and furniture, and cleaning scheduled around the events calendar."),
            ("h3", "Official residences"),
            ("p", "They combine representation areas with private living areas. The work is agreed zone by zone and hour by hour with whoever manages the residence, and the privacy of the people who live there is respected."),
            ("h3", "Restricted and secure areas"),
            ("p", "These are zones that not everyone can enter, even inside the mission. They are cleaned only when and how security authorizes, with staff from the mission accompanying if so defined."),

            ("h2", "How is staff access coordinated with the mission's security?"),
            ("p", "Before starting, the mission's security defines who may enter, through where, at what hours and with what record. The usual arrangement is a prior list of authorized staff and schedules coordinated with the premises' internal security."),
            ("p", "With fixed teams for each site, that list does not change every week. It is worth agreeing that any substitution is notified in advance, so security can authorize it before the person arrives."),

            ("h2", "What vetting and confidentiality commitment does the staff have?"),
            ("p", "Go Services staff go through background checks and work under confidentiality protocols. They are on the formal payroll, so each person is identified and answers to an employer."),
            ("p", "It is worth having the contract formalize those commitments in writing. Client data is handled under Panama's Law 81 of 2019 on Personal Data Protection."),

            ("h2", "What happens with documents and equipment left in view?"),
            ("p", "The rule is not to touch what is not part of cleaning. Drawers and folders are not opened, documents are not moved and equipment is not handled, and surfaces with papers or devices are cleaned around or left for their owner to clear."),
            ("p", "Areas holding reserved material are agreed case by case with the mission's security: whether they are cleaned, when, and with whom present."),
            ("todo", 'confirm with the client the real protocol. The previous page said "discreet handling of restricted areas and sensitive documentation" and "staff trained for high-security environments"; for now it is described only as a general do-not-touch principle.'),

            ("h2", "How is cleaning prepared before a reception or an event?"),
            ("p", "Events concentrate the demands: the hall has to be spotless at an exact hour, and afterward the space has to be returned to its normal state. Deep cleaning is scheduled around the mission's events calendar and coordinated with the protocol team."),
            ("p20", 'Floors and upholstery in the halls often call for specific treatments depending on the material. For that, see <a href="cuidado-pisos">floor care</a> and <a href="alfombras-muebles">carpets and furniture</a>.'),
        ],
    ),

    # ------------------------------------------------------------ EN call-centers
    dict(
        file="en/call-centers.html", lang="en", img="call-center.webp",
        url="https://www.go-cleaning.com/en/call-centers",
        list_id="operaciones", list_name="Types of continuous operation we serve",
        service_type="Call center and continuous operation cleaning",
        h1="Call center and 24/7 operation cleaning", alt="Call center",
        lead="Continuous cleaning that interrupts neither the operation nor the focus.",
        meta="Cleaning for call centers and continuous operations in Panama: shifts that do not interrupt calls, headsets and shared peripherals, shift handover and technical rooms.",
        svc_desc="Cleaning for call centers and continuous operations in Panama: shifts that do not interrupt calls, headsets and shared peripherals, shift handover and technical rooms.",
        cta_h2="Request an assessment for your operation",
        cta_p="Tell us what your shifts look like and how many stations or rooms the floor has, and we will design a cleaning arrangement that does not interrupt.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20cleaning%20assessment%20for%20my%20call%20center",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "A call center runs on rotating shifts, with staff at fixed stations for hours. The environment degrades fast: shared headsets, desks in constant use, high-turnover break areas. Cleaning has to happen in parallel with the operation, without excessive noise, without strong-smelling chemicals and without interrupting live calls."),
            ("p20", 'This page is about what is specific to continuous operations. The daily office program, with zones, frequencies and reporting, is at <a href="limpieza-corporativa">corporate cleaning</a>.'),

            ("h2", "How does cleaning change by type of continuous operation?"),
            ("p", "An operation that never closes is not cleaned the same way in every area."),
            ("h3", "The call center floor"),
            ("p", "Rows of stations occupied for hours, with equipment, headsets and plenty of contact with surfaces. It is cleaned in short blocks, without pulling anyone from their seat, and with mild-smelling products."),
            ("h3", "Data centers and NOC rooms"),
            ("p", "These are technical rooms with limited access and sensitive equipment. Which zones are touched, with which products and with whom present is agreed with the client before starting, and no liquids are used near the equipment."),
            ("h3", "Back office and shared service centers"),
            ("p", "Administrative operations with steadier shifts, where cleaning resembles that of a large office and can be scheduled by zone and hour."),
            ("h3", "Break areas, kitchens and high-turnover restrooms"),
            ("p", "These are where wear concentrates: in a rotating-shift operation there is never a moment without use. They are attended more often and in rounds."),

            ("h2", "How is cleaning done without interrupting calls or focus?"),
            ("p", "With low noise, products without strong odors and work in short blocks, so no zone is worked on for long. The round is coordinated with floor supervisors to avoid call peaks."),
            ("p", "If the client asks, station cleaning is done between shifts, when the station is free for a few minutes, rather than with the agent present."),

            ("h2", "How are headsets and shared peripherals sanitized?"),
            ("p", "Shared stations, with headsets, keyboards, mice and phones, are the point of most contact on the floor. The working rule is to sanitize between one shift and the next, with products compatible with electronic equipment and without spraying onto it, using barely damp cloths."),
            ("p", "Ear cushions and other personal-use accessories depend on each operation's policy, and it is worth setting out in writing what is sanitized on site and what is replaced."),
            ("todo", "confirm with the client the exact procedures for headsets and peripherals (products, cloths, timing of sanitizing) before stating them as the company's own protocol; for now they are described as general practice."),

            ("h2", "How is cleaning coordinated with the client's rotating shifts?"),
            ("p", "Cleaning is organized around the client's shifts: each cleaning team knows the operation's handover time and avoids working right at the change. With fixed teams for each site, staff know the floor, the schedules and the critical points."),
            ("p", "Each shift leaves a report of what was carried out, so the client's supervisor can see what was done on their shift without having to accompany the team."),

            ("h2", "How are weekends, holidays and absences covered?"),
            ("p", "A continuous operation does not close on holidays, so the cleaning calendar is agreed for every day of the year. Absences and replacements are handled through <a href=\"outsourcing\">staff outsourcing</a>, so a shift is not left uncovered."),
            ("todo", "confirm with the client the real 24/7 and holiday coverage capacity; the title and the menu already promise it, and the previous closing line (operational capacity to cover 24/7 shifts) was removed until it is confirmed."),
        ],
    ),
]
