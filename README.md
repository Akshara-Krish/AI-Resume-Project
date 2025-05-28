# AI Resume Matcher

**AI Resume Matcher** is a Python-based project that automatically compares multiple resumes against a given job description using Natural Language Processing (NLP) and Machine Learning techniques.

This tool helps HR professionals and recruiters quickly identify the most suitable candidates for a job by ranking resumes based on relevance to the job description.

## 🔍 Features

- Extracts text from PDF resumes using PyMuPDF
- Uses TF-IDF Vectorization to process resume and job description
- Compares using Cosine Similarity
- Ranks resumes by match score

## 🛠 Technologies Used

- Python 3.x
- PyMuPDF (`fitz`)
- scikit-learn (TF-IDF)
- Basic NLP and file handling

## ▶️ How to Run

1. Install Python 3 if not already installed.
2. Install required libraries:
pip install PyMuPDF scikit-learn
3. Put resume PDFs in the `resumes/` folder.
4. Write the job description inside `job_description.txt`.
5. Run the script:
python main.py



## 📁 Folder Structure

AI-Resume-Project/
├── main.py
├── job_description.txt
├── resumes/
│ ├── resume1.pdf
│ ├── resume2.pdf
│ └── resume3.pdf


## ✅ Output

The script prints resumes in the order of best match to job description.

## 📌 Ideal For

- AI/ML beginners building a portfolio
- HR tech mini-projects
- Resume screening automation tools
