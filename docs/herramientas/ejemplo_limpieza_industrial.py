# -*- coding: utf-8 -*-
"""Servicio limpieza-industrial (ES y EN). Hermana de industria: puertos (ya reescrita).

Frontera, que aqui es el problema principal:
  - puertos (industria) = como se organiza la limpieza en una terminal o parque
    logistico: zonas, operacion continua, acceso restringido, intemperie. Esa
    pagina ya promete que "el desengrase, la maquinaria y la limpieza de plantas
    de produccion" estan AQUI, asi que hay que entregarlo.
  - limpieza-industrial (servicio) = el trabajo en si: que se limpia, con que
    quimico, sobre que superficie y en que ventana. NADA de "operacion continua",
    "por zonas" ni "acceso restringido": es el marco de puertos y repetirlo
    dispararia la similitud (fue el error de colegios/hospitales en v10).
  - cuidado-pisos = tratamiento del material (pulido, sellado, cristalizado).
  - proyectos-especiales = parada mayor, traslado, siniestro.
  - otros-servicios = residuos comunes de oficina y comedor.
  - fumigacion / vidrios-fachadas / limpieza-post-construccion: sin solape.

Se retiran del texto original, por no tener respaldo en los hechos publicados:
"personal certificado en seguridad industrial", "equipos industriales propios",
"manejo de residuos industriales segun normativa ambiental" (ninguna norma
citada) y "personal certificado" de la meta. Quedan 4 TODOs.
"""

WA = "https://wa.me/50769823165?text="

PAGES = [
    dict(
        file="es/limpieza-industrial.html", lang="es", img="limpieza-industrial.webp",
        url="https://www.go-cleaning.com/es/limpieza-industrial",
        list_id="frentes",
        list_name="Frentes de limpieza en una planta industrial",
        service_type="Limpieza industrial",
        h1="Limpieza industrial para plantas y bodegas",
        alt="Limpieza industrial en planta",
        lead="Limpieza que opera al ritmo de la planta, no al revés.",
        meta="Limpieza industrial para plantas y bodegas en Panamá: desengrase de pisos y maquinaria, estructura alta, drenajes y trabajo en paradas programadas.",
        svc_desc="Limpieza industrial para plantas, bodegas y zonas de producción en Panamá: desengrase de pisos y maquinaria, estructura alta, campanas y drenajes.",
        cta_h2="Cuéntanos qué produce tu planta",
        cta_p="Dinos qué se produce, qué superficies hay y con qué frecuencia necesitas el servicio, y preparamos una propuesta.",
        cta_href=WA + "Hola%2C%20quiero%20cotizar%20limpieza%20industrial%20para%20mi%20planta",
        cta_btn="Solicitar una propuesta",
        blocks=[
            ("p20", "La limpieza de una planta no es la de una oficina a mayor escala. Lo que se retira es distinto, grasa y aceite y polvo de proceso, las superficies toleran cosas distintas, y el entorno tiene riesgos que no existen en un edificio de oficinas: maquinaria en movimiento, superficies calientes y energía almacenada."),
            ("p20", 'Esta página trata del trabajo en sí: qué se limpia, con qué y en qué ventana. Si lo que buscas es cómo se organiza la limpieza en una terminal o un parque logístico, eso está en <a href="puertos">puertos y zonas logísticas</a>.'),

            ("h2", "¿Qué se limpia en una planta industrial?"),
            ("p", "Son cuatro frentes, cada uno con su equipo y su frecuencia. Casi nunca se contratan los cuatro a la vez."),
            ("p", "Lo que define el alcance no es el tamaño de la planta sino qué produce: una planta de alimentos y un taller metalmecánico ensucian de maneras que no se parecen en nada."),
            ("h3", "Pisos y zonas de producción"),
            ("p", 'Es el frente más constante. Se acumulan grasa, aceite y residuo de proceso, y el piso tiene que quedar limpio sin quedar resbaloso, que es la parte difícil. El tratamiento del material en sí, cuando el concreto está pulido o sellado, va aparte en <a href="cuidado-pisos">cuidado de pisos</a>.'),
            ("h3", "Maquinaria y equipos"),
            ("p", "El exterior de las máquinas, sus bases y el área alrededor, donde se concentra lo que la producción expulsa. Qué se toca y qué no se toca es una línea que se define por escrito antes de empezar, no sobre la marcha."),
            ("h3", "Estructura alta, ductos y campanas"),
            ("p", "Vigas, luminarias, ductos de extracción y campanas acumulan polvo de proceso durante meses sin que nadie los mire, hasta que cae sobre la línea o aparece en una auditoría. Se trabajan con la planta detenida y con andamio o plataforma."),
            ("h3", "Canaletas, trampas de grasa y drenajes"),
            ("p", "Es el frente que más seguido queda fuera del contrato y el primero que da problemas: un drenaje saturado devuelve al piso de producción el agua del lavado."),

            ("h2", "¿En qué se diferencia el desengrase industrial de lavar un piso?"),
            ("p", "En que el producto se elige por la superficie y por lo que tiene encima, no por el tipo de local."),
            ("p", "Un desengrasante alcalino que funciona sobre concreto puede manchar el aluminio o atacar un recubrimiento epóxico. La grasa animal de una planta de alimentos no se retira igual que el aceite mineral de un taller. Y la temperatura y la presión del agua pesan tanto como el químico: con demasiada presión, el agua esparce la grasa en vez de arrastrarla y la mete donde no debe entrar."),
            ("p20", "Por eso el desengrase arranca por identificar la superficie y el tipo de residuo, y por probar en un área pequeña antes de aplicarlo a toda la nave."),
            ("todo", "confirmar con el cliente si los equipos industriales (hidrolavadoras, fregadoras, aspiradoras de solidos y liquidos) son propios de Go Services o se alquilan. La pagina anterior afirmaba \"equipos industriales propios\"."),

            ("h2", "¿Qué se hace durante una parada de planta?"),
            ("p", "Una parada programada es la única ventana para llegar a lo que no se puede tocar con la línea andando."),
            ("p", "Son intervenciones cortas y con hora de cierre: estructura alta, interiores de equipo, drenajes y las zonas que quedan detrás de la maquinaria. Se planifican al revés, desde la hora en que la planta tiene que volver a arrancar, y conviene acordar de antemano qué se deja para la próxima si el tiempo no alcanza."),
            ("p20", 'Una parada mayor, un traslado o una limpieza después de un siniestro ya no es un programa recurrente sino un proyecto con cronograma y cuadrilla propios: eso se trata en <a href="proyectos-especiales">proyectos especiales</a>.'),

            ("h2", "¿Quién limpia la maquinaria, el operador o el personal de limpieza?"),
            ("p", "Conviene resolverlo antes de firmar, porque de la respuesta depende quién responde si algo se daña."),
            ("p", "La regla razonable es que el personal de limpieza trabaja sobre superficies externas y sobre el entorno del equipo, y que todo lo que exija abrir, desmontar o desenergizar una máquina lo hace o lo autoriza el personal de mantenimiento de la planta, con el equipo bloqueado. Esa frontera se escribe en el alcance, máquina por máquina si hace falta."),
            ("p20", "Hay además un paso previo que no se salta: la inducción de seguridad de la planta y el permiso de trabajo cuando aplica. Las reglas las pone la instalación, no el proveedor."),
            ("todo", "confirmar con el cliente si el personal interviene maquinaria directamente o solo su entorno, y que certificaciones de seguridad industrial tiene el personal. La pagina anterior afirmaba \"personal certificado en seguridad industrial\" sin especificar ninguna."),

            ("h2", "¿A dónde van el agua y los residuos del lavado?"),
            ("p", "El agua que sale de un desengrase lleva grasa y químico, así que no es agua de limpieza común."),
            ("p", "Lo habitual es que pase por la trampa de grasa o por el tratamiento que la planta ya tiene, y que el residuo sólido se separe en el punto donde se genera. Lo que no puede pasar es que termine en un drenaje pluvial."),
            ("p", 'Los residuos peligrosos, los químicos de proceso y las sustancias controladas tienen su propia cadena, a cargo del generador o de un gestor autorizado, y el servicio de limpieza no la sustituye. Los residuos comunes de oficina y comedor se tratan en <a href="otros-servicios">otros servicios de facilities</a>.'),
            ("todo", "confirmar con el cliente el alcance real de los residuos industriales y si hay alguna norma ambiental citable. La pagina anterior decia \"manejo de residuos industriales segun normativa ambiental\" sin citar ninguna. Confirmar tambien si Go Services atiende paradas de planta y con que anticipacion se coordinan."),
        ],
    ),
    dict(
        file="en/limpieza-industrial.html", lang="en", img="limpieza-industrial.webp",
        url="https://www.go-cleaning.com/en/limpieza-industrial",
        list_id="frentes",
        list_name="Cleaning fronts in an industrial plant",
        service_type="Industrial cleaning",
        h1="Industrial cleaning for plants and warehouses",
        alt="Industrial cleaning in a plant",
        lead="Cleaning that runs at the plant's pace, not the other way around.",
        meta="Industrial cleaning for plants and warehouses in Panama: degreasing of floors and machinery, overhead structure, drains and work during scheduled shutdowns.",
        svc_desc="Industrial cleaning for plants, warehouses and production areas in Panama: degreasing of floors and machinery, overhead structure, hoods and drains.",
        cta_h2="Tell us what your plant produces",
        cta_p="Tell us what is produced, what surfaces are involved and how often you need the service, and we will prepare a proposal.",
        cta_href=WA + "Hello%2C%20I%27d%20like%20a%20quote%20for%20industrial%20cleaning%20at%20my%20plant",
        cta_btn="Request a proposal",
        blocks=[
            ("p20", "Cleaning a plant is not cleaning an office on a larger scale. What comes off is different, grease and oil and process dust, the surfaces tolerate different things, and the setting carries risks that do not exist in an office building: moving machinery, hot surfaces and stored energy."),
            ("p20", 'This page is about the work itself: what gets cleaned, with what, and in which window. If what you are looking for is how cleaning is organized across a terminal or a logistics park, that is covered under <a href="puertos">ports and logistics zones</a>.'),

            ("h2", "What gets cleaned in an industrial plant?"),
            ("p", "There are four fronts, each with its own equipment and its own frequency. All four are rarely contracted at once."),
            ("p", "What sets the scope is not the size of the plant but what it makes: a food plant and a metalworking shop get dirty in ways that have nothing in common."),
            ("h3", "Floors and production areas"),
            ("p", 'This is the steadiest front. Grease, oil and process residue build up, and the floor has to end up clean without ending up slippery, which is the hard part. Treating the material itself, when the concrete is polished or sealed, is handled separately under <a href="cuidado-pisos">floor care</a>.'),
            ("h3", "Machinery and equipment"),
            ("p", "The outside of the machines, their bases and the area around them, where whatever production throws off collects. What is touched and what is not is a line set out in writing before the work starts, not as it goes along."),
            ("h3", "Overhead structure, ducts and hoods"),
            ("p", "Beams, light fixtures, extraction ducts and hoods collect process dust for months with nobody looking at them, until it falls onto the line or shows up in an audit. They are worked on with the plant stopped, from scaffolding or a lift."),
            ("h3", "Channels, grease traps and drains"),
            ("p", "This is the front most often left out of the contract and the first one to cause trouble: a clogged drain sends the wash water back onto the production floor."),

            ("h2", "How is industrial degreasing different from washing a floor?"),
            ("p", "The product is chosen for the surface and for what is sitting on it, not for the type of premises."),
            ("p", "An alkaline degreaser that works on concrete can stain aluminum or attack an epoxy coating. Animal fat in a food plant does not come off the way mineral oil does in a machine shop. And water temperature and pressure count as much as the chemical: at too much pressure, water spreads the grease instead of carrying it away and drives it where it should not go."),
            ("p20", "That is why degreasing starts by identifying the surface and the type of residue, and by testing on a small area before it is applied across the floor."),
            ("todo", "confirm with the client whether the industrial equipment (pressure washers, scrubbers, wet and dry vacuums) belongs to Go Services or is rented. The previous page claimed \"our own industrial equipment\"."),

            ("h2", "What gets done during a plant shutdown?"),
            ("p", "A scheduled shutdown is the only window for reaching what cannot be touched while the line is running."),
            ("p", "These are short jobs with a closing time: overhead structure, the inside of equipment, drains, and the areas behind the machinery. They are planned backward, from the hour the plant has to start up again, and it is worth agreeing in advance what gets left for next time if the clock runs out."),
            ("p20", 'A major shutdown, a relocation or a cleanup after an incident is no longer a recurring program but a project with its own schedule and crew: that is covered under <a href="proyectos-especiales">special projects</a>.'),

            ("h2", "Who cleans the machinery, the operator or the cleaning staff?"),
            ("p", "This is worth settling before signing, because the answer decides who answers for it if something is damaged."),
            ("p", "The sensible rule is that cleaning staff work on external surfaces and on the area around the equipment, and that anything calling for a machine to be opened, taken apart or de-energized is done or authorized by the plant's own maintenance staff, with the equipment locked out. That boundary goes into the scope, machine by machine if need be."),
            ("p20", "There is also a step beforehand that does not get skipped: the plant's safety induction and the work permit where one applies. The facility sets the rules, not the provider."),
            ("todo", "confirm with the client whether staff work on machinery directly or only around it, and which industrial-safety certifications the staff hold. The previous page claimed \"staff certified in industrial safety\" without naming any."),

            ("h2", "Where do the wash water and the waste end up?"),
            ("p", "The water coming off a degreasing job carries grease and chemical, so it is not ordinary cleaning water."),
            ("p", "It normally goes through the grease trap or through the treatment the plant already has, with solid residue separated at the point where it is generated. What cannot happen is for it to end up in a storm drain."),
            ("p", 'Hazardous waste, process chemicals and controlled substances have their own chain, in the hands of the generator or an authorized waste manager, and the cleaning service does not replace it. Ordinary office and break-room waste is covered under <a href="otros-servicios">additional facility services</a>.'),
            ("todo", "confirm with the client the real scope of industrial waste and whether there is any citable environmental regulation. The previous page said \"industrial waste handling per environmental regulations\" without citing one. Confirm as well whether Go Services covers plant shutdowns and how far in advance they are coordinated."),
        ],
    ),
]
