import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial de la página
st.set_page_config(page_title="MC-14 y MPDI", layout="wide")

# Estilo CSS personalizado para mejorar la estética
st.markdown(
    """
    <style>
        /* Fondo oscuro para toda la página */
        body {
            background-color: #2c3e50;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Estilo para los botones del selectbox */
        .stSelectbox > div {
            background-color: #34495e;
            border-radius: 8px;
            padding: 10px;
            color: white;
            font-size: 16px;
        }

        .stSelectbox > div:hover {
            background-color: #2980b9;
        }

        /* Estilo para los subtítulos */
        h2 {
            color: #ecf0f1;
            text-align: center;
        }

        /* Contenedor del diagrama */
        .diagram-container {
            background-color: #34495e;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título de la aplicación
st.title("Selecciona una metodología")

# Definir los diagramas Mermaid con colores inline
mc14_diagram = """
flowchart TD
    %% Colores inline para MC-14
    A([🔍 Observación Curiosa]):::obs --> B[❓ Planteamiento del Problema]:::problem
    B --> C[/📚 📖 Revisión de Literatura/]:::review
    C --> D{💡 Hipótesis}:::hypothesis
    D -->|Formulación| E[🔨 🔩 Diseño Experimental]:::design
    E --> F([📋 Recolección de Datos]):::data
    F --> G[[📈 📊 Análisis de Datos]]:::analysis
    G --> H{ ✅ Conclusión}:::conclusion
    H -->|👍 Apoya Hipótesis| I[/📂 Redacción del Informe/]:::report
    H -->|👎 ❌ No Apoya| J[[📌 Revisión de Hipótesis]]:::revision
    J --> E
    I --> K((👨 👩 Revisión por Pares)):::peer
    K --> L[(📂 📥 Publicación)]:::publication
    L --> M([♻️ Retroalimentación]):::feedback
    M -->|Nuevas Preguntas| A
    M -->|🏁 Fin del Proceso| N([🏁 Fin]):::end

    %% Clases para colores
    classDef obs fill:#1abc9c,stroke:#16a085,color:#fff
    classDef problem fill:#3498db,stroke:#2980b9,color:#fff
    classDef review fill:#9b59b6,stroke:#8e44ad,color:#fff
    classDef hypothesis fill:#e67e22,stroke:#d35400,color:#fff
    classDef design fill:#f1c40f,stroke:#f39c12,color:#000
    classDef data fill:#2ecc71,stroke:#27ae60,color:#000
    classDef analysis fill:#e74c3c,stroke:#c0392b,color:#fff
    classDef conclusion fill:#1abc9c,stroke:#16a085,color:#fff
    classDef report fill:#3498db,stroke:#2980b9,color:#fff
    classDef revision fill:#9b59b6,stroke:#8e44ad,color:#fff
    classDef peer fill:#e67e22,stroke:#d35400,color:#fff
    classDef publication fill:#f1c40f,stroke:#f39c12,color:#000
    classDef feedback fill:#2ecc71,stroke:#27ae60,color:#000
    classDef end fill:#e74c3c,stroke:#c0392b,color:#fff
"""

mpdi_diagram = """
flowchart TD
    %% Colores inline para MPDI
    A([🏠 Empatizar y Contextualizar]):::context --> B[/❓ Definir el Problema/]:::problem
    B --> C[/👨‍💻 💾 📲 🔗 Investigación Web y DeepSearch/]:::research
    C --> D{💡 ✨ Ideación y Conceptualización}:::ideation
    D -->|Generación| E[✏️ 📝 🎨 📐 Bocetos, Render 2D y Prototipos 3D]:::prototyping
    E --> F([⚖️ 🔧 Evaluación Técnica]):::evaluation
    F --> G[[⚙️ Iteración y Refinamiento]]:::iteration
    G --> H{📑 Documentación Técnica}:::documentation
    H -->|📄 Documentación| I[/👤 Validación con Usuarios/]:::validation
    H -->|👎 No Aprobado ❌| J[[🔄 Revisión de Diseño]]:::redesign
    J --> E
    I --> K((🏭 🔩 Producción y Fabricación)):::production
    K --> L[(🚀 Lanzamiento)]:::launch
    L --> M([📢 👪 👤 Comunicación y Marketing para Usuarios]):::marketing
    M -->|Nuevas Mejoras| A
    M -->|🎯 Fin del Proceso| N([🎯 Fin]):::end

    %% Clases para colores
    classDef context fill:#1abc9c,stroke:#16a085,color:#fff
    classDef problem fill:#3498db,stroke:#2980b9,color:#fff
    classDef research fill:#9b59b6,stroke:#8e44ad,color:#fff
    classDef ideation fill:#e67e22,stroke:#d35400,color:#fff
    classDef prototyping fill:#f1c40f,stroke:#f39c12,color:#000
    classDef evaluation fill:#2ecc71,stroke:#27ae60,color:#000
    classDef iteration fill:#e74c3c,stroke:#c0392b,color:#fff
    classDef documentation fill:#1abc9c,stroke:#16a085,color:#fff
    classDef validation fill:#3498db,stroke:#2980b9,color:#fff
    classDef redesign fill:#9b59b6,stroke:#8e44ad,color:#fff
    classDef production fill:#e67e22,stroke:#d35400,color:#fff
    classDef launch fill:#f1c40f,stroke:#f39c12,color:#000
    classDef marketing fill:#2ecc71,stroke:#27ae60,color:#000
    classDef end fill:#e74c3c,stroke:#c0392b,color:#fff
"""

# Función para renderizar el diagrama Mermaid
def render_mermaid(diagram):
    mermaid_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <div class="diagram-container">
        <div class="mermaid" style="overflow: auto; max-height: 800px;">
        {diagram}
        </div>
    </div>
    <script>
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    """
    components.html(mermaid_html, height=800, scrolling=True)

# Botones para seleccionar la metodología
option = st.selectbox(
    "Elige una metodología",
    ["MC-14: Método Científico", "MPDI: Diseño Industrial"]
)

# Mostrar el diagrama correspondiente
if option == "MC-14: Método Científico":
    st.subheader("MC-14: Método Científico")
    render_mermaid(mc14_diagram)
elif option == "MPDI: Diseño Industrial":
    st.subheader("MPDI: Diseño Industrial")
    render_mermaid(mpdi_diagram)
