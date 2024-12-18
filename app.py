import streamlit as st
import whisper
import tempfile
import os

os.system("ffmpeg -version")

# Load the Whisper model
model = whisper.load_model("base")

# Title of the Streamlit App
st.set_page_config(page_title="ASR", layout="wide")
st.markdown("""
    <h1 style="text-align: start; display: inline-block; border-bottom: 1px solid #ef233c; padding-bottom: 3px; width: 100%; max-width: 10800px;">
        Advanced Speech Recognition
    </h1>
""", unsafe_allow_html=True)
st.subheader("Voice to text transcription")


# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV, M4A, etc.)", type=["mp3", "wav", "m4a"])

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_filepath = temp_file.name

    # Transcribe audio
    with st.spinner("Transcribing..."):
        result = model.transcribe(temp_filepath, language="English")

    # Display the transcription
    st.subheader("Transcription")
    st.write(result["text"])

    # Collapsible section for detailed transcription with timestamps
    with st.expander("Show Detailed Transcription with Timestamps"):
        for segment in result["segments"]:
            start_time = segment["start"]
            end_time = segment["end"]
            text = segment["text"]
            st.write(f"**[{start_time:.2f} - {end_time:.2f}]** {text}")

    # Option to download the transcription
    st.download_button("Download Transcription", result["text"], key="download_button")

    # Clean up temporary file
    os.remove(temp_filepath)
