# -*- coding: utf-8 -*-
"""Industria puertos (ES y EN). Hermana de servicio: limpieza-industrial (no se toca).

Frontera: limpieza-industrial = plantas, desengrase, maquinaria. puertos = lo
propio de una terminal o parque logistico: zonas distintas, operacion que no se
detiene, acceso restringido, intemperie, residuos y sustancias.

Se retiran del texto original, por no tener fuente ni respaldo en los hechos
publicados: "retencion de carga, multas o perdida de contratos", "personal
certificado" y "operacion 24/7" (meta), y "cumplimiento de normativas sanitarias
de zona franca y autoridad maritima". Quedan TODOs para confirmarlos.
"""

WA = "https://wa.me/50769823165?text="

PAGES = [
    dict(
        file="es/puertos.html", lang="es", img="puertos.webp",
        url="https://www.go-cleaning.com/es/puertos",
        list_id="zonas", list_name="Zonas de una instalación portuaria o logística",
        service_type="Limpieza de puertos y zonas logísticas",
        h1="Limpieza de puertos y zonas logísticas", alt="Puerto y terminal logística",
        lead="Operaciones que no paran exigen limpieza que no falla.",
        meta="Limpieza para puertos, terminales y zonas logísticas en Panamá: operación continua, acceso restringido, clima y residuos. Equipos fijos y reporte por turno.",
        svc_desc="Limpieza para puertos, terminales y zonas logísticas en Panamá: operación continua, acceso restringido, intemperie y residuos.",
        cta_h2="Solicita una evaluación para tu instalación",
        cta_p="Háblanos de la instalación, sus zonas y sus turnos de operación, y preparamos una propuesta.",
        cta_href=WA + "Hola%2C%20quiero%20una%20evaluacion%20de%20limpieza%20para%20mi%20terminal%20o%20zona%20logistica",
        cta_btn="Solicitar una evaluación",
        blocks=[
            ("p20", "Un puerto o una zona logística opera bajo inspecciones y auditorías constantes, tanto de las autoridades como de las empresas que mueven su carga por ahí. Una falla de limpieza no es cosmética: afecta la operación y la confianza de quienes contratan. A la vez, la limpieza tiene que convivir con maquinaria pesada, tránsito de camiones y turnos continuos."),
            ("p20", 'Esta página trata de lo que es propio de un puerto o un parque logístico. El desengrase, la maquinaria y la limpieza de plantas de producción están en <a href="limpieza-industrial">limpieza industrial</a>.'),

            ("h2", "¿Cómo cambia la limpieza según la zona de una instalación logística?"),
            ("p", "Una terminal o un parque logístico mezcla áreas muy distintas, y cada una tiene su riesgo, su tránsito y su horario."),
            ("h3", "Patios, muelles y zonas de tránsito"),
            ("p", "Son áreas abiertas, de paso de camiones y maquinaria, donde se acumulan polvo, lodo y residuos de la carga. La limpieza se programa por tramos y en coordinación con operaciones, para no cruzarse con el movimiento de equipos."),
            ("h3", "Bodegas y centros de distribución"),
            ("p", 'Pisos de gran superficie, estanterías y zonas de carga y descarga. Lo que más pesa es mantener los pasillos y las zonas de despacho limpios y despejados sin detener el flujo. Las plagas son un riesgo propio de estas áreas, y su control se contrata aparte en <a href="fumigacion">fumigación</a>.'),
            ("h3", "Oficinas administrativas y áreas del personal"),
            ("p", 'Oficinas, comedores, vestidores y baños del personal, que operan por turnos y piden frecuencia más que complejidad. Se atienden como un programa diario, igual que en <a href="limpieza-corporativa">limpieza corporativa</a>.'),
            ("h3", "Garitas, accesos y zonas de inspección"),
            ("p", "Son los puntos por donde entra y sale todo, con mucho contacto entre personas y vehículos. Piden desinfección de las superficies de contacto y atención al piso, que recibe la mayor parte del tránsito."),

            ("h2", "¿Cómo se limpia en una operación que no se detiene?"),
            ("p", "Una instalación portuaria o logística opera por turnos, muchas veces de forma continua, así que no hay un momento en que esté vacía. La limpieza se organiza por zonas y por ventanas acordadas con operaciones, de modo que cada tramo se interviene cuando el movimiento lo permite."),
            ("p", "Los turnos de limpieza se diseñan según la operación de cada cliente, con rutas y horarios definidos por escrito y con la zona señalizada mientras se trabaja."),
            ("todo", "confirmar con el cliente si ofrece cobertura 24/7 en puertos (la meta anterior lo afirmaba) y como se coordinan las ventanas con operaciones; hoy se describe solo como criterio general."),

            ("h2", "¿Qué cambia en una zona de acceso restringido?"),
            ("p", "Una terminal tiene áreas donde solo entra personal acreditado. Quien limpia necesita credencial, rutas permitidas y, según la zona, registro de ingreso y salida. Eso convierte la rotación de personal en un problema logístico y no solo operativo."),
            ("p", "Con personal en planilla formal, verificación de antecedentes y equipos fijos por instalación, el grupo que se acredita una vez es el que sigue trabajando después."),

            ("h2", "¿Cómo afectan la intemperie y el clima a la limpieza?"),
            ("p", "En el clima tropical de Panamá, la lluvia, la humedad y, en instalaciones costeras, el salitre aceleran el deterioro de las superficies y arrastran lodo hacia el interior. La limpieza exterior se programa con ese ritmo en mente, y las entradas de bodegas y oficinas se refuerzan para que la suciedad no pase."),
            ("p20", 'Los pisos que se mojan con frecuencia necesitan además acabado antideslizante y señalización, porque un resbalón en un patio con maquinaria pesa más que en una oficina. Para el tratamiento de pisos de concreto, ver <a href="cuidado-pisos">cuidado de pisos</a>.'),

            ("h2", "¿Quién maneja los residuos industriales y las sustancias controladas?"),
            ("p", "Los residuos peligrosos y las sustancias controladas tienen su propio manejo en una instalación portuaria, a cargo del operador o de un gestor autorizado. La limpieza general no sustituye esa cadena."),
            ("p", "Por eso conviene definir por escrito qué residuos retira el servicio de limpieza y cuáles gestiona el operador, para que nada quede sin responsable."),
            ("todo", 'confirmar con el cliente el alcance real. La pagina anterior afirmaba "manejo de residuos industriales y sustancias controladas" y "cumplimiento de normativas sanitarias de zona franca y autoridad maritima" sin citar ninguna norma; si hay normas citables, indicarlas.'),
        ],
    ),
    dict(
        file="en/puertos.html", lang="en", img="puertos.webp",
        url="https://www.go-cleaning.com/en/puertos",
        list_id="zonas", list_name="Zones of a port or logistics facility",
        service_type="Port and logistics zone cleaning",
        h1="Port and logistics zone cleaning", alt="Port and logistics terminal",
        lead="Operations that never stop demand cleaning that never fails.",
        meta="Cleaning for ports, terminals and logistics zones in Panama: continuous operation, restricted access, weather and waste. Fixed teams and a report for every shift.",
        svc_desc="Cleaning for ports, terminals and logistics zones in Panama: continuous operation, restricted access, weather exposure and waste.",
        cta_h2="Request an assessment for your facility",
        cta_p="Tell us about the facility, its zones and its operating shifts, and we will prepare a proposal.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20cleaning%20assessment%20for%20my%20terminal%20or%20logistics%20zone",
        cta_btn="Request an assessment",
        blocks=[
            ("p20", "A port or logistics zone operates under constant inspections and audits, both from the authorities and from the companies that move their cargo through it. A cleaning failure is not cosmetic: it affects operations and the confidence of those who contract. At the same time, cleaning has to coexist with heavy machinery, truck traffic and continuous shifts."),
            ("p20", 'This page is about what is specific to a port or a logistics park. Degreasing, machinery and the cleaning of production plants are covered under <a href="limpieza-industrial">industrial cleaning</a>.'),

            ("h2", "How does cleaning change by zone in a logistics facility?"),
            ("p", "A terminal or logistics park mixes very different areas, and each has its own risk, traffic and schedule."),
            ("h3", "Yards, docks and transit zones"),
            ("p", "These are open areas, used by trucks and machinery, where dust, mud and cargo debris build up. Cleaning is scheduled section by section and in coordination with operations, so it does not cross paths with equipment movements."),
            ("h3", "Warehouses and distribution centers"),
            ("p", 'Large floor areas, racking, and loading and unloading zones. What weighs most is keeping aisles and dispatch zones clean and clear without stopping the flow. Pests are a risk specific to these areas, and pest control is contracted separately under <a href="fumigacion">fumigation</a>.'),
            ("h3", "Administrative offices and staff areas"),
            ("p", 'Offices, dining areas, locker rooms and staff restrooms, which run in shifts and call for frequency more than complexity. They are handled as a daily program, as in <a href="limpieza-corporativa">corporate cleaning</a>.'),
            ("h3", "Gatehouses, entrances and inspection zones"),
            ("p", "These are the points everything passes through, with a lot of contact between people and vehicles. They call for disinfection of touched surfaces and attention to the floor, which takes most of the traffic."),

            ("h2", "How is cleaning done in an operation that never stops?"),
            ("p", "A port or logistics facility runs in shifts, often continuously, so there is no moment when it is empty. Cleaning is organized by zone and by windows agreed with operations, so each section is worked on when the movement allows it."),
            ("p", "Cleaning shifts are designed around each client's operation, with routes and schedules set out in writing and the zone marked off while work is under way."),
            ("todo", "confirm with the client whether it offers 24/7 coverage at ports (the previous meta description claimed it) and how windows are coordinated with operations; for now it is described only as general practice."),

            ("h2", "What changes in a restricted-access zone?"),
            ("p", "A terminal has areas where only accredited staff may enter. Whoever cleans needs a credential, permitted routes and, depending on the zone, a record of entry and exit. That turns staff turnover into a logistics problem and not just an operational one."),
            ("p", "With staff on the formal payroll, background checks and fixed teams for each facility, the group that is accredited once is the group that keeps working afterward."),

            ("h2", "How do weather and exposure affect cleaning?"),
            ("p", "In Panama's tropical climate, rain, humidity and, at coastal facilities, salt air speed up the wear on surfaces and carry mud indoors. Exterior cleaning is scheduled with that rhythm in mind, and the entrances to warehouses and offices are reinforced so dirt does not get through."),
            ("p20", 'Floors that get wet often also need a non-slip finish and signage, because a slip in a yard with heavy machinery matters more than in an office. For treating concrete floors, see <a href="cuidado-pisos">floor care</a>.'),

            ("h2", "Who handles industrial waste and controlled substances?"),
            ("p", "Hazardous waste and controlled substances have their own handling at a port facility, in the hands of the operator or an authorized waste manager. General cleaning does not replace that chain."),
            ("p", "That is why it is worth setting out in writing which waste the cleaning service removes and which the operator manages, so nothing is left without an owner."),
            ("todo", 'confirm with the client the real scope. The previous page claimed "handling of industrial waste and controlled substances" and "compliance with free-zone and maritime-authority sanitary regulations" without citing any regulation; if there are citable regulations, name them.'),
        ],
    ),
]
