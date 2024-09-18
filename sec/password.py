import streamlit as st
import random

char_set_1 = '~!@#$%^&*()_+={[}]\\:;\'"<,>.?/'
char_set_1_mobile_friendly = '!@$&*()-:;",.?/'
char_set_2 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

st.title('Password Generator')

col1, col2 = st.columns(2)

with col1:
    is_mobile = st.checkbox('Mobile Friendly', value=True)
    length = st.slider('Password length', value=10, max_value=20)

with col2:
    chosen_set = char_set_1_mobile_friendly if is_mobile else char_set_1
    special_chars = st.text_input('Specials', value=chosen_set)
    char_set_2 = st.text_input('Numbers and Letters', value=char_set_2)

password_space = special_chars + char_set_2

def generate_password(space, length):
    return ''.join(random.SystemRandom().choice(space) for _ in range(length))

st.info(generate_password(password_space, length))
