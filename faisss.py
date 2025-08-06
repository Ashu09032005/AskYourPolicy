from flask import Flask, request, jsonify, render_template
import faiss
import numpy as np
import re
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load model and embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = np.load("embeddings.npy")
with open("chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("\n---\n")

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def generate_answer(question):
    query_embedding = model.encode([question], convert_to_numpy=True).astype("float32")
    D, I = index.search(query_embedding, k=3)
    best_chunk = chunks[I[0][0]].strip()
    best_chunk_lower = best_chunk.lower()

    if "waiting period" in best_chunk_lower and "covered" in best_chunk_lower:
        return "Yes, covered after waiting period.", best_chunk
    elif "not covered" in best_chunk_lower and "until" in best_chunk_lower:
        return "Yes, covered after waiting period.", best_chunk
    elif "not covered" in best_chunk_lower and "covered" in best_chunk_lower:
        return "Yes, covered after waiting period.", best_chunk
    elif "not covered" in best_chunk_lower and "excluded" in best_chunk_lower:
        return "No, permanently excluded.", best_chunk
    elif "not covered" in best_chunk_lower:
        return "No, not covered.", best_chunk
    elif "covered" in best_chunk_lower or "reimbursed" in best_chunk_lower or "included" in best_chunk_lower:
        return "Yes, covered.", best_chunk
    elif "waiting period" in best_chunk_lower:
        return "Waiting period details: " + best_chunk, best_chunk
    else:
        return "Unclear: " + best_chunk, best_chunk

@app.route("/", methods=["GET", "POST"])
def home():
    answer = context = question = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            answer, context = generate_answer(question)
    return render_template("index.html", answer=answer, context=context, question=question)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' in request."}), 400

    question = data["question"]
    answer, context = generate_answer(question)

    return jsonify({
        "question": question,
        "answer": answer,
        "context": context
    })

if __name__ == "__main__":
    app.run(debug=True)
