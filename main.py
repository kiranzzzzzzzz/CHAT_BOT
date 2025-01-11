import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


load_dotenv()


st.set_page_config(
    page_title="Chat with Kiran's Personal ChatBot",
    page_icon="🤖",
    layout="centered",
)


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    gen_ai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("Google API key is missing. Please set it in the environment variables.")


try:
    model = gen_ai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Failed to load Gemini-Pro model: {e}")
    st.stop()


def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role


if "chat_session" not in st.session_state:
    try:
        st.session_state.chat_session = model.start_chat(history=[])
    except Exception as e:
        st.error(f"Failed to start chat session: {e}")
        st.stop()


st.title("🤖 Kiran's ChatBot")



for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)



user_prompt = st.chat_input("Ask the bot...")
if user_prompt:
    
    st.chat_message("user").markdown(user_prompt)


    try:
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    except Exception as e:
        st.error(f"Error generating response: {e}")
