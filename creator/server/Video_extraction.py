import json
import base64
import cv2
import numpy as np
import easyocr

reader = easyocr.Reader(['en'])

def save_frames_to_text(frames, text_file_path):
    try:
        with open(text_file_path, 'w') as f:
            for frame in frames:
                f.write(f"Timestamp: {frame['timestamp']}\n")
                f.write("Detected text:\n")
                for text in frame['text']:
                    f.write(f"{text}\n")
                f.write("\n")
        print(f"Frames information saved to {text_file_path}")
    except Exception as e:
        print("Error:", e)

def process_video(video_path, time_interval, text_file_path):
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error: Unable to open video file")
            return

        frame_rate = cap.get(cv2.CAP_PROP_FPS)

        frame_interval = int(time_interval * frame_rate)

        frames = []
        frame_id = 0
        print("framing")
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_id += 1

            if frame_id % frame_interval == 0:
                print("framing......")
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                result = reader.readtext(gray_frame)
                timestamp_seconds = frame_id / frame_rate
                filtered_text = []
                for detection in result:
                    text = detection[1]
                    if len(text.strip()) > 3:
                        filtered_text.append(text)

                if filtered_text:
                    frames.append({"timestamp": timestamp_seconds, "text": filtered_text})

        cap.release()
        save_frames_to_text(frames, text_file_path)
    except Exception as e:
        print("Error:", e)

