import streamlit as st
from PIL import Image
st.set_page_config(
    page_title = "Cover Letter Generator",
    page_icon = '📃🖊️',
)
file = 'png_logo.png'
c1, c2 = st.columns([2, 5])
image = Image.open(file)
image = image.resize((130,130))
c1.image(image)

c2.markdown("<h1 style='text-align: left; color: #36CC9B; font: 90px Segoe Script;'>Feather</h1>", unsafe_allow_html=True)
c2.markdown('-AI Based Auto CV Generator')
'---'

st.subheader('Cover Letter')
a1, a2 = st.columns(2)
image1 = Image.open('cv2.png')
a1.image(image1)
image2 = Image.open('cv3.png')
a2.image(image2)
image4 = Image.open('cv4.png')
a2.image(image4)

a1.subheader('🧑‍🎓Profile')
a1.subheader('📃Skills')
a1.subheader('🎯Body')
a1.subheader('🧑‍🎓Conclusion')

'---'

st.subheader('Resume')
b1, b2 = st.columns(2)
image1 = Image.open('resume1.png')
b1.image(image1)
image2 = Image.open('Resume2.jpeg')
b2.image(image2)
