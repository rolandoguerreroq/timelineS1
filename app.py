import streamlit as st
st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
st.title("Modelo de Predicción de tipo de cambio PEN a USD")
st.write("Autor: Rolando Guerrero - Grupo 04 | ISIL")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la IA.")
# URLs de imágenes en GitHub
base_url = "https://raw.githubusercontent.com/rolandoguerreroq/timelineS1/main/timeline_images/"
imagenes = {
   1: base_url + "timeline1.png",
   2: base_url + "timeline2.png",
   3: base_url + "timeline3.png",
   4: base_url + "timeline4.png",
   5: base_url + "timeline5.png"
}
# Slider
opcion = st.slider(
 "Selecciona un punto del timeline",
 min_value=1,
 max_value=5,
 value=1,
 step=1
)
# Mostrar imagen según slider
st.image(imagenes[opcion], use_container_width=True)
if opcion == 1:
 st.info(" **1990 – Modelos Estructurales**")
 st.info("**Descripción:** Se basan en la teoría económica (ej. modelos de equilibrio general estocástico, modelos IS-LM de economía abierta) para relacionar el tipo de cambio con fundamentales macroeconómicos (tasas de interés, balanza de pagos, términos de intercambio, oferta y demanda monetaria).")
 st.info("**Implementación Clave:** El BCRP ha desarrollado y actualizado modelos macroeconómicos de proyección, como el Modelo de Proyección Trimestral (MPT), que incluyen la determinación del tipo de cambio.")
if opcion == 2:
 st.info(" **(Desde los '90 - 2000) Modelos Econométricos de Series de Tiempo**")
 st.info("**Descripción:** Se enfocan en el patrón estadístico de la propia serie histórica del tipo de cambio, ignorando (en su forma simple) los fundamentos económicos.")
 st.info("**Implementación Clave:** Han sido ampliamente utilizados en la investigación académica (universidades) y como referencia base para la predicción en el BCRP.")
if opcion == 3:
 st.info(" **(Desde los 2000 - 2010) – Modelos de Aprendizaje Automático/Redes Neuronales**")
 st.info("**Descripción:** Algoritmos de Machine Learning que buscan patrones complejos y no lineales en los datos, a menudo superando las limitaciones de supuestos de los modelos tradicionales.")
 st.info("**Implementación Clave:** Principalmente en la investigación del BCRP y en trabajos de tesis universitarias.")
if opcion == 4:
 st.info(" **(Desde 2010 a la fecha) – Híbridos / Ensamble**")
 st.info("**Descripción:** Los modelos que combinan la estructura lineal (como ARIMA para la tendencia) con la no linealidad (como Redes Neuronales para los residuos) o aquellos que combinan predicciones de múltiples modelos (modelos de Ensamble o Ensemble forecasting) son los que han mostrado la mayor robustez y precisión en estudios recientes para series de tiempo complejas como el tipo de cambio.")
if opcion == 5:
 st.info(" **(Desde 2010 a la fecha) – Modelos de Aprendizaje Profundo (Deep Learning)**")
 st.info("**Descripción:** Específicamente, las Redes Neuronales Recurrentes (RNN) o LSTM (Long Short-Term Memory) han ganado tracción. Estos modelos son excelentes para manejar secuencias de datos (series de tiempo) y capturar dependencias a largo plazo, lo que los hace prometedores para la predicción financiera.")
