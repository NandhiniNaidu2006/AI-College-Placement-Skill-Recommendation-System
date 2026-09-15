job_skills = {
    "Data Scientist": [
        "Python",
        "SQL",
        "Statistics",
        "Machine Learning",
        "Pandas",
        "NumPy"
    ],
    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Statistics"
    ],
    "Python Developer": [
        "Python",
        "OOP",
        "Django",
        "SQL",
        "Git"
    ],
    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ]
}

student_skills = [
    "Python",
    "SQL",
    "HTML",
    "CSS"
]

target_job = "Data Scientist"

required_skills = job_skills[target_job]

missing_skills = []

for skill in required_skills:
    if skill not in student_skills:
        missing_skills.append(skill)

print("TARGET JOB:", target_job)
print("STUDENT SKILLS:", student_skills)
print("RECOMMENDED SKILLS:")

for skill in missing_skills:
    print("-", skill)