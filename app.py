import streamlit as st
import streamlit.components.v1 as components

# Configuración inicial de la página
st.set_page_config(page_title="MC-14 y MPDI", layout="wide")

# Título de la aplicación
st.title("Selecciona una metodología")

# Información para las ventanas emergentes
info_mc14 = {
    "🔍 Observación Curiosa": "Etapa 1: Identificación del fenómeno que despierta curiosidad.",
    "❓ Planteamiento del Problema": "Etapa 2: Definición clara del problema a investigar.",
    "📚 📖 Revisión de Literatura": "Etapa 3: Contextualización mediante la revisión de estudios previos.",
    "💡 Hipótesis": "Etapa 4: Propuesta de una explicación predictiva basada en observaciones.",
    "🔨 🔩 Diseño Experimental": "Etapa 5: Planificación de los métodos para probar la hipótesis.",
    "📋 Recolección de Datos": "Etapa 6: Ejecución del experimento y recolección de datos.",
    "📈 📊 Análisis de Datos": "Etapa 7: Interpretación estadística o cualitativa de los datos obtenidos.",
    "✅ Conclusión": "Etapa 8: Evaluación de si los resultados apoyan la hipótesis.",
    "📂 Redacción del Informe": "Etapa 9: Documentación formal de todo el proceso.",
    "👨 👩 Revisión por Pares": "Etapa 10: Evaluación externa por expertos en el campo.",
    "📂 📥 Publicación": "Etapa 11: Difusión de los resultados en revistas científicas.",
    "♻️ Retroalimentación": "Etapa 12: Generación de nuevas preguntas o aplicaciones prácticas.",
    "🏁 Fin": "Fin del proceso científico."
}

info_mpdi = {
    "🏠 Empatizar y Contextualizar": "Etapa 1: Investigación de necesidades, contexto social y usuarios finales.",
    "❓ Definir el Problema": "Etapa 2: Definición clara del problema de diseño industrial.",
    "👨‍💻 💾 📲 🔗 Investigación Web y DeepSearch": "Etapa 3: Análisis de tendencias, materiales y casos similares.",
    "💡 ✨ Ideación y Conceptualización": "Etapa 4: Generación creativa de ideas con diversos métodos.",
    "✏️ 📝 🎨 📐 Bocetos, Render 2D y Prototipos 3D": "Etapa 5: Creación de modelos básicos para explorar forma y función.",
    "⚖️ 🔧 Evaluación Técnica": "Etapa 6: Análisis de viabilidad técnica, costos y usabilidad.",
    "⚙️ Iteración y Refinamiento": "Etapa 7: Mejora basada en pruebas y retroalimentación.",
    "📑 Documentación Técnica": "Etapa 8: Definición de especificaciones técnicas y planos.",
    "👤 Validación con Usuarios": "Etapa 9: Pruebas en contextos reales con humanos para verificar funcionalidad, estética, ergonomía, precios, etc.",
    "🏭 🔩 Producción y Fabricación": "Etapa 10: Implementación y lanzamiento al mercado.",
    "📢 👪 👤 Comunicación y Marketing para Usuarios": "Etapa 11: Estrategias de comunicación y marketing para promover el producto.",
    "🎯 Fin": "Fin del proceso de diseño industrial."
}

# Función para renderizar el diagrama Mermaid con ventanas emergentes
def render_mermaid_with_tooltips(diagram, info):
    mermaid_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <div class="mermaid" style="overflow: auto; max-height: 800px;">
    {diagram}
    </div>
    <script>
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    """
    # Crear ventanas emergentes para cada ícono
    tooltip_html = ""
    for icon, description in info.items():
        tooltip_html += f"""
        <div id="tooltip-{icon}" style="display:none; position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); background:white; padding:20px; border:1px solid #ccc; z-index:1000;">
            <h3>{icon}</h3>
            <hr>
            <p>{description}</p>
            <button onclick="document.getElementById('tooltip-{icon}').style.display='none';">Cerrar</button>
        </div>
        """
        mermaid_html = mermaid_html.replace(icon, f'<span onclick="document.getElementById(\'tooltip-{icon}\').style.display=\'block\';">{icon}</span>')

    # Añadir tooltips al HTML
    mermaid_html += tooltip_html
    components.html(mermaid_html, height=800, scrolling=True)

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

# Botones para seleccionar la metodología
option = st.selectbox(
    "Elige una metodología",
    ["MC-14: Método Científico", "MPDI: Diseño Industrial"]
)

# Mostrar el diagrama correspondiente
if option == "MC-14: Método Científico":
    st.subheader("MC-14: Método Científico")
    render_mermaid_with_tooltips(mc14_diagram, info_mc14)
elif option == "MPDI: Diseño Industrial":
    st.subheader("MPDI: Diseño Industrial")
    render_mermaid_with_tooltips(mpdi_diagram, info_mpdi)
