# 🤖 AI-Powered Resume Screening & Candidate Ranking System

An intelligent ATS (Applicant Tracking System) that automatically screens resumes, matches them against job descriptions, and ranks candidates — built with Python, NLP, and Semantic AI. Comes in two versions: a **Jupyter Notebook** for exploration and a **Streamlit Web App** for real-world use.

---

## 📂 Project Structure

```
├── AI_Powered_Resume_Screening.ipynb   # Version 1 — Notebook (exploration & prototyping)
├── app.py                              # Version 2 — Streamlit Web App (production-ready)
├── resumes/                            # Folder to place PDF resumes
└── README.md
```

---

## 🔄 Two Versions

### 📓 Version 1 — Jupyter Notebook
A step-by-step exploratory build:
- Parses a single PDF resume using **PyPDF2**
- Matches skills from a curated **skills database** (25+ tech skills)
- Calculates an **ATS score** based on keyword overlap
- Shows matched/missing skills with suggestions
- Ranks multiple candidates using **Sentence Transformers + Cosine Similarity**
- Outputs a **bar chart** of candidate rankings

### 🌐 Version 2 — Streamlit Web App
A full recruiter dashboard with:
- Upload **multiple PDF resumes** at once
- Paste any **Job Description**
- **Dual scoring system** — Keyword Match (40%) + Semantic Similarity (60%)
- Visual **progress bars** per candidate
- Matched ✅ and Missing ❌ skills per resume
- **Downloadable PDF report** per candidate
- **Ranked leaderboard** of all candidates
- **Recruiter Dashboard** — bar chart + stats (total candidates, average score, top score)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| PyPDF2 | PDF text extraction |
| NLTK | Text tokenization |
| Sentence-Transformers (`paraphrase-MiniLM-L3-v2`) | Semantic embeddings |
| Scikit-learn | Cosine similarity |
| Streamlit | Web app UI |
| FPDF | PDF report generation |
| Pandas & NumPy | Data handling |
| Matplotlib | Candidate ranking chart |

---

## 🚀 How to Run the Web App

**1. Install dependencies**
```bash
pip install streamlit PyPDF2 sentence-transformers fpdf2 matplotlib scikit-learn
```

**2. Run the app**
```bash
streamlit run app.py
```

**3. Use the app**
- Upload one or more PDF resumes
- Paste a Job Description
- Click **Analyze Resumes** 🚀

---

## 📊 How Scoring Works

```
Final ATS Score = (Keyword Score × 40%) + (Semantic Score × 60%)
```

- **Keyword Score** — Exact skill/keyword match between resume and JD
- **Semantic Score** — Deep contextual similarity using sentence embeddings (understands meaning, not just words)

---

## 📋 Sample Output

```
📄 candidate1.pdf
ATS Score:        78.45%
Keyword Score:    65.00%
Semantic Score:   87.30%

✅ Skills Found: python, sql, machine learning, tensorflow, git
❌ Missing Skills: docker, aws
```

---

## 💡 Use Cases

- Recruiters screening large volumes of resumes quickly
- Job seekers optimizing their resumes for a specific role
- HR teams building a lightweight internal ATS tool

---

## 🔮 Future Improvements

- [ ] Add support for DOCX resumes
- [ ] Deploy on Streamlit Cloud / Hugging Face Spaces
- [ ] Add email notifications for top candidates
- [ ] GPT-powered personalized resume feedback

---

## 📬 Connect

Feel free to fork, star ⭐, or raise issues. Contributions welcome!
