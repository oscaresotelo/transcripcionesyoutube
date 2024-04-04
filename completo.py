
# import streamlit as st 
# from pytube import YouTube 
# from youtube_transcript_api import YouTubeTranscriptApi 
# from youtubesearchpython import VideosSearch , Search
# from huggingface_hub import InferenceClient 

# endpoint_url = "https://your-endpoint-url-here" 

# # Caché para resultados de búsqueda 
# @st.cache_data 
# def buscar_videos(palabra_clave): 
#     try: 
#         videos_search = Search(palabra_clave, limit=30) 
#         results = videos_search.result()['result'] 
#         # videos_info = [{'title': video['title'], 'image': video['thumbnails'][0]['url'], 'url': f"https://www.youtube.com/watch?v={video['id']}"} for video in results] 
#         videos_info = [{'title': video['title'], 'video': f"https://www.youtube.com/embed/{video['id']}", 'url': f"https://www.youtube.com/watch?v={video['id']}"} for video in results]
#         return videos_info 
#     except Exception as e: 
#         st.error(f'Ocurrió un error al buscar videos: {e}') 
#         return [] 

# # Función para obtener la transcripción y mostrarla en pantalla 
# def obtener_transcripcion(video_url): 
#     try: 
#         video_id = video_url.split('=')[-1] 
#         yt = YouTube(video_url) 
#         streams = yt.streams.filter(only_audio=True) 
#         if streams: 
#             audio_stream = streams[0] 
#             # audio_stream.download(filename='temp_audio') 
#             transcripcion = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en']) 
#             transcripcion_texto = '\n'.join(segmento['text'] for segmento in transcripcion) 
#             return transcripcion_texto 
#         else: 
#             st.error('No se pudo obtener el audio del video para generar la transcripción.') 
#     except Exception as e: 
#         st.error(f'Ocurrió un error al obtener la transcripción: {e}') 
#         return None 

# # Interfaz de usuario con Streamlit 
# st.title('Obtener Transcripción de YouTube') 

# # Validación de entrada de usuario 
# palabra_clave = st.text_input('Ingrese la palabra clave para buscar videos en YouTube:', value='') 
# if not palabra_clave: 
#     st.warning('Ingrese una palabra clave válida.') 
# else: 

#     # Búsqueda de videos 
#     videos = buscar_videos(palabra_clave) 
#     if videos: 
#         st.session_state.videos = videos 
#         st.write('Selecciona un video:') 
#         for video in videos: 
#             st.video(video['video']) 
#             if st.button(f"{video['title']}", key=video['title']): 
#                 st.session_state.video_url = video['url'] 
#                 resultado = obtener_transcripcion(video['url']) 
#                 transcripcion = "Resumir y explicar detalladamente con ejemplos en base al siguiente tema,  " + video['title'] + ",  si contiene algo relacionado a programacion extraer el codigo que meciona el siguiente texto : "   + resultado  
#                 if transcripcion: 
#                     headers = {"Authorization": "Bearer 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"} 
#                     prompt = f"[INST] {transcripcion} [/INST]" 
#                     client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1" , headers=headers) 
#                     response = client.text_generation(prompt, max_new_tokens=2500, do_sample=True, temperature=0.7, top_p=0.95, top_k=40, repetition_penalty=1.1) 
#                     st.write(f"Resumen: {response}") 
#                 else: 
#                     st.error('No se pudo generar la transcripción.') 
#                 break 
#     else: 
#         st.warning('No se encontraron videos con la palabra clave ingresada.')

import streamlit as st  
from pytube import YouTube  
from youtube_transcript_api import YouTubeTranscriptApi  
from youtubesearchpython import VideosSearch , Search 
from huggingface_hub import InferenceClient 
import pandas as pd  

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
                     .container {
                display: flex;
            }
            .logo-text {
                font-weight:700 !important;
                font-size:30px !important;
                color: black !important;
                padding-top: 50px !important;
            }
            .logo-img {
                float:right;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("estilos.css")

# Caché para resultados de búsqueda  
@st.cache_data 
def buscar_videos(palabra_clave):  
    try:  
        videos_search = Search(palabra_clave, limit=30)  
        results = videos_search.result()['result']  
        videos_info = [{'title': video['title'], 'image': video['thumbnails'][0]['url'], 'url': f"https://www.youtube.com/watch?v={video['id']}"} for video in results] 
        return videos_info  
    except Exception as e:  
        st.error(f'Ocurrió un error al buscar videos: {e}')  
        return []  

# Función para obtener la transcripción y mostrarla en pantalla  
def obtener_transcripcion(video_url):  
    try:  
        video_id = video_url.split('=')[-1]  
        yt = YouTube(video_url)  
        streams = yt.streams.filter(only_audio=True)  
        if streams:  
            audio_stream = streams[0]  
            transcripcion = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en'])  
            transcripcion_texto = '\n'.join(segmento['text'] for segmento in transcripcion)  
            return transcripcion_texto  
        else:  
            st.error('No se pudo obtener el audio del video para generar la transcripción.')  
    except Exception as e:  
        st.error(f'Ocurrió un error al obtener la transcripción: {e}')  
        return None  

# Interfaz de usuario con Streamlit  
st.title('Resumir desde  YouTube')  

# Validación de entrada de usuario  
palabra_clave = st.text_input('Ingrese la palabra clave para buscar videos en YouTube:', value='')  
if not palabra_clave:  
    st.warning('Ingrese una palabra clave válida.')  
else:  

    # Búsqueda de videos  
    videos = buscar_videos(palabra_clave)  
    if videos:  
        st.session_state.videos = videos  
        st.write('Resultados de la búsqueda:')  
        for video in videos:  
            col1, col2 = st.columns([1, 4])  
            with col1:  
                st.image(video['image'])  
            with col2:  
                st.write(f"**{video['title']}**")  
                st.markdown(f"[{video['url']}]({video['url']})")  
            if st.button(f"{video['title']}", key=video['title']): 
                with st.spinner('Resumiendo...'):
 
                    st.session_state.video_url = video['url']  
                    resultado = obtener_transcripcion(video['url'])  
                    transcripcion = "Resumir  el siguiente tema,  " + video['title'] + ",  si contiene algo relacionado a programacion extraer el codigo que meciona el siguiente texto : "   + resultado   
                    if transcripcion:

                        headers = {"Authorization": "Bearer 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"}  
                        prompt = f"[INST] {transcripcion} [/INST]"  
                        client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1" , headers=headers)  
                        response = client.text_generation(prompt, max_new_tokens=2500, do_sample=True, temperature=0.7, top_p=0.95, top_k=40, repetition_penalty=1.1)  
                        st.write(f"Resumen: {response}")  
                    else:  
                        st.error('No se pudo generar la transcripción.')  
                    break  
    else:  
        st.warning('No se encontraron videos con la palabra clave ingresada.')