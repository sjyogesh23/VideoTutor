from flask import jsonify, send_file
import os
import subprocess
import json
from flask import request

def get_description():
    confirm_description_folder = 'Confirm_File'
    temp_html_path = os.path.join(confirm_description_folder, 'temp.html')
    title_path = 'OutputFiles/Title.json'

    if os.path.exists(temp_html_path):
        return send_file(temp_html_path, as_attachment=True)
    else:
        return send_file('OutputFiles/Summary.txt', as_attachment=True)

def get_title():
    confirm_title_path = 'Confirm_File/title.json'
    default_title_path = 'OutputFiles/Title.json'

    if os.path.exists(confirm_title_path):
        with open(confirm_title_path) as f:
            title_data = json.load(f)
        return jsonify(title_data)
    elif os.path.exists(default_title_path):
        with open(default_title_path) as f:
            title_data = json.load(f)
        return jsonify(title_data)
    else:
        return jsonify({'error': 'Title file not found'}), 404

def save_description():
    data = request.json
    description = data.get('description')

    if not description:
        return jsonify({'error': 'Description is empty'}), 400

    save_folder = 'Confirm_File'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    docx_filename = os.path.join(save_folder, 'Confirm_Description.docx')
    with open(os.path.join(save_folder, 'temp.html'), 'w') as f:
        f.write(description)

    subprocess.run(['pandoc', '--from', 'html', '--to', 'docx', os.path.join(save_folder, 'temp.html'), '-o', docx_filename])

    os.remove(os.path.join(save_folder, 'temp.html'))

    return jsonify({'message': 'Description saved successfully'}), 200

def save_title():
    data = request.json
    title = data.get('title')

    if not title:
        return jsonify({'error': 'Title is empty'}), 400

    save_folder = 'Confirm_File'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    title_path = os.path.join(save_folder, 'title.json')
    with open(title_path, 'w') as f:
        json.dump({'title': title}, f)

    return jsonify({'message': 'Title saved successfully'}), 200
