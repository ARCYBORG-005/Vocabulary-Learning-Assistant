def load_words():
    try:
        with open("words.txt", "r") as f:
            return [w.strip() for w in f.readlines() if w.strip()]
    except:
        return []

def add_word(word):
    words = load_words()

    word = word.strip().lower()

    if word not in words:
        with open("words.txt", "a") as f:
            f.write(word + "\n")