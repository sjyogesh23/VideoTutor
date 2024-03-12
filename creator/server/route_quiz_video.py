from flask import Flask, jsonify, send_file, request
import os
import subprocess
import json  # Add this import statement

app = Flask(__name__)

@app.route('/get-Quiz', methods=['GET'])
def get_Quiz():
    confirm_Quiz_folder = 'Confirm_File'
    Quiz_json_path = os.path.join(confirm_Quiz_folder, 'Quiz.json')
    title_path = 'OutputFiles/Title.json'

    if os.path.exists(Quiz_json_path):
        return send_file(Quiz_json_path, as_attachment=True)
    else:
        return send_file('OutputFiles/Quiz.json', as_attachment=True)

@app.route('/save-Quiz', methods=['POST'])
def save_Quiz():
    data = request.json
    Quiz = data.get('quiz')  # 'quiz' should be lowercase here

    if not Quiz:
        return jsonify({'error': 'Quiz is empty'}), 400

    save_folder = 'Confirm_File'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Save the Quiz.json file
    with open(os.path.join(save_folder, 'Quiz.json'), 'w') as f:
        json.dump(Quiz, f)

    # Convert JSON to DOCX using Pandoc
    docx_filename = os.path.join(save_folder, 'Confirm_Quiz.docx')
    subprocess.run(['pandoc', '--from', 'json', '--to', 'docx', os.path.join(save_folder, 'Quiz.json'), '-o', docx_filename])

    return jsonify({'message': 'Quiz saved successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)