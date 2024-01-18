import streamlit as st
import time

st.set_page_config(page_title="Email App", page_icon="📧", layout="centered")
st.header("Email App")
    
st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# st.image("kid.jpg")
# st.audio("Audio.mp3")
# st.video("video.mp4")

st.checkbox('yes')
st.button('Click')
# st.radio('Pick your gender',['Male','Female'])
# st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):    
	time.sleep(3)
 
st.success("You did it !")
st.error("Error")
st.warning("This is a warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click me")
st.sidebar.radio("Pick your gender", ["Male", "Female"])

container = st.container()
container.write("This is inside the container")
st.write("This is outside the container")