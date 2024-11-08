### AI Chatbot with Web Search Integration

This project is a conversational AI chatbot built using Streamlit, LangChain, and OpenAI's GPT-4 model, with real-time web search capabilities integrated through SerpApi. The bot can remember the context of conversations, answer questions, and retrieve up-to-date information from the web as needed.

**Features**

   - Conversational Memory: Remembers the context of previous messages to generate coherent and contextually aware responses.
   - Web Search Integration: Uses SerpApi to perform Google searches for up-to-date information, enhancing responses with relevant snippets.
   - Streamlit Interface: Simple, interactive user interface for engaging with the chatbot.
   - Environment Configuration: .env file is used to store sensitive API keys securely.

**Project Structure**

   * **`app4.py`** - Main application file that sets up the Streamlit chatbot.
   * **`.env`**    - Environment file for sensitive information, including API keys.
   * **`Dockerfile`**     - Docker configuration file for containerizing the application.

**Getting Started**

***Prerequisites***

  *  Python 3.8 or later
  *  Docker (optional, for containerized deployment)

**Installation**

  1. Clone the Repository:

```bash
git clone https://github.com/your-username/assignment-llm-ai-task.git
```
```bash
cd stavol-llm-ai-task1
```

**Set Up Environment Variables:**

   * Create a .env file in the root directory of the project with the following variables:
```makefile
LANGCHAIN_API_KEY=your_langchain_api_key
OPENAI_API_KEY=your_openai_api_key
SERP_API_KEY=your_serpapi_key
```
   * Replace your_langchain_api_key, your_openai_api_key, and your_serpapi_key with your actual API keys.

**Install Dependencies:**

   * Use requirements.txt (if provided) or install dependencies manually:
```bash
pip install -r requirements.txt
```
#### Running the Application Locally
```bash
Run Streamlit:
streamlit run app4.py
Access the app in your browser at http://localhost:8501.
```
**Docker Setup**

    Build the Docker Image:

docker build -t my-streamlit-chatbot .

**Run the Docker Container:**

    docker run -p 8501:8501 --env-file .env my-streamlit-chatbot

    Open your browser to http://localhost:8501 to interact with the bot.

**Usage**

    Click on "New question" to start a new conversation.
    Enter your question in the dialog box and press "Submit".
    The bot will respond based on both previous conversation history and web search results if relevant information is found online.

**Example Workflow**

    User: What is the capital of France?
    Bot: The capital of France is Paris.
    User: What is the population of Paris?
    Bot: According to recent data, Paris has a population of approximately 2.1 million.

In this example, the bot remembers context and can conduct web searches if necessary.
Configuration and Customization

    Modify Prompt Template: Change the template in app4.py to customize the bot’s response style.
    API Keys: Manage API keys in .env for enhanced security and flexibility.

**Dependencies**

See requirements.txt for a complete list of dependencies.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

For questions or collaboration, please contact stavolpro@gmail.com
