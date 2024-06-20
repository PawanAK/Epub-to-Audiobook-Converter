import streamlit as st
import subprocess

# Title of the app
st.title('OpenAI TTS Conversion')

# Button to perform conversion
if st.button('Run Command'):
    # Perform conversion
    command = 'python main.py "examples\\test.epub" "english" --tts openai'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Display output and errors
    st.text('Output:')
    st.text(stdout.decode('utf-8'))
    if stderr:
        st.text('Errors:')
        st.text(stderr.decode('utf-8'))