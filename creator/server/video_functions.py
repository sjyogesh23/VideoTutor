from flask import jsonify, request
import os
import subprocess  # for calling main.py as a subprocess

def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['video']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    upload_folder = 'Video'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    file.save(os.path.join(upload_folder, 'Video.mp4'))

    # Call main.py to process the uploaded video
    try:
        subprocess.run(["python", "main.py"])
    except Exception as e:
        return jsonify({'error': 'Failed to process video', 'details': str(e)}), 500

    return jsonify({'message': 'File uploaded and processed successfully'}), 200

def delete_video():
    upload_folder = 'Video'
    video_path = os.path.join(upload_folder, 'Video.mp4')
    try:
        os.remove(video_path)
        return jsonify({'message': 'Video file deleted successfully'}), 200
    except FileNotFoundError:
        return jsonify({'error': 'Video file not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to delete video file', 'details': str(e)}), 500
