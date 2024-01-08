import streamlit as st
from openai import OpenAI

def main():
    # Streamlit interface setup
    st.markdown("<h1 style='text-align: center; color: white;'>FeedbackAI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>FeedbackAI is a startup idea generator that can give you feedback and critique on your startup idea</p>", unsafe_allow_html=True)
    
    st.write('---')

    # Sidebar for API key input
    with st.sidebar:
        st.write("## API Key Configuration")
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        st.write("#### Built by [nixo](https://nixo.framer.website)")

    # Check if the API key is set
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
        return
    else:
        client = OpenAI(api_key=api_key)

    # Function to get response from OpenAI
    def get_response(client, prompt):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant specialized in analyzing and providing feedback on startup ideas. Generate innovative startup ideas, offer constructive feedback, and provide critical analysis with an emphasis on market viability, innovation, and potential challenges."},
                {"role": "user", "content": prompt}
            ])
        return completion.choices[0].message.content

    # Streamlit interface for input and buttons
    idea_input = st.text_input('Write your startup idea here')
    
    tab1, tab2, tab3 = st.tabs(['Get Feedback', 'Get Critique', 'Don’t have an idea?'])
    
    with tab1:
        if st.button('Submit for Feedback'):
            feedback_prompt = f"Provide detailed, constructive feedback on this startup idea:\n\n{idea_input}"
            st.write(get_response(client, feedback_prompt))

    with tab2:
        if st.button('Submit for Critique'):
            critique_prompt = f"Offer a critical analysis of this startup idea:\n\n{idea_input}"
            st.write(get_response(client, critique_prompt))

    with tab3:
        if st.button('Generate a new idea'):
            idea_prompt = "Generate a detailed startup idea that addresses a current technology trend or market need."
            st.write(get_response(client, idea_prompt))

if __name__ == '__main__':
    main()
