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

# Título de la aplicación
st.title("Selecciona una metodología")

# Descripciones para MC-14
mc14_descriptions = {
    "🔍 Observación Curiosa": "Identificación del fenómeno mediante una observación curiosa.",
    "❓ Planteamiento del Problema": "Definición clara del problema a investigar.",
    "📚 📖 Revisión de Literatura": "Contextualización del problema mediante la revisión de literatura.",
    "💡 Hipótesis": "Explicación predictiva que guía la investigación.",
    "🔨 🔩 Diseño Experimental": "Planificación de métodos para abordar el problema.",
    "📋 Recolección de Datos": "Ejecución de la recolección de datos.",
    "📈 📊 Análisis de Datos": "Interpretación estadística o cualitativa de los datos.",
    "✅ Conclusión": "Relación de los resultados con la hipótesis planteada.",
    "📂 Redacción del Informe": "Documentación formal de la investigación.",
    "👨 👩 Revisión por Pares": "Evaluación externa del informe por expertos.",
    "📂 📥 Publicación": "Difusión de los resultados en revistas científicas.",
    "♻️ Retroalimentación": "Generación de nuevas preguntas o aplicaciones.",
}

# Descripciones para MPDI
mpdi_descriptions = {
    "🏠 Empatizar y Contextualizar": "Investigación de necesidades, contexto social y usuarios finales.",
    "❓ Definir el Problema": "Definición clara del problema de diseño industrial.",
    "👨‍💻 💾 📲 🔗 Investigación Web y DeepSearch": "Análisis de tendencias, materiales y casos similares.",
    "💡 ✨ Ideación y Conceptualización": "Generación creativa de ideas con diversos métodos.",
    "✏️ 📝 🎨 📐 Bocetos y Prototipado Inicial": "Creación de modelos básicos para explorar forma y función.",
    "⚖️ 🔧 Evaluación Técnica": "Análisis de viabilidad técnica, costos y usabilidad.",
    "⚙️ Iteración y Refinamiento": "Mejora basada en pruebas y retroalimentación.",
    "📑 Documentación Técnica": "Definición de especificaciones técnicas y planos.",
    "👤 Validación con Usuarios": "Pruebas en contextos reales con humanos para verificar funcionalidad, estética, ergonomía, precios, etc.",
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
                <div style="background-color: #34495e; color: white; padding: 15px 20px; border-radius: 8px; font-size: 18px;">
                    <h3 style="margin: 0 0 10px;">${{title}}</h3>
                    <p style="margin: 0;">${{description}}</p>
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
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
            z-index: 1000;
            max-width: 400px;
            font-size: 18px;
            pointer-events: none;
            transition: all 0.2s ease;
            border: 1px solid #45566e;
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

# Selector de metodología
option = st.selectbox(
    "Elige una metodología",
    ["MC-14: Método Científico", "MPDI: Diseño Industrial"]
)

if option == "MC-14: Método Científico":
    st.subheader("MC-14: Método Científico")
    render_mermaid(mc14_diagram, mc14_descriptions)
elif option == "MPDI: Diseño Industrial":
    st.subheader("MPDI: Diseño Industrial")
    render_mermaid(mpdi_diagram, mpdi_descriptions)

# Pie de página
st.markdown("---")
st.markdown("Desarrollado por Ibar Federico Anderson © 2025")
