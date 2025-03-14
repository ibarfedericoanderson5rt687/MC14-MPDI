import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial de la página
st.set_page_config(page_title="MC-14 y MPDI", layout="wide")

# Información del autor (Texto en blanco)
st.markdown("""
<div style='background-color: #2D2D2D; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
    <h2 style='color: white;'>👤 Autor</h2>
    <p style='color: white;'>© 2025 <strong>Ibar Federico Anderson, Ph.D., Master, Industrial Designer</strong></p>
    <div style='display: flex; justify-content: space-between; margin-top: 10px;'>
        <div>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" style="height: 20px; vertical-align: middle;"> <a href="https://scholar.google.com/citations?user=mXD4RFUAAAAJ&hl=en" target="_blank" style='color: white;'>Google Scholar</a></p>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" style="height: 20px; vertical-align: middle;"> <a href="https://orcid.org/0000-0002-9732-3660" target="_blank" style='color: white;'>ORCID</a></p>
        </div>
        <div>
            <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/ResearchGate_icon_SVG.svg" style="height: 20px; vertical-align: middle;"> <a href="https://www.researchgate.net/profile/Ibar-Anderson" target="_blank" style='color: white;'>Research Gate</a></p>
            <p style='color: white;'><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 20px; vertical-align: middle;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 20px; vertical-align: middle;"> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" style='color: white;'>CC BY 4.0 License</a></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Título de la aplicación con ISO 5807:1985 (Texto en negro)
st.markdown("""
<h1 style='text-align: center; color: black;'>Selecciona una metodología</h1>
<p style='text-align: center; color: black; font-size: 18px;'>Los diagramas de flujo computacionales (Flowcharts) están basados en la norma <strong>ISO 5807:1985</strong>, que define las convenciones gráficas para representar procesos lógicos y estructuras de datos.</p>
""", unsafe_allow_html=True)

# Botones personalizados para seleccionar metodología
col1, col2 = st.columns(2)

with col1:
    if st.button("MC-14: Método Científico", key="mc14_button", help="Selecciona esta opción para ver el flujo del Método Científico"):
        st.session_state["selected_option"] = "MC-14: Método Científico"

with col2:
    if st.button("MPDI: Diseño Industrial", key="mpdi_button", help="Selecciona esta opción para ver el flujo del Diseño Industrial"):
        st.session_state["selected_option"] = "MPDI: Diseño Industrial"

# Descripciones ampliadas para MC-14
mc14_descriptions = {
    "🔍 Observación Curiosa": """
        La observación curiosa es el punto de partida del método científico. Consiste en identificar fenómenos o patrones inusuales que despierten interés investigativo. Este paso implica estar atento a detalles que otros podrían pasar por alto.
    """,
    "❓ Planteamiento del Problema": """
        El planteamiento del problema consiste en formular una pregunta clara y específica que guíe la investigación. Debe ser lo suficientemente precisa para permitir una solución práctica y relevante.
    """,
    "📚 📖 Revisión de Literatura": """
        La revisión de literatura implica explorar estudios previos, teorías y datos existentes relacionados con el problema. Este paso ayuda a contextualizar el problema dentro del conocimiento actual y evitar duplicaciones innecesarias.
    """,
    "💡 Hipótesis": """
        La hipótesis es una afirmación predictiva que intenta explicar el fenómeno observado. Debe ser comprobable mediante experimentos y debe proporcionar una base sólida para la investigación.
    """,
    "🔨 🔩 Diseño Experimental": """
        El diseño experimental incluye la planificación de métodos, herramientas y procedimientos para recolectar datos de manera sistemática. Este paso asegura que los resultados sean válidos y reproducibles.
    """,
    "📋 Recolección de Datos": """
        La recolección de datos implica ejecutar los métodos planificados para obtener información relevante. Este proceso debe ser riguroso y seguir protocolos establecidos para garantizar la calidad de los datos.
    """,
    "📈 📊 Análisis de Datos": """
        El análisis de datos incluye la interpretación estadística o cualitativa de los datos recolectados. Este paso busca identificar patrones, tendencias o relaciones significativas que respalden o refuten la hipótesis.
    """,
    "✅ Conclusión": """
        La conclusión evalúa si los resultados obtenidos apoyan la hipótesis inicial. Este paso también puede generar nuevas preguntas o ajustes en el marco teórico.
    """,
    "📂 Redacción del Informe": """
        La redacción del informe documenta formalmente todo el proceso de investigación, incluyendo objetivos, métodos, resultados y conclusiones. Es esencial para la comunicación científica.
    """,
    "👨 👩 Revisión por Pares": """
        La revisión por pares es un proceso crítico en el que expertos externos evalúan el informe para garantizar su rigor y validez. Este paso mejora la calidad y credibilidad del trabajo.
    """,
    "📂 📥 Publicación": """
        La publicación difunde los resultados en revistas científicas o conferencias especializadas. Este paso permite que otros investigadores accedan y construyan sobre el trabajo realizado.
    """,
    "♻️ Retroalimentación": """
        La retroalimentación genera nuevas preguntas, aplicaciones o mejoras en el proceso investigativo. Este ciclo continuo fomenta el avance del conocimiento científico.
    """,
}

# Descripciones ampliadas para MPDI
mpdi_descriptions = {
    "🏠 Empatizar y Contextualizar": """
        La empatía implica comprender profundamente las necesidades, deseos y limitaciones de los usuarios finales. Este paso también incluye analizar el contexto social, cultural y ambiental donde se utilizará el producto.
    """,
    "❓ Definir el Problema": """
        Definir el problema consiste en identificar claramente qué necesidad o desafío se intenta resolver. Este paso debe ser específico y centrarse en los usuarios y sus interacciones con el entorno.
    """,
    "👨‍💻 💾 📲 🔗 Investigación Web y DeepSearch": """
        La investigación web incluye buscar tendencias actuales, materiales innovadores y casos similares. Esta etapa utiliza herramientas digitales avanzadas para recopilar información relevante.
    """,
    "💡 ✨ Ideación y Conceptualización": """
        La ideación es un proceso creativo que genera múltiples soluciones potenciales al problema. Se utilizan técnicas como brainstorming, mapas mentales y prototipado rápido para explorar ideas.
    """,
    "✏️ 📝 🎨 📐 Bocetos y Prototipado Inicial": """
        Los bocetos y prototipos iniciales permiten visualizar y explorar formas, funciones y usabilidad. Este paso es clave para materializar ideas abstractas en conceptos tangibles.
    """,
    "⚖️ 🔧 Evaluación Técnica": """
        La evaluación técnica analiza la viabilidad del diseño desde perspectivas técnicas, económicas y de usabilidad. Este paso asegura que el producto sea funcional, seguro y rentable.
    """,
    "⚙️ Iteración y Refinamiento": """
        La iteración implica mejorar el diseño basado en pruebas y retroalimentación. Este proceso cíclico garantiza que el producto final sea óptimo y cumpla con las expectativas del usuario.
    """,
    "📑 Documentación Técnica": """
        La documentación técnica incluye especificaciones detalladas, planos y manuales de uso. Este paso es esencial para la producción y mantenimiento del producto.
    """,
    "👤 Validación con Usuarios": """
        La validación con usuarios prueba el producto en contextos reales para verificar su funcionalidad, estética, ergonomía y aceptación. Este paso asegura que el diseño satisfaga las necesidades del usuario.
    """,
}

# Diagramas de flujo en Mermaid
mc14_diagram = """
%%{init: {'theme': 'base', 'themeVariables': { 'fontFamily': 'arial', 'fontSize': '16px' }}}%%
flowchart TD
    A([🔍 Observación Curiosa]) --> B[❓ Planteamiento del Problema]
    B --> C[/📚 📖 Revisión de Literatura/]
    C --> D{💡 Hipótesis}
    D -->|Formulación| E[🔨 🔩 Diseño Experimental]
    E --> F([📋 Recolección de Datos])
    F --> G[[📈 📊 Análisis de Datos]]
    G --> H{ ✅ Conclusión}
    H -->|👍 Apoya Hipótesis| I[/📂 Redacción del Informe/]
    H -->|👎 ❌ No Apoya| J[[📌 Revisión de Hipótesis]]
    J --> E
    I --> K((👨 👩 Revisión por Pares))
    K --> L[(📂 📥 Publicación)]
    L --> M([♻️ Retroalimentación])
    M -->|Nuevas Preguntas| A
    M -->|🏁 Fin del Proceso| N([🏁 Fin])

    classDef default fill:#3498db,stroke:#2980b9,color:white,stroke-width:2px
    classDef round fill:#e74c3c,stroke:#c0392b,color:white,cursor:pointer
    classDef diamond fill:#2ecc71,stroke:#27ae60,color:white,cursor:pointer
    classDef parallel fill:#9b59b6,stroke:#8e44ad,color:white,cursor:pointer
    classDef circle fill:#f1c40f,stroke:#f39c12,color:white,cursor:pointer
    classDef database fill:#1abc9c,stroke:#16a085,color:white,cursor:pointer

    linkStyle default stroke:#ffffff,stroke-width:2px

    class A,F,M,N round
    class D,H diamond
    class G,J parallel
    class K circle
    class L database
"""

mpdi_diagram = """
%%{init: {'theme': 'base', 'themeVariables': { 'fontFamily': 'arial', 'fontSize': '16px' }}}%%
flowchart TD
    A([🏠 Empatizar y Contextualizar]) --> B[/❓ Definir el Problema/]
    B --> C[/👨‍💻 💾 📲 🔗 Investigación Web y DeepSearch/]
    C --> D{💡 ✨ Ideación y Conceptualización}
    D -->|Generación| E[✏️ 📝 🎨 📐 Bocetos, Render 2D y Prototipos 3D]
    E --> F([⚖️ 🔧 Evaluación Técnica])
    F --> G[[⚙️ Iteración y Refinamiento]]
    G --> H{📑 Documentación Técnica}
    H -->|📄 Documentación| I[/👤 Validación con Usuarios/]
    H -->|👎 No Aprobado ❌| J[[🔄 Revisión de Diseño]]
    J --> E
    I --> K((🏭 🔩 Producción y Fabricación))
    K --> L[(🚀 Lanzamiento)]
    L --> M([📢 👪 👤 Comunicación y Marketing para Usuarios])
    M -->|Nuevas Mejoras| A
    M -->|🎯 Fin del Proceso| N([🎯 Fin])

    classDef default fill:#3498db,stroke:#2980b9,color:white,stroke-width:2px
    classDef round fill:#e74c3c,stroke:#c0392b,color:white,cursor:pointer
    classDef diamond fill:#2ecc71,stroke:#27ae60,color:white,cursor:pointer
    classDef parallel fill:#9b59b6,stroke:#8e44ad,color:white,cursor:pointer
    classDef circle fill:#f1c40f,stroke:#f39c12,color:white,cursor:pointer
    classDef database fill:#1abc9c,stroke:#16a085,color:white,cursor:pointer

    linkStyle default stroke:#ffffff,stroke-width:2px

    class A,F,M,N round
    class D,H diamond
    class G,J parallel
    class K circle
    class L database
"""

def render_mermaid(diagram, descriptions):
    mermaid_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        function showTooltip(event, title, description) {{
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.innerHTML = `
                <div style="background-color: #34495e; color: white; padding: 25px 30px; border-radius: 12px; font-size: 24px; line-height: 1.4;">
                    <h3 style="margin: 0 0 15px; font-size: 30px;">${{title}}</h3>
                    <hr style="border: 1px solid white; margin: 15px 0;">
                    <p style="margin: 0; font-size: 24px;">${{description.trim()}}</p>
                </div>`;
            tooltip.style.position = 'fixed';
            tooltip.style.left = (event.pageX + 10) + 'px';
            tooltip.style.top = (event.pageY + 10) + 'px';
            document.body.appendChild(tooltip);
        }}

        function hideTooltip() {{
            const tooltips = document.querySelectorAll('.tooltip');
            tooltips.forEach(t => t.remove());
        }}

        document.addEventListener('DOMContentLoaded', function() {{
            setTimeout(() => {{
                const nodes = document.querySelectorAll('.node');
                nodes.forEach(node => {{
                    node.style.cursor = 'pointer';
                    const title = node.textContent.trim();
                    const description = {descriptions}[title] || '';
                    node.addEventListener('click', (e) => {{
                        showTooltip(e, title, description);
                    }});
                    node.addEventListener('mouseout', hideTooltip);
                }});
            }}, 2000);
        }});
    </script>
    <style>
        body {{
            background-color: #2c3e50;
            color: white;
        }}
        .stApp {{
            background-color: #2c3e50;
        }}
        .css-1d391kg {{
            background-color: #2c3e50;
        }}
        .stSelectbox label {{
            color: white !important;
        }}
        .mermaid {{
            background-color: #2c3e50;
        }}
        .tooltip {{
            position: fixed;
            background-color: #34495e;
            color: white;
            padding: 25px 30px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.3);
            z-index: 1000;
            max-width: 600px; /* Más ancho */
            font-size: 24px; /* Fuente más grande */
            line-height: 1.4; /* Espaciado entre líneas */
            pointer-events: none;
            transition: all 0.2s ease;
            border: 2px solid #45566e;
        }}
    </style>
    <div class="mermaid" style="overflow: auto; max-height: 800px;">
    {diagram}
    </div>
    <script>
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    """
    components.html(mermaid_html, height=800, scrolling=True)

# Mostrar el diagrama según la selección
if "selected_option" in st.session_state:
    option = st.session_state["selected_option"]

    if option == "MC-14: Método Científico":
        st.subheader("MC-14: Método Científico")
        render_mermaid(mc14_diagram, mc14_descriptions)
    elif option == "MPDI: Diseño Industrial":
        st.subheader("MPDI: Diseño Industrial")
        render_mermaid(mpdi_diagram, mpdi_descriptions)

# Pie de página
st.markdown("---")
st.markdown("Desarrollado por Ibar Federico Anderson © 2025")
