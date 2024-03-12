from flask import jsonify, send_file
import os
import subprocess
import json
from flask import request
import re

def get_Notes():
    confirm_Notes_folder = 'Confirm_File'
    Notes_txt_path = os.path.join(confirm_Notes_folder, 'Audio_trans.txt')
    title_path = 'OutputFiles/Title.json'

    if os.path.exists(Notes_txt_path):
        return send_file(Notes_txt_path, as_attachment=True)
    else:
        return send_file('OutputFiles/Audio_trans.txt', as_attachment=True)

def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def save_Notes():
    data = request.json
    Notes = data.get('Notes')

    if not Notes:
        return jsonify({'error': 'Notes is empty'}), 400

    save_folder = 'Confirm_File'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    txt_filename = os.path.join(save_folder, 'Notes.txt')
    
    # Strip HTML tags from the input text
    Notes = strip_html_tags(Notes)
    
    with open(txt_filename, 'w') as f:
        f.write(Notes)

    return jsonify({'message': 'Notes saved successfully'}), 200
