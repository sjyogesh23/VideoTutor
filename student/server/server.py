from flask import Flask, request, jsonify
from chatbot import bot_response, get_google_link

app = Flask(__name__)

@app.route('/QnA', methods=['POST'])
def QnA():
    data = request.json
    print(data)
    user_input = data.get('question', '') 
    
    bot_res = bot_response(user_input)
    response = {"response": bot_res}
    
    if "Out of context" in bot_res:
        google_link = get_google_link(user_input)
        response["google_link"] = google_link if google_link else "Couldn't find any relevant links for the query."
    
    return jsonify(response)
    
if __name__ == '__main__':
    app.run(port=5000)
