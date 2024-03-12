import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
import json

nltk.download('punkt')
nltk.download('stopwords')

def generate_title(text):
    sentences = sent_tokenize(text)
    combined_text = ' '.join(sentences)
    words = word_tokenize(combined_text)

    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words and word not in string.punctuation]

    if not filtered_words:
        return "No Title Generated"

    freq_dist = FreqDist(filtered_words)
    title = freq_dist.most_common(1)[0][0]

    # Write the title to a JSON file
    with open('OutputFiles/Title.json', 'w') as json_file:
        json.dump({"title": title}, json_file)
