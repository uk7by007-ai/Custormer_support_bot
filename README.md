# Customer Support Chatbot

A simple AI-powered customer support chatbot that answers FAQs using TF-IDF and Cosine Similarity. The bot is trained on a dataset of common e-commerce questions (`data/faq.csv`).

## Features
- **Natural Language Understanding**: Uses TF-IDF to understand user queries.
- **FAQ Matching**: Matches user questions to the most relevant FAQ answer.
- **Multiple Interfaces**:
  - **Streamlit**: A modern web interface.
  - **Gradio**: A simple chat interface.

## Installation

1. Clone the repository (if you haven't already).
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Streamlit App
To run the Streamlit interface:

```bash
streamlit run app_streamlit.py
```

### Running the Gradio App
To run the Gradio interface:

```bash
python app_gradio.py
```

### Running Tests
To run the unit tests:

```bash
python -m unittest test_bot_logic.py
```

## Project Structure
- `src/bot.py`: Core chatbot logic class.
- `data/faq.csv`: The dataset containing questions and answers.
- `app_streamlit.py`: Streamlit application file.
- `app_gradio.py`: Gradio application file.
- `test_bot_logic.py`: Unit tests for the chatbot.
