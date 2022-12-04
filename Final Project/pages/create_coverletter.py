import streamlit as st
import time
from coverletter import cover_letter     # coverletter function
from PIL import Image
from fpdf import FPDF
pdf = FPDF()
import pyautogui
 



file = 'png_logo.png'
c1, c2 = st.columns([2, 5])
image = Image.open(file)
image = image.resize((130,130))
c1.image(image)

c2.markdown("<h1 style='text-align: left; color: #36CC9B; font: 60px Georgia, sans-serif;'>Cover Letter</h1>", unsafe_allow_html=True)
c2.markdown('-AI Based Auto CV Generator')

'---'

col1, col2 = st.columns(2)
name = col1.text_input("Name")
job_title = col2.text_input("Job Title")
skills = st.text_area('Skills', height=200)



'---'


intro = 'name:'+name+'\n'+'job_title:'+job_title+'\n'+'skills:'+skills +'\ncover letter:'
cv_cover= name + ' | ' + job_title + '\n' + 'skills:\n'+ skills  + '\n\n'


def create_cover_letter(data, cv_cover):
        cv =cover_letter.cv(data)
        return cv_cover + cv + '\n'+name


create = st.checkbox('Create CV')

if create:
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    
    
    
    st.write("Wait a moment...")
    st.info('Edit Your Final text below', icon="ℹ️")
    text = create_cover_letter(intro, cv_cover)
    output = st.text_area('Cover letter', value=text, height=1000)
    st.success('Success', icon="✅")


    option = st.radio('Select',
    ('Select', 'All Good, Proceed', 'Not Satisfied'))

    if option == 'All Good, Proceed':
        f = open('data.txt', 'w')
        f.write(output)
        f.close()
        st.write('File is Getting Ready!')

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1)
    
    
        st.write('Almost there!')
        time.sleep(0.3)
        pdf.add_page()
        pdf.set_font("Arial", size = 10)
        pdf.add_font("Arial", "", "arial.ttf", uni=True)
        f = open("data.txt", "r")
        for x in f:
            pdf.multi_cell(w=0,h=5,txt = x, align = 'L',border=0)

        data = pdf.output("CV.pdf")
        st.success('PDF Created', icon="✅") 

        with open("CV.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="Download CV", 
                data=PDFbyte,
                file_name="FinalCV.pdf",
                mime='application/octet-stream')


        

    elif option == 'Not Satisfied':
        st.write('Do you want to reset the CV')
        if st.button('Reset'):
            
            pyautogui.hotkey("ctrl","F5")
        
            
    else:
        st.write('Please Select')
    


