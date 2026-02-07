import gradio as gr
from src.bot import ChatBot

# Initialize ChatBot
bot = ChatBot()

def chat_response(message, history):
    """
    Wrapper function for Gradio chat interface.
    """
    return bot.get_response(message)

# Create Gradio Interface
demo = gr.ChatInterface(
    fn=chat_response,
    title="🤖 Customer Support Bot",
    description="Ask me about orders, returns, and policies.",
    theme="soft",
    examples=["Where is my order?", "Return policy", "Payment failed"],
    retry_btn=None,
    undo_btn=None,
    clear_btn="Clear Chat"
)

if __name__ == "__main__":
    demo.launch()
