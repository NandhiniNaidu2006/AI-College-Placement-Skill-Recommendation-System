job_skills = {
    "Data Scientist": {
        "Python", "SQL", "Statistics",
        "Machine Learning", "Pandas", "NumPy"
    },

    "Data Analyst": {
        "Python", "SQL", "Excel",
        "Power BI", "Statistics"
    },

    "Python Developer": {
        "Python", "OOP", "Django",
        "SQL", "Git"
    },

    "Web Developer": {
        "HTML", "CSS", "JavaScript",
        "React", "Git"
    }
}

student_skills = {
    "Python",
    "SQL",
    "Statistics",
    "Machine Learning",
    "Pandas",
    "NumPy"
}

scores = {}

for job, required_skills in job_skills.items():
    matched_skills = student_skills.intersection(required_skills)
    score = len(matched_skills) / len(required_skills) * 100
    scores[job] = score

recommended_jobs = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

print("RECOMMENDED JOBS:")

for job, score in recommended_jobs:
    print(job, "-", round(score, 2), "% match")