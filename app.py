import streamlit as st
import PyPDF2
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
import re
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
@st.cache_resource
def load_model():
    return SentenceTransformer(
        "paraphrase-MiniLM-L3-v2"
    )
def extract_keywords(text):

    # Convert to lowercase
    text = text.lower()

    # Extract words and phrases
    words = re.findall(r'\b[a-zA-Z][a-zA-Z+\-]{1,}\b', text)

    stop_words = {
        "the","and","or","for","with","from",
        "into","must","should","will","have",
        "has","are","job","role","candidate",
        "required","experience","years","year",
        "looking","good","strong","excellent",
        "ability","knowledge","skills","skill"
    }

    keywords = []

    for word in words:

        if word not in stop_words:

            keywords.append(word)

    return list(set(keywords))

# -----------------------------------
# ATS Score Calculation
# -----------------------------------

def calculate_score(
    resume_text,
    jd_text
):

    jd_skills = extract_keywords(
        jd_text
    )

    resume_skills = extract_keywords(
        resume_text
    )

    matched = 0

    for skill in jd_skills:

        if skill in resume_skills:

            matched += 1

    score = (
        matched /
        max(len(jd_skills),1)
    ) * 100

    return round(score,2)

def semantic_score(
    resume_text,
    jd_text
):

    model = load_model()

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    jd_embedding = model.encode(
        jd_text,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        resume_embedding,
        jd_embedding
    )

    return round(
        float(similarity[0][0]) * 100,
        2
    )
# -----------------------------------
# PDF Report Generator
# -----------------------------------

def create_pdf_report(
    candidate_name,
    score,
    matched_skills,
    missing_skills
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(
        200,
        10,
        text="AI Resume Screening Report",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.ln(5)

    pdf.set_font("Arial", size=12)

    pdf.cell(
        200,
        10,
        text=f"Candidate: {candidate_name}",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.cell(
        200,
        10,
        text=f"ATS Score: {score}%",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        text="Skills Found:",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    for skill in matched_skills:

        pdf.cell(
            200,
            10,
            text=f"- {skill}",
            new_x="LMARGIN",
            new_y="NEXT"
        )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        text="Missing Skills:",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    for skill in missing_skills:

        pdf.cell(
            200,
            10,
            text=f"- {skill}",
            new_x="LMARGIN",
            new_y="NEXT"
        )

    filename = (
        candidate_name.replace(".pdf", "")
        + "_report.pdf"
    )

    pdf.output(filename)

    return filename


# -----------------------------------
# Page Setup
# -----------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title(
    "📄 AI Resume Screening & Candidate Ranking System"
)

st.write(
    "Upload resumes and compare them against a Job Description."
)

# -----------------------------------
# Upload Resumes
# -----------------------------------

uploaded_resumes = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# -----------------------------------
# Job Description
# -----------------------------------

job_description = st.text_area(
    "Paste Job Description Here"
)

# -----------------------------------
# Analyze
# -----------------------------------

if st.button("🚀 Analyze Resumes"):

    if not uploaded_resumes:

        st.error(
            "Please upload at least one resume."
        )

    elif not job_description:

        st.error(
            "Please enter a Job Description."
        )

    else:

        results = []

        st.header("📊 Resume Analysis")

        for resume in uploaded_resumes:

            try:

                pdf_reader = PyPDF2.PdfReader(
                    resume
                )

                text = ""

                for page in pdf_reader.pages:

                    extracted = page.extract_text()

                    if extracted:
                        text += extracted

                # Extract keywords

                jd_skills = extract_keywords(
                job_description
                )

                resume_skills = extract_keywords(
                    text
                )

# Calculate ATS score

                keyword_score = calculate_score(
                  text,
                job_description
                )

                semantic_ats = semantic_score(
                text,
                job_description
               )

                score = round(
    (keyword_score * 0.4)
    +
    (semantic_ats * 0.6),
    2
)

# Find matched and missing skills

                matched_skills = []
                missing_skills = []

                for skill in jd_skills:

                  if skill in resume_skills:

                     matched_skills.append(skill)

                else:

                    missing_skills.append(skill)

# Store result for ranking

                results.append(
    (
        resume.name,
        score
    )
)

                st.markdown("---")

                st.subheader(
                    f"📄 {resume.name}"
                )

                st.success(
                    f"ATS Score: {score}%"
                )
                st.info(
    f"Keyword Score: {keyword_score}%"
)

                st.info(
    f"Semantic Score: {semantic_ats}%"
)

                st.progress(
                    min(
                        int(score),
                        100
                    )
                )

                st.write("### ✅ Skills Found")

                if matched_skills:

                    for skill in matched_skills:
                        st.write(f"✔ {skill}")

                else:

                    st.write(
                        "No matching skills found."
                    )

                st.write("### ❌ Missing Skills")

                if missing_skills:

                    for skill in missing_skills:
                        st.write(f"✖ {skill}")

                else:

                    st.write(
                        "No missing skills."
                    )

                # PDF REPORT

                report_file = create_pdf_report(
                    resume.name,
                    score,
                    matched_skills,
                    missing_skills
                )

                with open(
                    report_file,
                    "rb"
                ) as file:

                    st.download_button(
                        label="📥 Download Report",
                        data=file,
                        file_name=report_file,
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(
                    f"Error processing {resume.name}: {e}"
                )

        # -----------------------------------
        # Ranking
        # -----------------------------------

        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

        st.markdown("---")

        st.header(
            "🏆 Candidate Ranking"
        )

        for rank, (
            name,
            score
        ) in enumerate(
            results,
            start=1
        ):

            st.write(
                f"{rank}. {name} - {score}%"
            )

        # -----------------------------------
        # Dashboard
        # -----------------------------------

        names = [
            x[0]
            for x in results
        ]

        scores = [
            x[1]
            for x in results
        ]

        st.markdown("---")

        st.header(
            "📊 Recruiter Dashboard"
        )

        fig, ax = plt.subplots()

        ax.bar(
            names,
            scores
        )

        ax.set_title(
            "Candidate ATS Scores"
        )

        ax.set_xlabel(
            "Candidates"
        )

        ax.set_ylabel(
            "ATS Score"
        )

        st.pyplot(fig)

        # -----------------------------------
        # Statistics
        # -----------------------------------

        st.markdown("---")

        st.header(
            "📈 Recruitment Statistics"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Candidates",
                len(scores)
            )

        with col2:

            st.metric(
                "Average Score",
                f"{sum(scores)/len(scores):.2f}%"
            )

        with col3:

            st.metric(
                "Top Score",
                f"{max(scores):.2f}%"
            )