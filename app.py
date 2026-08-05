import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Test Teológico", page_icon="📖", layout="centered")

st.title("Test Teológico: ¿Qué crees vs. Dónde te congregas? 🏛️")
st.markdown("---")

st.subheader("1️⃣ Lee las siguientes posturas")
st.write("Lee detenidamente estas 5 creencias y piensa cuál representa mejor lo que hay en tu corazón:")

# Mostramos los textos completos en bloques destacados
st.info("**Creencia 1:** Yo estaba completamente muerto en mis delitos y pecados; mi voluntad estaba esclavizada y jamás habría buscado a Dios por mi cuenta. Él no me escogió porque miró el futuro y vio que yo iba a creer; al contrario, la única razón por la que yo pude creer hoy, es porque Él me escogió desde la eternidad por pura gracia inmerecida (Elección Incondicional). Él hizo todo el trabajo: me dio vida, cambió mi corazón de piedra por uno de carne (Llamamiento Eficaz) y me regaló la fe. Mi salvación es obra 100% suya de principio a fin, y como es obra suya, no la puedo perder.")

st.info("**Creencia 2:** Dios me escogió primero porque Él es omnisciente. Antes de crear el universo, Él miró a través del corredor del tiempo (Conocimiento Previo / Presciencia) y vio exactamente el día y la hora en que yo iba a escuchar el Evangelio y decidiría creer en Jesús por mi propia voluntad. Basado en esa fe que Él vio que yo iba a tener, me eligió. Y a diferencia de otros, yo creo que una vez que tomé esa decisión y nací de nuevo, mi salvación está blindada; soy salvo para siempre y no puedo perder mi salvación por un error.")

st.info("**Creencia 3:** Si Dios no me hubiera buscado primero, yo jamás lo habría buscado a Él. Yo estaba ciego, pero Dios derramó su gracia (Gracia Preveniente) y el Espíritu Santo tocó la puerta de mi corazón. Esa ayuda divina despertó mi libre albedrío para que yo pudiera elegir. Dios me escogió desde antes de la fundación del mundo porque, al mirar el futuro, vio que yo iba a aprovechar esa ayuda y le iba a decir que sí. Y así como tuve la libertad de decirle que sí, debo cuidarme, porque tengo la libertad de alejarme y perder mi salvación.")

st.info("**Creencia 4:** Dios no hizo una lista con nombres y apellidos individuales antes de crear el mundo, decidiendo quién se salva y quién no. Lo que Dios escogió desde el principio fue a Cristo y a un grupo: 'La Iglesia' (Elección Corporativa). Él me amó primero al crear ese plan de salvación y abrir la puerta. Yo me convertí en un 'escogido' el día en que escuché el mensaje, usé mi libertad para creer en Jesús, y me subí a ese tren que Dios ya había escogido. Cualquiera que decida subirse a ese tren, se vuelve parte de los escogidos.")

st.info("**Creencia 5:** Dios tomó la iniciativa absoluta de mi salvación y me amó primero, dándome Su gracia, la cual recibí inicialmente a través del sacramento del Bautismo. Él llama a toda la humanidad a la salvación y nos da la gracia necesaria para poder responderle. Creo que Dios predestina al cielo, pero rechazo totalmente que Dios predestine a alguien al infierno; Él respeta mi libre albedrío. Por lo tanto, mi responsabilidad es 'cooperar' libre y activamente con esa gracia todos los días mediante la fe, los sacramentos y las buenas obras. Y sí, si cometo un pecado mortal y decido alejarme de Dios sin arrepentirme, puedo perder la gracia de la salvación.")

st.markdown("---")

st.subheader("2️⃣ Selecciona tu creencia")
# Botones simples y limpios
opcion_creencia = st.radio(
    "¿Con cuál de las opciones de arriba te identificas más?",
    ["Creencia 1", "Creencia 2", "Creencia 3", "Creencia 4", "Creencia 5"]
)

st.markdown("---")

st.subheader("3️⃣ Selecciona tu congregación actual")
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

identidad_teologica = {
    "Creencia 1": "Bautista Reformado / Calvinista",
    "Creencia 2": "Bautista Tradicional / Arminianismo Clásico",
    "Creencia 3": "Metodista / Pentecostal / Arminianismo Wesleyano",
    "Creencia 4": "Evangélico No Denominacional / Elección Corporativa",
    "Creencia 5": "Católico Romano"
}

if st.button("Descubrir mi resultado 🔍", use_container_width=True):
    teologia_real = identidad_teologica[opcion_creencia]
    
    st.success(f"### Según lo que crees, tu teología es: **{teologia_real}**")
    
    indice_creencia = list(identidad_teologica.keys()).index(opcion_creencia)
    indice_iglesia = iglesias.index(opcion_iglesia)
    
    if indice_iglesia == 5:
        st.info("💡 Interesante. Tienes una postura teológica bien definida, independientemente de dónde te congregues actualmente.")
    elif indice_creencia == indice_iglesia:
        st.balloons()
        st.info(f"✅ **¡Coincidencia total!** Lo que crees personalmente está en perfecta sintonía con la doctrina oficial de la **{opcion_iglesia}** a la que asistes.")
    else:
        st.warning(f"⚠️ **Contraste interesante:** Te identificas con la teología **{teologia_real}**, pero actualmente asistes a una **{opcion_iglesia}**. Es muy probable que tu postura personal difiera de lo que enseña oficialmente tu congregación sobre la salvación.")
