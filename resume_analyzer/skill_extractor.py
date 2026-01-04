import pandas as pd

skills = pd.read_csv("skills.csv")['skill'].tolist()

def extract_skills(text):
    found = []
    for skill in skills:
        if skill.lower() in text:
            found.append(skill)
    return list(set(found))
