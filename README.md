# Hugging Face Language Model Chatbot

## Overview
This Streamlit web application serves as an interactive chatbot that utilizes a pre-trained language model from Hugging Face's `transformers` library. Users can input text messages, and the chatbot responds with generated text based on the input.

Deployment on Streamlit:
https://chatbot-hugging.streamlit.app/
## Features
- **User Text Input:** Users can type their messages into a text input field.
- **Language Model Response:** The app uses a pre-trained GPT-2 model from Hugging Face to generate responses to user input.
- **Response Display:** The chatbot's responses are displayed in a separate text area on the web page.

## Installation

Before you can run this app, you need to install the necessary dependencies. Here's how you can do it:

1. Make sure you have Python 3.6 or later installed. If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/).

2. Clone this repository to your local machine.

3. Navigate to the project directory in your terminal and create a virtual environment:

    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

5. Install the necessary packages:

    ```bash
    pip install -r requirements.txt
    ```
# Running the App

After you've installed the necessary packages, you can run the app with the following command:

```bash
streamlit run app.py
```
This will start the Streamlit server and open the app in your default web browser by navigating to the URL provided in the terminal (usually `http://localhost:8501`).

## Acknowledgements
- `Hugging Face` for providing the `transformers` library and pre-trained language models.
- `Streamlit` for the framework that was used to create this web application.
