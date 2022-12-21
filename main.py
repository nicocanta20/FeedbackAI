import streamlit as st
import openai

def response(p):
    #import the api key from toml file
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=p,
        temperature=0.8,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    return response.choices[0].text
    
def feedback(idea):
    prompt = "make a detail constructive feedback of the following startup idea:" + idea
    return response(prompt)

def critique(idea):
    prompt = "make a detail hard critique of the following startup idea:" + idea 
    return response(prompt)

def idea():
    prompt = "return one detailed startup idea"
    return response(prompt)

#streamlit app interface
def main():
    st.markdown("<h1 style='text-align: center; color: white;'>FeedbackAI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'> FeedbackAI is a startup idea generator that can give you feedback and critique on your startup idea</p>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white;'>built by @nixo (with GPT-3)</h5>", unsafe_allow_html=True)
    st.write('---')
    #make an input to write the idea
    idea_input = st.text_input('Write your startup idea here')
    #make two tabs for feedback and critique
    tab1,tab2,tab3 = st.tabs(['Get Feedback','Get Critique','Dont have an idea?'])
    with tab1:
        if st.button('Submit',key='feedback'):
            st.write(feedback(idea_input))
    with tab2:
        if st.button('Submit',key='critique'):
            st.write(critique(idea_input))
    with tab3:
        if st.button('Generate a new idea'):
            st.write(idea())

if __name__ == '__main__':
    main()