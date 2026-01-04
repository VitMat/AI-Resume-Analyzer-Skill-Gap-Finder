import streamlit as st
from resume_parser import extract_text
from preprocess import clean_text
from skill_extractor import extract_skills
from matcher import match_resume

st.title("AI Resume Analyzer & Skill Gap Finder")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:
    with open(resume_file.name, "wb") as f:
        f.write(resume_file.getbuffer())

    raw_text = extract_text(resume_file.name)
    clean_resume = clean_text(raw_text)
    clean_jd = clean_text(job_desc)

    resume_skills = extract_skills(clean_resume)
    jd_skills = extract_skills(clean_jd)

    match_score = match_resume(clean_resume, clean_jd)
    missing_skills = list(set(jd_skills) - set(resume_skills))

    st.subheader(f"Match Percentage: {match_score}%")
    st.write("Resume Skills:", resume_skills)
    st.write("Missing Skills:", missing_skills)
