import streamlit as st
from src.bot import ChatBot

# Page Configuration
st.set_page_config(
    page_title="Customer Support Bot",
    page_icon="🤖",
    layout="centered"
)

# Initialize ChatBot
@st.cache_resource
def get_chatbot():
    return ChatBot()

bot = get_chatbot()

# Header
st.title("🤖 Customer Support Assistant")
st.markdown("Ask me anything about your order, delivery, or returns!")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = bot.get_response(prompt)
            st.markdown(response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
