# Podcast-Transcription

A tool for transcribing podcast episodes using AssemblyAI and ListenNotes APIs, and displaying them with Streamlit.

## Features
- Download podcast audio using ListenNotes API.
- Transcribe the podcast using AssemblyAI API.
- Display the podcast transcription and chapters using Streamlit.

## Tech Stack
- Python
- Streamlit
- AssemblyAI API
- ListenNotes API

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/podcast-transcription.git
    cd podcast-transcription
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your AssemblyAI and ListenNotes API keys to `api_secrets.py`:

    ```python
    API_KEY_ASSEMBLYAI = 'your-assemblyai-api-key-here'
    API_KEY_LISTENNOTES = 'your-listennotes-api-key-here'
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

2. In the sidebar, input the podcast episode ID you want to transcribe.

    <img width="397" alt="Screenshot 2024-09-24 at 16 48 58" src="https://github.com/user-attachments/assets/84e1331a-30cf-4799-ab61-9c9a372e412a">


4. The transcription and chapter summaries will be displayed in the app interface.
   
    <img width="917" alt="Screenshot 2024-09-24 at 16 49 32" src="https://github.com/user-attachments/assets/9e8dba5e-595f-45fc-b4cb-2a01d41a2c64">


