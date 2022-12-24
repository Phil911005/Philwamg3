import streamlit as st
from PIL import Image
year_list={'2022','2021','2020','2019','2018'}
option_year=st.sidebar.selectbox("選擇年度",year_list)
type_list={'抒情歌曲':{'抒情','抒情1','抒情2','抒情3','抒情4','抒情5','抒情6','抒情7','抒情8','抒情9','抒情10'},'流行歌曲':{'流行1','流行2','流行3','流行4','流行5','流行6','流行7','流行8','流行9','流行10'},'搖滾歌曲':{'搖滾1','搖滾2','搖滾3','搖滾4','搖滾5','搖滾6','搖滾7','搖滾8','搖滾9','搖滾10'},'饒舌歌曲':{'饒舌1','饒舌2','饒舌3','饒舌4','饒舌5','饒舌6','饒舌7','饒舌8','饒舌9','饒舌10'},'民謠歌曲':{'民謠1','民謠2','民謠3','民謠4','民謠5','民謠6','民謠7','民謠8','民謠9','民謠10'}}
option_musiclist=st.sidebar.selectbox("選擇類型",type_list)  
option_music=st.selectbox("選擇音樂",type_list[option_musiclist])
audio_file = open(option_music+'.mp3', "rb")
st.audio(audio_file.read())
