import requests

def generate_practice(word):

    prompt = f"""
    Word: {word}

    Give:
    1. Meaning
    2. One example sentence
    3. MCQ (4 options, 1 correct)

    Format strictly:

    Meaning: ...
    Sentence: ...
    Options:
    A. ...
    B. ...
    C. ...
    D. ...
    Answer: ...
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                 "model": "llama3:latest",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        if "response" not in data:
            raise Exception("No response from Ollama")

        text = data["response"]

    except Exception as e:
        print("❌ ERROR:", e)
        return {
            "meaning": "AI not working",
            "sentence": "Check Ollama server",
            "options": ["A", "B", "C", "D"],
            "answer": "A"
        }

    meaning, sentence, options, answer = "", "", [], ""

    for line in text.split("\n"):
        line = line.strip()

        if line.startswith("Meaning:"):
            meaning = line.replace("Meaning:", "").strip()

        elif line.startswith("Sentence:"):
            sentence = line.replace("Sentence:", "").strip()

        elif line.startswith(("A.", "B.", "C.", "D.")):
            options.append(line[2:].strip())

        elif "Answer:" in line:
            answer = line.split("Answer:")[-1].strip()

    return {
        "meaning": meaning,
        "sentence": sentence,
        "options": options,
        "answer": answer
    }