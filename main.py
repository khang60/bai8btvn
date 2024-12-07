import streamlit as st
with st.sidebar:
  image = 'assets/lovepik-dad-carrying-daughter-cartoon-png-image_401395167_wh1200.png'
  st.image(image,caption = "Dad")
  st.write('Họ và tên: Lương Cao Dũng')


st.title('Bài hát yêu thích')
st.write('Cha già rồi đúng không')
sound = open('assets/ChaGiaRoiDungKhong-PhamHongPhuoc-4721051.mp3', 'rb')
st.audio(sound, format = 'audio/mp3')
st.title('Video yêu thích')
st.write('Cha Và Con Gái')
video = 'https://www.youtube.com/watch?v=1Y0jeAPH_Pc'
st.video(video, format = 'video/mp4')
