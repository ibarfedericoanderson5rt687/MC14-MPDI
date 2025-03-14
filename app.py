import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial de la página
st.set_page_config(page_title="MC-14 y MPDI", layout="wide")

# Título de la aplicación
st.title("Selecciona una metodología")

# Definir los diagramas Mermaid
mc14_diagram = """
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
"""

mpdi_diagram = """
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
"""

# Función para renderizar el diagrama Mermaid
def render_mermaid(diagram):
    mermaid_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <div class="mermaid" style="overflow: auto; max-height: 800px;">
    {diagram}
    </div>
    <script>
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    """
    # Aumentamos la altura del componente HTML
    components.html(mermaid_html, height=800, scrolling=True)

# Botones para seleccionar la metodología
option = st.selectbox(
    "Elige una metodología",
    ["MC-14: Método Científico", "MPDI: Diseño Industrial"]  # Usamos una lista explícita
)

# Mostrar el diagrama correspondiente
if option == "MC-14: Método Científico":
    st.subheader("MC-14: Método Científico")
    render_mermaid(mc14_diagram)
elif option == "MPDI: Diseño Industrial":
    st.subheader("MPDI: Diseño Industrial")
    render_mermaid(mpdi_diagram)
