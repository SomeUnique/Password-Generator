import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")

st.markdown("""
## Welcome to the ultimate password strength checker! 👋  
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.  
We will give you helpful tips to create a **Strong Password**! 🔥
""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌Password should be 8 Character Long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else :
        feedback.append("❌Password should contain both Upper and Lower Case Characters.")

    if re.search(r'\d', password):
        score += 1
    else :
        feedback.append("❌Password should contain atleast one digit.")

    if re.search(r'[!@$%*&]', password):
        score += 1
    else:
        feedback.append("❌Password should contain atleast one Special Character(!@$%*&).")

    if score == 4:
        feedback.append("🎊 Your Password is strong! 🎊")

    elif score == 3:
        feedback.append("🟡 Your Password is not strong enough. It could be Stronger.")
    else :
        feedback.append("🔴 Your Password is Weak. Please make it Stronger.")

    if feedback:
        st.markdown("## Improvement suggestion")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")
