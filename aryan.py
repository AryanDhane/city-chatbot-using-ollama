from langchain_ollama import ChatOllama
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv(override=True)

#-------------------------------------------------------------
# Streamlit page setup

st.set_page_config(page_title="Information ", page_icon="🎯")

st.title(" Information about City using langchain + ollama")

st.write(" Enter a City name and category (e.g., Information, location, temples) to get more information about it. ")

#--------------User Input Section--------------------------------

City = st.text_input(" Enter the name of the City: ")

category = st.text_input(" Enter the category (e.g., Information, location): ")

#----------------- Button to trigger the LLM call ----------------------

if st.button(" Get information "):
    if not City or not category:
        st.warning(" Please enter both product name and category.")
    else:
        with st.spinner(" Fetching information... "):
            try:
                prompt = ChatPromptTemplate.from_messages([
                ("system", "you are a helpful assistant."),
                ("user", "Tell me a information of {City} in 4 bulleted points in {category} and If you don't know the answer please Say I don't have any information about City/category")
                ])

                # llm = ChatOllama(model="llama3.2:latest")
                llm = GoogleGenerativeAI(model="gemini-2.5-pro")

                chain = prompt | llm

                response = chain.invoke({"City": City, "category": category})

                # Display the response
                st.write(response)

            except Exception as e:
                st.error(f"An error occurred: {e}")