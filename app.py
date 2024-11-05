from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
 # .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("GOOGLE_API_KEY")

# API 키 설정
genai.configure(api_key=api_key)

st.set_page_config(page_title="Audio Summarizer of SON",page_icon="🤖")
 
st.header("Audio Summarizer Web Application of SON")
 
uploaded_audio = st.file_uploader("Upload an audio file to summarize",type=['mp3'])
 
if uploaded_audio is not None:
    ## Save the audio file to a temporary file
    audio_file_name = uploaded_audio.name
    with open(audio_file_name,"wb") as f:
        f.write(uploaded_audio.getbuffer())
 
    st.audio(audio_file_name)
 
    st.write("Uploading file...")
 
    audio_file = genai.upload_file(path=audio_file_name)
 
    st.write("Upload Completed : {}".format(audio_file.uri))
 
    st.write("Generating the summary....")
 
    prompt = """Listen carefully to the following audio file and provide the brief summary 
                in 200-250 words"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt,audio_file])
    st.write(response.text)