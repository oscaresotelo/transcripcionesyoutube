
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
st.title("hola")
# Función para obtener la transcripción y mostrarla en pantalla
def obtener_transcripcion(video_id):
    try:
        vista = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
        transcripcion = '\n'.join(segmento['text'] for segmento in vista)
        st.text_area('Transcripción', value=transcripcion, height=400)
    except Exception as e:
        st.error(f'Ocurrió un error al obtener la transcripción: {e}')

# Interfaz de usuario con Streamlit
st.title('Obtener Transcripción de YouTube')
video_id = st.text_input('Ingrese el ID del video de YouTube:')
if st.button('Obtener Transcripción'):
    obtener_transcripcion(video_id)
