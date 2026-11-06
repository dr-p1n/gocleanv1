# -*- coding: utf-8 -*-
"""Contenido del par limpieza-hospitalaria (servicio) / hospitales (industria).

Regla de diferenciacion:
  SERVICIO  -> que se hace y como: protocolo por area, desinfeccion terminal,
               limpiar/desinfectar/esterilizar, residuos, registro.
  INDUSTRIA -> que necesita el comprador: tipo de centro, que exigir al
               proveedor, tercerizar o no, como arranca, y puente al servicio.
Ninguna cifra, tarifa, SLA, cliente ni norma citada por nombre.
"""

WA = "https://wa.me/50769823165?text="

PAGES = [
    # ------------------------------------------------------------ ES servicio
    dict(
        file="es/limpieza-hospitalaria.html", lang="es", img="hospital.webp",
        url="https://www.go-cleaning.com/es/limpieza-hospitalaria",
        list_id="protocolos", list_name="Protocolos de limpieza hospitalaria por tipo de área",
        service_type="Limpieza Hospitalaria",
        h1="Limpieza hospitalaria y bioseguridad clínica", alt="Limpieza hospitalaria",
        lead="El protocolo de limpieza hospitalaria, área por área: qué se hace, cómo y con qué registro.",
        meta="Protocolos de limpieza hospitalaria por tipo de área: desinfección terminal, residuos bioinfecciosos y registro de cada intervención. Panamá.",
        svc_desc="Limpieza hospitalaria con protocolos por tipo de área, desinfección terminal y manejo de residuos bioinfecciosos. ISO 9001, ISSA, GBAC.",
        cta_h2="Solicita una evaluación de tus áreas",
        cta_p="La clasificación de áreas y el protocolo correcto se definen recorriendo las instalaciones. Cuéntanos qué tipo de centro es y qué áreas tiene, y evaluamos cómo organizar el servicio.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20hospitalaria",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "La limpieza hospitalaria tiene reglas que la limpieza comercial no contempla: el protocolo cambia según el riesgo de cada área, se trabaja de lo menos contaminado a lo más contaminado y cada intervención deja un registro. Esta página explica cómo se organiza ese trabajo."),
            ("p20", 'Go Services opera como extensión del equipo clínico, con personal entrenado en bioseguridad hospitalaria y documentación lista para auditoría. Si administras un centro de salud y lo que necesitas es decidir cómo contratar este servicio, esa guía está en <a href="hospitales">limpieza para hospitales y centros de salud</a>.'),

            ("h2", "¿Qué incluye la limpieza hospitalaria en cada tipo de área?"),
            ("p", "El nivel de riesgo de cada área define el producto, la frecuencia y el equipo. Estas son las cuatro situaciones que más cambian el protocolo."),
            ("h3", "Áreas críticas"),
            ("p", "Quirófanos, unidades de cuidados intensivos y salas de emergencia, donde el paciente es más vulnerable a una infección. El criterio es limpiar de las superficies menos contaminadas a las más contaminadas, con el piso al final, usar paños y utensilios exclusivos del área y desinfectar con rigor los puntos de contacto frecuente: barandas, equipos fijos, interruptores y manijas."),
            ("h3", "Áreas semicríticas"),
            ("p", "Habitaciones de hospitalización, consultorios, laboratorios y áreas de imagenología. Combinan la limpieza concurrente diaria con la desinfección de las superficies que más se tocan: mesas de cama, timbres, camillas y manijas. El riesgo es moderado, y es la frecuencia de paso lo que lo mantiene así."),
            ("h3", "Áreas no críticas"),
            ("p", "Pasillos, salas de espera, oficinas administrativas y áreas de servicio. Rige la limpieza de mantenimiento habitual, con atención a los puntos de contacto de las salas de espera, donde circulan pacientes y acompañantes durante todo el día."),
            ("h3", "Habitaciones de aislamiento"),
            ("p", "Pacientes con enfermedades que se transmiten por contacto, gotas o aire. El criterio es limpiarlas al final del recorrido para no arrastrar contaminación al resto de áreas, con el equipo de protección personal que indique el tipo de aislamiento y con utensilios que no salen de la habitación."),
            ("todo", "confirmar con el cliente los procedimientos exactos por area (orden de limpieza, utensilios exclusivos, EPP) antes de afirmarlos como protocolo propio; hoy se describen como criterio hospitalario general."),

            ("h2", "¿Qué es la desinfección terminal y cuándo se hace?"),
            ("p", "Es la limpieza y desinfección completa de una habitación o área cuando el paciente se va, ya sea por alta o por traslado, y antes de recibir al siguiente. Cubre mobiliario, superficies de contacto frecuente, equipos fijos, baño y piso, y se hace una vez retirados la ropa de cama y los residuos."),
            ("p", "Se distingue de la desinfección concurrente, que se hace a diario con el paciente en la habitación. Tras un paciente en aislamiento, la desinfección terminal es más exigente, porque la habitación no puede reutilizarse hasta quedar liberada."),

            ("h2", "¿Cuál es la diferencia entre limpiar, desinfectar y esterilizar?"),
            ("p", "Los tres términos se usan como sinónimos, y son procesos distintos:"),
            ("ul", [
                "<strong>Limpiar.</strong> Retira la suciedad y la materia orgánica de la superficie. Es el paso previo: un desinfectante no actúa bien sobre una superficie sucia.",
                "<strong>Desinfectar.</strong> Reduce los microorganismos de la superficie a un nivel seguro, con un producto aplicado durante el tiempo de contacto que indica su ficha técnica.",
                "<strong>Esterilizar.</strong> Elimina toda forma de vida microbiana, incluidas las esporas. Se hace sobre instrumental en la central de esterilización del hospital, no sobre pisos ni superficies.",
            ]),
            ("p20", "La limpieza de superficies llega hasta la desinfección. Si una propuesta ofrece “esterilizar” un área, conviene preguntar qué quiere decir exactamente."),

            ("h2", "¿Cómo se manejan los residuos bioinfecciosos?"),
            ("p", "Se separan en el punto donde se generan: los residuos bioinfecciosos en bolsa roja y los objetos cortopunzantes en contenedor rígido. Nunca se mezclan con los residuos comunes, y se retiran por la ruta interna que define cada centro, con el personal usando el equipo de protección que corresponde."),
            ("p", "El destino final de estos residuos corresponde a un operador autorizado, conforme a la normativa sanitaria vigente."),
            ("todo", "confirmar con el cliente el alcance exacto (segregacion, ruta interna, transporte, disposicion final) y que norma del MINSA se puede citar por nombre. La version anterior afirmaba cumplimiento de la normativa MINSA sin citar ninguna."),

            ("h2", "¿Qué documentación queda de cada intervención?"),
            ("p", "Cada intervención se registra con la hora, la zona, el producto aplicado y el responsable. Esos registros se organizan en checklists por área y en un reporte por turno, de modo que una auditoría, interna o del Ministerio de Salud, pueda reconstruir qué se hizo, dónde y quién lo hizo."),
            ("p20", 'Esa trazabilidad es lo que distingue la limpieza hospitalaria de la comercial. También es lo que permite comparar propuestas: si un proveedor no puede mostrar cómo registra cada intervención, el protocolo existe solo en el papel. Para la desinfección fuera del entorno clínico, ver <a href="desinfeccion-sanitizacion">desinfección y sanitización</a>.'),
        ],
    ),

    # ------------------------------------------------------------ ES industria
    dict(
        file="es/hospitales.html", lang="es", img="hospital.webp",
        url="https://www.go-cleaning.com/es/hospitales",
        list_id="tipos-de-centro", list_name="Tipos de centro de salud que atendemos",
        service_type="Limpieza de hospitales y centros de salud",
        h1="Limpieza de hospitales y centros de salud", alt="Centro de salud",
        lead="Donde la limpieza es parte del protocolo médico, no un servicio auxiliar.",
        meta="Qué debe pedir un hospital, clínica o centro de salud a su proveedor de limpieza: tipo de centro, contratación, personal y puesta en marcha. Panamá.",
        svc_desc="Limpieza para hospitales, clínicas, laboratorios y centros de salud en Panamá: qué exigir al proveedor, cómo contratar y cómo se inicia el servicio.",
        cta_h2="Solicita una evaluación para tu centro",
        cta_p="Cuéntanos qué tipo de centro es, cuántas áreas tiene y en qué turnos opera, y evaluamos cómo estructurar el servicio.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20para%20mi%20centro%20de%20salud",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "En un hospital, una superficie mal desinfectada puede convertirse en un vector de infección intrahospitalaria. La limpieza clínica no es estética, es epidemiológica. Los centros de salud enfrentan auditorías del Ministerio de Salud, acreditaciones y la responsabilidad directa de proteger a pacientes inmunocomprometidos."),
            ("p20", 'Esta página es para quien administra un centro de salud y tiene que decidir cómo contratar la limpieza. El detalle técnico de los protocolos, con áreas, desinfección terminal y residuos, está en <a href="limpieza-hospitalaria">limpieza hospitalaria y bioseguridad clínica</a>.'),

            ("h2", "¿Qué cambia según el tipo de centro de salud?"),
            ("p", "No todos los centros tienen el mismo riesgo ni el mismo ritmo, y lo que se contrata cambia con ellos."),
            ("h3", "Hospitales y clínicas con hospitalización"),
            ("p", "Tienen áreas críticas, habitaciones que rotan con cada alta y residuos bioinfecciosos todos los días. La limpieza es continua y por turnos, y lo que más pesa al contratar es la desinfección terminal y la trazabilidad de cada intervención."),
            ("h3", "Policlínicas y centros de salud ambulatorios"),
            ("p", "Atienden mucho volumen de pacientes en poco tiempo, sobre todo en salas de espera y consultorios. El foco está en las superficies de contacto frecuente y en limpiar entre consultas sin frenar la atención."),
            ("h3", "Laboratorios y centros de diagnóstico"),
            ("p", "Manejan muestras y, según el área, equipos sensibles. El personal necesita saber qué zonas se limpian y qué equipos no se tocan, y cómo se gestionan los residuos biológicos de la toma de muestras."),
            ("h3", "Consultorios y clínicas especializadas"),
            ("p", "Espacios más pequeños, con una o pocas salas de procedimiento, como odontología o dermatología. Necesitan un protocolo claro por sala y una frecuencia pactada, sin la estructura de un hospital."),

            ("h2", "¿Qué debe pedir un centro de salud a su proveedor de limpieza?"),
            ("p", "Más allá del precio, estos son los criterios que separan a un proveedor preparado para un entorno clínico de uno que solo limpia:"),
            ("ul", [
                "Personal en planilla formal y con verificación de antecedentes",
                "Capacitación en bioseguridad y en uso de equipo de protección personal",
                "Un plan por áreas según el nivel de riesgo, no un servicio uniforme para todo el centro",
                "Registro de cada intervención y reporte por turno que el centro pueda auditar",
                "Un equipo fijo asignado a la instalación y supervisión en sitio",
                "Una forma clara de cubrir las ausencias sin dejar un área sin atender",
                "Productos con ficha técnica disponible",
            ]),
            ("p20", 'Go Services trabaja con personal en planilla formal y verificación de antecedentes, equipos fijos por instalación y checklists auditables con reportería por turno. La guía de <a href="como-elegir-empresa-limpieza">cómo elegir una empresa de limpieza</a> amplía estos criterios para comparar propuestas.'),

            ("h2", "¿Conviene tercerizar la limpieza de un hospital o tener personal propio?"),
            ("p", "Depende de la capacidad del centro para contratar, capacitar, supervisar y reemplazar personal. Con personal propio, el centro controla directamente al equipo, pero asume también la capacitación continua, las ausencias y la supervisión."),
            ("p20", 'Con un proveedor, esa gestión se traslada y el centro conserva el control por contrato: exige protocolos, registros y supervisión. También es posible combinar ambos modelos, con personal propio en las áreas más sensibles y un proveedor en el resto. El detalle de cómo funciona está en <a href="outsourcing">outsourcing de personal</a>.'),

            ("h2", "¿Cómo se inicia el servicio en un centro de salud?"),
            ("p", "El arranque sigue una secuencia, para que el protocolo exista antes del primer turno:"),
            ("ul", [
                "Recorrido de las instalaciones y clasificación de las áreas por nivel de riesgo",
                "Definición del protocolo, los checklists y la frecuencia de cada área, junto con la dirección del centro",
                "Asignación del equipo fijo de la instalación",
                "Inicio con supervisión y primer reporte por turno",
            ]),
            ("todo", "confirmar con el cliente que esta secuencia de arranque refleja su proceso real; esta redactada como secuencia general."),

            ("h2", "¿Es lo mismo la limpieza hospitalaria que la limpieza de un centro de salud?"),
            ("p", "Comparten la base: desinfección según el nivel de riesgo, manejo de residuos y registro de lo hecho. Pero responden a preguntas distintas."),
            ("p20", 'La limpieza hospitalaria es el servicio técnico: protocolos por área, desinfección terminal y residuos, que se detalla en <a href="limpieza-hospitalaria">limpieza hospitalaria y bioseguridad clínica</a>. La limpieza de un centro de salud es la decisión del cliente: qué tipo de centro es, qué riesgo tiene cada área y qué estructura de servicio necesita.'),
        ],
    ),

    # ------------------------------------------------------------ EN servicio
    dict(
        file="en/limpieza-hospitalaria.html", lang="en", img="hospital.webp",
        url="https://www.go-cleaning.com/en/limpieza-hospitalaria",
        list_id="protocolos", list_name="Hospital cleaning protocols by type of area",
        service_type="Hospital Cleaning",
        h1="Hospital cleaning and clinical biosafety", alt="Hospital cleaning",
        lead="The hospital cleaning protocol, area by area: what is done, how, and what record it leaves.",
        meta="Hospital cleaning protocols by area type: terminal disinfection, bio-infectious waste handling and a record of every intervention. Panama.",
        svc_desc="Hospital cleaning with protocols by area type, terminal disinfection and bio-infectious waste handling. ISO 9001, ISSA, GBAC.",
        cta_h2="Request an assessment of your areas",
        cta_p="The area classification and the right protocol are defined by walking the facility. Tell us what type of facility you run and which areas it has, and we will assess how to organize the service.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20hospital%20cleaning%20assessment",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "Hospital cleaning has rules that commercial cleaning does not cover: the protocol changes with the risk level of each area, work runs from the least contaminated surface to the most contaminated, and every intervention leaves a record. This page explains how that work is organized."),
            ("p20", 'Go Services operates as an extension of the clinical team, with staff trained in hospital biosafety and documentation ready for audit. If you run a health facility and need to decide how to contract this service, that guide is at <a href="hospitales">hospital and healthcare cleaning</a>.'),

            ("h2", "What does hospital cleaning include in each type of area?"),
            ("p", "The risk level of each area sets the product, the frequency and the equipment. These are the four situations that change the protocol most."),
            ("h3", "Critical areas"),
            ("p", "Operating rooms, intensive care units and emergency rooms, where the patient is most vulnerable to infection. The working rule is to clean from the least to the most contaminated surfaces, floor last, to use cloths and tools dedicated to the area, and to disinfect high-touch points with particular care: bed rails, fixed equipment, switches and handles."),
            ("h3", "Semi-critical areas"),
            ("p", "Inpatient rooms, consulting rooms, laboratories and imaging areas. They combine daily concurrent cleaning with disinfection of the surfaces touched most: bedside tables, call buttons, stretchers and handles. Risk is moderate here, and it is the frequency of the rounds that keeps it that way."),
            ("h3", "Non-critical areas"),
            ("p", "Corridors, waiting rooms, administrative offices and service areas. Routine maintenance cleaning applies, with attention to touch points in waiting rooms, where patients and companions pass through all day."),
            ("h3", "Isolation rooms"),
            ("p", "Rooms for patients with diseases transmitted by contact, droplets or air. The rule is to clean them at the end of the round so contamination is not carried into other areas, with the protective equipment the type of isolation calls for and with tools that never leave the room."),
            ("todo", "confirm with the client the exact procedures per area (cleaning order, dedicated tools, PPE) before stating them as the company's own protocol; for now they are described as general hospital practice."),

            ("h2", "What is terminal disinfection and when is it done?"),
            ("p", "It is the full cleaning and disinfection of a room or area once the patient leaves, whether by discharge or transfer, and before the next one arrives. It covers furniture, high-touch surfaces, fixed equipment, bathroom and floor, and is done once bedding and waste have been removed."),
            ("p", "It differs from concurrent disinfection, which is done daily with the patient in the room. After an isolation patient, terminal disinfection is more demanding, because the room cannot be reused until it has been released."),

            ("h2", "What is the difference between cleaning, disinfecting and sterilizing?"),
            ("p", "The three terms are often used interchangeably, and they are different processes:"),
            ("ul", [
                "<strong>Cleaning.</strong> Removes dirt and organic matter from the surface. It comes first: a disinfectant does not work well on a dirty surface.",
                "<strong>Disinfecting.</strong> Reduces microorganisms on the surface to a safe level, using a product applied for the contact time stated on its technical data sheet.",
                "<strong>Sterilizing.</strong> Destroys all microbial life, spores included. It is done on instruments in the hospital's sterilization department, not on floors or surfaces.",
            ]),
            ("p20", "Surface cleaning goes as far as disinfection. If a proposal offers to “sterilize” an area, ask what exactly it means."),

            ("h2", "How is bio-infectious waste handled?"),
            ("p", "It is separated at the point where it is generated: bio-infectious waste goes into red bags and sharps into rigid containers. It is never mixed with general waste, and it is removed along the internal route each facility defines, with staff wearing the protective equipment required."),
            ("p", "Final disposal falls to an authorized operator, under the health regulations in force."),
            ("todo", "confirm with the client the exact scope (segregation, internal route, transport, final disposal) and which MINSA regulation can be cited by name. The previous version claimed MINSA compliance without citing any."),

            ("h2", "What documentation is left after each intervention?"),
            ("p", "Each intervention is logged with the time, the zone, the product applied and the person responsible. Those records are organized into checklists by area and a report for each shift, so that an audit, internal or by the Ministry of Health, can reconstruct what was done, where and by whom."),
            ("p20", 'That traceability is what separates hospital cleaning from commercial cleaning. It is also what lets you compare proposals: if a provider cannot show how it records each intervention, the protocol exists only on paper. For disinfection outside clinical settings, see <a href="desinfeccion-sanitizacion">disinfection and sanitization</a>.'),
        ],
    ),

    # ------------------------------------------------------------ EN industria
    dict(
        file="en/hospitales.html", lang="en", img="hospital.webp",
        url="https://www.go-cleaning.com/en/hospitales",
        list_id="tipos-de-centro", list_name="Types of health facility we serve",
        service_type="Hospital and healthcare facility cleaning",
        h1="Hospital and healthcare cleaning", alt="Healthcare facility",
        lead="Where cleaning is part of the medical protocol, not an auxiliary service.",
        meta="What a hospital, clinic or health center should ask of its cleaning provider: facility type, outsourcing, staffing and start-up. Panama.",
        svc_desc="Cleaning for hospitals, clinics, laboratories and health centers in Panama: what to require from a provider, how to contract and how the service starts.",
        cta_h2="Request an assessment for your facility",
        cta_p="Tell us what type of facility you run, how many areas it has and which shifts it operates, and we will assess how to structure the service.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20cleaning%20assessment%20for%20my%20health%20facility",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "In a hospital, a poorly disinfected surface can become a vector for hospital-acquired infection. Clinical cleaning is not aesthetic, it is epidemiological. Health facilities face Ministry of Health audits, accreditations and the direct responsibility of protecting immunocompromised patients."),
            ("p20", 'This page is for whoever runs a health facility and has to decide how to contract its cleaning. The technical detail of the protocols, with areas, terminal disinfection and waste, is at <a href="limpieza-hospitalaria">hospital cleaning and clinical biosafety</a>.'),

            ("h2", "How does the type of health facility change what you need?"),
            ("p", "Facilities do not share the same risk or the same pace, and what you contract changes with them."),
            ("h3", "Hospitals and clinics with inpatient beds"),
            ("p", "They have critical areas, rooms that turn over with every discharge, and bio-infectious waste every day. Cleaning is continuous and runs in shifts, and what weighs most when contracting is terminal disinfection and the traceability of each intervention."),
            ("h3", "Polyclinics and outpatient health centers"),
            ("p", "They see a high volume of patients in a short time, above all in waiting rooms and consulting rooms. The focus is on high-touch surfaces and on cleaning between appointments without slowing care down."),
            ("h3", "Laboratories and diagnostic centers"),
            ("p", "They handle samples and, depending on the area, sensitive equipment. Staff need to know which zones are cleaned and which equipment is left alone, and how the biological waste from sample collection is managed."),
            ("h3", "Specialist clinics and consulting offices"),
            ("p", "Smaller spaces, with one or a few procedure rooms, such as dentistry or dermatology. They need a clear protocol for each room and an agreed frequency, without the structure of a hospital."),

            ("h2", "What should a health facility ask of its cleaning provider?"),
            ("p", "Beyond price, these are the criteria that separate a provider ready for a clinical setting from one that simply cleans:"),
            ("ul", [
                "Staff on the formal payroll, with background checks",
                "Training in biosafety and in the use of personal protective equipment",
                "A plan by area according to risk level, not one uniform service for the whole facility",
                "A record of every intervention and a report for each shift that the facility can audit",
                "A fixed team assigned to the site, with on-site supervision",
                "A clear way to cover absences without leaving an area unattended",
                "Products with a technical data sheet available",
            ]),
            ("p20", 'Go Services works with formal-payroll staff with background checks, fixed teams for each facility, and auditable checklists with a report for every shift. The guide to <a href="como-elegir-empresa-limpieza">how to choose a cleaning company</a> expands on these criteria for comparing proposals.'),

            ("h2", "Should a hospital outsource its cleaning or keep it in-house?"),
            ("p", "It depends on the facility's capacity to hire, train, supervise and replace staff. With in-house staff, the facility controls the team directly, but it also takes on ongoing training, absences and supervision."),
            ("p20", 'With a provider, that management shifts across and the facility keeps control through the contract: it requires protocols, records and supervision. It is also possible to combine both models, with in-house staff in the most sensitive areas and a provider for the rest. How this works is covered under <a href="outsourcing">staff outsourcing</a>.'),

            ("h2", "How does the service start in a health facility?"),
            ("p", "Start-up follows a sequence, so that the protocol exists before the first shift:"),
            ("ul", [
                "A walk-through of the site and classification of the areas by risk level",
                "A protocol, checklists and frequency for each area, defined together with the facility's management",
                "Assignment of the facility's fixed team",
                "A supervised start and the first shift report",
            ]),
            ("todo", "confirm with the client that this start-up sequence reflects their real process; it is written as a general sequence."),

            ("h2", "Is hospital cleaning the same as cleaning a health facility?"),
            ("p", "They share a base: disinfection according to risk level, waste handling and a record of what was done. But they answer different questions."),
            ("p20", 'Hospital cleaning is the technical service: protocols by area, terminal disinfection and waste, covered in <a href="limpieza-hospitalaria">hospital cleaning and clinical biosafety</a>. Cleaning a health facility is the client\'s decision: what type of facility it is, what risk each area carries and what service structure it needs.'),
        ],
    ),
]
