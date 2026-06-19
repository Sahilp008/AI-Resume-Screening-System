# 🤖 AI-Powered Resume Screening & Candidate Ranking System

An intelligent ATS (Applicant Tracking System) built in Python that automatically screens resumes, matches them against job descriptions, and ranks candidates using NLP and semantic similarity.

---

## 📌 Features

- **PDF Resume Parsing** — Extracts raw text from PDF resumes using PyPDF2
- **Skill Extraction** — Detects 25+ technical skills from a curated skills database
- **ATS Score Calculation** — Computes a match percentage between resume skills and job description requirements
- **Multi-Resume Ranking** — Scores and ranks multiple candidates using sentence-transformer embeddings + cosine similarity
- **Improvement Suggestions** — Highlights missing skills and gives actionable feedback
- **Visual Output** — Bar chart showing ranked candidates by match score

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| PyPDF2 | PDF text extraction |
| NLTK | Text tokenization |
| Pandas & NumPy | Data handling |
| Scikit-learn | Cosine similarity |
| Sentence-Transformers | Semantic embeddings |
| Matplotlib | Candidate ranking chart |

---

## 🚀 How It Works

1. **Resume Parsing** — Load a PDF resume and extract all text
2. **Skill Matching** — Compare extracted skills against a predefined skills database
3. **ATS Scoring** — Calculate `(matched skills / JD skills) × 100`
4. **Candidate Ranking** — Encode resumes and JD using sentence transformers, compute cosine similarity scores
5. **Output** — View ranked candidates, matched/missing skills, and suggestions

---

## 📂 Project Structure

```
├── AI_Powered_Resume_Screening.ipynb   # Main notebook
├── resumes/                            # Folder containing PDF resumes
│   ├── candidate1.pdf
│   └── candidate2.pdf
└── README.md
```

---

## ⚙️ Installation

```bash
pip install PyPDF2 pandas numpy nltk scikit-learn sentence-transformers matplotlib
```

---

## 📊 Sample Output

```
==================================================
ATS SCORE : 85.71%
==================================================

MATCHED SKILLS
✓ python
✓ sql
✓ machine learning
✓ tensorflow
✓ aws
✓ git

MISSING SKILLS
✗ docker

RESUME SUGGESTIONS
Excellent ATS Match.
Consider adding these skills if you have experience:
- docker
```

---

## 💡 Use Cases

- Recruiters screening large volumes of resumes quickly
- Job seekers optimizing their resumes for specific roles
- HR teams building lightweight internal ATS tools

---

## 📬 Connect

Feel free to fork, star ⭐, or raise issues. Contributions welcome!
