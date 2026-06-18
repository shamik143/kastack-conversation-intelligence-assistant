import streamlit as st
from src.chatbot import PersonaChatbot

st.set_page_config(
    page_title="Conversation Intelligence Assistant",
    page_icon="🤖",
    layout="wide"
)

bot = PersonaChatbot()

st.title("🤖 Conversation Intelligence Assistant")

st.markdown(
    "Topic Checkpoints • Persona Extraction • ChromaDB Retrieval • Semantic Search"
)

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Conversations", "11,000")

with col2:
    st.metric("Messages", "191,578")

with col3:
    st.metric("Topics", "25,516")

with col4:
    st.metric("Checkpoints", "1,916")

st.divider()

query = st.text_input(
    "Ask a Question",
    placeholder="Example: What kind of person is this user?"
)

if st.button(
    "🚀 Ask Chatbot",
    use_container_width=True
):

    if query:

        with st.spinner(
            "Analyzing conversations..."
        ):

            response = bot.answer(
                query
            )

        st.subheader(
            "📌 Response"
        )

        with st.container(
            border=True
        ):

            st.markdown(
                response
            )

    else:

        st.warning(
            "Please enter a question."
        )

st.divider()

st.info(
    "This system processes conversations chronologically, generates topic checkpoints, extracts user personas, and performs semantic retrieval using ChromaDB."
)