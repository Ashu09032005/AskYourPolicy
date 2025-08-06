import fitz  # PyMuPDF
import re
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def improved_chunking(text):
    pattern = r'(?=(?:\n|^)(?:Section|SECTION|Annexure|ANNEXURE)?\s?\d+(\.\d+)*[.:]?\s[A-Z])'
    raw_chunks = re.split(pattern, text)
    chunks = []
    for part in raw_chunks:
        if part and isinstance(part, str):
            cleaned = part.strip().replace("\n", " ")
            if len(cleaned) > 30:
                chunks.append(cleaned)
    return chunks

def preprocess(pdf_path):
    text = extract_text(pdf_path)
    chunks = improved_chunking(text)
    embeddings = model.encode(chunks, convert_to_numpy=True).astype("float32")

    np.save("embeddings.npy", embeddings)
    with open("chunks.txt", "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n---\n")

    print(f"[✓] Saved {len(chunks)} chunks and embeddings.")

if __name__ == "__main__":
    preprocess("sample1.pdf")
