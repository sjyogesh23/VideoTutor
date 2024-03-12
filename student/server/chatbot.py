from flask import Flask, request, jsonify
from flask_cors import CORS  
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from googlesearch import search
import warnings

warnings.filterwarnings('ignore')
nltk.download("punkt", quiet=True)

app = Flask(__name__)
CORS(app)  

def load_corpus_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            corpus = file.read()
        return corpus
    except Exception as e:
        print("Error loading corpus:", str(e))
        return None

file_path = "Summary.txt"  

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                # swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index

def bot_response(user_input, corpus):
    sentence_list = nltk.sent_tokenize(corpus)  
    sentence_list.append(user_input.lower())  
    bot_response = ""
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + " " + sentence_list[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break

    if response_flag == 0:
        bot_response = bot_response + " " + "Out of context"

    sentence_list.remove(user_input.lower())  

    return bot_response

def get_google_link(query):
    for j in search(query, num=1, stop=1, pause=2):  
        return j
    return None

@app.route("/QnA", methods=["POST"])
def handle_question():
    try:
        data = request.get_json()
        user_input = data["question"]
        corpus = load_corpus_from_file(file_path)
        if corpus is None:
            return jsonify({"response": "Error loading corpus"}), 500
        bot_res = bot_response(user_input, corpus)
        
        if "Out of context" in bot_res:
            google_link = get_google_link(user_input)
            response = {
                "response": bot_res,
                "google_link": google_link
            }
        else:
            response = {"response": bot_res}
        
        return jsonify(response), 200
    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"response": "Error occurred while processing the question"}), 500

if __name__ == "__main__":
    app.run(debug=True)
