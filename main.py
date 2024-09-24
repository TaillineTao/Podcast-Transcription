import streamlit as st
import glob
import json
from api_04 import save_transcript

st.title("Podcast Summaries")

# Fetch all json files in the directory
json_files = glob.glob('*.json')

episode_id = st.sidebar.text_input("Episode ID")
button = st.sidebar.button("Download Episode summary", on_click=save_transcript, args=(episode_id,))

def get_clean_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_t = f'{minutes:02d}:{seconds:02d}'
    return start_t

# Only proceed if button is clicked
if button:
    filename = episode_id + '_chapters.json'
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        # Safely extract the keys using `.get()`
        chapters = data.get('chapters', [])
        episode_title = data.get('episode_title', 'Unknown Title')
        thumbnail = data.get('thumbnail', None)
        podcast_title = data.get('podcast_title', 'Unknown Podcast')
        audio = data.get('audio_url', None)
        
        # Display the podcast and episode details
        st.header(f"{podcast_title} - {episode_title}")
        if thumbnail:
            st.image(thumbnail, width=200)
        st.markdown(f'#### {episode_title}')
        
        # Loop through chapters and display their gist and summaries
        if chapters:
            for chp in chapters:
                with st.expander(chp.get('gist', 'No Gist') + ' - ' + get_clean_time(chp.get('start', 0))):
                    st.write(chp.get('summary', 'No summary available'))
        else:
            st.write("No chapters available.")
    
    except FileNotFoundError:
        st.error(f"File {filename} not found.")
    except json.JSONDecodeError:
        st.error("Error reading the JSON file. It might be malformed.")
    except KeyError as e:
        st.error(f"KeyError: Missing key {str(e)} in the JSON data.")
