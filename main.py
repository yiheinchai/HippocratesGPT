import os

import openai
import streamlit as st
from langchain.chains import ChatVectorDBChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import NotionDirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)


@st.cache_resource
def generate_vectorstore():
    loader = NotionDirectoryLoader("NotionDB")
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index.vectorstore

@st.cache_resource
def generate_prompt():
    system_template="""Use the following pieces of context to answer the question.
    ----------------
    {context}"""

    messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}")
    ]
    return ChatPromptTemplate.from_messages(messages)


if 'history' not in st.session_state:
    st.session_state['history'] = []

# App 
st.header(":pink[HippocratesGPT]")
st.info("HippocratesGPT enables to you ask any question about medicine and get explanations!")

# Authentication
api_key = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = api_key

if api_key:
    # Use ChatGPT with index QA chain
    vectorstore = generate_vectorstore()
    llm = ChatOpenAI(temperature=0)
    prompt = generate_prompt()
    qa = ChatVectorDBChain.from_llm(ChatOpenAI(temperature=0), vectorstore,qa_prompt=prompt)
    print(prompt)

    question = st.text_area(":pink[What question do you have?:]", "Hi, I am a medical student requiring help.")

    try:
        result = qa({"question": question, "chat_history": st.session_state.history})
        st.session_state.history.append((question, result['answer']))
        st.subheader("Answer")
        for history in st.session_state.history[::-1]:
            st.markdown(history[1])
            st.info(history[0])
    except openai.error.InvalidRequestError:
        # Limitation w/ ChatGPT: 4096 token context length
        # https://github.com/acheong08/ChatGPT/discussions/649
        st.warning('Error with model request, often due to context length. Try reducing chunk size.', icon="⚠️")

else:
    st.info("`Please enter OpenAI Key to start`")