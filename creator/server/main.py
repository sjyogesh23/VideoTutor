from flask import Flask, request, jsonify
import os
from Title_extraction import generate_title
from Audio_extraction import extract_audio_transcription
from Video_extraction import process_video
from Notes_extraction import summarize_text_file
from quiz_gen import generate_quiz

app = Flask(__name__)

def check_and_summarize(input_file_path, output_file_path):
    if not os.path.exists(input_file_path):
        print(f"Input file '{input_file_path}' does not exist.")
        return
    
    with open(input_file_path, "r") as f:
        content = f.read()

    char_count = len(content)

    if char_count > 2500:
        summarize_text_file(input_file_path, output_file_path)
    else:
        with open(output_file_path, "w") as f:
            f.write(content)
        print("Copied content to output file.")

@app.route('/Fun_Ack', methods=['POST'])
def fun_ack():
    # Process the request as needed
    # For now, let's just return a simple acknowledgment message
    return jsonify({"message": "Function completed successfully"}), 200

if __name__ == "__main__":
    video_path = "Video/video.mp4"
    # process_video(video_path, 1, "OutputFiles/Video_trans.txt")
    extract_audio_transcription(video_path, "OutputFiles/Audio_trans.txt")
    check_and_summarize("OutputFiles/Audio_trans.txt", "OutputFiles/Summary.txt")
    
    with open("OutputFiles/Summary.txt", 'r') as file:
        content = file.read()
    generate_quiz(content, 10)
    generate_title(content)
