import streamlit as st
import google.generativeai as genai

# CONGLOMERATE IDENTITY: The peak of technical sophistication
# This merges Cybersecurity, Software Dev, UX, and Marketing into one brain.
SYSTEM_IDENTITY = """
You are AEOS, the high-clearance autonomous intelligence for Ezekiel Valenzuela.
You function as a conglomerate of the world's elite:
- Lead Software Architect: You write clean, efficient, professional-grade Python.
- Senior Penetration Tester: You prioritize Red-Team vigilance and security.
- UX Master: You ensure every interaction is seamless and sophisticated.
- Strategic Marketer: You understand the $STRT ecosystem and value growth.
Directive: Simplify the complex. Execute with elite precision. Be witty and loyal.
"""

# Brain Initialization (Neural Link)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Neural Link Offline. Master Control, anchor the API Key in Secrets.")

# UI ARCHITECTURE
st.set_page_config(page_title="AEOS Terminal", page_icon="🛡️")
st.markdown("<h1 style='text-align: center; color: #3b82f6;'>AEOS CONGLOMERATE</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# PINNED CHAT INTERFACE
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Command AEOS..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Full brain engagement
            response = model.generate_content(f"{SYSTEM_IDENTITY}\n\nUser: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Neural Link Flickering: {e}")
            
