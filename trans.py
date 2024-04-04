from youtube_transcript_api import YouTubeTranscriptApi

vista = YouTubeTranscriptApi.get_transcript('05xvP8m1xFk', languages=['es'])

# Crear un archivo TXT para escribir la transcripción
with open('transcripcion.txt', 'w', encoding='utf-8') as archivo:
    for segmento in vista:
        texto = segmento['text']
        archivo.write(texto + '\n')

print('Transcripción guardada en transcripcion.txt')
# import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi

# # Función para obtener la transcripción y mostrarla en pantalla
# def obtener_transcripcion(video_id):
#     try:
#         vista = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
#         transcripcion = '\n'.join(segmento['text'] for segmento in vista)
#         st.text_area('Transcripción', value=transcripcion, height=400)
#     except Exception as e:
#         st.error(f'Ocurrió un error al obtener la transcripción: {e}')

# # Interfaz de usuario con Streamlit
# st.title('Obtener Transcripción de YouTube')
# video_id = st.text_input('Ingrese el ID del video de YouTube:')
# if st.button('Obtener Transcripción'):
#     obtener_transcripcion(video_id)
