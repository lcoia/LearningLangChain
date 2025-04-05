from langchain_groq.chat_models import ChatGroq
from langchain_openai.chat_models import ChatOpenAI
import gradio as gr
from dotenv import load_dotenv
import os


# Load environment variables from the .env file
load_dotenv()

# Instantiate LLM models. Choose low cost or free models.
OpenAI_model = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
Groq_model = ChatGroq(model="llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))


response = Groq_model.invoke("The sky is")


with gr.Blocks() as demo:
    prompt = gr.Textbox(label="Prompt", lines=7, show_label=True, interactive=True)
    ai_model = gr.Dropdown(
        label="AI Model",
        choices=['gpt-4o-mini', 'llama3-70b-8192'],
        value='llama3-70b-8192', interactive=True)
    submit_button = gr.Button()

demo.launch()
# print(response.content)
