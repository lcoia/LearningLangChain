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


def call_llm(model, prompt_text):
    """
    Call the selected LLM with a prompt and return the response.

    Parameters:
    - model: a string
    - prompt_text: a string

    Returns:
    - LLM response: a string
    """
    match model:
        case "gpt-4o-mini":
            llm_response = OpenAI_model.invoke(prompt_text)
            print(llm_response)
            return llm_response.content
        case "llama3-70b-8192":
            llm_response = Groq_model.invoke(prompt_text)
            print(llm_response)
            return llm_response.content
        case _:
            return "Error: which model are you using?"


"""
Gradio Blocks for rendering web UI
    - Text box to enter the prompt.
    - Dropdown to select the AI model
    - Submit button to call the LLM
    - Output text box for displaying LLM output
"""
with gr.Blocks() as demo:
    prompt = gr.Textbox(label="Prompt", lines=7, show_label=True, interactive=True)
    ai_model = gr.Dropdown(
        label="AI Model",
        choices=['gpt-4o-mini', 'llama3-70b-8192'],
        value='llama3-70b-8192', interactive=True)
    submit_button = gr.Button("Submit")
    output = gr.Textbox(lines=9, show_label=True, label="Output")
    submit_button.click(call_llm, inputs=[ai_model, prompt], outputs=output)

demo.launch()
