import textwrap
import whisper

def extract_audio_transcription(video_path, output_text_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)

    transcription_text = result['text']

    wrap_width = 80
    wrapped_transcription = textwrap.fill(transcription_text, width=wrap_width)

    print(wrapped_transcription)

    with open(output_text_path, "w") as file:
        file.write(wrapped_transcription)

if __name__ == "__main__":
    extract_audio_transcription("Video/video.mp4", "Audio_trans.txt")
