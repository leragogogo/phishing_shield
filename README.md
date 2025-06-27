# Phishing Shield
A Python-based command-line tool that detects phishing emails using machine learning. 
Trained on labeled email text and powered by a Random Forest classifier.

## Features

- Detects phishing emails based on content
- Uses TF-IDF for text vectorization
- Random Forest classifier via `scikit-learn`
- CLI-based input for real email snippets
- Saves results to SQLite database
- Dockerized for easy setup and execution

## Running with Docker

### 1. Clone the Repository
```bash
git clone https://github.com/leragogogo/phishing_shield.git
cd phishing_shield
```

### 2. Build the Docker Image
```bash
docker build -t phishing-shield .
```

### 3. Run the App
```bash
docker run -it phishing-shield
```

You will be prompted to paste an email into the terminal. After pasting, press:

- `Ctrl + D` on **macOS/Linux**
- `Ctrl + Z` then **Enter** on **Windows**

to submit the text for analysis.
