from flask import Flask, jsonify, request
import video_functions
import route_about_video
import route_notes_video
import route_quiz_video
import os
import base64

app = Flask(__name__)

# Routes related to video
app.route('/upload', methods=['POST'])(video_functions.upload_video)
app.route('/delete-video', methods=['DELETE'])(video_functions.delete_video)

# Routes related to description and title
app.route('/title', methods=['GET'])(route_about_video.get_title)
app.route('/save-title', methods=['POST'])(route_about_video.save_title)
app.route('/description', methods=['GET'])(route_about_video.get_description)
app.route('/save-description', methods=['POST'])(route_about_video.save_description)

# Routes related to Notes
app.route('/Notes', methods=['GET'])(route_notes_video.get_Notes)
app.route('/save-Notes', methods=['POST'])(route_notes_video.save_Notes)

# Routes related to Quiz
app.route('/get-Quiz', methods=['GET'])(route_quiz_video.get_Quiz)
app.route('/save-Quiz', methods=['POST'])(route_quiz_video.save_Quiz)


@app.route('/get-files-and-video', methods=['GET'])
def get_files_and_video():
    # Read video file
    video_path = 'Video/Video.mp4'
    with open(video_path, 'rb') as f:
        video_data = f.read()
    video_base64 = base64.b64encode(video_data).decode('utf-8')

    # Placeholder data for other files, you need to read and encode them similarly
    transcript_base64 = ""
    summary_base64 = ""
    notes_base64 = ""
    description_base64 = ""
    
    # Placeholder data for quiz
    quiz_data = [
        {
            "id": 1,
            "question": "Sample Question 1",
            "options": [
                {"op": "a", "text": "Option A", "correct": True},
                {"op": "b", "text": "Option B", "correct": False},
                {"op": "c", "text": "Option C", "correct": False},
                {"op": "d", "text": "Option D", "correct": False}
            ]
        }
    ]

    json_data = {
        "Id": 1,
        "Title": "Sample Title",
        "Video": {
            "name": "sample_video.mp4",
            "type": "video/mp4",
            "data": video_base64
        },
        "Transcript": {
            "name": "sample_transcript.txt",
            "type": "text/plain",
            "data": transcript_base64
        },
        "Summary": {
            "name": "sample_summary.txt",
            "type": "text/plain",
            "data": summary_base64
        },
        "Notes": {
            "name": "sample_notes.docx",
            "type": "text/plain",
            "data": notes_base64
        },
        "Description": {
            "name": "sample_description.txt",
            "type": "text/html",
            "data": description_base64
        },
        "Quiz": quiz_data
    }

    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
