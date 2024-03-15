import streamlit as st
import pdf2image
from io import BytesIO
import base64
from PIL import Image


st.header("PDF to Image Conversion GUI")

upload = st.file_uploader("Choose an PDF:", type=[".pdf"])
if upload is not None:
    name = upload.name
    name = name[:-4]

options = ['JPEG', 'PNG']
output_type = st.selectbox("Output Type:", options, index=0, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
if output_type == 'JPEG':
    ext = 'jpg'
else:
    ext = 'png'

size = st.number_input("Size:")
dpi = st.number_input("DPI:")

button = st.button("Confirm")

if button and upload is not None:

    if upload.type == "application/pdf":
        images = pdf2image.convert_from_bytes(pdf_file=upload.read(), size=size)
        for i, page in enumerate(images):

            st.subheader("Preview:")
            st.image(page, use_column_width=True)
            
            img = page
            buf = BytesIO()
            img.save(buf, format=output_type, dpi=(dpi, dpi))
            byte_im = buf.getvalue()
            st.download_button("Download", data=byte_im, file_name=f"{name}.{ext}")
