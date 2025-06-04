import streamlit as st
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Define job roles and sample descriptions
job_roles = {
    "Data Scientist": "Experience in Python, machine learning, statistics, and data analysis.",
    "AI Engineer": "Expertise in AI models, neural networks, deep learning, and Python.",
    "Web Developer": "Strong skills in HTML, CSS, JavaScript, and React or Django.",
    "Software Engineer": "Knowledge of software design, algorithms, coding, and debugging.",
    "ML Engineer": "Background in machine learning, TensorFlow/PyTorch, data preprocessing."
}

# UI Title
st.title("AI Resume Matcher")

# Dropdown for job roles
selected_role = st.selectbox("Select a Job Role", list(job_roles.keys()))
job_description = job_roles[selected_role]
st.write("**Job Description:**")
st.info(job_description)

# Upload PDF resumes
uploaded_files = st.file_uploader("Upload Resume PDFs", type="pdf", accept_multiple_files=True)

# PDF to text
def extract_text_from_pdf(pdf_file):
    with open(pdf_file.name, "wb") as f:
        f.write(pdf_file.getbuffer())
    doc = fitz.open(pdf_file.name)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Match resumes
if st.button("Match Resumes"):
    if uploaded_files and job_description:
        resume_texts = []
        file_names = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resume_texts.append(text)
            file_names.append(file.name)

        # Vectorize and compare
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([job_description] + resume_texts)
        similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

        # Show results
        results = sorted(zip(file_names, similarities), key=lambda x: x[1], reverse=True)
        st.subheader("Match Results:")
        for name, score in results:
            st.write(f"{name} — Match Score: {score * 100:.2f}%")
    else:
        st.warning("Please upload at least one resume.")
