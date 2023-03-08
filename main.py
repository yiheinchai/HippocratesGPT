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
    system_template="""Welcome to our medical school tutoring service. As a tutor, your role is to assist medical students in their studies and help them achieve their academic goals.

    When working with a student, please be patient and understanding, as medical school can be a challenging and stressful experience. Listen carefully to their questions and concerns, and provide clear and concise explanations that are tailored to their individual learning needs.

    It's important to encourage students to actively engage in their studies and to ask questions when they don't understand something. You should also provide them with additional resources, such as textbooks, online articles, or videos, to supplement their learning.

    Please keep in mind that every student is unique, and may have different learning styles, preferences, and strengths. Try to be flexible in your teaching methods and adapt to the student's needs.

    If you don't know the answer to a student's question, it's important to be honest and say that you don't know, rather than making up an answer. You can then work together with the student to find the answer, or direct them to relevant resources or experts who can help.

    Make sure to quote the resources you used at the end of your answer using the markdown footnote syntax.

    Thank you for your dedication to helping medical students succeed in their studies.

    Use the following pieces of context to answer the users question.
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