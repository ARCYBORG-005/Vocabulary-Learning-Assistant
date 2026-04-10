from flask import Flask, render_template, request, redirect
from storage import load_words, add_word
from generator import generate_practice

app = Flask(__name__)

@app.route('/')
def home():
    words = load_words()
    return render_template("index.html", words=words)

@app.route('/add', methods=['POST'])
def add():
    word = request.form['word']
    add_word(word)
    return redirect('/')

@app.route('/practice/<word>')
def practice(word):
    words = load_words()
    data = generate_practice(word)

    return render_template(
        "index.html",
        words=words,
        current_word=word,
        meaning=data["meaning"],
        sentence=data["sentence"],
        options=data["options"],
        answer=data["answer"]
    )

@app.route('/mcq/<word>', methods=['POST'])
def mcq(word):
    user_answer = request.form['answer']
    data = generate_practice(word)

    result = "Correct!" if user_answer == data["answer"] else f"❌ inCorrect: {data['answer']}"

    words = load_words()

    return render_template(
        "index.html",
        words=words,
        current_word=word,
        options=data["options"],
        result=result
    )

if __name__ == '__main__':
    print("🚀 Server running...")
    app.run(debug=True)
