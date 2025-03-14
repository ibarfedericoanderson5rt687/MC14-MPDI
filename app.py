import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial de la página
st.set_page_config(page_title="MC-14 y MPDI", layout="wide")

# Información del autor
st.markdown("""
<div style='background-color: #2D2D2D; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
    <h2>馃懁 Autor</h2>
    <p>漏 2025 <strong>Ibar Federico Anderson, Ph.D., Master, Industrial Designer</strong></p>
    <div style='display: flex; justify-content: space-between; margin-top: 10px;'>
        <div>
            <p><img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" style="height: 20px; vertical-align: middle;"> <a href="https://scholar.google.com/citations?user=mXD4RFUAAAAJ&hl=en" target="_blank">Google Scholar</a></p>
            <p><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" style="height: 20px; vertical-align: middle;"> <a href="https://orcid.org/0000-0002-9732-3660" target="_blank">ORCID</a></p>
        </div>
        <div>
            <p><img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/ResearchGate_icon_SVG.svg" style="height: 20px; vertical-align: middle;"> <a href="https://www.researchgate.net/profile/Ibar-Anderson" target="_blank">Research Gate</a></p>
            <p><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 20px; vertical-align: middle;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 20px; vertical-align: middle;"> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">CC BY 4.0 License</a></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Título de la aplicación
st.title("Selecciona una metodología")

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
"""

def render_mermaid(diagram):
    mermaid_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        function showTooltip(event, node) {{
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.innerHTML = `
                <div style="background-color: #34495e; color: white; padding: 10px 15px; border-radius: 6px;">
                    <h3>${{node.title}}</h3>
                    <p>${{node.description}}</p>
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
                    node.addEventListener('click', (e) => {{
                        const title = node.getAttribute('data-title') || node.textContent;
                        const description = node.getAttribute('data-description') || '';
                        showTooltip(e, {{ title, description }});
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
            padding: 10px 15px;
            border-radius: 6px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
            z-index: 1000;
            max-width: 300px;
            font-size: 14px;
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
    render_mermaid(mc14_diagram)
elif option == "MPDI: Diseño Industrial":
    st.subheader("MPDI: Diseño Industrial")
    render_mermaid(mpdi_diagram)

# Pie de página
st.markdown("---")
st.markdown("Desarrollado por Ibar Federico Anderson © 2025")
