# tarea
import streamlit as st
st.title("mi primera aplicacion de streamlit")
st.subheader("¡hola, streamlit!")

#inicio de la barra lateral 
st.sidebar.title("mi primera barra lateral de streamlit")
st.sidebar.text("¡hola, barra lateral!")

#Area principal
st.text("esta es una aplicacion simple")
st.image("https://researchers.uss.cl/skin/footerIcon/", width=250)

#Boton de area principal
if st.button("haz click"):
  st.write("¡Boton presionado!")

#Campo de texto del area principal
nombre_texto = st.text_input("escribe algo:")
st.write(f"escribiste: {nombre_texto}")

#barra lateral
st.sidebar.text("Esto es una barra lateral")
st.sidebar.image("https://researchers.uss.cl/skin/footerIcon/", width=200)

#boton de la barra
if st.sidebar.button("haz click pero en la barra lateral"):
  st.sidebar.write("¡Boton de la barra presionada!")

#Campo de texto de la barra lateral
texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
st.sidebar.write(f"Escribiste en la barra: {texto_barra}")
