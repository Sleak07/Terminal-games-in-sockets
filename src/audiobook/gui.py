# gui.py
import streamlit as st
from pdf_extractor import Extractor
from audio import TextToSpeech  # Import the updated TextToSpeech class


def main():
    st.title("PDF Text-to-Speech Converter")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully!")

        # Extract text from the uploaded PDF
        extractor = Extractor("temp.pdf")
        try:
            extracted_text = extractor.get_chunks()

            # Display extracted text
            st.text_area("Extracted Text", extracted_text, height=300)

            # Initialize TextToSpeech class
            tts = TextToSpeech()

            # Optionally allow the user to customize voice, rate, and volume
            rate = st.slider(
                "Speech Rate (words per minute)", min_value=50, max_value=300, value=150
            )
            volume = st.slider("Volume", min_value=0.0, max_value=1.0, value=1.0)

            tts.set_rate(rate)
            tts.set_volume(volume)

            # Button to start the text-to-speech conversion
            if st.button("Convert to Speech"):
                st.info("Converting text to speech...")
                tts.speak(extracted_text)
                st.success("Conversion complete!")

        except FileNotFoundError as e:
            st.error(f"Error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
