# 📘 LexiForm – AI Vocabulary Learning Assistant

## 🚀 Overview

LexiForm is a lightweight AI-powered vocabulary learning web application that helps users capture, organize, and practice new words using intelligent question generation.

The system uses a local LLM (via Ollama) to generate meanings, example sentences, and multiple-choice questions, enabling active learning without relying on paid APIs.

---

## 🎯 Key Features

* Add and store new vocabulary words
*  AI-generated:

  * Meaning
  * Example sentence
  * Multiple-choice questions (MCQs)
*  Practice mode for each word
* Instant answer validation
* Lcal storage (no database required)
*  No API key or credit card needed (runs fully offline using Ollama)
---

## 🏗️ Project Structure

```
vocab/
│── app.py
│── generator.py
│── storage.py
│── words.txt
│── templates/
    └── index.html
```

---

## 📂 File Descriptions

### 1. `app.py` – Main Application (Flask Backend)

* Initializes the Flask app
* Handles routing and user interaction
* Connects UI with backend logic

#### Key Routes:

* `/` → Home page (displays words)
* `/add` → Add new word
* `/practice/<word>` → Generate AI-based practice
* `/mcq/<word>` → Evaluate MCQ answer

---

### 2. `generator.py` – AI Logic (Core Component)

* Communicates with Ollama (local LLM)
* Sends prompts to the model
* Parses structured AI responses

#### Responsibilities:

* Generate:

  * Meaning
  * Example sentence
  * MCQ options
  * Correct answer
* Handle API errors gracefully

---

### 3. `storage.py` – Data Handling

* Manages reading and writing words
* Uses a simple text file (`words.txt`) instead of a database

#### Functions:

* `load_words()` → Loads all saved words
* `add_word(word)` → Adds new word (avoids duplicates)

---

### 4. `words.txt` – Storage File

* Stores vocabulary words line-by-line
* Acts as a lightweight database

---

### 5. `templates/index.html` – Frontend UI

* Displays:

  * Word list
  * Practice interface
  * MCQ options
* Built using basic HTML + Jinja templating

---

## ⚙️ Installation & Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install flask requests
```

---

## 🤖 Ollama Setup (Important)

### Install Ollama

Download from: https://ollama.com

### Start Server

```bash
ollama serve
```

### Pull Model

```bash
ollama pull llama3
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User adds a word
2. Word is stored in `words.txt`
3. User clicks "Practice"
4. Backend sends prompt to Ollama
5. AI generates:

   * Meaning
   * Sentence
   * MCQ
6. User answers → system validates response

---

## 🔍 Example Prompt Sent to AI

```
Word: narcissist

Give:
1. Meaning
2. One example sentence
3. MCQ (4 options, 1 correct)
```

---

## ⚠️ Limitations

* Depends on local Ollama server
* AI output format may vary slightly
* No advanced UI (basic HTML)

---

## 🚀 Future Enhancements

* ✨ Sentence correction using AI
* ✨ Flashcards & spaced repetition
* ✨ User authentication
* ✨ Progress tracking dashboard
* ✨ Mobile-friendly UI
* ✨ Database integration (MySQL / MongoDB)

---

## 💡 Tech Stack

* Python (Flask)
* HTML 
* Ollama (LLM - LLaMA 3)
* Requests (API calls)

---

#
---

## 🙌 Author

Built as a personal AI learning project to improve vocabulary using real-world context and active recall techniques.

---
