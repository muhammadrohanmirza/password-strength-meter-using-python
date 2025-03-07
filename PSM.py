import streamlit as st
import random
import string
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check uppercase & lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use both uppercase and lowercase letters.")

    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one digit (0-9).")

    # Check special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Use at least one special character (!@#$%^&*).")

    # Determine strength level
    if score == 4:
        return "✅ Strong Password! 👍", "green"
    elif score == 3:
        return "⚠️ Moderate Password. Try adding more complexity.", "orange"
    else:
        return "❌ Weak Password! " + " ".join(feedback), "red"

# Function to generate a strong password
def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Input password
password = st.text_input("Enter your password:", type="password")

if password:
    message, color = check_password_strength(password)
    st.markdown(f'<p style="color:{color}; font-size:18px;">{message}</p>', unsafe_allow_html=True)

# Password Generator Section
st.subheader("🔑 Generate a Strong Password")

# Slider for password length (6 to 35)
password_length = st.slider("Select password length:", min_value=6, max_value=35, value=12)

if st.button("Generate Password"):
    strong_password = generate_password(password_length)
    
    # Show password
    st.code(strong_password, language="plaintext")
    
    # Show warning for passwords below 12 characters
    if password_length < 12:
        st.warning("⚠️ You can copy the password at your own risk.")
    else:
        st.success("✅ Your password is secure.")

