import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Test Teológico", page_icon="📖", layout="centered")

st.title("Test Teológico: ¿Qué crees vs. Dónde te congregas? 🏛️")
st.markdown("---")

# Diccionario con las 5 creencias completas
creencias = {
    "Creencia 1": "Yo estaba completamente muerto en mis delitos y pecados... (Él hizo todo el trabajo: me dio vida, cambió mi corazón y me regaló la fe).",
    "Creencia 2": "Dios me escogió primero porque Él es omnisciente. Miró a través del tiempo, vio que yo decidiría creer en Jesús por mi propia voluntad, y basado en eso me eligió.",
    "Creencia 3": "Si Dios no me hubiera buscado primero, yo jamás lo habría buscado. El Espíritu Santo tocó mi puerta, despertó mi libre albedrío, y como Dios vio en el futuro que yo diría que sí, me escogió.",
    "Creencia 4": "Dios no hizo una lista individual. Él escogió a Cristo y a 'La Iglesia'. Me convertí en escogido el día que usé mi libertad para creer y me subí a ese tren que Dios ya había preparado.",
    "Creencia 5": "Dios tomó la iniciativa absoluta y me amó primero, dándome Su gracia a través del Bautismo. Respeta mi libre albedrío y mi responsabilidad es cooperar activamente con esa gracia."
}

# Diccionario para mapear la creencia elegida con su teología real
identidad_teologica = {
    "Creencia 1": "Bautista Reformado / Calvinista",
    "Creencia 2": "Bautista Tradicional / Arminianismo Clásico",
    "Creencia 3": "Metodista / Pentecostal / Arminianismo Wesleyano",
    "Creencia 4": "Evangélico No Denominacional / Elección Corporativa",
    "Creencia 5": "Católico Romano"
}

st.subheader("1️⃣ Selecciona tu creencia")
st.write("Lee detenidamente y elige la opción que mejor represente lo que crees en tu corazón:")

# Selector de creencia
opcion_creencia = st.radio(
    "Selecciona una opción:",
    list(creencias.keys()),
    format_func=lambda x: f"{x}: {creencias[x]}"
)

st.markdown("---")

st.subheader("2️⃣ Selecciona tu congregación actual")
# Opciones de iglesias que coinciden con las teologías
iglesias = [
    "Iglesia Bautista Reformada / Presbiteriana / UCB",
    "Iglesia Bautista Tradicional (ej. PIBS Chile) / Evangélica Libre",
    "Iglesia Pentecostal (Asambleas de Dios, Metodista Pentecostal, etc.)",
    "Iglesia Comunitaria / No denominacional",
    "Iglesia Católica",
    "Otra / Ninguna"
]

opcion_iglesia = st.selectbox("¿A qué iglesia asistes actualmente?", iglesias)

st.markdown("---")

# Botón de evaluación y lógica de resultados
if st.button("Descubrir mi resultado 🔍", use_container_width=True):
    
    # 1. Mostrar la identidad teológica real de lo que seleccionó
    teologia_real = identidad_teologica[opcion_creencia]
    
    st.success(f"### Según lo que crees, tu teología es: **{teologia_real}**")
    
    # 2. Lógica de comparación cruzada
    # Evaluamos si hay coincidencia entre la creencia (1 a 5) y el índice del selectbox de iglesia
    indice_creencia = list(creencias.keys()).index(opcion_creencia)
    indice_iglesia = iglesias.index(opcion_iglesia)
    
    if indice_iglesia == 5: # Seleccionó "Otra / Ninguna"
        st.info("💡 Interesante. Tienes una postura teológica bien definida, independientemente de dónde te congregues actualmente.")
    elif indice_creencia == indice_iglesia: # Hay coincidencia exacta
        st.balloons()
        st.info(f"✅ **¡Coincidencia total!** Lo que crees personalmente está en perfecta sintonía con la doctrina oficial de la **{opcion_iglesia}** a la que asistes.")
    else: # No hay coincidencia
        st.warning(f"⚠️ **Contraste interesante:** Te identificas con la teología **{teologia_real}**, pero actualmente asistes a una **{opcion_iglesia}**. Es muy probable que tu postura personal difiera de lo que enseña oficialmente tu congregación sobre la salvación.")
