import os
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read job description
with open("job_description.txt", "r", encoding="utf-8") as f:
    job_desc = f.read()

# Read all resume PDFs
resume_texts = []
file_names = []

for filename in os.listdir("resumes"):
    if filename.endswith(".pdf"):
        path = os.path.join("resumes", filename)
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        resume_texts.append(text)
        file_names.append(filename)

# Compare job description with resumes
vectorizer = TfidfVectorizer()
all_texts = [job_desc] + resume_texts
vectors = vectorizer.fit_transform(all_texts)

# Compute similarity
scores = cosine_similarity(vectors[0:1], vectors[1:])[0]

# Show top matches
ranked = sorted(zip(file_names, scores), key=lambda x: x[1], reverse=True)
print("\nTop matching resumes:")
for file, score in ranked:
    print(f"{file} - Score: {score:.2f}")
