import streamlit as st

st.title('seller page')

import streamlit as st

with st.form("my_form"):
   st.write('Generates image and description for the entered product')
   product = st.text_input("Enter product name")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
    st.write('Product is ', product)
    st.write('Product Description is')
    st.write('Product Image is')


