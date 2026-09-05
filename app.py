import streamlit as st

from services.transcription import transcribe_audio
from services.llm import generate_action_items


st.set_page_config(
    page_title="Voice Notes → Action Items",
    page_icon="🎙️",
    layout="centered",
)


st.title("🎙️ Voice Notes → Action Items")
st.write(
    "Upload or record a voice note and turn it into "
    "a clear summary, action items, and important deadlines."
)

st.divider()

st.subheader("Choose or record your voice note")

audio_file = st.file_uploader(
    "Choose an audio file",
    type=["mp3", "wav", "m4a", "mp4", "mpeg", "webm"],
)

st.write("Or record a voice note")

recorded_audio = st.audio_input(
    "Record your voice note",
    sample_rate=16000,
)


if audio_file is not None or recorded_audio is not None:
    if recorded_audio is not None:
        audio_file = recorded_audio
        st.success(f"Recording ready: {audio_file.name}")
    else:
        st.success(f"Audio uploaded: {audio_file.name}")

    st.audio(
        audio_file,
        format=audio_file.type,
    )

    if st.button("Process Voice Note"):
        try:
            with st.spinner("Transcribing audio..."):
                transcript = transcribe_audio(audio_file)

            if not transcript:
                st.error("No speech could be detected in the audio.")
                st.stop()

            st.subheader("Transcript")
            st.write(transcript)

        except Exception as e:
            st.error(f"Transcription failed: {e}")
            st.stop()

        try:
            with st.spinner("Generating summary and action items..."):
                result = generate_action_items(transcript)

            if not result:
                st.error("The AI could not generate a result.")
                st.stop()

            st.subheader("Summary & Action Items")
            st.markdown(result)

        except Exception as e:
            error_message = str(e)

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                st.warning(
                    "⚠️ Gemini API quota has been reached. "
                    "Please try again after the free-tier quota resets."
                )
            else:
                st.error(f"AI processing failed: {e}")