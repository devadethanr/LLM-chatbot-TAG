import cohere 
import streamlit as st

co = cohere.Client('ECmZASmuWPzS4Np9LEgveRZkD9RZ3GTaD3li6rmJ') # This is your trial API key

import streamlit as st

st.title("Echo Bot")

# Initialize chat history
def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    init_state()
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})


#response check
    lim_response = co.chat(
        # message="hi"
        model = "command",
        message = "Hi",
    )
    print(lim_response)
    
    
    
if __name__ == "__main__":
    main()