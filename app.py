import streamlit as st 
from langchain_ollama import ChatOllama
# %pip install -U langchain-ollama
#pip install langchain
st.title("Building a LangChain Chatbot with Ollama for Career Counselling !!!")
st.write("Hi Guys")

with st.form('llmform'):
    text=st.text_area("Enter your question or statement")
    submit=st.form_submit_button("submit")

def generate_response(input_text):
    model=ChatOllama(model='llama3.2')

    response=model.invoke(input_text)

    return response.content

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

if submit and text:
    with st.spinner('Generate response.....'):
        response=generate_response(text)
        st.session_state['chat_history'].append({"user": text,'ollama':response})
        st.write(response)

st.write("Chat History")
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**user**:{chat['user']}")
    st.write(f"**Assistance**:{chat['ollama']}")
    st.write("---")