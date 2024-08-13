from pathlib import Path

import yaml
from openai import OpenAI
import streamlit as st
import streamlit_authenticator as stauth

from streamlit_authenticator import Hasher
from yaml import SafeLoader


BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "chatgpt_proxy_site" / "config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
)

name, authentication_status, username = authenticator.login("sidebar")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.write(f"Welcome *{name}*")
    st.title("💬 Chatbot")
    st.caption("🚀 A Streamlit chatbot powered by OpenAI")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        # if not openai_api_key:
        #     st.info("Please add your OpenAI API key to continue.")
        #     st.stop()

        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=st.session_state.messages
        )
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
