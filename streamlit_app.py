import streamlit as st
import openai

def response(p):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=p,
        temperature=0.8,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    return response.choices[0].text
    
def feedback(idea):
    prompt = f"Provide a detailed, constructive feedback on the following startup idea, focusing on its potential market impact, uniqueness, and scalability:\n\n{idea}"
    return response(prompt)

def critique(idea):
    prompt = f"Offer a detailed, critical analysis of the following startup idea, highlighting areas of potential concern, such as market competition, feasibility, and risk factors:\n\n{idea}"
    return response(prompt)

def idea():
    prompt = "Generate a detailed startup idea that addresses a current technology trend or market need, including its unique value proposition and potential customer base"
    return response(prompt)

#streamlit app interface
def main():
    
    st.markdown("<h1 style='text-align: center; color: white;'>FeedbackAI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'> FeedbackAI is a startup idea generator that can give you feedback and critique on your startup idea</p>", unsafe_allow_html=True)
    
    st.write('---')

    # Sidebar for API key input
    with st.sidebar:
        st.write("## API Key Configuration")
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        st.write("#### Built by [nixo](https://nixo.framer.website)")

    # Updating the API key in the session state
    if api_key:
        st.session_state["OPENAI_API_KEY"] = api_key
        openai.api_key = api_key
    else:
        openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else None

    # Check if the API key is set
    if openai.api_key is None:
        st.error("Please enter your OpenAI API key in the sidebar.")
        return
    
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