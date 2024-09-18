from flask import Flask, request, render_template
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app = Flask(__name__)

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text):
    sentences = sent_tokenize(text)
    if len(sentences) == 0:
        return ["No summary available."]
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
   
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]

    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    try:
        tfidf_matrix = vectorizer.fit_transform(sentences)
        tfidf_scores = tfidf_matrix.toarray()
        N = min(5, len(sentences))  
        top_sentence_indices = tfidf_scores.sum(axis=1).argsort()[-N:][::-1]      
        summary = [sentences[i] for i in top_sentence_indices]
        
    except ValueError:  
        summary = ["Unable to summarize the text."]
    return summary

@app.route("/", methods=["GET", "POST"])
def summarize():
    if request.method == "POST":
        text = request.form["text"]
        summary = summarize_text(text)
        return render_template("summary.html", summary=summary)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
