import streamlit as st 
import random

char_set_1 = ''! @#$%^&*()_+={[}] [\:;"\'<,>.?/'
char_set_1_mobile_friendly = ''!@$&*()-:;",.?/"
char_set_2 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

st.title(' Password Generator')

coll, col2 st.columns(2)

with coll:
is_mobile st.checkbox('Mobile Friendly', value=True) length = st.slider('Password length', value=10, max_value=20)

with col2:

chosen_set char_set_1 char_set_1_mobile_friendly if is_mobile else char_set_1 st.text_input('Specials', value=chosen_set) char_set_2 = st.text_input('Numbers and Letters', value=char_set_2)

password_space char_set_1 + char_set_2

def generate_password(space, length): for in range(length): yield random. SystemRandom().choice(space)

st.info('.join(generate_password(password_space, length)))