import streamlit as st
from PIL import Image, ImageOps
#import pytesseract
import numpy as np
import tensorflow as tf
#pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def app():
  @st.cache(allow_output_mutation=True)
  def load_model():
    model=tf.keras.models.load_model('Digit_recognizer_model.hdf5')
    return model
  with st.spinner('Model is being loaded..'):
    model=load_model()
    
    st.write("""
          # Image Text/Digit Recognition
          """
          )

    file = st.file_uploader("Please upload a file", type=["jpg", "png","jpeg"])
    #def image_to_text(image_data):
        #text = str(pytesseract.image_to_string(Image.open(file)))
    #    return text
    def import_and_predict(img):
      #img = Image.open(img)
      #plt.imshow(img)
      img = img.convert('L', dither=Image.NONE)
      img = img.resize((28,28))
      img = np.array(img)
      img=np.invert(img)
      predicted=np.argmax(model.predict(img.reshape(-1,28,28,1)))
    # plt.imshow(img,interpolation='nearest')
      return predicted  
    if file is None:
      st.write("""
      #### Please upload an image file""")
    else:
      image = Image.open(file)
      image.thumbnail((700,700))
      st.image(image)
      #string = str(image_to_text(file))
      string=import_and_predict(image)
      st.write("**The digit is **")
      st.write("""
      ## {}
      """.format(string))
      #print(string)

