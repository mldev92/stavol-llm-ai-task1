import os
from dotenv import load_dotenv
import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from serpapi import GoogleSearch
from langchain.prompts import PromptTemplate

load_dotenv()
# Set environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_PROJECT"] = "bdf_task"
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

# Initialize conversation memory and LLM
memory = ConversationBufferMemory(return_messages=True)
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
prompt_template = PromptTemplate(
    input_variables=["combined_input"],
    template="""
    Below is the conversation history between a user and the assistant
    Information:
    {combined_input}
    Based on the above context, provide a helpful and updated response to the user's question.
    """
)

conversation_chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)

def web_search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv('SERP_API_KEY'),
        "num": 3
    }
    search = GoogleSearch(params)
    results = search.get_dict().get("organic_results", [])
    snippets = [result['snippet'] for result in results if 'snippet' in result]
    return snippets


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "input_ready" not in st.session_state:
    st.session_state.input_ready = False

st.title("AI Chatbot with Web Search Integration")
st.write("Press 'New question' and enter your question to get a response.")

# Display conversation history above the input field
st.write("### Chat History:")
for message in st.session_state.chat_history:
    st.markdown(f"**User**: {message['user']}")
    st.markdown(f"**Bot**: {message['bot']}")

# Process the user input and generate bot response if input is provided
if st.session_state.input_ready:
    # Get snippets from web search
    snips = web_search(st.session_state.user_input)

    # Compile the conversation context
    conversation_context = "\n".join(
        [f"User: {msg['user']}\nBot: {msg['bot']}" for msg in st.session_state.chat_history]
    )
    combined_input = "Search Snippets: " + " ".join(snips) + "\nConversation Context: " + conversation_context + "\nUser's Latest Question: " + st.session_state.user_input

    # Generate a response
    with st.spinner("Generating response..."):
        summarized_response = conversation_chain.invoke({"combined_input": combined_input})

    # Display the bot's response
    st.write("User: ", st.session_state.user_input)
    st.write("Bot: ", summarized_response['text'])

    # Save the conversation to session state and memory
    st.session_state.chat_history.append({"user": st.session_state.user_input, "bot": summarized_response['text']})
    memory.save_context({"input": st.session_state.user_input}, {"output": summarized_response['text']})

    st.session_state.input_ready = False
    st.session_state.user_input = ""

@st.dialog("New question", width='large')
def show_dialog():
    user_input_temp = st.text_input("Your question:", value="" if st.session_state.input_ready else None)

    if st.button("Submit"):
        if user_input_temp.strip() != "":  # Ensure the input is not empty
            # Save the user input to session state and set the flag for processing
            st.session_state.user_input = user_input_temp
            st.session_state.input_ready = True  # Indicate that input is ready for processing

        st.rerun()

# Open the dialog when the button is clicked.
if st.button("New question"):
    show_dialog()